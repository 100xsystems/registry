---
slug: ml-09-ensemble-methods
title: "Ensemble Methods: Bagging & Random Forests"
description: "How combining many weak learners creates a strong one — bagging, random forests, and the wisdom of crowds."
order: 9
tags:
  - machine-learning
  - ensemble
  - random-forest
  - bagging
  - bootstrap
prerequisites:
  - ml-08-decision-trees
  - ml-03-the-learning-problem
references:
  - title: "Random Forests — Leo Breiman (2001)"
    url: "https://link.springer.com/article/10.1023/A:1010933404324"
    description: "The original random forests paper — a must-read classic"
  - title: "scikit-learn: Random Forests User Guide"
    url: "https://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees"
    description: "Official documentation with practical guidance and examples"
  - title: "StatQuest: Random Forests"
    url: "https://www.youtube.com/watch?v=J4Wdy0Wc_xQ"
    description: "Josh Starmer's intuitive explanation of how random forests work"
  - title: "Elements of Statistical Learning, Ch. 15"
    url: "https://hastie.su.domains/ElemStatLearn/printings/ESLII_print12_toc.pdf"
    description: "Chapter on Random Forests and bagging — the theoretical foundation"
  - title: "Out-of-Bag Estimation (Breiman)"
    url: "https://www.stat.berkeley.edu/~breiman/OOBestimation.pdf"
    description: "The OOB estimation technique that eliminates the need for a separate validation set"
knowledge_refs:
  - ml-08-decision-trees
  - ml-10-gradient-boosting
  - ml-16-cross-validation
---

# Ensemble Methods: Bagging & Random Forests

The key insight of ensemble methods is that **combining many models that are individually mediocre can produce a model that is excellent**. Random forests, built on this principle, remain one of the most reliable and widely-used ML algorithms.

## The Wisdom of Crowds

Imagine asking 100 people to estimate the number of jellybeans in a jar. Individually, most will be wrong. But the **average** of all 100 estimates is typically very close to the true number. This is the core insight behind ensemble methods.

