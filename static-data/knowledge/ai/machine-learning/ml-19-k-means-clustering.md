---
slug: ml-19-k-means-clustering
title: "K-Means & Clustering"
description: "The most widely-used unsupervised learning algorithm — partitioning data into meaningful groups without labels."
order: 19
tags:
  - machine-learning
  - clustering
  - k-means
  - unsupervised
  - dbscan
prerequisites:
  - ml-03-the-learning-problem
  - ml-14-feature-scaling
references:
  - title: "scikit-learn: Clustering User Guide"
    url: "https://scikit-learn.org/stable/modules/clustering.html"
    description: "Official documentation covering all clustering algorithms"
  - title: "K-Means++: The Advantages of Careful Seeding"
    url: "https://dl.acm.org/doi/10.1145/1283383.1283494"
    description: "Arthur & Vassilvitskii's K-means++ initialization paper"
  - title: "DBSCAN: A Density-Based Algorithm"
    url: "https://www.aaai.org/Papers/KDD/1996/KDD96-037.pdf"
    description: "The original DBSCAN paper by Ester et al."
  - title: "StatQuest: K-Means Clustering"
    url: "https://www.youtube.com/watch?v=4b5d3muPQmA"
    description: "Josh Starmer's intuitive visual explanation of K-means"
  - title: "A Density-Based Notion of Clustering (HDBSCAN)"
    url: "https://hdbscan.readthedocs.io/"
    description: "HDBSCAN documentation — hierarchical density-based clustering"
knowledge_refs:
  - ml-14-feature-scaling
  - ml-20-dimensionality-reduction
  - ml-12-k-nearest-neighbors
---

# K-Means & Clustering

Clustering finds natural groups in unlabeled data. K-means is the simplest and most widely-used clustering algorithm — and understanding it opens the door to more sophisticated methods.

## K-Means Algorithm

K-means partitions $N$ data points into $K$ clusters by minimizing the **inertia** (within-cluster sum of squares):

$$\text{Inertia} = \sum_{k=1}^{K} \sum_{\mathbf{x}_i \in C_k} \|\mathbf{x}_i - \boldsymbol{\mu}_k\|^2$$

where $\boldsymbol{\mu}_k$ is the centroid of cluster $C_k$.

