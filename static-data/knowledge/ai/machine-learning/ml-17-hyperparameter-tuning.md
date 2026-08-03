---
{
  "title": "Hyperparameter Tuning",
  "description": "Search parameter space systematically with grid, random and Bayesian strategies — without leaking into the test set.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Distinguish parameters from hyperparameters",
    "Run grid search with cross-validation",
    "Use randomized search for large spaces",
    "Avoid tuning on the test set"
  ],
  "knowledge_refs": [
    "machine-learning/ml-16-cross-validation",
    "llm-engineering/llm-16-cost-optimization",
    "reinforcement-learning/rl-12-proximal-policy-optimization"
  ],
  "prerequisites": [
    "ML-16: Cross-Validation"
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

# ML-17-HYPERPARAMETER-TUNING: Hyperparameter Tuning

## Introduction

Search parameter space systematically with grid, random and Bayesian strategies — without leaking into the test set. By the end of this lesson you will be able to: Distinguish parameters from hyperparameters; Run grid search with cross-validation; Use randomized search for large spaces; Avoid tuning on the test set.

## Key Concepts

### 1. Distinguish parameters from hyperparameters

Target: Distinguish parameters from hyperparameters. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
search = GridSearchCV(
    RandomForestClassifier(random_state=0),
    {"n_estimators": [50, 200], "max_depth": [2, None]},
    cv=5,
)
search.fit(X, y)
print("best params:", search.best_params_)
```
### 2. Run grid search with cross-validation

Target: Run grid search with cross-validation. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import randint

search = RandomizedSearchCV(
    RandomForestClassifier(random_state=0),
    {"n_estimators": randint(50, 300), "max_depth": randint(2, 10)},
    n_iter=10, cv=5, random_state=0,
)
print("random search ready:", search.param_distributions.keys())
```
### 3. Use randomized search for large spaces

Target: Use randomized search for large spaces. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression

param_grid = {"C": [0.01, 0.1, 1, 10, 100], "solver": ["lbfgs"]}
search = GridSearchCV(LogisticRegression(max_iter=1000), param_grid, cv=5)
print("grid points:", len(param_grid["C"]), "x 1 solver")
```
### 4. Avoid tuning on the test set

Target: Avoid tuning on the test set. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# The tuning trap: the best CV model still needs a held-out check
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=0)
best = RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0)
print("cv:", round(cross_val_score(best, X_tr, y_tr, cv=5).mean(), 3))
print("test:", round(best.fit(X_tr, y_tr).score(X_te, y_te), 3))
```

## Practice Questions

1. What is the key idea behind "Hyperparameter Tuning"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Hyperparameter Tuning with analogies and real-world examples"
1. "Show me common mistakes beginners make with Hyperparameter Tuning"
1. "Provide advanced patterns and performance considerations for Hyperparameter Tuning"

## Key Takeaways

- Master the core ideas of Hyperparameter Tuning through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
