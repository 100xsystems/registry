---
{
  "title": "Probability Distributions",
  "description": "The distributions that show up everywhere in data work — normal, binomial, Poisson and uniform — and how to sample from them.",
  "type": "lesson",
  "order": 10,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain the normal distribution and the 68-95-99.7 rule",
    "Model counts with binomial and Poisson distributions",
    "Compute probabilities with scipy.stats",
    "Choose a distribution that matches the data-generating process"
  ],
  "knowledge_refs": [
    "data-science/ds-10-probability-distributions"
  ],
  "prerequisites": [
    "DS-09: Statistics Fundamentals"
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

# DS-10-PROBABILITY-DISTRIBUTIONS: Probability Distributions

## Introduction

The distributions that show up everywhere in data work — normal, binomial, Poisson and uniform — and how to sample from them. By the end of this lesson you will be able to: Explain the normal distribution and the 68-95-99.7 rule; Model counts with binomial and Poisson distributions; Compute probabilities with scipy.stats; Choose a distribution that matches the data-generating process.

## Key Concepts

### 1. Explain the normal distribution and the 68-95-99.7 rule

Target: Explain the normal distribution and the 68-95-99.7 rule. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np
from scipy import stats

x = np.linspace(-4, 4, 200)
pdf = stats.norm.pdf(x, loc=0, scale=1)
print("pdf at 0:", round(pdf[100], 4))
```
### 2. Model counts with binomial and Poisson distributions

Target: Model counts with binomial and Poisson distributions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from scipy import stats

# P(X <= 3) for X ~ Binomial(n=10, p=0.5)
print("P(X<=3):", round(stats.binom.cdf(3, n=10, p=0.5), 4))
# P(X = 2) for X ~ Poisson(lambda=3)
print("P(X=2):", round(stats.poisson.pmf(2, mu=3), 4))
```
### 3. Compute probabilities with scipy.stats

Target: Compute probabilities with scipy.stats. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

rng = np.random.default_rng(0)
samples = rng.normal(loc=0, scale=1, size=100_000)
within_1 = np.mean(np.abs(samples) <= 1)
within_2 = np.mean(np.abs(samples) <= 2)
print(f"within 1 sd: {within_1:.3f} (expect 0.68)")
print(f"within 2 sd: {within_2:.3f} (expect 0.95)")
```
### 4. Choose a distribution that matches the data-generating process

Target: Choose a distribution that matches the data-generating process. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
from scipy import stats

# Events per hour ~ Poisson(5); probability of <= 3 events
print("P(<=3):", round(stats.poisson.cdf(3, mu=5), 4))
```

## Practice Questions

1. What is the key idea behind "Probability Distributions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Probability Distributions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Probability Distributions"
1. "Provide advanced patterns and performance considerations for Probability Distributions"

## Key Takeaways

- Master the core ideas of Probability Distributions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
