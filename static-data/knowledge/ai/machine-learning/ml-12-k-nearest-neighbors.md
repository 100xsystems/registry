---
slug: ml-12-k-nearest-neighbors
title: "K-Nearest Neighbors"
description: "The simplest instance-based learning algorithm — no training at all, just memorize the data and vote."
order: 12
tags:
  - machine-learning
  - instance-based
  - knn
  - distance-metrics
prerequisites:
  - ml-03-the-learning-problem
  - ml-14-feature-scaling
references:
  - title: "scikit-learn: Nearest Neighbors User Guide"
    url: "https://scikit-learn.org/stable/modules/neighbors.html"
    description: "Official documentation with practical guidance"
  - title: "K-Nearest Neighbors for Recommender Systems"
    url: "https://datarecognition.io/knn-based-recommender-systems-a-comprehensive-survey/"
    description: "Survey of KNN in recommender systems"
  - title: "Cover and Hart: Nearest Neighbor Pattern Classification (1967)"
    url: "https://ieeexplore.ieee.org/document/1053964"
    description: "The foundational paper on KNN classification"
  - title: "Annoy: Approximate Nearest Neighbors in C++/Python"
    url: "https://github.com/spotify/annoy"
    description: "Spotify's library for efficient approximate nearest neighbor search"
  - title: "KD-Trees: A Survey"
    url: "https://en.wikipedia.org/wiki/K-d_tree"
    description: "Wikipedia's comprehensive article on KD-tree data structures"
knowledge_refs:
  - ml-14-feature-scaling
  - ml-11-support-vector-machines
  - ml-19-clustering
---

# K-Nearest Neighbors

K-Nearest Neighbors (KNN) is the simplest machine learning algorithm — it performs **no training at all**. It memorizes the entire training set and classifies new points by majority vote among their $K$ closest neighbors.

## How KNN Works

**Classification:**
1. Given a new point $\mathbf{x}$, find the $K$ closest training points
2. Each neighbor "votes" for its class
3. Predict the majority class

**Regression:**
1. Find the $K$ closest training points
2. Predict the average (or weighted average) of their target values

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(
    n_neighbors=5,
    weights='uniform',  # or 'distance' for weighted voting
    metric='minkowski',
    p=2  # Euclidean distance
)
knn.fit(X_train, y_train)
predictions = knn.predict(X_test)
```

## Distance Metrics

The choice of distance metric is critical:

**Euclidean (L2):**
$$d(\mathbf{x}, \mathbf{z}) = \sqrt{\sum_{i=1}^{D}(x_i - z_i)^2}$$
Standard choice, works well for continuous features.

**Manhattan (L1):**
$$d(\mathbf{x}, \mathbf{z}) = \sum_{i=1}^{D}|x_i - z_i|$$
Better for high-dimensional data, more robust to outliers.

**Minkowski (Lp):**
$$d(\mathbf{x}, \mathbf{z}) = \left(\sum_{i=1}^{D}|x_i - z_i|^p\right)^{1/p}$$
Generalizes Euclidean ($p=2$) and Manhattan ($p=1$).

**Cosine similarity:**
$$\cos(\mathbf{x}, \mathbf{z}) = \frac{\mathbf{x}^T \mathbf{z}}{\|\mathbf{x}\| \|\mathbf{z}\|}$$
Best for text data where magnitude doesn't matter.

**Hamming distance:**
Counts positions where features differ. Used for categorical/binary features.

## Feature Scaling is Critical

KNN is a distance-based algorithm, so features with larger scales dominate:

```python
# MUST scale features before KNN
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

