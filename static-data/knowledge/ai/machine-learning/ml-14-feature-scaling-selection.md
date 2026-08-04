---
slug: ml-14-feature-scaling-selection
title: "Feature Scaling & Selection"
description: "Preprocessing is not glamorous but critical — scaling prevents algorithms from breaking, and selection removes noise."
order: 14
tags:
  - machine-learning
  - preprocessing
  - feature-scaling
  - feature-selection
  - standardization
prerequisites:
  - ml-03-the-learning-problem
  - ml-06-gradient-descent
references:
  - title: "scikit-learn: Preprocessing Data"
    url: "https://scikit-learn.org/stable/modules/preprocessing.html"
    description: "Official documentation on scaling, encoding, and feature transformation"
  - title: "Feature Engineering and Selection (Kuhn & Johnson)"
    url: "https://bookdown.org/max/FES/"
    description: "Free online book covering feature scaling, selection, and engineering"
  - title: "An Introduction to Feature Selection (Guyon & Elisseeff)"
    url: "https://jmlr.org/papers/v3/guyon03a.html"
    description: "Foundational survey on feature selection methods"
  - title: "When to Standardize: A Practical Guide"
    url: "https://scikit-learn.org/stable/modules/preprocessing.html#standardization-or-mean-removal-and-variance-scaling"
    description: "When scaling helps and when it doesn't"
  - title: "Mutual Information for Feature Selection"
    url: "https://scikit-learn.org/stable/modules/feature_selection.html"
    description: "scikit-learn's feature selection guide with MI, chi², and RFE"
knowledge_refs:
  - ml-15-regularization
  - ml-06-gradient-descent
  - ml-12-k-nearest-neighbors
---

# Feature Scaling & Selection

Feature preprocessing is unglamorous but **critical**. Wrong scaling can break algorithms; irrelevant features add noise. These two steps — scaling and selection — often matter more than model choice.

## Why Feature Scaling Matters

Many ML algorithms are **not** invariant to feature scales:

| Scale-Invariant | Scale-Sensitive |
|---|---|
| Decision Trees | K-Nearest Neighbors |
| Random Forests | Support Vector Machines |
| XGBoost / LightGBM | Neural Networks |
| Naive Bayes | Linear/Logistic Regression (with L1/L2) |
| | PCA, K-Means, gradient descent |

**Example**: If feature A ranges [0, 1] and feature B ranges [0, 100000], distance-based methods will only "see" feature B. Gradient descent will have elongated, zig-zagging contours.

## Standardization (Z-score)

Transforms each feature to mean 0, standard deviation 1:

$$z = \frac{x - \mu}{\sigma}$$

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fit on train, transform train
X_test_scaled = scaler.transform(X_test)  # only transform test!
```

**When to use**: Default choice for most algorithms. Works well when features are approximately Gaussian.

**⚠️ Critical**: Fit the scaler on training data only, then transform both train and test. Never fit on the full dataset — this leaks test information.

## Normalization (Min-Max)

Scales features to [0, 1]:

$$x_{\text{norm}} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$$

```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()  # scales to [0, 1]
```

**When to use**: When you need bounded values (neural network inputs, image pixels). Sensitive to outliers.

## Robust Scaling

Uses median and IQR instead of mean and std — robust to outliers:

$$x_{\text{robust}} = \frac{x - \text{median}}{Q_3 - Q_1}$$

```python
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()  # uses median and IQR
```

**When to use**: Data with significant outliers. Never use MinMaxScaler with outliers — they compress the useful range.

## Power Transformations

Make data more Gaussian-shaped, which helps many algorithms:

**Yeo-Johnson** (handles zeros and negatives):
```python
from sklearn.preprocessing import PowerTransformer
pt = PowerTransformer(method='yeo-johnson')
```

**Box-Cox** (positive values only):
```python
pt = PowerTransformer(method='box-cox')
```

## When NOT to Scale

- **Tree-based models** (Random Forest, XGBoost, LightGBM): Scale-invariant
- **Models with built-in regularization**: Regularization handles scale
- **Sparse data with mostly zeros**: Scaling would destroy sparsity
- **When interpretability of raw features matters**: Don't scale if you need to explain coefficients in original units

## Feature Selection Methods

Removing irrelevant or redundant features improves model performance, reduces overfitting, and speeds up training.

### Filter Methods (Fast, Model-Agnostic)

Select features based on statistical tests, independent of the model:

**Variance Threshold** (remove low-variance features):
```python
from sklearn.feature_selection import VarianceThreshold
selector = VarianceThreshold(threshold=0.01)  # remove near-constant features
X_selected = selector.fit_transform(X)
```

**Mutual Information** (measures dependency between feature and target):
```python
from sklearn.feature_selection import mutual_info_classif, SelectKBest

selector = SelectKBest(mutual_info_classif, k=20)  # top 20 features
X_selected = selector.fit_transform(X, y)
```

**Chi-squared** (for non-negative features, e.g., word counts):
```python
from sklearn.feature_selection import chi2

selector = SelectKBest(chi2, k=1000)
X_selected = selector.fit_transform(X, y)  # X must be non-negative
```

**Correlation-based**: Remove features highly correlated with each other (multicollinearity).

### Wrapper Methods (Model-Specific, Slower)

Use the model's performance to evaluate feature subsets:

**Recursive Feature Elimination (RFE)**:
```python
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier

rfe = RFE(estimator=RandomForestClassifier(n_estimators=100),
          n_features_to_select=20, step=5)
X_selected = rfe.fit_transform(X, y)
```

### Embedded Methods (Built Into the Model)

**L1 regularization** (Lasso) sets some feature weights to exactly zero:
```python
from sklearn.linear_model import LassoCV

lasso = LassoCV(cv=5)
lasso.fit(X_train, y_train)
important_features = X_train.columns[lasso.coef_ != 0]
```

**Tree-based feature importance**:
```python
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100).fit(X, y)
importances = rf.feature_importances_
top_features = importances.argsort()[-20:]  # top 20
```

## The Pipeline

Always put scaling and selection in a pipeline to prevent data leakage:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.ensemble import RandomForestClassifier

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('selector', SelectKBest(mutual_info_classif, k=50)),
    ('classifier', RandomForestClassifier(n_estimators=200))
])

# Cross-validation sees properly scaled + selected features
from sklearn.model_selection import cross_val_score
scores = cross_val_score(pipeline, X, y, cv=5)
```

## Practical Guidelines

| Algorithm | Scaling? | Selection? |
|---|---|---|
| KNN | Required | Helpful |
| SVM | Required | Helpful |
| Linear/Logistic (with L2) | Recommended | Optional |
| Linear/Logistic (with L1) | Recommended | Built-in |
| Decision Trees | Not needed | Not needed |
| Random Forest | Not needed | Optional (for speed) |
| XGBoost/LightGBM | Not needed | Optional (for speed) |
| Neural Networks | Required | Helpful |

## Common Mistakes

1. **Scaling on the full dataset**: Leaks test information — fit only on train
2. **Scaling binary features**: Usually unnecessary, can hurt interpretability
3. **Ignoring outliers**: MinMaxScaler is destroyed by outliers — use RobustScaler
4. **Selecting features before splitting**: Feature selection must use only training data
5. **Over-selecting**: Too many filters can remove useful features — cross-validate

## Further Reading

- Kuhn & Johnson's "Feature Engineering and Selection" is the definitive free resource
- Guyon & Elisseeff's survey covers the theoretical foundations
- For high-dimensional feature selection, look into Boruta (all-relevant feature selection)
- SHAP values can also guide feature importance in a model-agnostic way