**The algorithm:**
1. Initialize $K$ centroids (randomly or via K-means++)
2. **Assignment step**: Assign each point to the nearest centroid
3. **Update step**: Move each centroid to the mean of its assigned points
4. Repeat 2-3 until convergence (centroids don't move)

```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=5, init='k-means++', n_init=10, random_state=42)
labels = kmeans.fit_predict(X)
centroids = kmeans.cluster_centers_
inertia = kmeans.inertia_
```

## K-means++ Initialization

Random initialization can lead to poor results. K-means++ (Arthur & Vassilvitskii, 2007) picks initial centroids that are spread out:

1. Choose first centroid randomly
2. For each remaining centroid, choose a point with probability proportional to its squared distance from the nearest existing centroid
3. Repeat until $K$ centroids are chosen

This is the default in scikit-learn (`init='k-means++'`).

## Choosing K: The Elbow Method

Plot inertia vs. $K$ and look for the "elbow" — the point where adding more clusters doesn't significantly reduce inertia:

```python
inertias = []
K_range = range(2, 15)
for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X)
    inertias.append(km.inertia_)

import matplotlib.pyplot as plt
plt.plot(K_range, inertias, 'bo-')
plt.xlabel('Number of clusters K')
plt.ylabel('Inertia')
plt.title('Elbow Method')
```

**Better methods:**
- **Silhouette Score**: Measures how similar a point is to its own cluster vs. other clusters
- **Gap Statistic**: Compares inertia to what expected under null reference distribution
- **Calinski-Harabasz Index**: Ratio of between-cluster to within-cluster dispersion

```python
from sklearn.metrics import silhouette_score

scores = []
for k in range(2, 15):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(X)
    scores.append(silhouette_score(X, labels))

optimal_k = list(range(2, 15))[scores.index(max(scores))]
```

## K-Means Variants

### Mini-Batch K-Means
For large datasets — uses random mini-batches instead of full dataset:
```python
from sklearn.cluster import MiniBatchKMeans
mbk = MiniBatchKMeans(n_clusters=5, batch_size=1000)
labels = mbk.fit_predict(X)
```

### Bisecting K-Means
Hierarchical approach: start with one cluster, repeatedly split the largest cluster:
```python
from sklearn.cluster import BisectingKMeans
bkm = BisectingKMeans(n_clusters=5)
labels = bkm.fit_predict(X)
```

## DBSCAN: Density-Based Clustering

DBSCAN finds clusters of arbitrary shape based on density:

- **Core points**: Have at least `min_samples` neighbors within `eps` distance
- **Border points**: Within `eps` of a core point but don't have enough neighbors
- **Noise points**: Neither core nor border — labeled as cluster -1

```python
from sklearn.cluster import DBSCAN

dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(X)
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
n_noise = (labels == -1).sum()
```

**Advantages over K-means:**
- No need to specify $K$
- Finds arbitrary-shaped clusters
- Identifies noise/outliers
- Works with varying densities (with HDBSCAN)

**HDBSCAN** extends DBSCAN with hierarchical density estimation:
```python
import hdbscan
clusterer = hdbscan.HDBSCAN(min_cluster_size=15)
labels = clusterer.fit_predict(X)
```

## Hierarchical Clustering

Builds a tree (dendrogram) of clusters:

**Agglomerative** (bottom-up): Start with each point as its own cluster, merge closest pairs.

```python
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Create dendrogram
linkage_matrix = linkage(X, method='ward')
dendrogram(linkage_matrix)

# Cut at desired number of clusters
agg = AgglomerativeClustering(n_clusters=5, linkage='ward')
labels = agg.fit_predict(X)
```

**Linkage criteria:**
- **Ward**: Minimize within-cluster variance (default)
- **Complete**: Maximum distance between clusters
- **Average**: Average distance between clusters
- **Single**: Minimum distance (can find elongated clusters)

## Clustering Evaluation

### Silhouette Score
$$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$$

where $a(i)$ is mean distance to same-cluster points, $b(i)$ is mean distance to nearest other cluster. Range: [-1, 1]. Higher is better.

```python
from sklearn.metrics import silhouette_score, silhouette_samples
avg_score = silhouette_score(X, labels)
per_sample_scores = silhouette_samples(X, labels)
```

### Calinski-Harabasz Index
$$CH = \frac{\text{tr}(B_k) / (K-1)}{\text{tr}(W_k) / (N-K)}$$

Higher is better. Measures ratio of between-cluster to within-cluster dispersion.

### Davies-Bouldin Index
Ratio of within-cluster distances to between-cluster distances. Lower is better.

## When to Use What

| Scenario | Algorithm |
|---|---|
| Spherical clusters, known K | K-means |
| Large dataset (> 100K points) | Mini-Batch K-Means |
| Unknown K, arbitrary shapes | HDBSCAN |
| Need hierarchy | Agglomerative |
| Noisy data with outliers | DBSCAN / HDBSCAN |
| Text clustering | K-means on TF-IDF vectors |

## Practical Tips

1. **Always scale features** before clustering
2. **K-means assumes spherical clusters** — if clusters aren't round, try DBSCAN
3. **Use K-means++ initialization** — never random
4. **Run multiple times** (`n_init=10`) — K-means can get stuck in local minima
5. **Use silhouette score** to evaluate, not just inertia
6. **PCA or t-SNE** can help visualize clusters in 2D

## Clustering as Preprocessing

Clustering is often used as a feature engineering step:
- **Cluster assignment as a feature**: Add cluster labels as a categorical feature to supervised models
- **Cluster-based stratification**: Ensure train/test splits have similar cluster distributions
- **Dimensionality reduction**: Replace features with cluster distances

## Further Reading

- Arthur & Vassilvitskii (2007) proved K-means++ gives O(log K)-competitive approximation
- Ester et al. (1996) introduced DBSCAN — one of the most cited data mining papers
- HDBSCAN (Campello et al., 2013) combines the best of DBSCAN and hierarchical clustering
- For high-dimensional clustering, consider subspace clustering (CLIQUE, PROCLUS)
