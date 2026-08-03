---
{
  "title": "An End-to-End Data Science Project",
  "description": "Assemble everything into one reproducible project: ask, fetch, clean, explore, model, evaluate, and ship the notebook.",
  "type": "lesson",
  "order": 20,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Structure a reproducible project layout",
    "Chain cleaning, EDA and modeling into one pipeline",
    "Evaluate and select a model with held-out data",
    "Package conclusions with code and artifacts"
  ],
  "knowledge_refs": [
    "data-science/ds-20-end-to-end-project"
  ],
  "prerequisites": [
    "DS-19: Communicating Results"
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

# DS-20-END-TO-END-PROJECT: An End-to-End Data Science Project

## Introduction

Assemble everything into one reproducible project: ask, fetch, clean, explore, model, evaluate, and ship the notebook. By the end of this lesson you will be able to: Structure a reproducible project layout; Chain cleaning, EDA and modeling into one pipeline; Evaluate and select a model with held-out data; Package conclusions with code and artifacts.

## Key Concepts

### 1. Structure a reproducible project layout

Target: Structure a reproducible project layout. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
project = {
    "data/raw": "original download",
    "data/processed": "cleaned tables",
    "notebooks/": "analysis",
    "src/": "reusable functions",
    "reports/": "findings",
}
for d, purpose in project.items():
    print(f"{d:22} {purpose}")
```
### 2. Chain cleaning, EDA and modeling into one pipeline

Target: Chain cleaning, EDA and modeling into one pipeline. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import pandas as pd

def clean_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df = df.dropna(subset=["price"])
    df["price"] = df["price"].clip(lower=0)
    return df

df = pd.DataFrame({"price": ["9.99", None, "oops", "5.00"]})
print(clean_pipeline(df))
```
### 3. Evaluate and select a model with held-out data

Target: Evaluate and select a model with held-out data. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd

df = pd.DataFrame({"a": range(20), "b": [i % 2 for i in range(20)], "y": [1 if i % 3 == 0 else 0 for i in range(20)]})
X = df[["a", "b"]]
y = df["y"]
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=0)
m = LogisticRegression().fit(X_tr, y_tr)
print("test accuracy:", round(accuracy_score(y_te, m.predict(X_te)), 2))
```
### 4. Package conclusions with code and artifacts

Target: Package conclusions with code and artifacts. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import json

# Every run logs its metrics for later comparison
run = {"model": "LogisticRegression", "test_accuracy": 0.75, "features": ["a", "b"]}
with open("run.json", "w") as fh:
    json.dump(run, fh, indent=2)
print("saved run.json")
```

## Practice Questions

1. What is the key idea behind "An End-to-End Data Science Project"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain An End-to-End Data Science Project with analogies and real-world examples"
1. "Show me common mistakes beginners make with An End-to-End Data Science Project"
1. "Provide advanced patterns and performance considerations for An End-to-End Data Science Project"

## Key Takeaways

- Master the core ideas of An End-to-End Data Science Project through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
