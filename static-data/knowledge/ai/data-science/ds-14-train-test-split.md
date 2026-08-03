---
{
  "title": "Train/Test Splits & Validation",
  "description": "Split data honestly, avoid leakage, and use holdout sets and cross-validation to measure real performance.",
  "type": "lesson",
  "order": 14,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain why the test set must never touch training",
    "Perform train/test and train/validation/test splits",
    "Identify and avoid data leakage",
    "Use k-fold cross-validation"
  ],
  "knowledge_refs": [
    "machine-learning/ml-16-cross-validation",
    "data-science/ds-18-model-evaluation",
    "data-science/ds-13-feature-engineering"
  ],
  "prerequisites": [
    "DS-13: Feature Engineering"
  ],
  "references": [
    {
      "title": "scikit-learn — Cross-Validation",
      "url": "https://scikit-learn.org/stable/modules/cross_validation.html",
      "description": "The official guide to train/test splits, KFold and model selection."
    },
    {
      "title": "Common Pitfalls in ML — Data Leakage (Google)",
      "url": "https://developers.google.com/machine-learning/crash-course/overfitting",
      "description": "Google's ML crash course explanation of leakage and overfitting."
    },
    {
      "title": "Python Data Science Handbook — Validation",
      "url": "https://jakevdp.github.io/PythonDataScienceHandbook/",
      "description": "Hyperparameters and model validation chapter."
    },
    {
      "title": "Leakage in Data Mining — Kaufman et al.",
      "url": "https://www.cs.umb.edu/~marc/cs690/Lec/KDD09-leakage.pdf",
      "description": "The classic academic treatment of target leakage."
    }
  ]
}
---

# DS-14-TRAIN-TEST-SPLIT: Train/Test Splits & Validation

## Introduction

The central question of applied ML is: *will this model work on data it has never seen?* You cannot answer it by scoring the model on the data it trained on — a model that memorizes its training data looks brilliant and generalizes terribly. The solution is to **hold out** a portion of data the model never sees during training, and measure performance there. This lesson covers the discipline of splitting, the pitfall of **data leakage**, and the standard practice of **cross-validation**.

## Key Concepts

### 1. Why a holdout set

If a model sees the test data during training, its test score is optimistic — potentially by a lot. The entire point of a test set is that it is *untouched*: no training, no feature selection, no threshold tuning, no eyeballing. The rule is absolute: **the test set must never influence any decision you make while building the model.**

### 2. The standard split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

Common sizes: 80/20 or 70/30. Use `random_state` for reproducibility. For **classification**, add `stratify=y` so rare classes are represented proportionally in both sets; for **time series**, split by time (train on the past, test on the future) — a random split of dated data leaks the future into training.

### 3. Train / validation / test

If you tune hyperparameters on the test set, you are still leaking (the test set shaped your model). The fix is a **three-way split**:

- **Train**: fit the model.
- **Validation**: tune hyperparameters and compare model variants.
- **Test**: a single final evaluation, run only once, at the very end.

### 4. Data leakage: the quiet killer

Leakage = information from the test set (or the future) sneaking into training. Two classic forms:

**Target leakage.** You include a feature that would not be known at prediction time. Example: predicting whether a patient has a disease, but including "was prescribed this medicine" — the medicine is given *because* of the disease, so the feature encodes the answer. This inflates scores to fantasy levels.

**Preprocessing leakage.** You fit scalers/imputers/encoders on the *whole* dataset before splitting. The scaler has now "seen" test data. The fix: **fit transformers on the training set only**, then transform test with the fitted object:

```python
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

pipe = Pipeline([
    ("scale", StandardScaler()),
    ("model", LogisticRegression()),
])
pipe.fit(X_train, y_train)          # scaler learns train stats only
pipe.score(X_test, y_test)
```

Pipelines make this the default instead of an accident.

### 5. K-fold cross-validation

With little data, a single 80/20 split wastes data and gives a noisy estimate. **K-fold cross-validation** splits the data into k folds, trains on k−1, evaluates on the remaining one, and repeats k times — every row gets used for both training and evaluation:

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(pipe, X_train, y_train, cv=5)   # 5-fold
print(scores, scores.mean())
```

Cross-validation gives you a *distribution* of scores rather than one lucky number — the honest estimate of how the model will behave. Use it for model selection, then evaluate once on the held-out test set.

## Practice Questions

1. Why must the test set stay untouched until the final evaluation?
2. Describe two concrete examples of target leakage.
3. What's wrong with fitting `StandardScaler` on all data before splitting? Fix it with a pipeline.
4. When would you choose 10-fold CV over a single 80/20 split?

## LLM Prompts for Deeper Understanding

1. "Give me 10 real-world examples of data leakage in machine learning."
2. "Explain the difference between train/validation/test splits and k-fold cross-validation, and when each is appropriate."
3. "How do you split time-series data without leaking the future?"

## Key Takeaways

- The test set must never influence model building.
- Use train/validation/test when tuning; stratify for classification; split by time for series.
- Fit scalers/imputers on training data only — pipelines enforce this.
- Leakage (target or preprocessing) silently inflates scores.
- K-fold CV estimates real performance; evaluate on test once, at the end.

## Footnotes & Attribution

1. scikit-learn documentation, *Cross-Validation*. [https://scikit-learn.org/stable/modules/cross_validation.html](https://scikit-learn.org/stable/modules/cross_validation.html)
2. Google Developers, *Machine Learning Crash Course — Overfitting*. [https://developers.google.com/machine-learning/crash-course/overfitting](https://developers.google.com/machine-learning/crash-course/overfitting)
3. Jake VanderPlas, *Python Data Science Handbook* — validation chapter. [https://jakevdp.github.io/PythonDataScienceHandbook/](https://jakevdp.github.io/PythonDataScienceHandbook/)
4. Kaufman, Rosset, Perlich, *Leakage in Data Mining* (KDD 2009). [https://www.cs.umb.edu/~marc/cs690/Lec/KDD09-leakage.pdf](https://www.cs.umb.edu/~marc/cs690/Lec/KDD09-leakage.pdf)
