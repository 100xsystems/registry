---
{
  "title": "Feature Engineering",
  "description": "Turn raw data into features models can learn from: encodings, scaling, transforms and derived variables.",
  "type": "lesson",
  "order": 13,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Encode categorical variables appropriately",
    "Scale and transform numeric features",
    "Create derived and date-based features",
    "Handle missing values as features"
  ],
  "knowledge_refs": [
    "data-science/ds-06-data-cleaning",
    "machine-learning/ml-14-feature-scaling-and-selection",
    "data-science/ds-14-train-test-split"
  ],
  "prerequisites": [
    "DS-12: Correlation & Causation"
  ],
  "references": [
    {
      "title": "Feature Engineering for Machine Learning — Zheng & Casari (O'Reilly)",
      "url": "https://www.oreilly.com/library/view/feature-engineering-for/9781491953235/",
      "description": "The foundational text on transforming raw data into model-ready features."
    },
    {
      "title": "scikit-learn — Feature Extraction",
      "url": "https://scikit-learn.org/stable/modules/feature_extraction.html",
      "description": "Official docs for text, categorical and image feature extraction."
    },
    {
      "title": "scikit-learn — Encoding Categorical Features",
      "url": "https://scikit-learn.org/stable/modules/preprocessing.html",
      "description": "OneHotEncoder, OrdinalEncoder and target encoding guidance."
    },
    {
      "title": "Feature Engineering — Kaggle Learn",
      "url": "https://www.kaggle.com/learn/feature-engineering",
      "description": "Hands-on micro-course with practical techniques."
    }
  ]
}
---

# DS-13-FEATURE-ENGINEERING: Feature Engineering

## Introduction

Models are only as good as the features you feed them. **Feature engineering** is the craft of turning raw data — categories, dates, text, numbers with missing values — into the numeric representations models can actually learn from. The creators of the O'Reilly book on the subject put it simply: "features determine the maximum performance a model can achieve; algorithms only approximate that ceiling" [1]. This lesson covers the essential transformations you'll use on almost every tabular project.

## Key Concepts

### 1. Encoding categorical variables

Most models need numbers, not strings. The two core encodings:

```python
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.DataFrame({"city": ["ny", "sf", "ny", "la"]})

# 1) One-hot: one binary column per category (no ordinal meaning)
enc = OneHotEncoder(sparse_output=False)
onehot = enc.fit_transform(df[["city"]])
print(onehot)                      # 4 rows x 3 city columns

# 2) Ordinal: integers for *ordered* categories (e.g., low < medium < high)
from sklearn.preprocessing import OrdinalEncoder
ord_enc = OrdinalEncoder(categories=[["low", "medium", "high"]])
```

Rules of thumb: **one-hot** for unordered categories (cities, plans); **ordinal** only for genuinely ordered levels; **target encoding** (mean of target per category) when a category has many levels and you can guard against overfitting — Kaggle's course covers the trade-offs [4].

### 2. Scaling numeric features

Models like KNN, SVM, and gradient descent treat feature *units* as meaningful — so features on wildly different scales (age ~30, income ~60000) must be standardized:

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

X = df[["age", "income"]]
X_scaled = StandardScaler().fit_transform(X)   # mean 0, std 1 — the default
X_norm = MinMaxScaler().fit_transform(X)       # range [0, 1]
```

Tree-based models (random forests, gradient boosting) are *scale-invariant* — you can skip scaling for them. This is why "do I need to scale?" depends on the algorithm, covered in detail in the Machine Learning course.

### 3. Transforms: taming skew and revealing structure

- **Log transform** on right-skewed positive features (prices, revenue) makes them more normal and often improves linear models.
- **Polynomial features** (`X²`, `X·Y`) let linear models capture curvature and interactions.

```python
df["log_revenue"] = np.log1p(df["revenue"])     # log(1+x): safe for zeros
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(df[["age", "orders"]])  # adds age², orders², age*orders
```

### 4. Date and derived features

Dates are rich but rarely useful raw. The standard decomposition:

```python
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["dow"] = df["date"].dt.dayofweek          # 0=Monday
df["hour"] = df["date"].dt.hour              # for timestamps
df["days_since_signup"] = (df["date"] - df["signup_date"]).dt.days
```

Derived features encode *domain knowledge*: for a churn model, "days since last order" and "orders in last 30 days" are often more predictive than any raw column.

### 5. Missing values as features

Instead of only imputing, preserve the information that a value was missing:

```python
df["income_missing"] = df["income"].isna().astype(int)
df["income"] = df["income"].fillna(df["income"].median())
```

For some problems, the *fact of missingness* is itself predictive (e.g., users who skip filling income differ from those who don't).

## Practice Questions

1. When would you use one-hot vs ordinal encoding? Give an example of each.
2. Why does scaling matter for KNN but not for random forests?
3. Create three derived features from a `signup_date` and `last_active` pair.
4. Why add an `income_missing` indicator if you're already imputing income?

## LLM Prompts for Deeper Understanding

1. "Explain target encoding with an example, and how to prevent it from overfitting."
2. "Show me a feature-engineering checklist for a tabular churn dataset."
3. "When do polynomial features help, and when do they hurt?"

## Key Takeaways

- Features cap model performance; algorithms only approach that ceiling.
- One-hot unordered categories; ordinal for ordered ones; target encoding for high-cardinality.
- Standardize for distance-based models; skip scaling for trees.
- Log transforms tame skew; polynomial features add curvature.
- Decompose dates; build domain-derived features; keep missingness as an indicator.

## Footnotes & Attribution

1. Alice Zheng & Amanda Casari, *Feature Engineering for Machine Learning* (O'Reilly). [https://www.oreilly.com/library/view/feature-engineering-for/9781491953235/](https://www.oreilly.com/library/view/feature-engineering-for/9781491953235/)
2. scikit-learn documentation, *Feature Extraction*. [https://scikit-learn.org/stable/modules/feature_extraction.html](https://scikit-learn.org/stable/modules/feature_extraction.html)
3. scikit-learn documentation, *Preprocessing and Encoding*. [https://scikit-learn.org/stable/modules/preprocessing.html](https://scikit-learn.org/stable/modules/preprocessing.html)
4. Kaggle Learn, *Feature Engineering*. [https://www.kaggle.com/learn/feature-engineering](https://www.kaggle.com/learn/feature-engineering)
