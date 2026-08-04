{
  "title": "Linear Regression",
  "description": "Master the most fundamental ML algorithm: ordinary least squares, R-squared, model assumptions, and practical diagnostics.",
  "type": "lesson",
  "order": 5,
  "duration": "50 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Derive and implement simple and multiple linear regression",
    "Compute and interpret R-squared and adjusted R-squared",
    "Understand the assumptions of linear regression and how to check them",
    "Diagnose and address multicollinearity"
  ],
  "knowledge_refs": [
    "machine-learning/ml-01-what-is-machine-learning",
    "machine-learning/ml-06-gradient-descent",
    "machine-learning/ml-15-regularization"
  ],
  "prerequisites": ["ML-04: The Python ML Stack"],
  "references": [
    {
      "title": "StatQuest: Linear Regression — Josh Starmer",
      "url": "https://www.youtube.com/watch?v=7ArmBVF2dCs",
      "description": "The best intuitive explanation of linear regression, with clear visual examples of line fitting and R-squared."
    },
    {
      "title": "scikit-learn LinearRegression Documentation",
      "url": "https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares",
      "description": "Official scikit-learn documentation on linear regression with code examples and mathematical details."
    },
    {
      "title": "ISLR Chapter 3: Linear Regression",
      "url": "https://www.statlearning.com/",
      "description": "Clear textbook treatment of linear regression including assumptions, diagnostics, and extensions."
    },
    {
      "title": "Linearity Assumption in Linear Regression — Towards Data Science",
      "url": "https://towardsdatascience.com/linear-regression-101-b8b4446b84d2",
      "description": "Practical guide to checking and addressing violations of linear regression assumptions."
    },
    {
      "title": "Multiple Regression — Penn State STAT 501",
      "url": "https://online.stat.psu.edu/stat501/",
      "description": "Comprehensive online course covering multiple regression with real datasets and R code."
    }
  ]
}
---

Linear regression is the "hello world" of machine learning. It's simple, interpretable, and surprisingly powerful. Understanding it deeply — including its limitations — is essential before moving to more complex algorithms.

---

## Simple Linear Regression

The simplest case: predict a continuous target `y` from a single feature `x` using a straight line.

### The Model

```
y = β₀ + β₁x + ε
```

Where:
- `β₀` is the **intercept** (y-value when x = 0)
- `β₁` is the **slope** (change in y per unit change in x)
- `ε` is the **error term** (noise we can't explain)

### Finding the Best Line

The "best" line minimizes the **sum of squared residuals** (SSR):

```
SSR = Σ(yᵢ - ŷᵢ)²
```

This is the **ordinary least squares** (OLS) solution. The closed-form solution for the slope is:

```
β₁ = Σ(xᵢ - x̄)(yᵢ - ȳ) / Σ(xᵢ - x̄)²
```

And the intercept: `β₀ = ȳ - β₁x̄`

### Code Example

```python
import numpy as np
from sklearn.linear_model import LinearRegression

# Simple linear regression
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

model = LinearRegression()
model.fit(X, y)

print(f"Intercept: {model.intercept_:.2f}")
print(f"Slope: {model.coef_[0]:.2f}")
print(f"R²: {model.score(X, y):.3f}")
```

---

## Multiple Linear Regression

When you have more than one feature, the model extends naturally:

```
y = β₀ + β₁x₁ + β₂x₂ + ... + βₚxₚ + ε
```

Each coefficient `βⱼ` represents the change in `y` for a one-unit change in `xⱼ`, **holding all other features constant** (this is why it's called "multiple" — not "multivariate").

### The Normal Equation

For multiple regression, the OLS solution uses matrix algebra:

```
β̂ = (XᵀX)⁻¹Xᵀy
```

Where `X` is the design matrix (features with a column of 1s for the intercept).

### Code Example

```python
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load housing data
df = pd.read_csv('housing.csv')
X = df[['sqft', 'bedrooms', 'age']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

print("Coefficients:")
for name, coef in zip(X.columns, model.coef_):
    print(f"  {name}: ${coef:,.0f}")
print(f"R²: {model.score(X, y):.3f}")
```

---

## R-Squared: How Well Does Your Model Fit?

R-squared (R²) measures the proportion of variance in the target explained by the model:

```
R² = 1 - SSR/SST
```

Where SST (total sum of squares) = Σ(yᵢ - ȳ)² is the variance of y around its mean.

### Interpretation

- **R² = 1.0**: Perfect prediction (all variance explained)
- **R² = 0.7**: Model explains 70% of the variance
- **R² = 0.0**: Model explains nothing (as good as predicting the mean)
- **R² < 0**: Model is worse than predicting the mean (something is wrong)

### The Trap of R²

Adding more features **always increases R²**, even if they're irrelevant. This is misleading. Use **adjusted R²** instead:

```
Adjusted R² = 1 - (1 - R²)(n - 1)/(n - p - 1)
```

Where `n` is the number of samples and `p` is the number of features. Adjusted R² penalizes unnecessary features.

---

## Assumptions of Linear Regression

Linear regression only works well when certain assumptions hold. Violating these assumptions doesn't make the model "wrong," but it makes the statistical inferences unreliable.

### 1. Linearity

The relationship between features and target is linear.

**Check**: Plot residuals vs. predicted values. If there's a pattern (curve, funnel), the linearity assumption is violated.

**Fix**: Add polynomial features, use log transforms, or switch to a nonlinear model.

### 2. Independence of Errors

Residuals are independent — no autocorrelation.

**Check**: Durbin-Watson test (values near 2 = good, near 0 or 4 = problem).

**Common in**: Time series data, where today's error is correlated with yesterday's.

### 3. Homoscedasticity

Residuals have constant variance across all predicted values.

**Check**: Plot residuals vs. predicted values. A funnel shape (fan out or fan in) indicates heteroscedasticity.

**Fix**: Weighted least squares, log transform the target, or use robust standard errors.

### 4. Normality of Errors

Residuals are normally distributed.

**Check**: Q-Q plot or Shapiro-Wilk test.

**Why it matters**: Affects confidence intervals and hypothesis tests, not prediction accuracy.

### 5. No Multicollinearity

Features are not highly correlated with each other.

**Check**: Variance Inflation Factor (VIF). VIF > 10 indicates serious multicollinearity.

**Fix**: Remove one of the correlated features, combine them, or use regularization.

---

## Multicollinearity: The Silent Killer

When two or more features are highly correlated, the model can't determine which one is responsible for the effect on the target. This inflates coefficient standard errors, making them unreliable.

### Example

Predicting house price using both "square footage" and "number of rooms." These are highly correlated — larger houses have more rooms. The model can't tell whether the price increase is due to size or room count.

### Detection

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Compute VIF for each feature
vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) 
                    for i in range(X.shape[1])]
