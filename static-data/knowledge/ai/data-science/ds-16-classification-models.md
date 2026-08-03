---
{
  "title": "Classification Models",
  "description": "Predict categories with logistic regression, decision trees and k-NN — and understand what a classifier actually outputs.",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain classification and its outputs",
    "Fit logistic regression and interpret probabilities",
    "Use decision trees and k-nearest neighbors",
    "Choose between classifiers for a problem"
  ],
  "knowledge_refs": [
    "machine-learning/ml-07-logistic-regression",
    "machine-learning/ml-08-decision-trees",
    "data-science/ds-18-model-evaluation"
  ],
  "prerequisites": [
    "DS-15: Regression Models"
  ],
  "references": [
    {
      "title": "scikit-learn — Classifier Guide",
      "url": "https://scikit-learn.org/stable/classifiers.html",
      "description": "Official comparison of every classifier in scikit-learn."
    },
    {
      "title": "scikit-learn — Logistic Regression",
      "url": "https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression",
      "description": "Logistic regression docs: probabilities, penalties, and multi-class."
    },
    {
      "title": "Python Data Science Handbook — Classification",
      "url": "https://jakevdp.github.io/PythonDataScienceHandbook/",
      "description": "Practical classification examples with scikit-learn."
    },
    {
      "title": "scikit-learn — Decision Trees",
      "url": "https://scikit-learn.org/stable/modules/tree.html",
      "description": "Decision tree documentation and tips."
    }
  ]
}
---

# DS-16-CLASSIFICATION-MODELS: Classification Models

## Introduction

**Classification** predicts a *category* — will this user churn (yes/no), which plan will they pick (free/pro/team), is this email spam (spam/not). Unlike regression's continuous output, classifiers produce either a hard label or (more usefully) a **probability** for each class. This lesson covers the three classifiers you'll reach for first — logistic regression, decision trees, and k-nearest neighbors — and the crucial skill of *interpreting probabilities*, which unlocks threshold decisions and honest evaluation.

## Key Concepts

### 1. What a classifier outputs

A classifier typically outputs a probability per class, e.g. `P(churn) = 0.87`. You convert to a label by choosing a **threshold** — the default is 0.5, but the threshold is a *business decision*: for spam, you might want to flag aggressively (low threshold) because a missed spam costs little but a false positive is embarrassing. This "probability-first" view is the modern, honest way to use classifiers.

### 2. Logistic regression: the linear classifier

Despite the name, logistic regression is a *classifier*. It fits a linear combination of features, then squashes it through the logistic (sigmoid) function into [0, 1]:

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000).fit(X_train, y_train)
probs = model.predict_proba(X_test)[:, 1]    # P(class=1)
labels = model.predict(X_test)                # threshold 0.5
```

- **Interpretable**: coefficients work like linear regression, on log-odds. A positive coefficient pushes probability up.
- **Fast and reliable**: an excellent default for tabular data, especially with regularization.

### 3. Decision trees: rules you can read

A decision tree learns a sequence of yes/no questions that best split the data (e.g., "income > 40k?" then "orders > 3?"). They need no scaling, handle mixed feature types, and — at small depths — are fully readable:

```python
from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(max_depth=4, random_state=42).fit(X_train, y_train)
```

`max_depth` controls complexity: shallow trees generalize, deep trees overfit. Trees are also the building blocks of random forests and gradient boosting — the strongest tabular models (covered in the ML course).

### 4. k-nearest neighbors: the intuitive baseline

k-NN predicts the majority class among the k *closest training points* to the new sample. Zero training time, but it needs **scaled features** (otherwise "distance" is dominated by large-scale columns) and slows down with big datasets:

```python
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline

knn = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
knn.fit(X_train, y_train)
```

### 5. Which classifier when?

| Situation | Reach for |
| --- | --- |
| Need interpretability, tabular data | Logistic regression |
| Non-linear relationships, readable rules | Decision tree (shallow) |
| Strongest default accuracy on tables | Random forest / gradient boosting |
| Small data, simple baseline | k-NN |

A practical workflow: start with logistic regression as the sanity baseline, then try a tree ensemble, and let **cross-validated evaluation** (next lessons) decide — never trust intuition over measured performance.

## Practice Questions

1. What is the difference between `predict` and `predict_proba`, and why does the latter matter?
2. When would you set a decision threshold below 0.5?
3. Why must features be scaled for k-NN but not for decision trees?
4. Describe the "predict churn" problem: which classifier would you start with and why?

## LLM Prompts for Deeper Understanding

1. "Explain the logistic function and why it maps log-odds to probabilities."
2. "How do decision trees choose split points? Walk me through one split."
3. "Compare logistic regression vs random forest on interpretability, speed, and accuracy."

## Key Takeaways

- Classifiers output probabilities; labels come from a threshold you choose.
- Logistic regression: fast, interpretable, excellent tabular default.
- Decision trees: readable rules, no scaling, base of the tree ensembles.
- k-NN: simple baseline that requires scaled features.
- Start with a simple baseline, then compare with cross-validated scores.

## Footnotes & Attribution

1. scikit-learn documentation, *Classifier Guide*. [https://scikit-learn.org/stable/classifiers.html](https://scikit-learn.org/stable/classifiers.html)
2. scikit-learn documentation, *Logistic Regression*. [https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)
3. Jake VanderPlas, *Python Data Science Handbook* — classification. [https://jakevdp.github.io/PythonDataScienceHandbook/](https://jakevdp.github.io/PythonDataScienceHandbook/)
4. scikit-learn documentation, *Decision Trees*. [https://scikit-learn.org/stable/modules/tree.html](https://scikit-learn.org/stable/modules/tree.html)
