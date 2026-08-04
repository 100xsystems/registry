---
slug: ml-08-decision-trees
title: "Decision Trees"
description: "The most interpretable machine learning algorithm — and the building block for the most powerful tabular ML methods."
order: 8
tags:
  - machine-learning
  - decision-trees
  - classification
  - regression
  - interpretable-ml
prerequisites:
  - ml-03-the-learning-problem
  - ml-07-logistic-regression
references:
  - title: "scikit-learn: Decision Trees User Guide"
    url: "https://scikit-learn.org/stable/modules/tree.html"
    description: "Official documentation with practical guidance"
  - title: "Visual Introduction to Decision Trees"
    url: "http://www.r2d3.us/visual-intro-to-machine-learning-part-1/"
    description: "R2D3's beautiful interactive visual introduction"
  - title: "A Tutorial on Decision Trees (Quinlan)"
    url: "https://link.springer.com/chapter/10.1007/978-1-4615-3686-4_7"
    description: "Ross Quinlan's foundational paper on ID3 and C4.5"
  - title: "Elements of Statistical Learning, Ch. 9"
    url: "https://hastie.su.domains/ElemStatLearn/printings/ESLII_print12_toc.pdf"
    description: "Chapter on Tree-Based Methods — the authoritative reference"
  - title: "StatQuest: Decision Trees"
    url: "https://www.youtube.com/watch?v=_L39rN6gz7Y"
    description: "Josh Starmer's intuitive explanation of how trees split"
knowledge_refs:
  - ml-09-ensemble-methods
  - ml-10-gradient-boosting
  - ml-07-logistic-regression
---

# Decision Trees

Decision trees are one of the most intuitive machine learning algorithms. They recursively split the data into regions based on feature thresholds, creating a flowchart-like model that's easy to visualize and explain.

## How Decision Trees Work

A decision tree makes predictions by asking a sequence of binary questions:

```
Is feature x₁ ≤ threshold t₁?
├── YES → Is feature x₂ ≤ threshold t₂?
│   ├── YES → Predict class A
│   └── NO → Predict class B
└── NO → Is feature x₃ ≤ threshold t₃?
    ├── YES → Predict class C
    └── NO → Predict class B
```

Each internal node splits on a feature and threshold, each branch is an outcome, and each leaf is a prediction. For regression trees, the leaf predicts the mean of training samples in that region.

## Splitting Criteria

The key question is: **which feature and threshold to split on?** Different criteria lead to different tree algorithms:

### Information Gain (ID3, C4.5)

**Entropy** measures impurity:
$$H(S) = -\sum_{k=1}^{K} p_k \log_2(p_k)$$

where $p_k$ is the proportion of class $k$ in set $S$. Pure sets have $H=0$; maximally impure sets have $H=\log_2(K)$.

**Information gain** is the reduction in entropy after splitting:
$$IG(S, A) = H(S) - \sum_{v \in \text{values}(A)} \frac{|S_v|}{|S|} H(S_v)$$

The tree greedily chooses the split that maximizes information gain.

### Gini Impurity (CART)

$$G(S) = 1 - \sum_{k=1}^{K} p_k^2$$

Gini impurity ranges from 0 (pure) to $1 - 1/K$ (maximally impure). It's computationally cheaper than entropy (no logarithm) and produces nearly identical trees in practice. This is the default in scikit-learn.

### Variance Reduction (Regression)

For regression trees, the split minimizes the variance (or MSE) of the target in each child node:
$$\text{Var}(S) = \frac{1}{|S|} \sum_{i \in S} (y_i - \bar{y})^2$$

## The Splitting Algorithm

1. For each feature, find all unique split points
2. For each split point, compute the impurity reduction
3. Choose the feature and threshold with the highest reduction
4. Recurse on each child until stopping criteria are met

```python
from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(
    criterion='gini',      # or 'entropy'
    max_depth=5,           # limit tree depth
    min_samples_split=20,  # minimum samples to split a node
    min_samples_leaf=5,    # minimum samples in a leaf
    max_features=None      # consider all features at each split
)
tree.fit(X_train, y_train)
```

## Pruning: Preventing Overfitting

Decision trees can grow to memorize the training data. **Pruning** cuts back branches that don't improve generalization:

**Pre-pruning (early stopping):**
- `max_depth`: Maximum depth of the tree
- `min_samples_split`: Minimum samples required to split a node
- `min_samples_leaf`: Minimum samples in a leaf node
- `max_leaf_nodes`: Maximum number of leaf nodes

**Post-pruning:**
Grow the full tree first, then remove branches that don't improve validation performance. Cost-complexity pruning (CART) penalizes tree complexity:
$$R_\alpha(T) = R(T) + \alpha |T|$$

where $|T|$ is the number of leaves and $\alpha$ controls the trade-off.

```python
# Cost-complexity pruning path
path = tree.cost_complexity_pruning_path(X_train, y_train)
alphas = path.ccp_alphas

# Find optimal alpha via cross-validation
from sklearn.model_selection import cross_val_score
scores = [cross_val_score(DecisionTreeClassifier(ccp_alpha=a), X_train, y_train, cv=5).mean() for a in alphas]
optimal_alpha = alphas[np.argmax(scores)]
```

## Regression Trees

For continuous targets, decision trees predict the mean value in each leaf:
```python
from sklearn.tree import DecisionTreeRegressor
reg_tree = DecisionTreeRegressor(max_depth=4, min_samples_leaf=10)
reg_tree.fit(X_train, y_train)
predictions = reg_tree.predict(X_test)  # mean of training targets in leaf
```

## Strengths

- **Highly interpretable**: You can draw the tree and explain every decision
- **No feature scaling needed**: Trees are invariant to monotonic transformations
- **Handles mixed features**: Numerical and categorical together
- **Captures non-linear relationships**: No assumption about feature-target relationship
- **Fast training and prediction**: O(N × D × log N) training, O(log N) prediction
- **Handles missing values**: Some implementations (XGBoost) handle NaN natively
- **Feature importance**: Built-in, based on impurity reduction

## Limitations

- **Overfitting**: Prone to memorizing training data without pruning
- **Unstable**: Small data changes can produce completely different trees
- **Greedy optimization**: Can't guarantee globally optimal tree
- **Axis-aligned splits**: Only orthogonal decision boundaries
- **Poor extrapolation**: Can't predict outside the range of training values
- **Biased toward high-cardinality features**: Features with more levels appear more important

## Feature Importance

Trees provide feature importance scores based on total impurity reduction:
```python
importances = tree.feature_importances_
for name, imp in sorted(zip(feature_names, importances), key=lambda x: -x[1]):
    print(f"{name}: {imp:.3f}")
```

**Warning**: Feature importance can be misleading — it's biased toward high-cardinality features. Use permutation importance for more reliable estimates.

## The Foundation for Ensembles

Decision trees are rarely used alone in production. Their real power comes as building blocks for **ensemble methods**:
- **Random Forests** (bagging + feature randomness) → robust, hard to overfit
- **Gradient Boosting** (sequential, error-correcting) → state-of-the-art on tabular data

These ensemble methods are the subject of the next lessons and represent the most powerful approach for structured/tabular data.

## Further Reading

- The r2d3 interactive visual introduction is the best first exposure
- Quinlan's original papers on ID3 and C4.5 are foundational to ML history
- ESL Chapter 9 covers pruning, boosting, and bagging comprehensively
- For interpretability, look into surrogate models and LIME as alternatives to reading tree structures
