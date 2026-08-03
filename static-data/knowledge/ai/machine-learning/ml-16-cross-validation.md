---
{
  "title": "Cross-Validation",
  "description": "k-fold cross-validation gives a more honest error estimate than a single split — and catches tuning leaks.",
  "type": "lesson",
  "order": 16,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Run k-fold cross-validation with scikit-learn",
    "Explain why k-fold beats one train/test split",
    "Use CV to tune hyperparameters without touching the test set",
    "Stratify folds for imbalanced targets"
  ],
  "knowledge_refs": [
    "machine-learning/ml-16-cross-validation"
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

# ML-16-CROSS-VALIDATION: Cross-Validation

## Introduction

k-fold cross-validation gives a more honest error estimate than a single split — and catches tuning leaks. By the end of this lesson you will be able to: Run k-fold cross-validation with scikit-learn; Explain why k-fold beats one train/test split; Use CV to tune hyperparameters without touching the test set; Stratify folds for imbalanced targets.

## Key Concepts

### 1. Run k-fold cross-validation with scikit-learn

Target: Run k-fold cross-validation with scikit-learn. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
scores = cross_val_score(RandomForestClassifier(random_state=0), X, y, cv=5)
print("fold scores:", scores.round(3))
print("mean:", round(scores.mean(), 3))
```
### 2. Explain why k-fold beats one train/test split

Target: Explain why k-fold beats one train/test split. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
for C in [0.1, 1, 10]:
    score = cross_val_score(LogisticRegression(C=C, max_iter=500), X, y, cv=5).mean()
    print(f"C={C}: cv accuracy {score:.3f}")
```
### 3. Use CV to tune hyperparameters without touching the test set

Target: Use CV to tune hyperparameters without touching the test set. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.model_selection import StratifiedKFold

kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
print("stratified folds keep class balance")
```
### 4. Stratify folds for imbalanced targets

Target: Stratify folds for imbalanced targets. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Leave-one-out intuition for small datasets
from sklearn.model_selection import LeaveOneOut

X = np.arange(6).reshape(3, 2)
loo = LeaveOneOut()
print("LOO folds:", sum(1 for _ in loo.split(X)))
```

## Practice Questions

1. What is the key idea behind "Cross-Validation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Cross-Validation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Cross-Validation"
1. "Provide advanced patterns and performance considerations for Cross-Validation"

## Key Takeaways

- Master the core ideas of Cross-Validation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
