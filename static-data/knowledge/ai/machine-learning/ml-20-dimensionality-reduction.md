---
{
  "title": "Dimensionality Reduction with PCA",
  "description": "Project high-dimensional data onto its principal components — for visualization, denoising and speed.",
  "type": "lesson",
  "order": 20,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain what principal components capture",
    "Apply PCA and read explained variance",
    "Use PCA before clustering or visualization",
    "Know when PCA hurts"
  ],
  "knowledge_refs": [
    "machine-learning/ml-19-kmeans-clustering"
  ],
  "prerequisites": [
    "ML-19: K-Means & Clustering"
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

# ML-20-DIMENSIONALITY-REDUCTION: Dimensionality Reduction with PCA

## Introduction

Project high-dimensional data onto its principal components — for visualization, denoising and speed. By the end of this lesson you will be able to: Explain what principal components capture; Apply PCA and read explained variance; Use PCA before clustering or visualization; Know when PCA hurts.

## Key Concepts

### 1. Explain what principal components capture

Target: Explain what principal components capture. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits

X, _ = load_digits(return_X_y=True)
pca = PCA(n_components=2).fit(X)
print("explained variance:", pca.explained_variance_ratio_.round(3))
```
### 2. Apply PCA and read explained variance

Target: Apply PCA and read explained variance. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from sklearn.decomposition import PCA
import numpy as np

X = np.random.default_rng(0).normal(size=(100, 50))
pca = PCA().fit(X)
cum = np.cumsum(pca.explained_variance_ratio_)
print("components for 95%:", int(np.argmax(cum >= 0.95)) + 1)
```
### 3. Use PCA before clustering or visualization

Target: Use PCA before clustering or visualization. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

X = [[1, 2, 3, 1], [2, 3, 4, 2], [10, 11, 12, 10], [11, 12, 13, 11]]
X2 = PCA(n_components=2).fit_transform(X)
print("cluster on 2 dims:", KMeans(n_clusters=2, n_init=10, random_state=0).fit_predict(X2))
```
### 4. Know when PCA hurts

Target: Know when PCA hurts. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
from sklearn.decomposition import PCA

# PCA centers the data first; scale before use if units differ
import numpy as np
X = np.array([[1, 1000], [2, 2000], [3, 1500]])
print(PCA(n_components=1).fit_transform(X).round(2).ravel())
```

## Practice Questions

1. What is the key idea behind "Dimensionality Reduction with PCA"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Dimensionality Reduction with PCA with analogies and real-world examples"
1. "Show me common mistakes beginners make with Dimensionality Reduction with PCA"
1. "Provide advanced patterns and performance considerations for Dimensionality Reduction with PCA"

## Key Takeaways

- Master the core ideas of Dimensionality Reduction with PCA through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
