---
{
  "title": "Hypothesis Testing",
  "description": "Null hypotheses, p-values, t-tests and the judgment calls that separate rigorous analysis from pattern-chasing.",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "State a null and alternative hypothesis clearly",
    "Run t-tests and chi-square tests with scipy",
    "Interpret p-values and effect sizes correctly",
    "Recognize multiple-comparison and p-hacking traps"
  ],
  "knowledge_refs": [
    "data-science/ds-11-hypothesis-testing"
  ],
  "prerequisites": [
    "DS-10: Probability Distributions"
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

# DS-11-HYPOTHESIS-TESTING: Hypothesis Testing

## Introduction

Null hypotheses, p-values, t-tests and the judgment calls that separate rigorous analysis from pattern-chasing. By the end of this lesson you will be able to: State a null and alternative hypothesis clearly; Run t-tests and chi-square tests with scipy; Interpret p-values and effect sizes correctly; Recognize multiple-comparison and p-hacking traps.

## Key Concepts

### 1. State a null and alternative hypothesis clearly

Target: State a null and alternative hypothesis clearly. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np
from scipy import stats

control = np.array([12, 15, 14, 16, 13])
treated = np.array([17, 19, 18, 21, 16])
t, p = stats.ttest_ind(control, treated)
print(f"t={t:.2f} p={p:.3f}")
```
### 2. Run t-tests and chi-square tests with scipy

Target: Run t-tests and chi-square tests with scipy. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from scipy import stats

# Observed vs expected counts
observed = [42, 58]
expected = [50, 50]
chi2, p = stats.chisquare(observed, expected)
print(f"chi2={chi2:.2f} p={p:.3f}")
```
### 3. Interpret p-values and effect sizes correctly

Target: Interpret p-values and effect sizes correctly. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# Effect size: Cohen's d (signal relative to noise)
a = np.array([12, 15, 14, 16, 13])
b = np.array([17, 19, 18, 21, 16])
pooled = np.sqrt((a.var(ddof=1) + b.var(ddof=1)) / 2)
d = (b.mean() - a.mean()) / pooled
print(f"Cohen's d = {d:.2f}")
```
### 4. Recognize multiple-comparison and p-hacking traps

Target: Recognize multiple-comparison and p-hacking traps. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np
from scipy import stats

# Multiple comparisons: correct with Bonferroni
pvals = np.array([0.04, 0.02, 0.6])
corrected = np.minimum(pvals * len(pvals), 1.0)
print("corrected:", corrected)
```

## Practice Questions

1. What is the key idea behind "Hypothesis Testing"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Hypothesis Testing with analogies and real-world examples"
1. "Show me common mistakes beginners make with Hypothesis Testing"
1. "Provide advanced patterns and performance considerations for Hypothesis Testing"

## Key Takeaways

- Master the core ideas of Hypothesis Testing through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
