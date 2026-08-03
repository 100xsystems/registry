---
{
  "title": "Regularization",
  "description": "Penalize complexity: L1 and L2 regularization, and the bias-variance trade-off made concrete.",
  "type": "lesson",
  "order": 15,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain L1 and L2 penalties",
    "Use Ridge and Lasso for shrinkage",
    "Use L1 for automatic feature selection",
    "Tune the regularization strength"
  ],
  "knowledge_refs": [
    "deep-learning/dl-11-regularization-for-deep-learning",
    "machine-learning/ml-14-feature-scaling-and-selection"
  ],
  "prerequisites": [
    "ML-06: Gradient Descent"
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

# ML-15-REGULARIZATION: Regularization

## Introduction

Penalize complexity: L1 and L2 regularization, and the bias-variance trade-off made concrete. By the end of this lesson you will be able to: Explain L1 and L2 penalties; Use Ridge and Lasso for shrinkage; Use L1 for automatic feature selection; Tune the regularization strength.

## Key Concepts

### 1. Explain L1 and L2 penalties

Target: Explain L1 and L2 penalties. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.linear_model import Ridge, Lasso

X = [[1, 1], [2, 2], [3, 3], [4, 4]]
y = [2, 4, 6, 8]
print("ridge:", Ridge(alpha=1.0).fit(X, y).coef_.round(2))
print("lasso:", Lasso(alpha=0.5).fit(X, y).coef_.round(2))
```
### 2. Use Ridge and Lasso for shrinkage

Target: Use Ridge and Lasso for shrinkage. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# L2 penalty pulls weights toward zero
def ridge_step(w, grad, lr, alpha):
    return w - lr * (grad + 2 * alpha * w)

w = 2.0
for _ in range(50):
    w = ridge_step(w, 2 * (w - 1), 0.1, 0.3)
print("shrunk weight:", round(w, 3))
```
### 3. Use L1 for automatic feature selection

Target: Use L1 for automatic feature selection. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.linear_model import Lasso

X = [[1, 0, 50], [2, 1, 60], [3, 0, 70]]
y = [5, 8, 11]
for alpha in [0.001, 10]:
    coefs = Lasso(alpha=alpha).fit(X, y).coef_
    print(f"alpha={alpha}: coefs {coefs.round(2)}")
```
### 4. Tune the regularization strength

Target: Tune the regularization strength. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
from sklearn.linear_model import RidgeCV

X = [[1], [2], [3], [4]]
y = [2, 4, 6, 8]
best = RidgeCV(alphas=[0.1, 1, 10]).fit(X, y)
print("chosen alpha:", best.alpha_)
```

## Practice Questions

1. What is the key idea behind "Regularization"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Regularization with analogies and real-world examples"
1. "Show me common mistakes beginners make with Regularization"
1. "Provide advanced patterns and performance considerations for Regularization"

## Key Takeaways

- Master the core ideas of Regularization through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
