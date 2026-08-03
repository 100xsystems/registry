---
{
  "title": "Statistics Fundamentals",
  "description": "Mean, variance, standard error, and the sampling ideas that let you reason from data to conclusions.",
  "type": "lesson",
  "order": 9,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Compute and interpret central tendency and spread",
    "Distinguish population parameters from sample statistics",
    "Explain the standard error and the central limit theorem",
    "Use confidence intervals to quantify uncertainty"
  ],
  "knowledge_refs": [
    "data-science/ds-09-statistics-fundamentals"
  ],
  "prerequisites": [
    "DS-07: Exploratory Data Analysis"
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

# DS-09-STATISTICS-FUNDAMENTALS: Statistics Fundamentals

## Introduction

Mean, variance, standard error, and the sampling ideas that let you reason from data to conclusions. By the end of this lesson you will be able to: Compute and interpret central tendency and spread; Distinguish population parameters from sample statistics; Explain the standard error and the central limit theorem; Use confidence intervals to quantify uncertainty.

## Key Concepts

### 1. Compute and interpret central tendency and spread

Target: Compute and interpret central tendency and spread. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

x = np.array([23, 41, 30, 67, 52])
print("mean:", x.mean())
print("var (sample):", x.var(ddof=1))
print("std (sample):", x.std(ddof=1))
```
### 2. Distinguish population parameters from sample statistics

Target: Distinguish population parameters from sample statistics. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

rng = np.random.default_rng(7)
pop = rng.normal(100, 15, size=100_000)
for n in [10, 100, 1000]:
    means = [rng.choice(pop, size=n).mean() for _ in range(500)]
    print(f"n={n}: sd of sample means = {np.std(means):.2f}")
```
### 3. Explain the standard error and the central limit theorem

Target: Explain the standard error and the central limit theorem. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

x = np.array([23, 41, 30, 67, 52])
n = x.size
se = x.std(ddof=1) / np.sqrt(n)
# 95% CI for the mean (approx, z=1.96)
lo, hi = x.mean() - 1.96 * se, x.mean() + 1.96 * se
print(f"95% CI: [{lo:.1f}, {hi:.1f}]")
```
### 4. Use confidence intervals to quantify uncertainty

Target: Use confidence intervals to quantify uncertainty. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 4, 6, 8, 10])
print("corr:", np.corrcoef(a, b)[0, 1])
```

## Practice Questions

1. What is the key idea behind "Statistics Fundamentals"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Statistics Fundamentals with analogies and real-world examples"
1. "Show me common mistakes beginners make with Statistics Fundamentals"
1. "Provide advanced patterns and performance considerations for Statistics Fundamentals"

## Key Takeaways

- Master the core ideas of Statistics Fundamentals through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
