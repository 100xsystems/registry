---
{
  "title": "Classification Models",
  "description": "Predict categories with logistic regression and neighbors, and learn what decision boundaries really mean.",
  "type": "lesson",
  "order": 16,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Frame a business question as a classification task",
    "Fit and interpret logistic regression",
    "Use k-NN and understand decision boundaries",
    "Read probability outputs, not just labels"
  ],
  "knowledge_refs": [
    "data-science/ds-16-classification-models"
  ],
  "prerequisites": [
    "DS-15: Regression Models"
  ],
  "references": [
    {
      "title": "Python for Data Analysis — Wes McKinney",
      "url": "https://wesmckinney.com/book/",
      "description": "The definitive guide to pandas, NumPy and the PyData stack."
    },
    {
      "title": "Pandas User Guide",
      "url": "https://pandas.pydata.org/docs/user_guide/index.html",
      "description": "Official documentation for the pandas data-analysis library."
    },
    {
      "title": "The Elements of Statistical Learning",
      "url": "https://hastie.su.domains/ElemStatLearn/",
      "description": "The classic statistical-learning reference (free PDF)."
    },
    {
      "title": "Kaggle Learn — Data Science",
      "url": "https://www.kaggle.com/learn",
      "description": "Hands-on micro-courses covering pandas, EDA and modeling."
    },
    {
      "title": "scikit-learn User Guide",
      "url": "https://scikit-learn.org/stable/user_guide.html",
      "description": "Authoritative guide to the Python machine-learning toolbox."
    }
  ]
}
---

# DS-16-CLASSIFICATION-MODELS: Classification Models

## Introduction

Predict categories with logistic regression and neighbors, and learn what decision boundaries really mean. By the end of this lesson you will be able to: Frame a business question as a classification task; Fit and interpret logistic regression; Use k-NN and understand decision boundaries; Read probability outputs, not just labels.

## Key Concepts

### 1. Frame a business question as a classification task

Target: Frame a business question as a classification task. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.array([[1, 2], [2, 3], [3, 1], [8, 8], [9, 9], [7, 10]])
y = np.array([0, 0, 0, 1, 1, 1])
model = LogisticRegression().fit(X, y)
print("accuracy:", round(model.score(X, y), 2))
print("class prob:", model.predict_proba([[4, 5]]).round(2))
```
### 2. Fit and interpret logistic regression

Target: Fit and interpret logistic regression. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from sklearn.linear_model import LogisticRegression

X = [[1, 2], [2, 3], [3, 1], [8, 8], [9, 9], [7, 10]]
y = [0, 0, 0, 1, 1, 1]
model = LogisticRegression().fit(X, y)
print("coefs:", model.coef_.round(3), "intercept:", round(model.intercept_[0], 3))
```
### 3. Use k-NN and understand decision boundaries

Target: Use k-NN and understand decision boundaries. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.neighbors import KNeighborsClassifier

X = [[0, 0], [0, 1], [5, 5], [6, 5]]
y = [0, 0, 1, 1]
for k in [1, 3]:
    m = KNeighborsClassifier(n_neighbors=k).fit(X, y)
    print(f"k={k}: pred for (2,2) ->", m.predict([[2, 2]])[0])
```
### 4. Read probability outputs, not just labels

Target: Read probability outputs, not just labels. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [10], [11], [12]]
y = [0, 0, 0, 1, 1, 1]
m = LogisticRegression().fit(X, y)
for point in [[2], [6], [10]]:
    print(f"x={point[0]} -> P(class=1) = {m.predict_proba(point)[0][1]:.2f}")
```

## Practice Questions

1. What is the key idea behind "Classification Models"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Classification Models with analogies and real-world examples"
1. "Show me common mistakes beginners make with Classification Models"
1. "Provide advanced patterns and performance considerations for Classification Models"

## Key Takeaways

- Master the core ideas of Classification Models through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
