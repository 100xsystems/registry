---
{
  "title": "The Data Science Pipeline",
  "description": "Walk through the six stages of a data science project and learn where real projects fail — and why iteration matters.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Identify the six stages of the data science pipeline",
    "Explain why iteration beats a linear flow",
    "Map real project tasks onto pipeline stages",
    "Anticipate the most common failure points"
  ],
  "knowledge_refs": [
    "data-science/ds-02-the-data-science-pipeline"
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

# DS-02-THE-DATA-SCIENCE-PIPELINE: The Data Science Pipeline

## Introduction

Walk through the six stages of a data science project and learn where real projects fail — and why iteration matters. By the end of this lesson you will be able to: Identify the six stages of the data science pipeline; Explain why iteration beats a linear flow; Map real project tasks onto pipeline stages; Anticipate the most common failure points.

## Key Concepts

### 1. Identify the six stages of the data science pipeline

Target: Identify the six stages of the data science pipeline. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
stages = ["ask", "collect", "clean", "explore", "model", "communicate"]

# A pipeline is a loop, not a line:
for stage in stages:
    print(f"-> {stage}")
print("(then go back to the question and refine)")
```
### 2. Explain why iteration beats a linear flow

Target: Explain why iteration beats a linear flow. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import pandas as pd

raw = pd.DataFrame({"id": [1, 2, 3], "price": ["9.99", "oops", "29.99"]})
# Cleaning stage: coerce to numeric, keep track of what failed
raw["price"] = pd.to_numeric(raw["price"], errors="coerce")
print(raw)
```
### 3. Map real project tasks onto pipeline stages

Target: Map real project tasks onto pipeline stages. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from sklearn.model_selection import train_test_split

X = pd.DataFrame({"a": range(100), "b": range(100, 200)})
y = pd.Series([i % 2 for i in range(100)])
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"train={len(X_tr)} test={len(X_te)}")
```
### 4. Anticipate the most common failure points

Target: Anticipate the most common failure points. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
def estimate_hours(stage: str, data_quality: float) -> int:
    """Stage effort grows when data is messy."""
    base = {"collect": 2, "clean": 1, "model": 3}.get(stage, 1)
    return int(base * (1 + (1 - data_quality)))

print("clean stage:", estimate_hours("clean", data_quality=0.4), "days")
```

## Practice Questions

1. What is the key idea behind "The Data Science Pipeline"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain The Data Science Pipeline with analogies and real-world examples"
1. "Show me common mistakes beginners make with The Data Science Pipeline"
1. "Provide advanced patterns and performance considerations for The Data Science Pipeline"

## Key Takeaways

- Master the core ideas of The Data Science Pipeline through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
