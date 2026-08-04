---
slug: ml-20-dimensionality-reduction
title: "Dimensionality Reduction"
description: "PCA, t-SNE, and UMAP — compressing high-dimensional data into human-interpretable spaces while preserving structure."
order: 20
tags:
  - machine-learning
  - dimensionality-reduction
  - pca
  - tsne
  - umap
prerequisites:
  - ml-14-feature-scaling
  - ml-03-the-learning-problem
references:
  - title: "scikit-learn: Decomposition User Guide"
    url: "https://scikit-learn.org/stable/modules/decomposition.html"
    description: "Official documentation covering PCA, SVD, and more"
  - title: "Visualizing Data using t-SNE (van der Maaten & Hinton)"
    url: "https://jmlr.org/papers/v9/vandermaaten08a.html"
    description: "The foundational t-SNE paper"
  - title: "UMAP: Uniform Manifold Approximation and Projection"
    url: "https://arxiv.org/abs/1802.03426"
    description: "The UMAP paper by McInnes, Healy, and Melville"
  - title: "A Tutorial on Principal Component Analysis (Shlens)"
    url: "https://arxiv.org/abs/1404.1100"
    description: "Shlens' accessible PCA tutorial from a signal processing perspective"
  - title: "How to Use t-SNE Effectively"
    url: "https://distill.pub/2016/misread-tsne/"
    description: "Distill.pub interactive guide to avoiding t-SNE pitfalls"
knowledge_refs:
  - ml-14-feature-scaling
  - ml-19-k-means-clustering
  - ml-12-k-nearest-neighbors
---

# Dimensionality Reduction

High-dimensional data is hard to visualize, slow to process, and prone to the curse of dimensionality. Dimensionality reduction compresses data into fewer dimensions while preserving meaningful structure.

## Why Reduce Dimensions?

1. **Visualization**: Plot 10,000-dimensional data in 2D/3D
2. **Speed**: Fewer features = faster training
3. **Curse of dimensionality**: Distance metrics become meaningless in high dimensions
4. **Noise reduction**: Remove irrelevant dimensions
5. **Feature engineering**: Create compact representations for downstream models

## PCA (Principal Component Analysis)

PCA finds the directions of maximum variance and projects data onto them:

1. Standardize the data (zero mean, unit variance)
2. Compute the covariance matrix
3. Compute eigenvalues and eigenvectors
4. Sort eigenvectors by eigenvalue (variance explained)
5. Keep top $k$ eigenvectors (principal components)

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=0.95)  # keep 95% of variance
X_reduced = pca.fit_transform(X)

print(f"Original: {X.shape[1]} features")
print(f"Reduced: {X_reduced.shape[1]} components")
print(f"Variance explained: {pca.explained_variance_ratio_.cumsum()[-1]:.3f}")
```

### Choosing the Number of Components

```python
pca = PCA().fit(X)
cumvar = pca.explained_variance_ratio_.cumsum()

import matplotlib.pyplot as plt
plt.plot(range(1, len(cumvar)+1), cumvar, 'bo-')
plt.axhline(y=0.95, color='r', linestyle='--', label='95% variance')
plt.xlabel('Number of components')
plt.ylabel('Cumulative variance explained')
plt.legend()
```

**Rules of thumb:**
- Keep components explaining 95% of variance
- Look for the "elow" in the scree plot
- Keep enough for visualization (2-3 for plots)

### PCA for Visualization

```python
# Reduce to 2D for visualization
pca_2d = PCA(n_components=2)
X_2d = pca_2d.fit_transform(X)

plt.scatter(X_2d[:, 0], X_2d[:, 1], c=labels, cmap='viridis', alpha=0.6)
plt.xlabel(f'PC1 ({pca_2d.explained_variance_ratio_[0]:.1%})')
plt.ylabel(f'PC2 ({pca_2d.explained_variance_ratio_[1]:.1%})')
```

### Kernel PCA

For non-linear structure, Kernel PCA applies the kernel trick:
```python
from sklearn.decomposition import KernelPCA
kpca = KernelPCA(n_components=2, kernel='rbf', gamma=15)
X_kpca = kpca.fit_transform(X)
```

## t-SNE (t-distributed Stochastic Neighbor Embedding)

t-SNE excels at preserving **local structure** — keeping nearby points nearby in the low-dimensional embedding. It's the gold standard for visualization.

**How it works:**
1. Compute pairwise similarities in high-D using Gaussian kernel
2. Initialize points randomly in low-D
3. Compute pairwise similarities in low-D using t-distribution
4. Minimize KL divergence between high-D and low-D similarities via gradient descent

```python
from sklearn.manifold import TSNE

