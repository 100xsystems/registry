---
{
  "title": "Pandas: DataFrames & Series",
  "description": "Load, inspect, filter, group and merge tabular data with the most important library in data science.",
  "type": "lesson",
  "order": 5,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Load tabular data into a DataFrame",
    "Inspect, filter and sort rows and columns",
    "Group by and aggregate with split-apply-combine",
    "Join datasets on keys"
  ],
  "knowledge_refs": [
    "data-science/ds-05-pandas-dataframes"
  ],
  "prerequisites": [
    "DS-04: NumPy: Arrays & Vectorization"
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

# DS-05-PANDAS-DATAFRAMES: Pandas: DataFrames & Series

## Introduction

Load, inspect, filter, group and merge tabular data with the most important library in data science. By the end of this lesson you will be able to: Load tabular data into a DataFrame; Inspect, filter and sort rows and columns; Group by and aggregate with split-apply-combine; Join datasets on keys.

## Key Concepts

### 1. Load tabular data into a DataFrame

Target: Load tabular data into a DataFrame. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
)
print(df.shape)
print(df.head(3))
```
### 2. Inspect, filter and sort rows and columns

Target: Inspect, filter and sort rows and columns. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import pandas as pd

df = pd.DataFrame({"species": ["A", "B", "A", "B"], "score": [1, 2, 3, 4]})
print(df[df["score"] > 2])
print(df.sort_values("score", ascending=False))
```
### 3. Group by and aggregate with split-apply-combine

Target: Group by and aggregate with split-apply-combine. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import pandas as pd

orders = pd.DataFrame({
    "region": ["east", "west", "east", "west", "east"],
    "revenue": [10, 20, 30, 40, 50],
})
summary = orders.groupby("region")["revenue"].agg(["sum", "mean", "count"])
print(summary)
```
### 4. Join datasets on keys

Target: Join datasets on keys. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import pandas as pd

users = pd.DataFrame({"user_id": [1, 2, 3], "name": ["a", "b", "c"]})
orders = pd.DataFrame({"user_id": [2, 3, 4], "total": [50, 75, 100]})
joined = users.merge(orders, on="user_id", how="left")
print(joined)
```

## Practice Questions

1. What is the key idea behind "Pandas: DataFrames & Series"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Pandas: DataFrames & Series with analogies and real-world examples"
1. "Show me common mistakes beginners make with Pandas: DataFrames & Series"
1. "Provide advanced patterns and performance considerations for Pandas: DataFrames & Series"

## Key Takeaways

- Master the core ideas of Pandas: DataFrames & Series through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
