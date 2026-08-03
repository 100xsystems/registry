---
{
  "title": "Python for Data Science",
  "description": "The Python fundamentals every data scientist leans on: collections, comprehensions, file I/O, and reproducible notebooks.",
  "type": "lesson",
  "order": 3,
  "duration": "50 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use lists, dicts and comprehensions fluently",
    "Read and write CSV data with the standard library",
    "Structure analysis code for reproducibility",
    "Profile a small script to find slow operations"
  ],
  "knowledge_refs": [
    "data-science/ds-03-python-for-data-science"
  ],
  "prerequisites": [
    "DS-01: What Is Data Science?"
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

# DS-03-PYTHON-FOR-DATA-SCIENCE: Python for Data Science

## Introduction

The Python fundamentals every data scientist leans on: collections, comprehensions, file I/O, and reproducible notebooks. By the end of this lesson you will be able to: Use lists, dicts and comprehensions fluently; Read and write CSV data with the standard library; Structure analysis code for reproducibility; Profile a small script to find slow operations.

## Key Concepts

### 1. Use lists, dicts and comprehensions fluently

Target: Use lists, dicts and comprehensions fluently. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
prices = [9.99, 19.99, 29.99, 49.99]
doubled = [p * 2 for p in prices if p > 15]
counts = {p: prices.count(p) for p in set(prices)}
print(doubled)
print(counts)
```
### 2. Read and write CSV data with the standard library

Target: Read and write CSV data with the standard library. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import csv
from io import StringIO

rows = [["day", "users"], ["mon", 120], ["tue", 210]]
buf = StringIO()
writer = csv.writer(buf)
writer.writerows(rows)
print(buf.getvalue())
reader = list(csv.reader(StringIO(buf.getvalue())))
print(reader[1])
```
### 3. Structure analysis code for reproducibility

Target: Structure analysis code for reproducibility. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
# Reproducible structure: keep transforms in functions
import pandas as pd

def load(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df.columns = [c.strip().lower() for c in df.columns]
    return df

# load("users.csv")  # every analysis starts from one clean entry point
```
### 4. Profile a small script to find slow operations

Target: Profile a small script to find slow operations. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import time

def slow(n: int) -> int:
    total = 0
    for i in range(n):
        total += i ** 2
    return total

t0 = time.perf_counter()
slow(1_000_000)
print(f"took {time.perf_counter() - t0:.3f}s")
```

## Practice Questions

1. What is the key idea behind "Python for Data Science"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Python for Data Science with analogies and real-world examples"
1. "Show me common mistakes beginners make with Python for Data Science"
1. "Provide advanced patterns and performance considerations for Python for Data Science"

## Key Takeaways

- Master the core ideas of Python for Data Science through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