knn_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(n_neighbors=5))
])
```

Without scaling, a feature in range [0, 1000] would completely dominate a feature in range [0, 1].

## Choosing K

| K | Effect |
|---|---|
| Small (1-3) | Low bias, high variance — sensitive to noise |
| Medium (5-15) | Good balance for most problems |
| Large (20+) | High bias, low variance — smooth boundaries |

**Rules of thumb:**
- Start with $K = \sqrt{N}$ (where $N$ is training set size)
- Use odd $K$ for binary classification (avoids ties)
- Use cross-validation to find optimal $K$
- Plot accuracy vs. $K$ to see the bias-variance trade-off

```python
# Find optimal K via cross-validation
import numpy as np
from sklearn.model_selection import cross_val_score

k_range = range(1, 31)
scores = [cross_val_score(KNeighborsClassifier(k), X_scaled, y, cv=5).mean() for k in k_range]
optimal_k = k_range[np.argmax(scores)]
```

## Weighted Voting

Uniform voting treats all neighbors equally. **Distance-weighted voting** gives closer neighbors more influence:

$$P(y=c \mid \mathbf{x}) = \sum_{i \in \text{neighbors}} \frac{1}{d(\mathbf{x}, \mathbf{x}_i)} \cdot \mathbb{1}[y_i = c]$$

```python
knn = KNeighborsClassifier(n_neighbors=7, weights='distance')
```

This is almost always better than uniform voting.

## The Curse of Dimensionality

KNN suffers severely in high dimensions:

- **Distances become meaningless**: All points become equidistant
- **Data becomes sparse**: You need exponentially more data to maintain density
- **Features become irrelevant**: Most dimensions are noise

**Solutions:**
1. **Feature selection**: Keep only relevant features
2. **Dimensionality reduction**: PCA, t-SNE before KNN
3. **Use different metrics**: Cosine for text, Manhattan for high-D
4. **Approximate nearest neighbors**: ANN for speed

## Efficient Nearest Neighbor Search

Brute-force KNN is $O(N \cdot D)$ per query. For large datasets, use approximate nearest neighbor (ANN) algorithms:

| Algorithm | Library | Use Case |
|---|---|---|
| KD-Tree | scikit-learn | Low-D, small dataset |
| Ball Tree | scikit-learn | Medium-D |
| Annoy | Spotify | Large-scale, sparse |
| FAISS | Facebook | GPU-accelerated, billions of vectors |
| HNSW | hnswlib | Best quality-speed trade-off |
| ScaNN | Google | Google-scale vector search |

```python
# For large datasets, use approximate nearest neighbors
from sklearn.neighbors import NearestNeighbors

# Ball tree for medium-sized datasets
nn = NearestNeighbors(n_neighbors=5, algorithm='ball_tree')
nn.fit(X_train)
distances, indices = nn.kneighbors(X_test)
```

## Strengths

- **No training**: Just store the data — zero training time
- **Naturally handles multi-class**: Just vote
- **Interpretable**: Show the neighbors that influenced the prediction
- **Non-parametric**: Makes no assumptions about data distribution
- **Adapts to any decision boundary**: Given enough data

## Limitations

- **Slow prediction**: Must compute distances to all training points
- **Memory intensive**: Stores entire training set
- **Curse of dimensionality**: Fails in high dimensions
- **Sensitive to irrelevant features**: All features contribute to distance
- **Sensitive to scale**: Must normalize
- **No model**: Can't learn generalizable patterns, just memorizes

## KNN in Practice

KNN is rarely used as a classifier in production (too slow, no generalization). But it's **essential** as:
- **Baseline**: Always try KNN first — if it works, your problem is easy
- **Feature in other models**: KNN features (distances to neighbors) are powerful
- **Recommendation systems**: User-user or item-item collaborative filtering IS KNN
- **Anomaly detection**: Points far from all neighbors are anomalies
- **Semi-supervised learning**: Label propagation via KNN graph

## Further Reading

- Cover & Hart (1967) proved KNN converges to Bayes optimal classifier as $N \to \infty$
- Spotify's Annoy and Facebook's FAISS are essential for production nearest neighbor search
- For understanding why KNN works theoretically, see "instance-based learning" literature
