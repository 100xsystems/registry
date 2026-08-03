---
{
  "title": "Clustering",
  "description": "Discover structure in unlabeled data with k-means and hierarchical clustering — and evaluate the result.",
  "type": "lesson",
  "order": 17,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain unsupervised learning and clustering",
    "Run k-means and choose k with the elbow method",
    "Use hierarchical clustering and dendrograms",
    "Evaluate clusters with silhouette scores"
  ],
  "knowledge_refs": [
    "machine-learning/ml-19-kmeans-clustering",
    "machine-learning/ml-20-dimensionality-reduction",
    "data-science/ds-16-classification-models"
  ],
  "prerequisites": [
    "DS-16: Classification Models"
  ],
  "references": [
    {
      "title": "scikit-learn — Clustering",
      "url": "https://scikit-learn.org/stable/modules/clustering.html",
      "description": "Official docs: k-means, hierarchical, DBSCAN and evaluation."
    },
    {
      "title": "scikit-learn — KMeans Documentation",
      "url": "https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html",
      "description": "KMeans API reference and parameters."
    },
    {
      "title": "Python Data Science Handbook — Clustering",
      "url": "https://jakevdp.github.io/PythonDataScienceHandbook/",
      "description": "Practical k-means, spectral and Gaussian mixture examples."
    },
    {
      "title": "StatQuest — K-Means Clustering",
      "url": "https://www.youtube.com/watch?v=4b5d3muPQmA",
      "description": "The clearest visual explanation of k-means."
    }
  ]
}
---

# DS-17-CLUSTERING: Clustering

## Introduction

Classification needs *labeled* data — but most of the world's data is unlabeled. **Clustering** is the core of unsupervised learning: it groups similar points together without any ground-truth labels, so you can *discover* structure. Businesses use clustering for customer segmentation, anomaly detection, and recommendation ("people who bought these also…"). This lesson covers k-means (the workhorse), hierarchical clustering (the most interpretable), and how to evaluate a clustering that, by definition, has no "right answer."

## Key Concepts

### 1. Unsupervised learning in one idea

In supervised learning you have (features, label) pairs; in unsupervised learning you have only features. The goal shifts from *predicting* to *understanding structure*: "which customers behave similarly?", "are there natural groups in this data?" Clustering's outputs are groups + a sense of how distinct they are — both of which feed directly into business strategy and feature engineering.

### 2. K-means: the workhorse

K-means partitions points into **k clusters** by iterating two steps: (1) assign each point to its nearest centroid, (2) move each centroid to the mean of its assigned points — until nothing moves. Because it depends on starting positions, run it with several random seeds.

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

X = StandardScaler().fit_transform(df[["spend", "orders", "tenure"]])
kmeans = KMeans(n_clusters=4, n_init=10, random_state=42).fit(X)
df["cluster"] = kmeans.labels_
```

Scale features first — k-means uses Euclidean distance, so unscaled columns dominate the geometry. `n_init=10` (default in current sklearn) protects against bad random starts.

### 3. Choosing k: the elbow method

The within-cluster sum of squares (inertia) always *decreases* as k grows. The elbow method looks for the point where adding another cluster stops buying much:

```python
import numpy as np

inertias = [KMeans(n_clusters=k, n_init=10, random_state=42).fit(X).inertia_ for k in range(2, 10)]
# plot inertias vs k — the "elbow" is your k
```

The elbow is a heuristic, not a theorem: combine it with domain judgment ("do the clusters make business sense?") rather than trusting it blindly.

### 4. Hierarchical clustering: dendrograms

Hierarchical clustering builds a tree of nested groups (agglomerative: start with each point as its own cluster, merge the closest pair, repeat). The **dendrogram** shows the full merging history, so you can cut the tree at any height to get any number of clusters — the most interpretable view:

```python
from scipy.cluster.hierarchy import dendrogram, linkage

Z = linkage(X, method="ward")
dendrogram(Z)                       # plot: cut horizontally for clusters
```

`method="ward"` minimizes within-cluster variance and generally gives compact, sensible clusters. Hierarchical clustering is great for small-to-medium datasets where interpretability matters.

### 5. Evaluating clusters: silhouette score

Since there are no labels, evaluation measures *cohesion vs separation*: how tight is each cluster, and how far is it from others?

- **Silhouette score** ∈ [−1, 1]: near +1 means points are well inside their cluster and far from others; near 0 means overlapping; negative means misassigned.

```python
from sklearn.metrics import silhouette_score

score = silhouette_score(X, kmeans.labels_)
print(f"{score:.3f}")
```

Use silhouette to compare different k values and different algorithms. And always sanity-check clusters by *profiling* them (mean spend, top category per cluster) — a statistically perfect cluster that describes no real segment is still useless.

## Practice Questions

1. What distinguishes supervised from unsupervised learning?
2. Why must features be scaled before k-means?
3. Describe the elbow method in one sentence, and its limitation.
4. What does a silhouette score near 0 tell you about your clusters?

## LLM Prompts for Deeper Understanding

1. "Walk me through the k-means algorithm step by step with a small example."
2. "When should I choose DBSCAN over k-means?"
3. "How do companies use customer clustering in practice, end to end?"

## Key Takeaways

- Clustering discovers groups in unlabeled data; evaluation is structural, not label-based.
- K-means: fast, simple, needs scaled features and a chosen k.
- Use the elbow + domain sense to pick k; run multiple random starts.
- Hierarchical clustering + dendrograms give the most interpretable grouping.
- Silhouette scores measure cohesion vs separation; profile clusters to validate.

## Footnotes & Attribution

1. scikit-learn documentation, *Clustering*. [https://scikit-learn.org/stable/modules/clustering.html](https://scikit-learn.org/stable/modules/clustering.html)
2. scikit-learn documentation, *KMeans*. [https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
3. Jake VanderPlas, *Python Data Science Handbook* — clustering. [https://jakevdp.github.io/PythonDataScienceHandbook/](https://jakevdp.github.io/PythonDataScienceHandbook/)
4. Josh Starmer, *StatQuest — K-Means Clustering*. [https://www.youtube.com/watch?v=4b5d3muPQmA](https://www.youtube.com/watch?v=4b5d3muPQmA)
