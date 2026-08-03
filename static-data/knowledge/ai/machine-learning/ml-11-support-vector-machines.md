---
{
  "title": "Support Vector Machines",
  "description": "Max-margin classification, the kernel trick, and when SVMs beat other models.",
  "type": "lesson",
  "order": 11,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain the maximum-margin idea",
    "Use the kernel trick for nonlinear boundaries",
    "Tune C and gamma",
    "Prefer SVMs on small, high-dimensional datasets"
  ],
  "knowledge_refs": [
    "machine-learning/ml-10-gradient-boosting",
    "generative-ai/genai-11-embeddings-and-vector-databases",
    "nlp/nlp-06-word-embeddings"
  ],
  "prerequisites": [
    "ML-07: Logistic Regression"
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

# ML-11-SUPPORT-VECTOR-MACHINES: Support Vector Machines

## Introduction

Max-margin classification, the kernel trick, and when SVMs beat other models. By the end of this lesson you will be able to: Explain the maximum-margin idea; Use the kernel trick for nonlinear boundaries; Tune C and gamma; Prefer SVMs on small, high-dimensional datasets.

## Key Concepts

### 1. Explain the maximum-margin idea

Target: Explain the maximum-margin idea. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.svm import SVC

X = [[1, 1], [2, 2], [2, 0], [8, 8], [9, 9], [8, 10]]
y = [0, 0, 0, 1, 1, 1]
clf = SVC(kernel="linear").fit(X, y)
print("support vectors:", len(clf.support_vectors_))
```
### 2. Use the kernel trick for nonlinear boundaries

Target: Use the kernel trick for nonlinear boundaries. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from sklearn.svm import SVC

# RBF kernel draws nonlinear boundaries
clf = SVC(kernel="rbf", C=10, gamma="scale").fit(X, y)
print("rbf accuracy:", round(clf.score(X, y), 2))
```
### 3. Tune C and gamma

Target: Tune C and gamma. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.svm import SVC

for C in [0.1, 10]:
    clf = SVC(kernel="linear", C=C).fit(X, y)
    print(f"C={C}: support vectors = {len(clf.support_vectors_)}")
```
### 4. Prefer SVMs on small, high-dimensional datasets

Target: Prefer SVMs on small, high-dimensional datasets. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
from sklearn.svm import SVC

# Margin intuition: distance from boundary to nearest point
import numpy as np
X = np.array([[1, 1], [2, 2], [2, 0], [8, 8], [9, 9], [8, 10]])
y = np.array([0, 0, 0, 1, 1, 1])
clf = SVC(kernel="linear", C=1e6).fit(X, y)
w = clf.coef_[0]
margin = 2 / np.linalg.norm(w)
print("margin width:", round(margin, 3))
```

## Practice Questions

1. What is the key idea behind "Support Vector Machines"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Support Vector Machines with analogies and real-world examples"
1. "Show me common mistakes beginners make with Support Vector Machines"
1. "Provide advanced patterns and performance considerations for Support Vector Machines"

## Key Takeaways

- Master the core ideas of Support Vector Machines through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