tsne = TSNE(n_components=2, perplexity=30, random_state=42, n_iter=1000)
X_embedded = tsne.fit_transform(X)
```

### Key Parameters

| Parameter | Effect | Default |
|---|---|---|
| `perplexity` | Balance local vs. global structure (5-50) | 30 |
| `n_iter` | Optimization steps (more = better convergence) | 1000 |
| `learning_rate` | Step size (10-1000) | 200 |
| `early_exaggeration` | How tight clusters are in early phase | 12 |

### t-SNE Pitfalls

- **Cluster distances are meaningless**: Don't interpret distances between clusters
- **Different runs give different results**: Always set `random_state`
- **Perplexity matters**: Try multiple values (5, 30, 50)
- **Not for downstream ML**: t-SNE is for visualization only (distortions are too large)
- **Computationally expensive**: $O(N^2)$ — subsample for large datasets

## UMAP (Uniform Manifold Approximation and Projection)

UMAP preserves both local and global structure better than t-SNE, is faster, and scales better:

```python
import umap

reducer = umap.UMAP(n_components=2, n_neighbors=15, min_dist=0.1, random_state=42)
X_embedded = reducer.fit_transform(X)
```

### Key Parameters

| Parameter | Effect | Default |
|---|---|---|
| `n_neighbors` | Balance local vs. global (5-50) | 15 |
| `min_dist` | How tightly points cluster (0-1) | 0.1 |
| `n_components` | Output dimensions (2, 3, or more) | 2 |
| `metric` | Distance metric to use | 'euclidean' |

### UMAP vs t-SNE

| Aspect | t-SNE | UMAP |
|---|---|---|
| Speed | Slow ($O(N^2)$) | Fast ($O(N)$ approximate) |
| Global structure | Poor | Better |
| Scalability | Subsample > 10K | Handles 100K+ |
| Inverse transform | No | Yes (approximate) |
| Supervised mode | No | Yes |
| New data | No (must retrain) | Yes (transform) |

### UMAP for ML Pipelines

Unlike t-SNE, UMAP can be used as a preprocessing step:
```python
import umap

reducer = umap.UMAP(n_components=10)
X_reduced = reducer.fit_transform(X_train)
X_test_reduced = reducer.transform(X_test)  # works on new data!

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(X_reduced, y_train)
```

## Other Methods

### Linear Discriminant Analysis (LDA)
Supervised dimensionality reduction — finds directions that maximize class separation:
```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X, y)  # needs labels!
```

### Independent Component Analysis (ICA)
Finds statistically independent components (not just uncorrelated like PCA):
```python
from sklearn.decomposition import FastICA
ica = FastICA(n_components=10)
X_ica = ica.fit_transform(X)
```

### Non-Negative Matrix Factorization (NMF)
For non-negative data (e.g., word counts, images):
```python
from sklearn.decomposition import NMF
nmf = NMF(n_components=10, random_state=42)
X_nmf = nmf.fit_transform(X)  # X must be non-negative
```

## Practical Guidelines

| Use Case | Method |
|---|---|
| Visualization | UMAP (default), t-SNE (for small N) |
| Preprocessing for ML | PCA (95% variance) or UMAP |
| Supervised reduction | LDA, Supervised UMAP |
| Text data | PCA on TF-IDF, or NMF for topic modeling |
| Image data | PCA (Eigenfaces), Autoencoders |
| Non-linear structure | Kernel PCA, UMAP |

## The Pipeline

Always scale before PCA:
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=0.95)),
    ('classifier', RandomForestClassifier())
])
scores = cross_val_score(pipeline, X, y, cv=5)
```

## Further Reading

- Shlens' PCA tutorial is the most accessible mathematical treatment
- The distill.pub t-SNE guide is essential for avoiding common pitfalls
- UMAP documentation covers both the math and practical usage
- For deep learning approaches, see autoencoders and variational autoencoders (VAEs)
