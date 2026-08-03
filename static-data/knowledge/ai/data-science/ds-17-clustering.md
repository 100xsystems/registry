---
{
  "title": "Clustering",
  "description": "Find structure without labels: k-means, distance metrics, and choosing the number of clusters honestly.",
  "type": "lesson",
  "order": 17,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain unsupervised learning and clustering goals",
    "Run k-means with scikit-learn",
    "Choose k with the elbow and silhouette methods",
    "Scale features before computing distances"
  ],
  "knowledge_refs": [
    "data-science/ds-17-clustering"
  ],
  "prerequisites": [
    "DS-16: Classification Models"
  ],
  "references": [
    {
      "title": "Python for Data Analysis — Wes McKinney",
      "url": "https://wesmckinney.com/book/",
      "description": "The definitive guide to pandas, NumPy and the PyData stack."
    },
    {
      "title": "Pandas User Guide",
      "url": "https://pandas.pydata.org/docs/user_guide/index.html",
      "description": "Official documentation for the pandas data-analysis library."
    },
    {
      "title": "The Elements of Statistical Learning",
      "url": "https://hastie.su.domains/ElemStatLearn/",
      "description": "The classic statistical-learning reference (free PDF)."
    },
    {
      "title": "Kaggle Learn — Data Science",
      "url": "https://www.kaggle.com/learn",
      "description": "Hands-on micro-courses covering pandas, EDA and modeling."
    },
    {
      "title": "scikit-learn User Guide",
      "url": "https://scikit-learn.org/stable/user_guide.html",
      "description": "Authoritative guide to the Python machine-learning toolbox."
    }
  ]
}
---

# DS-17-CLUSTERING: Clustering

## Introduction

Find structure without labels: k-means, distance metrics, and choosing the number of clusters honestly. By the end of this lesson you will be able to: Explain unsupervised learning and clustering goals; Run k-means with scikit-learn; Choose k with the elbow and silhouette methods; Scale features before computing distances.

## Key Concepts

### 1. Explain unsupervised learning and clustering goals

Target: Explain unsupervised learning and clustering goals. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1, 1], [1, 2], [2, 1], [8, 8], [9, 9], [8, 9]])
km = KMeans(n_clusters=2, n_init=10, random_state=0).fit(X)
print("labels:", km.labels_)
print("centers:", km.cluster_centers_)
```
### 2. Run k-means with scikit-learn

Target: Run k-means with scikit-learn. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np
from sklearn.cluster import KMeans

X = np.random.default_rng(0).normal(size=(200, 2))
inertias = [KMeans(n_clusters=k, n_init=10, random_state=0).fit(X).inertia_ for k in range(1, 7)]
print("inertia by k:", [round(i, 1) for i in inertias])
```
### 3. Choose k with the elbow and silhouette methods

Target: Choose k with the elbow and silhouette methods. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np

X = np.random.default_rng(1).normal(size=(100, 2))
for k in [2, 3, 4]:
    labels = KMeans(n_clusters=k, n_init=10, random_state=0).fit_predict(X)
    print(f"k={k} silhouette={silhouette_score(X, labels):.3f}")
```
### 4. Scale features before computing distances

Target: Scale features before computing distances. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Scale first: distance in raw units misleads
X = [[1, 1000], [2, 2000], [3, 1500], [50, 5000]]
Xs = StandardScaler().fit_transform(X)
print(KMeans(n_clusters=2, n_init=10, random_state=0).fit_predict(Xs))
```

## Practice Questions

1. What is the key idea behind "Clustering"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Clustering with analogies and real-world examples"
1. "Show me common mistakes beginners make with Clustering"
1. "Provide advanced patterns and performance considerations for Clustering"

## Key Takeaways

- Master the core ideas of Clustering through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
