---
{
  "title": "K-Nearest Neighbors",
  "description": "The simplest nonparametric model: predict by voting among the closest training points.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Explain how k-NN makes predictions",
    "Tune k and distance metrics",
    "Scale features for distance-based models",
    "Describe the curse of dimensionality"
  ],
  "knowledge_refs": [
    "machine-learning/ml-11-support-vector-machines"
  ],
  "prerequisites": [
    "ML-04: The Python ML Stack"
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

# ML-12-K-NEAREST-NEIGHBORS: K-Nearest Neighbors

## Introduction

The simplest nonparametric model: predict by voting among the closest training points. By the end of this lesson you will be able to: Explain how k-NN makes predictions; Tune k and distance metrics; Scale features for distance-based models; Describe the curse of dimensionality.

## Key Concepts

### 1. Explain how k-NN makes predictions

Target: Explain how k-NN makes predictions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.neighbors import KNeighborsClassifier

X = [[0, 0], [0, 1], [5, 5], [6, 5]]
y = [0, 0, 1, 1]
clf = KNeighborsClassifier(n_neighbors=3).fit(X, y)
print("pred (2,2):", clf.predict([[2, 2]])[0])
```
### 2. Tune k and distance metrics

Target: Tune k and distance metrics. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from sklearn.neighbors import KNeighborsRegressor

X = [[1], [2], [3], [4]]
y = [10, 20, 30, 40]
for k in [1, 3]:
    m = KNeighborsRegressor(n_neighbors=k).fit(X, y)
    print(f"k={k}: pred(2.5) = {m.predict([[2.5]])[0]:.1f}")
```
### 3. Scale features for distance-based models

Target: Scale features for distance-based models. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

X = [[1, 1000], [2, 2000], [3, 3000]]
y = [0, 1, 1]
Xs = StandardScaler().fit_transform(X)
print(KNeighborsClassifier(n_neighbors=1).fit(Xs, y).predict(StandardScaler().fit(X).transform([[2, 2100]])))
```
### 4. Describe the curse of dimensionality

Target: Describe the curse of dimensionality. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Curse of dimensionality: distance flattens in high dims
rng = np.random.default_rng(0)
for dim in [2, 20, 200]:
    pts = rng.uniform(size=(1000, dim))
    d = np.linalg.norm(pts - pts[0], axis=1)[1:]
    print(f"dim={dim}: mean dist {d.mean():.2f}, min {d.min():.2f}")
```

## Practice Questions

1. What is the key idea behind "K-Nearest Neighbors"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain K-Nearest Neighbors with analogies and real-world examples"
1. "Show me common mistakes beginners make with K-Nearest Neighbors"
1. "Provide advanced patterns and performance considerations for K-Nearest Neighbors"

## Key Takeaways

- Master the core ideas of K-Nearest Neighbors through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
