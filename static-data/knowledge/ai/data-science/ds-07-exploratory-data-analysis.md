---
{
  "title": "Exploratory Data Analysis",
  "description": "Systematically explore a dataset before modeling: distributions, group differences, and the questions they surface.",
  "type": "lesson",
  "order": 7,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Run a systematic EDA checklist on any table",
    "Summarize distributions with descriptive statistics",
    "Compare groups with group-by analysis",
    "Form hypotheses from visual and numeric evidence"
  ],
  "knowledge_refs": [
    "data-science/ds-07-exploratory-data-analysis"
  ],
  "prerequisites": [
    "DS-06: Data Cleaning & Wrangling"
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

# DS-07-EXPLORATORY-DATA-ANALYSIS: Exploratory Data Analysis

## Introduction

Systematically explore a dataset before modeling: distributions, group differences, and the questions they surface. By the end of this lesson you will be able to: Run a systematic EDA checklist on any table; Summarize distributions with descriptive statistics; Compare groups with group-by analysis; Form hypotheses from visual and numeric evidence.

## Key Concepts

### 1. Run a systematic EDA checklist on any table

Target: Run a systematic EDA checklist on any table. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import pandas as pd

df = pd.DataFrame({"age": [23, 45, 31, None, 67], "income": [40, 120, 65, 90, 150]})
print(df.describe(percentiles=[0.25, 0.5, 0.75, 0.9]))
```
### 2. Summarize distributions with descriptive statistics

Target: Summarize distributions with descriptive statistics. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import pandas as pd

df = pd.DataFrame({"segment": ["a"] * 5 + ["b"] * 5, "value": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
groups = df.groupby("segment")["value"].agg(["mean", "median", "std"])
print(groups)
```
### 3. Compare groups with group-by analysis

Target: Compare groups with group-by analysis. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import pandas as pd

sales = pd.DataFrame({
    "month": ["jan", "feb", "mar", "apr"],
    "revenue": [120, 140, 135, 175],
})
sales["growth"] = sales["revenue"].pct_change()
print(sales)
```
### 4. Form hypotheses from visual and numeric evidence

Target: Form hypotheses from visual and numeric evidence. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import pandas as pd

# Quick distribution check without a plot
s = pd.Series([1, 1, 2, 3, 3, 3, 4])
print(s.value_counts(normalize=True).sort_index())
```

## Practice Questions

1. What is the key idea behind "Exploratory Data Analysis"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Exploratory Data Analysis with analogies and real-world examples"
1. "Show me common mistakes beginners make with Exploratory Data Analysis"
1. "Provide advanced patterns and performance considerations for Exploratory Data Analysis"

## Key Takeaways

- Master the core ideas of Exploratory Data Analysis through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
