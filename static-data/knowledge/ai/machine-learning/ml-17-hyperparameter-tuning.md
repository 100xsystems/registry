---
slug: ml-17-hyperparameter-tuning
title: "Hyperparameter Tuning"
description: "From grid search to Bayesian optimization — systematic approaches to finding the best model configuration."
order: 17
tags:
  - machine-learning
  - hyperparameters
  - tuning
  - bayesian-optimization
  - optuna
prerequisites:
  - ml-16-cross-validation
  - ml-03-the-learning-problem
references:
  - title: "Bergstra & Bengio: Random Search for Hyper-Parameter Optimization"
    url: "https://jmlr.org/papers/v13/bergstra12a.html"
    description: "The seminal paper showing random search beats grid search"
  - title: "Bergstra et al.: Algorithms for Hyper-Parameter Optimization"
    url: "https://proceedings.neurips.cc/paper/2011/hash/86e8f7ab32cfd12577bc2619bc635690-Abstract.html"
    description: "Tree-structured Parzen Estimators (TPE) — the algorithm behind Optuna"
  - title: "Snoek et al.: Practical Bayesian Optimization of ML Hyperparameters"
    url: "https://proceedings.neurips.cc/paper/2012/hash/0531065a630b80211000958ed80c9ca9-Abstract.html"
    description: "GP-based Bayesian optimization for neural network hyperparameters"
  - title: "Optuna Documentation"
    url: "https://optuna.org/"
    description: "State-of-the-art hyperparameter optimization framework"
  - title: "scikit-learn: Tuning Hyper-parameters"
    url: "https://scikit-learn.org/stable/modules/grid_search.html"
    description: "Official guide on GridSearchCV and RandomizedSearchCV"
knowledge_refs:
  - ml-16-cross-validation
  - ml-15-regularization
  - ml-06-gradient-descent
---

# Hyperparameter Tuning

Hyperparameters are the knobs you set before training — learning rate, regularization strength, tree depth, number of layers. Finding the right configuration can be the difference between a mediocre model and a great one.

## What Are Hyperparameters?

| Model | Hyperparameters |
|---|---|
| Linear/Logistic Regression | C (regularization strength) |
| Random Forest | n_estimators, max_depth, min_samples_leaf |
| XGBoost/LightGBM | learning_rate, max_depth, n_estimators, subsample |
| Neural Networks | learning_rate, batch_size, dropout, hidden_size |
| SVM | C, kernel, gamma |

**Rule of thumb**: If you set it before training and it doesn't get learned from data, it's a hyperparameter.

## Grid Search (Exhaustive Search)

Try every combination in a predefined grid:

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'max_depth': [3, 5, 7, 10],
    'n_estimators': [100, 200, 500],
    'learning_rate': [0.01, 0.05, 0.1]
}
# 4 × 3 × 3 = 36 combinations × 5 folds = 180 model fits

grid = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=1
)
grid.fit(X_train, y_train)
print(f"Best: {grid.best_params_} → {grid.best_score_:.3f}")
```

**Problems with grid search:**
1. Combinatorial explosion: $O(K^D)$ where $K$ is values per param, $D$ is number of params
2. Wastes time on unimportant parameters
3. Can't adapt to early results

## Random Search (Bergstra & Bengio, 2012)

Sample random combinations instead of exhaustive grid:

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform

param_distributions = {
    'max_depth': randint(3, 20),
    'n_estimators': randint(50, 1000),
    'learning_rate': uniform(0.001, 0.3),
    'subsample': uniform(0.5, 0.5),
    'colsample_bytree': uniform(0.5, 0.5)
}

random_search = RandomizedSearchCV(
    estimator=model,
    param_distributions=param_distributions,
    n_iter=50,  # try 50 random combinations
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    random_state=42
)
random_search.fit(X_train, y_train)
```

