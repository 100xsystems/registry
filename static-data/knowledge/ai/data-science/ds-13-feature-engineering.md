---
{
  "title": "Feature Engineering",
  "description": "Turn raw columns into features that models can actually learn from: encodings, transforms, dates and domain knowledge.",
  "type": "lesson",
  "order": 13,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Encode categorical variables appropriately",
    "Create date, ratio and interaction features",
    "Scale numeric features for distance-based models",
    "Decide when a transform helps versus adds noise"
  ],
  "knowledge_refs": [
    "data-science/ds-13-feature-engineering"
  ],
  "prerequisites": [
    "DS-12: Correlation & Causation"
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

# DS-13-FEATURE-ENGINEERING: Feature Engineering

## Introduction

Turn raw columns into features that models can actually learn from: encodings, transforms, dates and domain knowledge. By the end of this lesson you will be able to: Encode categorical variables appropriately; Create date, ratio and interaction features; Scale numeric features for distance-based models; Decide when a transform helps versus adds noise.

## Key Concepts

### 1. Encode categorical variables appropriately

Target: Encode categorical variables appropriately. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import pandas as pd

df = pd.DataFrame({"color": ["red", "blue", "red", "green"]})
print(pd.get_dummies(df, columns=["color"]))
```
### 2. Create date, ratio and interaction features

Target: Create date, ratio and interaction features. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import pandas as pd

df = pd.DataFrame({"total": [100, 200, 50], "users": [10, 25, 5]})
df["revenue_per_user"] = df["total"] / df["users"]
df["is_high_value"] = df["revenue_per_user"] > 10
print(df)
```
### 3. Scale numeric features for distance-based models

Target: Scale numeric features for distance-based models. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[1, 1000], [2, 2000], [3, 1500]])
scaled = StandardScaler().fit_transform(X)
print(scaled.round(2))
```
### 4. Decide when a transform helps versus adds noise

Target: Decide when a transform helps versus adds noise. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import pandas as pd

orders = pd.DataFrame({"ts": pd.to_datetime(["2024-01-01 09:00", "2024-01-01 21:00"])})
orders["hour"] = orders["ts"].dt.hour
orders["weekday"] = orders["ts"].dt.dayofweek
orders["is_evening"] = orders["hour"] >= 18
print(orders)
```

## Practice Questions

1. What is the key idea behind "Feature Engineering"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Feature Engineering with analogies and real-world examples"
1. "Show me common mistakes beginners make with Feature Engineering"
1. "Provide advanced patterns and performance considerations for Feature Engineering"

## Key Takeaways

- Master the core ideas of Feature Engineering through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
