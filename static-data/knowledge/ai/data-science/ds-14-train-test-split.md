---
{
  "title": "Train/Test Splits & Validation",
  "description": "The disciplined way to estimate model quality: hold out data, avoid leakage, and validate like it matters.",
  "type": "lesson",
  "order": 14,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Split data into train, validation and test sets",
    "Prevent target leakage in preprocessing",
    "Explain why test data must stay untouched",
    "Handle time-series splits correctly"
  ],
  "knowledge_refs": [
    "data-science/ds-14-train-test-split"
  ],
  "prerequisites": [
    "DS-13: Feature Engineering"
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

# DS-14-TRAIN-TEST-SPLIT: Train/Test Splits & Validation

## Introduction

The disciplined way to estimate model quality: hold out data, avoid leakage, and validate like it matters. By the end of this lesson you will be able to: Split data into train, validation and test sets; Prevent target leakage in preprocessing; Explain why test data must stay untouched; Handle time-series splits correctly.

## Key Concepts

### 1. Split data into train, validation and test sets

Target: Split data into train, validation and test sets. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from sklearn.model_selection import train_test_split
import numpy as np

X = np.arange(100).reshape(50, 2)
y = np.arange(50)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_tr.shape, X_te.shape)
```
### 2. Prevent target leakage in preprocessing

Target: Prevent target leakage in preprocessing. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60]]
y = [0, 0, 1, 1, 0, 1]
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.33, random_state=0)
# Fit the scaler on TRAIN ONLY, then transform both
scaler = StandardScaler().fit(X_tr)
print(scaler.transform(X_te).round(2))
```
### 3. Explain why test data must stay untouched

Target: Explain why test data must stay untouched. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# Time series: never shuffle across time
dates = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
train, test = dates[:7], dates[7:]
print("train:", train, "test:", test)
```
### 4. Handle time-series splits correctly

Target: Handle time-series splits correctly. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.DataFrame({"x": [1, 2, 3, 4, 5, 6], "y": [0, 0, 1, 1, 1, 0]})
# Stratify keeps class proportions in both splits
tr, te = train_test_split(df, test_size=0.33, random_state=0, stratify=df["y"])
print(te)
```

## Practice Questions

1. What is the key idea behind "Train/Test Splits & Validation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Train/Test Splits & Validation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Train/Test Splits & Validation"
1. "Provide advanced patterns and performance considerations for Train/Test Splits & Validation"

## Key Takeaways

- Master the core ideas of Train/Test Splits & Validation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