print(vif_data)
```

### Solutions

1. **Remove one** of the correlated features
2. **Combine them** into a single feature (e.g., rooms_per_sqft)
3. **Use Ridge regression** (L2 regularization shrinks correlated coefficients)
4. **PCA** to create uncorrelated principal components

---

## Practical Workflow

```python
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 1. Load and inspect
df = pd.read_csv('housing.csv')
print(df.describe())
print(df.corr())  # Check correlations

# 2. Split data
X = df.drop('price', axis=1)
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 3. Train
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Evaluate
y_pred = model.predict(X_test)
print(f"R²: {r2_score(y_test, y_pred):.3f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):,.0f}")

# 5. Diagnose
residuals = y_test - y_pred
plt.scatter(y_pred, residuals)
plt.xlabel('Predicted')
plt.ylabel('Residuals')
plt.axhline(y=0, color='r', linestyle='--')
plt.title('Residual Plot')
plt.show()
```

---

## When Linear Regression Fails

- **Nonlinear relationships**: Use polynomial features or nonlinear models
- **Outliers**: OLS is sensitive to outliers; use robust regression
- **Categorical targets**: Use logistic regression instead
- **Complex interactions**: Use tree-based models or neural networks
- **High dimensionality**: Use regularization (Ridge, Lasso, Elastic Net)

---

## Key Takeaways

- Linear regression finds the best straight line through data using OLS
- R² measures explained variance; use adjusted R² for model comparison
- Five key assumptions: linearity, independence, homoscedasticity, normality, no multicollinearity
- Always check assumptions with residual plots and VIF
- Linear regression is the foundation — understand it before moving to complex models

---

## References

1. **StatQuest: Linear Regression** — Josh Starmer. Best intuitive explanation with visual examples. https://www.youtube.com/watch?v=7ArmBVF2dCs
2. **scikit-learn LinearRegression** — Official documentation with code examples. https://scikit-learn.org/stable/modules/linear_model.html
3. **ISLR Chapter 3** — James et al. Textbook treatment of linear regression. https://www.statlearning.com/
4. **Linearity Assumption Guide** — Towards Data Science. Practical diagnostics. https://towardsdatascience.com/linear-regression-101-b8b4446b84d2
5. **STAT 501: Multiple Regression** — Penn State. Comprehensive online course. https://online.stat.psu.edu/stat501/

---

## Footnotes

The OLS estimator was independently developed by Legendre (1805) and Gauss (1809). Gauss showed that OLS is the best linear unbiased estimator (BLUE) under the Gauss-Markov theorem when the assumptions hold. The practical diagnostics section draws on Kutner et al.'s *Applied Linear Statistical Models* (2005).