**Why random search is often better:**
- If one hyperparameter matters more than others, random search explores more values of the important one
- With the same budget (number of fits), random search finds better solutions on average
- Works well with continuous hyperparameters (grid can't represent them well)

## Bayesian Optimization

The smart approach: use results from previous trials to guide which configurations to try next.

**How it works:**
1. Start with a few random configurations
2. Build a **surrogate model** (Gaussian Process, Tree Parzen Estimator) predicting performance
3. Use an **acquisition function** to select the next configuration to try
4. Train the model, observe performance, update surrogate
5. Repeat until budget exhausted

```python
import optuna

def objective(trial):
    params = {
        'max_depth': trial.suggest_int('max_depth', 3, 15),
        'n_estimators': trial.suggest_int('n_estimators', 50, 1000),
        'learning_rate': trial.suggest_float('learning_rate', 0.001, 0.3, log=True),
        'subsample': trial.suggest_float('subsample', 0.5, 1.0),
        'colsample_bytree': trial.suggest_float('colsample_bytree', 0.5, 1.0),
        'reg_alpha': trial.suggest_float('reg_alpha', 1e-8, 10.0, log=True),
        'reg_lambda': trial.suggest_float('reg_lambda', 1e-8, 10.0, log=True)
    }
    
    model = xgb.XGBClassifier(**params, eval_metric='logloss')
    
    # Use cross-validation
    from sklearn.model_selection import cross_val_score
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
    return scores.mean()

study = optuna.create_study(direction='maximize', sampler=optuna.samplers.TPESampler())
study.optimize(objective, n_trials=100, show_progress_bar=True)

print(f"Best trial: {study.best_trial.params}")
print(f"Best score: {study.best_trial.value:.3f}")
```

### Acquisition Functions

The acquisition function balances **exploration** (trying uncertain regions) vs. **exploitation** (trying regions known to be good):

- **Expected Improvement (EI)**: Most popular — selects config expected to improve over current best
- **Upper Confidence Bound (UCB)**: Balances mean + uncertainty
- **Probability of Improvement (PI)**: Probability of beating current best

### Optuna Advanced Features

```python
import optuna

# Pruning bad trials early
def objective(trial):
    params = {
        'n_estimators': trial.suggest_int('n_estimators', 50, 1000),
        'learning_rate': trial.suggest_float('learning_rate', 0.001, 0.3, log=True),
    }
    
    # Use pruning callback
    model = xgb.XGBClassifier(**params)
    scores = cross_val_score(model, X_train, y_train, cv=5)
    
    # Report intermediate results
    for i, score in enumerate(scores):
        trial.report(score, i)
        if trial.should_prune():
            raise optuna.TrialPruned()
    
    return scores.mean()

# With pruning and visualization
study = optuna.create_study(
    direction='maximize',
    pruner=optuna.pruners.MedianPruner(n_warmup_steps=5)
)
study.optimize(objective, n_trials=100)

# Visualize
optuna.visualization.plot_optimization_history(study)
optuna.visualization.plot_param_importances(study)
optuna.visualization.plot_parallel_coordinate(study)
```

## Halving Search (Successive Halving)

A budget-efficient approach: start many configurations with small budgets, progressively allocate more resources to promising ones:

```python
from sklearn.experimental import enable_halving_search_cv
from sklearn.model_selection import HalvingRandomSearchCV

halving_search = HalvingRandomSearchCV(
    estimator=model,
    param_distributions=param_distributions,
    n_candidates=100,  # start with 100 candidates
    factor=3,          # eliminate 2/3 each round
    cv=5,
    scoring='accuracy',
    random_state=42
)
halving_search.fit(X_train, y_train)
```

## Tuning Strategy by Budget

| Budget | Method | n_trials | Notes |
|---|---|---|---|
| Very low (< 10 min) | Random search | 10-20 | Quick exploration |
| Low (10-60 min) | Random search | 30-50 | Better coverage |
| Medium (1-4 hours) | Bayesian (Optuna) | 50-200 | Smart exploration |
| High (> 4 hours) | Bayesian + pruning | 200+ | Maximize performance |

## Important Hyperparameters (Ordered by Impact)

For tree-based models:
1. `n_estimators` (use early stopping)
2. `learning_rate`
3. `max_depth` / `num_leaves`
4. `subsample` / `colsample_bytree`
5. `reg_alpha` / `reg_lambda`

For neural networks:
1. `learning_rate` (most critical)
2. `batch_size`
3. `architecture` (depth, width)
4. `dropout` / weight decay
5. `learning rate schedule`

## Common Pitfalls

1. **Tuning too many params at once**: Start with 2-3 most important, then expand
2. **Overfitting to validation set**: Use nested CV for final evaluation
3. **Not using logarithmic scales**: Learning rates, regularization — always log-scale
4. **Ignoring computational cost**: Some configs are much faster — consider accuracy/time
5. **Not setting random seeds**: Results won't be reproducible

## Further Reading

- Bergstra & Bengio (2012) proved random search beats grid search — essential reading
- Optuna's documentation is the best practical guide
- For neural network tuning, see the "population based training" paper (Jaderberg et al., 2017)
- AutoML systems (Auto-sklearn, H2O) automate tuning entirely
