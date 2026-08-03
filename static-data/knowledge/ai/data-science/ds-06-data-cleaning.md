---
{
  "title": "Data Cleaning & Wrangling",
  "description": "Handle missing values, duplicates, inconsistent types and outliers — the unglamorous 80% of real data work.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Detect and handle missing values deliberately",
    "Remove duplicates and enforce consistent types",
    "Standardize text and categorical values",
    "Find and treat outliers with domain-aware rules"
  ],
  "knowledge_refs": [
    "data-science/ds-06-data-cleaning"
  ],
  "prerequisites": [
    "DS-05: Pandas: DataFrames & Series"
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

# DS-06-DATA-CLEANING: Data Cleaning & Wrangling

## Introduction

Handle missing values, duplicates, inconsistent types and outliers — the unglamorous 80% of real data work. By the end of this lesson you will be able to: Detect and handle missing values deliberately; Remove duplicates and enforce consistent types; Standardize text and categorical values; Find and treat outliers with domain-aware rules.

## Key Concepts

### 1. Detect and handle missing values deliberately

Target: Detect and handle missing values deliberately. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import pandas as pd

df = pd.DataFrame({"a": [1, None, 3], "b": ["x", "y", None]})
print(df.isna().sum())
# Fill numeric with a sensible value, drop the rest
cleaned = df.assign(a=df["a"].fillna(df["a"].median())).dropna(subset=["b"])
print(cleaned)
```
### 2. Remove duplicates and enforce consistent types

Target: Remove duplicates and enforce consistent types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import pandas as pd

raw = pd.DataFrame({"date": ["2024-01-01", "2024-01-02"], "amt": ["$12.5", "$7.00"]})
raw["date"] = pd.to_datetime(raw["date"])
raw["amt"] = raw["amt"].str.replace("$", "").astype(float)
print(raw.dtypes)
```
### 3. Standardize text and categorical values

Target: Standardize text and categorical values. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import pandas as pd

labels = pd.Series(["  New York ", "new york", "NYC", "los angeles"])
normalized = labels.str.strip().str.lower().str.replace("nyc", "new york")
print(normalized.tolist())
```
### 4. Find and treat outliers with domain-aware rules

Target: Find and treat outliers with domain-aware rules. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np
import pandas as pd

x = pd.Series([1, 2, 3, 100, 4, 5])
q1, q3 = x.quantile([0.25, 0.75])
iqr = q3 - q1
outliers = x[(x < q1 - 1.5 * iqr) | (x > q3 + 1.5 * iqr)]
print("outliers:", outliers.tolist())
```

## Practice Questions

1. What is the key idea behind "Data Cleaning & Wrangling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Data Cleaning & Wrangling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Data Cleaning & Wrangling"
1. "Provide advanced patterns and performance considerations for Data Cleaning & Wrangling"

## Key Takeaways

- Master the core ideas of Data Cleaning & Wrangling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
