---
{
  "title": "Regression Models",
  "description": "Predict continuous values with linear and regularized regression, and read the results honestly.",
  "type": "lesson",
  "order": 15,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Fit and interpret linear regression",
    "Explain coefficients and their limits",
    "Apply ridge and lasso regularization",
    "Evaluate regression with R² and RMSE"
  ],
  "knowledge_refs": [
    "machine-learning/ml-05-linear-regression",
    "machine-learning/ml-15-regularization",
    "data-science/ds-14-train-test-split"
  ],
  "prerequisites": [
    "DS-14: Train/Test Splits & Validation"
  ],
  "references": [
    {
      "title": "scikit-learn — Linear Models",
      "url": "https://scikit-learn.org/stable/modules/linear_model.html",
      "description": "Official docs for LinearRegression, Ridge, Lasso and more."
    },
    {
      "title": "The Elements of Statistical Learning — Chapter 3",
      "url": "https://hastie.su.domains/ElemStatLearn/",
      "description": "The classic free textbook treatment of linear regression and shrinkage."
    },
    {
      "title": "OpenIntro Statistics — Linear Regression (Chapter 7)",
      "url": "https://www.openintro.org/book/os/",
      "description": "Accessible introduction to regression modeling."
    },
    {
      "title": "Python Data Science Handbook — Regression",
      "url": "https://jakevdp.github.io/PythonDataScienceHandbook/",
      "description": "Practical scikit-learn regression examples."
    }
  ]
}
---

# DS-15-REGRESSION-MODELS: Regression Models

## Introduction

**Regression** predicts a *continuous* target — price, revenue, temperature, wait time — from features. The workhorse is **linear regression**: model the target as a weighted sum of the features plus an intercept. It is the most interpretable model in data science: each coefficient directly tells you "a one-unit increase in this feature changes the prediction by this much." This lesson covers fitting linear models, reading coefficients responsibly, and the regularized variants (ridge/lasso) that keep them stable.

## Key Concepts

### 1. The linear model

```
y = β₀ + β₁x₁ + β₂x₂ + ... + βₚxₚ + ε
```

- `y` is the target, `xⱼ` the features, `βⱼ` the coefficients, `ε` the irreducible error.
- Fitting = choosing the `β`s that minimize the sum of squared errors (least squares).

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
model = LinearRegression().fit(X_train, y_train)

print(model.coef_)       # one coefficient per feature
print(model.intercept_)
print(model.score(X_test, y_test))   # R² on unseen data
```

### 2. Reading coefficients honestly

Three traps when interpreting coefficients:

1. **Units**: "increase of β" is per *one unit of that feature*. If you standardize features first, coefficients become comparable across features (which feature matters most).
2. **"All else equal"**: β measures the effect of xⱼ *holding other features constant* — but features are usually correlated, so "all else equal" is often a fiction.
3. **Correlation, not causation**: a significant coefficient is an association, not proof of causality (see the correlation lesson).

### 3. Evaluating regression: R² and RMSE

- **R²** (score): the fraction of target variance explained, 0→1 (can go negative on terrible models). "Explains 78% of the variance."
- **RMSE**: the typical error in the target's units. RMSE 4.2 on prices in dollars means "typically off by ~$4.20."
- **MAE**: median-style error, robust to outliers.

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

preds = model.predict(X_test)
print(r2_score(y_test, preds))
print(mean_squared_error(y_test, preds, squared=False))   # RMSE
print(mean_absolute_error(y_test, preds))
```

Use RMSE when large errors are especially bad; MAE when you want the typical error.

### 4. Regularization: ridge and lasso

Plain least squares can overfit when features are many or correlated — coefficients blow up to chase noise. **Regularization** adds a penalty for large coefficients:

- **Ridge** (L2): shrinks coefficients toward zero but never exactly to zero. Good when most features matter a little.
- **Lasso** (L1): can set coefficients *exactly* to zero — a built-in feature selector. Good when you suspect many features are useless.

```python
from sklearn.linear_model import Ridge, Lasso

ridge = Ridge(alpha=1.0).fit(X_train, y_train)
lasso = Lasso(alpha=0.1).fit(X_train, y_train)
```

`alpha` controls penalty strength — tune it with cross-validation (`RidgeCV`, `LassoCV`). Regularized models almost always beat plain linear regression on real data.

### 5. When linear models fail — and what to do

Linear regression assumes a roughly linear, additive relationship. When that fails:

- Log-transform skewed targets (prices, counts).
- Add polynomial or interaction features (see feature engineering).
- Switch to tree-based models (random forest, gradient boosting — covered in the ML course), which capture non-linear relationships with no scaling needed.

## Practice Questions

1. Fit a linear regression on any dataset and interpret one coefficient in plain language.
2. Why do standardized coefficients make features comparable?
3. What does R² = 0.78 mean? When can R² be misleading?
4. When would you choose lasso over ridge?

## LLM Prompts for Deeper Understanding

1. "Explain least squares vs ridge vs lasso with a visual intuition."
2. "What are the assumptions of linear regression, and how do I check them?"
3. "How do I interpret a regression coefficient when features are correlated?"

## Key Takeaways

- Linear regression predicts continuous targets as a weighted sum of features.
- Coefficients are per-unit, all-else-equal associations — not causes.
- R² (variance explained) and RMSE (typical error) are the core metrics.
- Ridge shrinks coefficients; lasso also selects features by zeroing them.
- Use transforms and trees when the relationship is non-linear.

## Footnotes & Attribution

1. scikit-learn documentation, *Linear Models*. [https://scikit-learn.org/stable/modules/linear_model.html](https://scikit-learn.org/stable/modules/linear_model.html)
2. Hastie, Tibshirani, Friedman, *The Elements of Statistical Learning* (Ch. 3). Free PDF. [https://hastie.su.domains/ElemStatLearn/](https://hastie.su.domains/ElemStatLearn/)
3. Diez, Barr, Çetinkaya-Rundel, *OpenIntro Statistics* (Ch. 7). [https://www.openintro.org/book/os/](https://www.openintro.org/book/os/)
4. Jake VanderPlas, *Python Data Science Handbook* — regression. [https://jakevdp.github.io/PythonDataScienceHandbook/](https://jakevdp.github.io/PythonDataScienceHandbook/)
