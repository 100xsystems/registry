---
slug: ml-10-gradient-boosting
title: "Gradient Boosting"
description: "The most powerful algorithm for tabular data — XGBoost, LightGBM, and CatBoost dominate Kaggle competitions and production ML."
order: 10
tags:
  - machine-learning
  - gradient-boosting
  - xgboost
  - lightgbm
  - catboost
prerequisites:
  - ml-08-decision-trees
  - ml-06-gradient-descent
  - ml-09-ensemble-methods
references:
  - title: "XGBoost: A Scalable Tree Boosting System"
    url: "https://arxiv.org/abs/1603.02754"
    description: "The original XGBoost paper by Tianqi Chen"
  - title: "LightGBM: A Highly Efficient Gradient Boosting Decision Tree"
    url: "https://arxiv.org/abs/1711.08229"
    description: "The LightGBM paper by Microsoft Research"
  - title: "CatBoost: unbiased boosting with categorical features"
    url: "https://arxiv.org/abs/1706.03662"
    description: "The CatBoost paper by Yandex with native categorical support"
  - title: "XGBoost Documentation"
    url: "https://xgboost.readthedocs.io/"
    description: "Official XGBoost docs with API reference and tutorials"
  - title: "Gradient Boosting: From First Principles"
    url: "https://explained.ai/gradient-boosting/"
    description: "A deep mathematical treatment of gradient boosting from first principles"
knowledge_refs:
  - ml-08-decision-trees
  - ml-09-ensemble-methods
  - ml-06-gradient-descent
---

# Gradient Boosting

Gradient boosting is the most powerful algorithm for structured/tabular data. It dominates Kaggle competitions, credit scoring, recommendation systems, and any domain with labeled tabular data. Understanding gradient boosting is essential for any ML practitioner.

## The Core Idea

While random forests build trees **independently**, gradient boosting builds them **sequentially** — each new tree corrects the errors of the previous ensemble:

$$F_m(x) = F_{m-1}(x) + \eta \cdot h_m(x)$$

where:
- $F_{m-1}(x)$ is the current ensemble prediction
- $h_m(x)$ is the new tree (the "weak learner")
- $\eta$ is the **learning rate** (shrinkage)
- $F_0(x)$ is typically the mean of the target

The new tree $h_m(x)$ is trained on the **pseudo-residuals** — the negative gradient of the loss with respect to the current predictions:

$$r_{im} = -\frac{\partial \mathcal{L}(y_i, F(x_i))}{\partial F(x_i)} \bigg|_{F=F_{m-1}}$$

For squared error loss, pseudo-residuals are just the actual residuals $(y_i - F_{m-1}(x_i))$. For other losses, they're the gradient of that loss.

## Gradient Descent in Function Space

This is why it's called **gradient** boosting — it performs gradient descent in function space:

1. Start with a simple function $F_0$ (mean for regression, log-odds for classification)
2. Compute pseudo-residuals (gradient of loss)
3. Fit a tree to the pseudo-residuals
4. Update: $F_m = F_{m-1} + \eta \cdot h_m$
5. Repeat until convergence

The learning rate $\eta$ (typically 0.01-0.3) shrinks each tree's contribution, making the model more robust and less prone to overfitting.

## The Gradient Boosting Algorithm

```
Initialize F₀(x) = argmin_γ Σ L(yᵢ, γ)

For m = 1 to M:
  1. Compute pseudo-residuals:
     rᵢₘ = -∂L(yᵢ, F(xᵢ)) / ∂F(xᵢ) |_{F=Fₘ₋₁}
  
  2. Fit a regression tree hₘ(x) to rᵢₘ
  
  3. For each leaf j of hₘ, find optimal output:
     γⱼₘ = argmin_γ Σ_{xᵢ∈leaf_j} L(yᵢ, Fₘ₋₁(xᵢ) + γ)
  
  4. Update: Fₘ(x) = Fₘ₋₁(x) + η · hₘ(x)
```

## XGBoost

XGBoost (Extreme Gradient Boosting) added several critical improvements:

**Regularized objective:**
$$\mathcal{L} = \sum_i l(y_i, \hat{y}_i) + \sum_k \Omega(f_k)$$

where $\Omega(f) = \gamma T + \frac{1}{2}\lambda \sum_{j=1}^{T} w_j^2$ penalizes tree complexity (number of leaves $T$ and leaf weights).

