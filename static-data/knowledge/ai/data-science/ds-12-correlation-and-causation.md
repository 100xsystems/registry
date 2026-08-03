---
{
  "title": "Correlation & Causation",
  "description": "Measure association, then reason carefully about whether an intervention actually causes the effect.",
  "type": "lesson",
  "order": 12,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Compute Pearson and Spearman correlations",
    "Explain why correlation does not imply causation",
    "Identify confounding variables and selection bias",
    "Describe when a randomized experiment is needed"
  ],
  "knowledge_refs": [
    "data-science/ds-12-correlation-and-causation"
  ],
  "prerequisites": [
    "DS-11: Hypothesis Testing"
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

# DS-12-CORRELATION-AND-CAUSATION: Correlation & Causation

## Introduction

Measure association, then reason carefully about whether an intervention actually causes the effect. By the end of this lesson you will be able to: Compute Pearson and Spearman correlations; Explain why correlation does not imply causation; Identify confounding variables and selection bias; Describe when a randomized experiment is needed.

## Key Concepts

### 1. Compute Pearson and Spearman correlations

Target: Compute Pearson and Spearman correlations. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np
from scipy import stats

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
r, p = stats.pearsonr(x, y)
print(f"Pearson r={r:.3f} (p={p:.3f})")
```
### 2. Explain why correlation does not imply causation

Target: Explain why correlation does not imply causation. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from scipy import stats

x = np.array([1, 2, 3, 4, 5, 100])
y = np.array([2, 4, 6, 8, 10, 1])
print("Pearson:", round(stats.pearsonr(x, y)[0], 3))
print("Spearman:", round(stats.spearmanr(x, y)[0], 3))
```
### 3. Identify confounding variables and selection bias

Target: Identify confounding variables and selection bias. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# Confounder: ice cream sales & drowning both rise with temperature
temp = np.array([20, 22, 25, 28, 30])
ice = temp * 10 + np.random.default_rng(0).normal(0, 5, 5)
print("spurious r:", round(np.corrcoef(temp, ice)[0, 1], 2))
```
### 4. Describe when a randomized experiment is needed

Target: Describe when a randomized experiment is needed. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Randomized assignment breaks the confounder link
rng = np.random.default_rng(1)
treatment = rng.choice([0, 1], size=100)
outcome = 2.0 * treatment + rng.normal(0, 1, 100)
print("ATE estimate:", round(outcome[treatment == 1].mean() - outcome[treatment == 0].mean(), 2))
```

## Practice Questions

1. What is the key idea behind "Correlation & Causation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Correlation & Causation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Correlation & Causation"
1. "Provide advanced patterns and performance considerations for Correlation & Causation"

## Key Takeaways

- Master the core ideas of Correlation & Causation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