For this to work, the individual estimates need to be:
1. **Unbiased** (each person has a roughly correct average)
2. **Independent** (errors don't correlate)

If everyone uses the same biased method, averaging doesn't help. We need **diversity**.

## Bootstrap Aggregating (Bagging)

**Bagging** (Breiman, 1996) creates diversity by training each model on a different random subset of the data:

1. Draw $B$ bootstrap samples (random sampling with replacement, each the same size as the original dataset)
2. Train a decision tree on each bootstrap sample
3. For classification: majority vote. For regression: average

Each bootstrap sample contains approximately 63.2% of the original data (the rest is "out-of-bag" — OOB). Each tree overfits to its bootstrap sample differently, creating diversity.

```python
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

bagging = BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=100,    # number of trees
    max_samples=0.8,     # fraction of data per tree
    max_features=1.0,    # fraction of features per split
    bootstrap=True,
    oob_score=True,      # use out-of-bag samples for validation
    n_jobs=-1
)
bagging.fit(X_train, y_train)
print(f"OOB Score: {bagging.oob_score_:.3f}")
```

## Random Forests

Random forests (Breiman, 2001) add **feature randomness** to bagging. At each split, only a random subset of features is considered:

$$m = \sqrt{D} \text{ (classification)} \quad \text{or} \quad m = D/3 \text{ (regression)}$$

where $D$ is the total number of features. This prevents all trees from splitting on the same dominant features, dramatically increasing diversity.

```python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(
    n_estimators=500,        # number of trees
    max_depth=None,          # fully grown trees
    min_samples_leaf=1,
    max_features='sqrt',     # sqrt(D) features per split (classification)
    bootstrap=True,
    oob_score=True,
    random_state=42,
    n_jobs=-1
)
rf.fit(X_train, y_train)
print(f"OOB: {rf.oob_score_:.3f}, Test: {rf.score(X_test, y_test):.3f}")
```

## Why Random Forests Work

The error of a random forest can be decomposed as:

$$\text{Error} = \text{Bias}^2 + \text{Variance} + \text{Noise}$$

- **Bias**: Stays roughly the same as individual trees (trees are low-bias)
- **Variance**: Decreases by a factor of ~B with bagging (if trees are independent)
- **Feature randomness**: Further reduces variance by decorrelating trees

The magic: **variance reduction without increasing bias**. Each deep tree is a low-bias, high-variance model. Averaging many uncorrelated high-variance models reduces variance dramatically while keeping bias low.

## Out-of-Bag (OOB) Estimation

Each tree's OOB samples (the ~36.8% of data not in its bootstrap) serve as a built-in validation set. OOB prediction aggregates predictions only from trees that didn't see each sample:

```python
# OOB score ≈ cross-validation score, but free!
rf.fit(X_train, y_train)
oob_predictions = rf.oob_decision_function_  # probabilities for each class
oob_predictions
```

This eliminates the need for a separate validation set — critical for small datasets.

## Feature Importance

Random forests provide two types of feature importance:

**Mean Decrease in Impurity (MDI)**:
```python
importances = rf.feature_importances_  # based on impurity reduction
```
⚠️ Biased toward high-cardinality features.

**Permutation Importance** (more reliable):
```python
from sklearn.inspection import permutation_importance

result = permutation_importance(rf, X_test, y_test, n_repeats=10, random_state=42)
importances = result.importances_mean  # decrease in accuracy when feature is shuffled
```

Permutation importance measures how much accuracy drops when a feature is randomly shuffled — no bias toward any feature type.

## Hyperparameters

| Parameter | Default | Effect | Tuning Advice |
|---|---|---|---|
| `n_estimators` | 100 | More trees = better (no overfitting) | 500-1000 is usually enough |
| `max_depth` | None | Tree depth | Leave None; trees should be deep |
| `min_samples_leaf` | 1 | Minimum leaf size | Increase for smaller datasets |
| `max_features` | sqrt(D) | Features per split | sqrt(D) for classif., D/3 for reg. |
| `max_samples` | None | Bootstrap sample size | 0.6-0.8 for large datasets |

**Key insight**: Increasing `n_estimators` never causes overfitting — it monotonically improves or plateaus. The only cost is computation.

## Comparison with Other Methods

| Property | Single Tree | Random Forest | Bagging |
|---|---|---|---|
| Variance | High | Low | Low |
| Bias | Low | Low | Low |
| Interpretability | High | Medium (feature importance) | Low |
| Overfitting risk | High | Low | Medium |
| Training speed | Fast | Moderate | Moderate |

## Strengths

- **Robust**: Rarely overfits with enough trees
- **Fast**: Parallelizable (trees are independent)
- **No scaling needed**: Invariant to feature transformations
- **Handles missing values**: Some implementations support NaN
- **Excellent baseline**: Often wins competitions without any tuning
- **OOB validation**: Free estimate of test performance

## Limitations

- **Memory**: Storing hundreds of trees is expensive
- **Prediction speed**: Must query all trees
- **Not great for extrapolation**: Can't predict outside training range
- **Biased toward categorical features with many levels**
- **Can be outperformed by gradient boosting** on many tabular tasks

## Random Forest Variants

- **Extra-Trees (Extremely Randomized Trees)**: Random thresholds in addition to random features. Even more diverse, sometimes better.
- **Balanced Random Forest**: Handles class imbalance by undersampling each bootstrap.
- **Rotation Forest**: Applies PCA to random feature subsets before splitting.

## Practical Tips

1. **Start with 500 trees** — more is rarely needed
2. **Use OOB score** instead of cross-validation for quick iteration
3. **Use permutation importance** over impurity importance
4. **For production**: Consider converting to lighter models (distillation, pruning)
5. **Parallelize**: Set `n_jobs=-1` to use all CPU cores

## Further Reading

- Breiman's 2001 paper is one of the most cited in all of ML — worth reading
- ESL Chapter 15 provides the statistical foundation
- For extreme randomization, see Geurts et al. (2006) "Extremely Randomized Trees"
- Biau & Scornet (2016) "A Random Forest Guided Tour" covers the theoretical properties