**Column subsampling**: Like random forests, each tree considers only a random subset of features — reduces overfitting and speeds up training.

**Exact greedy and approximate algorithms**: Efficient split-finding even on large datasets.

```python
import xgboost as xgb

# For classification
model = xgb.XGBClassifier(
    n_estimators=500,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_alpha=0.1,      # L1 regularization
    reg_lambda=1.0,     # L2 regularization
    eval_metric='logloss',
    early_stopping_rounds=50,
    random_state=42
)
model.fit(X_train, y_train, eval_set=[(X_val, y_val)], verbose=False)
```

## LightGBM

LightGBM (Microsoft, 2017) is optimized for speed and memory:

**Gradient-based One-Side Sampling (GOSS)**: Keeps instances with large gradients, randomly samples small gradients — fewer data points per split.

**Exclusive Feature Bundling (EFB)**: Bundles mutually exclusive features (never non-zero together) — fewer features to consider.

**Leaf-wise growth**: Instead of level-wise (all leaves at same depth), grows the leaf with highest loss reduction. Faster convergence but can overfit without `max_depth`.

```python
import lightgbm as lgb

model = lgb.LGBMClassifier(
    n_estimators=500,
    num_leaves=31,
    learning_rate=0.05,
    feature_fraction=0.8,
    bagging_fraction=0.8,
    bagging_freq=5,
    lambda_l1=0.1,
    lambda_l2=1.0,
    random_state=42
)
model.fit(X_train, y_train, eval_set=[(X_val, y_val)],
          callbacks=[lgb.early_stopping(50)])
```

## CatBoost

CatBoost (Yandex, 2017) specializes in **categorical features**:

**Ordered boosting**: Processes data in a random order, using only "previous" samples for target statistics — eliminates target leakage.

**Ordered target statistics**: Encodes categoricals using running averages without leaking test information.

```python
import catboost as cb

model = cb.CatBoostClassifier(
    iterations=500,
    depth=6,
    learning_rate=0.05,
    l2_leaf_reg=3,
    cat_features=categorical_columns,
    verbose=False
)
model.fit(X_train, y_train, eval_set=(X_val, y_val), early_stopping_rounds=50)
```

## When to Use Which

| Scenario | Best Choice |
|---|---|
| General tabular data | XGBoost or LightGBM |
| Many categorical features | CatBoost |
| Very large dataset (>1M rows) | LightGBM (fastest) |
| Small dataset | XGBoost with strong regularization |
| Need GPU acceleration | XGBoost or LightGBM (both support GPU) |
| Quick iteration | LightGBM (fastest training) |

## Tuning Guide

The most important hyperparameters, in order:

1. **`n_estimators`** (use early stopping)
2. **`learning_rate`** (lower = better, but more trees needed)
3. **`max_depth`** or **`num_leaves`** (controls tree complexity)
4. **`subsample`** / **`colsample_bytree`** (randomness for regularization)
5. **`reg_alpha`** / **`reg_lambda`** (L1/L2 regularization)

**Practical tuning strategy:**
```python
# 1. Set learning_rate=0.1, n_estimators=1000, use early_stopping
# 2. Tune max_depth (3-10) and num_leaves
# 3. Tune subsample and colsample_bytree (0.5-1.0)
# 4. Lower learning_rate to 0.01, increase n_estimators
# 5. Tune regularization
```

## Strengths

- **State-of-the-art on tabular data**: Wins most Kaggle tabular competitions
- **Handles mixed features**: Numerical + categorical + missing
- **Feature importance**: Built-in, permutation, and SHAP-based
- **Missing values**: Native handling (learns optimal direction)
- **Fast**: LightGBM can train millions of rows in seconds
- **GPU support**: All major implementations support GPU

## Limitations

- **Not for images/text**: Neural networks dominate for unstructured data
- **Prone to overfitting**: Requires careful regularization
- **Sequential training**: Harder to parallelize than random forests
- **Black box**: Harder to interpret than single trees or linear models
- **Doesn't extrapolate**: Predictions are bounded by training range

## Further Reading

- Chen & Guestrin (2016) introduced XGBoost — the most cited ML system paper
- Ke et al. (2017) introduced LightGBM with GOSS and EFB
- Prokhorenkova et al. (2018) introduced CatBoost's ordered boosting
- The explained.ai treatment provides a rigorous mathematical foundation
- SHAP (Lundberg & Lee, 2017) explains gradient boosting models — essential for interpretability
