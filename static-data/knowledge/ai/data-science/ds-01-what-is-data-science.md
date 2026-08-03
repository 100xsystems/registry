---
{
  "title": "What Is Data Science?",
  "description": "Define data science, understand its core disciplines, and map the roles and workflow of a modern data team.",
  "type": "lesson",
  "order": 1,
  "duration": "40 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define data science and contrast it with data analysis and statistics",
    "Identify the roles in a modern data science team",
    "Describe the data science workflow at a high level",
    "Recognize the core tools and languages used across the field"
  ],
  "knowledge_refs": [
    "data-science/ds-01-what-is-data-science"
  ],
  "prerequisites": [],
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

# DS-01-WHAT-IS-DATA-SCIENCE: What Is Data Science?

## Introduction

Define data science, understand its core disciplines, and map the roles and workflow of a modern data team. By the end of this lesson you will be able to: Define data science and contrast it with data analysis and statistics; Identify the roles in a modern data science team; Describe the data science workflow at a high level; Recognize the core tools and languages used across the field.

## Key Concepts

### 1. Define data science and contrast it with data analysis and statistics

Target: Define data science and contrast it with data analysis and statistics. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np
import pandas as pd

users = pd.DataFrame({
    "cohort": ["free", "pro", "team"],
    "signups": [1200, 340, 95],
    "revenue": [0.0, 19.99, 49.99],
})
print(users)
```
### 2. Identify the roles in a modern data science team

Target: Identify the roles in a modern data science team. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
pipeline = {
    1: "ask the question",
    2: "collect data",
    3: "clean and wrangle",
    4: "explore and visualize",
    5: "model and evaluate",
    6: "communicate results",
}
for step, task in pipeline.items():
    print(f"{step}. {task}")
```
### 3. Describe the data science workflow at a high level

Target: Describe the data science workflow at a high level. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
def describe_role(role: str) -> str:
    return f"{role} turns questions into data-driven decisions"

print(describe_role("data scientist"))
print(describe_role("ML engineer"))
print(describe_role("analytics engineer"))
```
### 4. Recognize the core tools and languages used across the field

Target: Recognize the core tools and languages used across the field. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import sys
import numpy as np
import pandas as pd

print(f"Python {sys.version_info.major}.{sys.version_info.minor}")
print(f"NumPy {np.__version__} | pandas {pd.__version__}")
```

## Practice Questions

1. What is the key idea behind "What Is Data Science?"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain What Is Data Science? with analogies and real-world examples"
1. "Show me common mistakes beginners make with What Is Data Science?"
1. "Provide advanced patterns and performance considerations for What Is Data Science?"

## Key Takeaways

- Master the core ideas of What Is Data Science? through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
