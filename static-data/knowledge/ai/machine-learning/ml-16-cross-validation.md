---
slug: ml-16-cross-validation
title: "Cross-Validation"
description: "The gold standard for model evaluation — k-fold, stratified, nested, and time-series cross-validation."
order: 16
tags:
  - machine-learning
  - evaluation
  - cross-validation
  - model-selection
prerequisites:
  - ml-03-the-learning-problem
  - ml-18-classification-metrics
references:
  - title: "scikit-learn: Cross-Validation User Guide"
    url: "https://scikit-learn.org/stable/modules/cross_validation.html"
    description: "Official documentation with all CV strategies"
  - title: "An Introduction to Statistical Learning, Ch. 5"
    url: "https://www.statlearning.com/"
    url: "https://www.statlearning.com/resources-second-edition"
    description: "Chapter on resampling methods — CV and bootstrap explained clearly"
  - title: "Nested Cross-Selection for Model Selection"
    url: "https://www.jstatsoft.org/article/view/v028i05"
    description: "Cawley & Talbot on the pitfalls of using CV for model selection"
  - title: "A Review of Cross-Validation Methods"
    url: "https://www.researchgate.net/publication/220332215"
    description: "Comprehensive review covering standard and advanced CV methods"
  - title: "Time Series Cross-Validation"
    url: "https://robjhyndman.com/hyndsight/tscv/"
    description: "Rob Hyndman's guide to proper CV for time series data"
knowledge_refs:
  - ml-03-the-learning-problem
  - ml-17-hyperparameter-tuning
  - ml-18-classification-metrics
---

# Cross-Validation

Cross-validation is the standard method for estimating how well a model will generalize to unseen data. It gives you a reliable performance estimate without wasting a test set.

## Why Not a Single Train/Test Split?

A single split has high variance — your performance estimate depends on which specific samples end up in train vs. test. With 1000 samples, a single 80/20 split means your test set has only 200 samples. Different random splits can give wildly different accuracy scores.

Cross-validation reduces this variance by averaging over multiple splits.

## K-Fold Cross-Validation

The most common approach:

1. Split the data into $K$ equal folds
2. For each fold $i$: train on the other $K-1$ folds, evaluate on fold $i$
3. Average the $K$ performance estimates

```python
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

scores = cross_val_score(
    RandomForestClassifier(n_estimators=100),
    X, y, cv=5, scoring='accuracy'
)
print(f"Accuracy: {scores.mean():.3f} ± {scores.std():.3f}")
```

**Standard choice**: $K=5$ or $K=10$. These balance bias (higher $K$ = lower bias) vs. computational cost.

| K | Bias | Variance | Computation |
|---|---|---|---|
| 2 | High | Low variance in estimate | Low |
| 5 | Medium | Medium | Medium |
| 10 | Low | Medium-high | High |
| N (LOO) | Lowest | Highest | Very high |

## Stratified K-Fold

Preserves class proportions in each fold — essential for imbalanced datasets:

```python
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skf)
```

Without stratification, a fold might accidentally have very few positive examples, giving a misleading performance estimate. scikit-learn uses stratified splits by default for classification.

## Leave-One-Out Cross-Validation (LOOCV)

Each fold has exactly one sample. Low bias but very high variance and very expensive:

```python
from sklearn.model_selection import LeaveOneOut

scores = cross_val_score(model, X, y, cv=LeaveOneOut())
```

**When to use LOOCV**: Very small datasets (< 50 samples). For most practical purposes, 5-fold or 10-fold is better.

## Time Series Cross-Validation

Standard k-fold breaks time series — it uses future data to predict the past (data leakage). Use expanding or sliding window:

```python
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=5)
# Fold 1: train=[0], test=[1]
# Fold 2: train=[0,1], test=[2]
# Fold 3: train=[0,1,2], test=[3]
# Fold 4: train=[0,1,2,3], test=[4]
# Fold 5: train=[0,1,2,3,4], test=[5]

scores = cross_val_score(model, X, y, cv=tscv)
```

**Key principles for time series**:
- Never shuffle — always respect temporal order
- Training set always precedes test set
- Consider a gap between train and test to avoid look-ahead bias

## Nested Cross-Validation

When using CV to both tune hyperparameters AND estimate performance, naive approaches leak information. Nested CV separates these concerns:

```python
from sklearn.model_selection import GridSearchCV, cross_val_score, StratifiedKFold

# Inner loop: tune hyperparameters
inner_cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
grid_search = GridSearchCV(
    RandomForestClassifier(),
    param_grid={'max_depth': [5, 10, 20], 'n_estimators': [100, 200]},
    cv=inner_cv,
    scoring='accuracy'
)

# Outer loop: estimate generalization performance
outer_cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
nested_scores = cross_val_score(grid_search, X, y, cv=outer_cv)
print(f"Nested CV: {nested_scores.mean():.3f} ± {nested_scores.std():.3f}")
```

**Why nested?** If you use the same CV for tuning and evaluation, you'll overestimate performance (you're evaluating on data used for selection).

## Repeated K-Fold

Repeats k-fold multiple times with different random splits — reduces variance further:

```python
from sklearn.model_selection import RepeatedStratifiedKFold

rskf = RepeatedStratifiedKFold(n_splits=5, n_repeats=10, random_state=42)
scores = cross_val_score(model, X, y, cv=rskf)
```

## Cross-Validation for Regression

Use the same methods but with regression metrics:

```python
scores = cross_val_score(
    model, X, y, cv=5,
    scoring='neg_mean_squared_error'  # negative because sklearn maximizes
)
rmse_scores = np.sqrt(-scores)
```

## The Leakage Problem

The most common CV mistake is data leakage:

1. **Feature scaling on full data**: Always use a Pipeline
   ```python
   # WRONG: scaler sees test data
   scaler.fit(X)  # leaks!
   cross_val_score(model, X, y, cv=5)
   
   # RIGHT: scaling inside CV loop
   pipeline = Pipeline([('scaler', StandardScaler()), ('model', model)])
   cross_val_score(pipeline, X, y, cv=5)
   ```

2. **Feature selection on full data**: Same issue — select inside CV
3. **Temporal leakage**: Using future data in training (time series)
4. **Group leakage**: Multiple samples from same entity in both train and test

```python
# For grouped data (e.g., multiple samples per patient)
from sklearn.model_selection import GroupKFold
gkf = GroupKFold(n_splits=5)
scores = cross_val_score(model, X, y, groups=patient_ids, cv=gkf)
```

## Practical Guidelines

1. **Use 5-fold stratified** as default for classification
2. **Use time series split** for temporal data
3. **Use nested CV** when selecting models/hyperparameters
4. **Use Pipeline** to prevent leakage from scaling/selection
5. **Report mean ± std** — variance matters as much as mean
6. **10-fold** when you want a more precise estimate and can afford computation
7. **Repeated 10-fold** when you need the most reliable estimate

## Cross-Validation vs. Bootstrap

| Method | Bias | Variance | Use When |
|---|---|---|---|
| 5-fold CV | Slight upward bias | Low | Default |
| 10-fold CV | Very slight bias | Low | Need precise estimate |
| 10×10 repeated CV | Very slight bias | Lowest | Final evaluation |
| Bootstrap .632+ | Low bias | Low | Small datasets |

## Further Reading

- ISLR Chapter 5 covers resampling methods beautifully
- Cawley & Talbot's nested CV paper is essential reading before tuning
- Hyndman's time series CV guide is the authoritative reference for temporal data
- For small datasets, consider the .632+ bootstrap as an alternative to LOO
