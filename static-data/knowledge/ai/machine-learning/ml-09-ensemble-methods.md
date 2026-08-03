---
{
  "title": "Ensemble Methods: Bagging & Random Forests",
  "description": "Combine many weak models into one strong predictor with bagging and random forests.",
  "type": "lesson",
  "order": 9,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain why averaging reduces variance",
    "Fit a random forest and tune its key knobs",
    "Compare single trees to forests",
    "Use out-of-bag scores as a free validation set"
  ],
  "knowledge_refs": [
    "machine-learning/ml-09-ensemble-methods"
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

# ML-09-ENSEMBLE-METHODS: Ensemble Methods: Bagging & Random Forests

## Introduction

Combine many weak models into one strong predictor with bagging and random forests. By the end of this lesson you will be able to: Explain why averaging reduces variance; Fit a random forest and tune its key knobs; Compare single trees to forests; Use out-of-bag scores as a free validation set.

## Key Concepts

### 1. Explain why averaging reduces variance

Target: Explain why averaging reduces variance. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
rf = RandomForestClassifier(n_estimators=100, random_state=0).fit(X, y)
print("forest accuracy:", round(rf.score(X, y), 3))
```
### 2. Fit a random forest and tune its key knobs

Target: Fit a random forest and tune its key knobs. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# Bagging: average of many bootstrap samples
rng = np.random.default_rng(0)
estimates = [rng.choice([3, 4, 5, 6, 7], size=10).mean() for _ in range(1000)]
print(f"mean of means: {np.mean(estimates):.2f} (vs single sample ~5)")
print(f"sd of means: {np.std(estimates):.2f}")
```
### 3. Compare single trees to forests

Target: Compare single trees to forests. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.ensemble import RandomForestRegressor

X = [[1], [2], [3], [4], [5], [6]]
y = [1, 4, 9, 16, 25, 36]
rf = RandomForestRegressor(n_estimators=50, random_state=0).fit(X, y)
print("prediction:", round(rf.predict([[7]])[0], 1))
```
### 4. Use out-of-bag scores as a free validation set

Target: Use out-of-bag scores as a free validation set. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
rf = RandomForestClassifier(n_estimators=200, oob_score=True, random_state=0).fit(X, y)
print("OOB score:", round(rf.oob_score_, 3))
```

## Practice Questions

1. What is the key idea behind "Ensemble Methods: Bagging & Random Forests"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Ensemble Methods: Bagging & Random Forests with analogies and real-world examples"
1. "Show me common mistakes beginners make with Ensemble Methods: Bagging & Random Forests"
1. "Provide advanced patterns and performance considerations for Ensemble Methods: Bagging & Random Forests"

## Key Takeaways

- Master the core ideas of Ensemble Methods: Bagging & Random Forests through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
