---
{
  "title": "Gradient Descent",
  "description": "The optimization loop under every model: compute the gradient, step downhill, repeat.",
  "type": "lesson",
  "order": 6,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain the gradient as the direction of steepest increase",
    "Implement gradient descent for a simple model",
    "Tune the learning rate",
    "Recognize convergence and divergence symptoms"
  ],
  "knowledge_refs": [
    "machine-learning/ml-05-linear-regression",
    "reinforcement-learning/rl-10-policy-gradient-methods"
  ],
  "prerequisites": [
    "ML-05: Linear Regression"
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

# ML-06-GRADIENT-DESCENT: Gradient Descent

## Introduction

The optimization loop under every model: compute the gradient, step downhill, repeat. By the end of this lesson you will be able to: Explain the gradient as the direction of steepest increase; Implement gradient descent for a simple model; Tune the learning rate; Recognize convergence and divergence symptoms.

## Key Concepts

### 1. Explain the gradient as the direction of steepest increase

Target: Explain the gradient as the direction of steepest increase. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

# f(x) = (x - 3)^2, gradient = 2(x - 3)
x = 10.0
for i in range(10):
    x = x - 0.1 * 2 * (x - 3)
print("converged to:", round(x, 3))
```
### 2. Implement gradient descent for a simple model

Target: Implement gradient descent for a simple model. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

X = np.array([1, 2, 3, 4])
y = np.array([2, 4, 6, 8])
w = 0.0
lr = 0.01
for _ in range(50):
    grad = -2 * np.mean(X * (y - w * X))
    w -= lr * grad
print("learned slope:", round(w, 3))
```
### 3. Tune the learning rate

Target: Tune the learning rate. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

x = 10.0
for lr in [0.01, 0.5, 1.2]:
    v = x
    for _ in range(20):
        v = v - lr * 2 * (v - 3)
    print(f"lr={lr}: final x = {round(v, 2)}")
```
### 4. Recognize convergence and divergence symptoms

Target: Recognize convergence and divergence symptoms. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Stochastic vs batch: noisy updates still converge
X = np.arange(1, 101, dtype=float)
y = 2 * X + 1
w = 0.0
for epoch in range(20):
    for i in range(0, len(X), 10):
        batch = slice(i, i + 10)
        grad = -2 * np.mean(X[batch] * (y[batch] - w * X[batch]))
        w -= 0.0001 * grad
print("mini-batch slope:", round(w, 2))
```

## Practice Questions

1. What is the key idea behind "Gradient Descent"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Gradient Descent with analogies and real-world examples"
1. "Show me common mistakes beginners make with Gradient Descent"
1. "Provide advanced patterns and performance considerations for Gradient Descent"

## Key Takeaways

- Master the core ideas of Gradient Descent through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
