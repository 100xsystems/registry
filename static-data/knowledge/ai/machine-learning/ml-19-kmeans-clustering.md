---
{
  "title": "K-Means & Clustering",
  "description": "Cluster unlabeled data with k-means, pick k responsibly, and interpret clusters as business segments.",
  "type": "lesson",
  "order": 19,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain the k-means objective and algorithm",
    "Preprocess data before clustering",
    "Choose k with inertia and silhouette",
    "Validate clusters with domain knowledge"
  ],
  "knowledge_refs": [
    "machine-learning/ml-18-classification-metrics"
  ],
  "prerequisites": [
    "ML-08: Decision Trees"
  ],
  "references": [
    {
      "title": "scikit-learn User Guide",
      "url": "https://scikit-learn.org/stable/user_guide.html",
      "description": "The authoritative guide to the Python ML toolbox."
    },
    {
      "title": "The Elements of Statistical Learning",
      "url": "https://hastie.su.domains/ElemStatLearn/",
      "description": "The classic statistical-learning reference (free PDF)."
    },
    {
      "title": "Hands-On Machine Learning — Aurélien Géron",
      "url": "https://github.com/ageron/handson-ml3",
      "description": "Practical ML with scikit-learn, Keras and TensorFlow."
    },
    {
      "title": "Andrew Ng — Machine Learning Specialization",
      "url": "https://www.coursera.org/specializations/machine-learning-introduction",
      "description": "The most popular introductory ML course in the world."
    },
    {
      "title": "Kaggle Learn — Intro to Machine Learning",
      "url": "https://www.kaggle.com/learn/intro-to-machine-learning",
      "description": "Hands-on micro-course for the fundamentals."
    }
  ]
}
---

# ML-19-KMEANS-CLUSTERING: K-Means & Clustering

## Introduction

Cluster unlabeled data with k-means, pick k responsibly, and interpret clusters as business segments. By the end of this lesson you will be able to: Explain the k-means objective and algorithm; Preprocess data before clustering; Choose k with inertia and silhouette; Validate clusters with domain knowledge.

## Key Concepts

### 1. Explain the k-means objective and algorithm

Target: Explain the k-means objective and algorithm. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.cluster import KMeans
import numpy as np

X = np.random.default_rng(0).normal(size=(300, 2))
km = KMeans(n_clusters=3, n_init=10, random_state=0).fit(X)
print("cluster sizes:", np.bincount(km.labels_))
```
### 2. Preprocess data before clustering

Target: Preprocess data before clustering. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

X = [[1, 1000], [2, 900], [3, 1100], [60, 4000], [70, 4200]]
Xs = StandardScaler().fit_transform(X)
print(KMeans(n_clusters=2, n_init=10, random_state=0).fit_predict(Xs))
```
### 3. Choose k with inertia and silhouette

Target: Choose k with inertia and silhouette. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np

X = np.random.default_rng(1).normal(size=(200, 2))
best_k, best_s = 2, -1
for k in range(2, 8):
    labels = KMeans(n_clusters=k, n_init=10, random_state=0).fit_predict(X)
    s = silhouette_score(X, labels)
    if s > best_s:
        best_k, best_s = k, s
print(f"best k={best_k}, silhouette={best_s:.3f}")
```
### 4. Validate clusters with domain knowledge

Target: Validate clusters with domain knowledge. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np
from sklearn.cluster import KMeans

# Centroids become interpretable segments
X = np.array([[1, 2], [1, 3], [2, 2], [8, 9], [9, 9]])
km = KMeans(n_clusters=2, n_init=10, random_state=0).fit(X)
print("centroids:", km.cluster_centers_.round(2))
```

## Practice Questions

1. What is the key idea behind "K-Means & Clustering"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain K-Means & Clustering with analogies and real-world examples"
1. "Show me common mistakes beginners make with K-Means & Clustering"
1. "Provide advanced patterns and performance considerations for K-Means & Clustering"

## Key Takeaways

- Master the core ideas of K-Means & Clustering through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
