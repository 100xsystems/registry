---
{
  "title": "Linear Regression",
  "description": "The workhorse of prediction: least squares, multiple predictors, and interpreting coefficients.",
  "type": "lesson",
  "order": 5,
  "duration": "55 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Fit linear regression with multiple features",
    "Interpret coefficients as conditional effects",
    "Diagnose residuals",
    "Avoid common misuse with correlated features"
  ],
  "knowledge_refs": [
    "machine-learning/ml-04-python-ml-stack",
    "deep-learning/dl-02-perceptron-and-linear-units",
    "computer-vision/cv-05-image-classification"
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

# ML-05-LINEAR-REGRESSION: Linear Regression

## Introduction

The workhorse of prediction: least squares, multiple predictors, and interpreting coefficients. By the end of this lesson you will be able to: Fit linear regression with multiple features; Interpret coefficients as conditional effects; Diagnose residuals; Avoid common misuse with correlated features.

## Key Concepts

### 1. Fit linear regression with multiple features

Target: Fit linear regression with multiple features. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.linear_model import LinearRegression

X = [[1, 5], [2, 6], [3, 7], [4, 8]]
y = [9, 14, 19, 24]
m = LinearRegression().fit(X, y)
print("coefs:", m.coef_.round(2), "intercept:", round(m.intercept_, 2))
```
### 2. Interpret coefficients as conditional effects

Target: Interpret coefficients as conditional effects. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# Prediction and residual diagnosis
pred = m.predict(X)
res = np.array(y) - pred
print("residual mean:", round(res.mean(), 6))
print("max |residual|:", round(np.abs(res).max(), 3))
```
### 3. Diagnose residuals

Target: Diagnose residuals. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.linear_model import LinearRegression

# Correlated features make individual coefficients unstable
X = [[1, 2], [2, 4], [3, 6], [4, 8]]
y = [3, 6, 9, 12]
m = LinearRegression().fit(X, y)
print("unstable coefs:", m.coef_.round(2))
```
### 4. Avoid common misuse with correlated features

Target: Avoid common misuse with correlated features. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Manually: closed-form normal equation for the slope
x = np.array([1, 2, 3, 4])
y = np.array([2, 4, 6, 8])
slope = np.sum((x - x.mean()) * (y - y.mean())) / np.sum((x - x.mean()) ** 2)
print("slope:", slope)
```

## Practice Questions

1. What is the key idea behind "Linear Regression"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Linear Regression with analogies and real-world examples"
1. "Show me common mistakes beginners make with Linear Regression"
1. "Provide advanced patterns and performance considerations for Linear Regression"

## Key Takeaways

- Master the core ideas of Linear Regression through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
