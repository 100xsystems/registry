---
{
  "title": "Logistic Regression",
  "description": "Probability for classification: the sigmoid, log loss, and decision boundaries that stay interpretable.",
  "type": "lesson",
  "order": 7,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain why linear models need a sigmoid for classification",
    "Interpret predicted probabilities",
    "Read log-odds coefficients",
    "Set decision thresholds by business cost"
  ],
  "knowledge_refs": [
    "machine-learning/ml-06-gradient-descent",
    "computer-vision/cv-05-image-classification",
    "nlp/nlp-07-text-classification"
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

# ML-07-LOGISTIC-REGRESSION: Logistic Regression

## Introduction

Probability for classification: the sigmoid, log loss, and decision boundaries that stay interpretable. By the end of this lesson you will be able to: Explain why linear models need a sigmoid for classification; Interpret predicted probabilities; Read log-odds coefficients; Set decision thresholds by business cost.

## Key Concepts

### 1. Explain why linear models need a sigmoid for classification

Target: Explain why linear models need a sigmoid for classification. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

for z in [-3, 0, 3]:
    print(f"z={z}: P = {sigmoid(z):.3f}")
```
### 2. Interpret predicted probabilities

Target: Interpret predicted probabilities. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [10], [11], [12]]
y = [0, 0, 0, 1, 1, 1]
m = LogisticRegression().fit(X, y)
print("coef:", round(m.coef_[0][0], 3), "intercept:", round(m.intercept_[0], 3))
```
### 3. Read log-odds coefficients

Target: Read log-odds coefficients. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# Threshold by cost: false negatives are 10x more expensive
scores = np.array([0.3, 0.6, 0.8])
for t in [0.5, 0.7]:
    preds = (scores >= t).astype(int)
    print(f"t={t} -> {preds}")
```
### 4. Set decision thresholds by business cost

Target: Set decision thresholds by business cost. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss

X = [[1], [2], [3], [10], [11], [12]]
y = [0, 0, 0, 1, 1, 1]
m = LogisticRegression().fit(X, y)
print("log loss:", round(log_loss(y, m.predict_proba(X)), 3))
```

## Practice Questions

1. What is the key idea behind "Logistic Regression"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Logistic Regression with analogies and real-world examples"
1. "Show me common mistakes beginners make with Logistic Regression"
1. "Provide advanced patterns and performance considerations for Logistic Regression"

## Key Takeaways

- Master the core ideas of Logistic Regression through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
