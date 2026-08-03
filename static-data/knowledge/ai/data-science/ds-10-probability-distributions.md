---
{
  "title": "Probability Distributions",
  "description": "The distributions behind data science: Bernoulli, binomial, Poisson, normal and more — and when to use each.",
  "type": "lesson",
  "order": 10,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Interpret probability as a model for uncertainty",
    "Recognize discrete distributions: Bernoulli, binomial, Poisson",
    "Recognize continuous distributions: uniform, normal, exponential",
    "Choose a distribution for a real dataset"
  ],
  "knowledge_refs": [
    "data-science/ds-09-statistics-fundamentals",
    "data-science/ds-11-hypothesis-testing",
    "machine-learning/ml-13-naive-bayes"
  ],
  "prerequisites": [
    "DS-09: Statistics Fundamentals"
  ],
  "references": [
    {
      "title": "Seeing Theory — Brown University",
      "url": "https://seeing-theory.brown.edu/",
      "description": "Interactive visualizations of probability distributions."
    },
    {
      "title": "OpenIntro Statistics — Chapter 3 (Distributions)",
      "url": "https://www.openintro.org/book/os/",
      "description": "Distributions of random variables with worked examples."
    },
    {
      "title": "Khan Academy — Random Variables & Distributions",
      "url": "https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library",
      "description": "Free video course on discrete and continuous distributions."
    },
    {
      "title": "SciPy Stats Documentation",
      "url": "https://docs.scipy.org/doc/scipy/reference/stats.html",
      "description": "The Python tooling for working with distributions programmatically."
    }
  ]
}
---

# DS-10-PROBABILITY-DISTRIBUTIONS: Probability Distributions

## Introduction

A **probability distribution** is a model of uncertainty: it tells you, for every possible outcome, how likely it is. When you fit or assume a distribution, you compress a dataset into a few parameters (like a mean and a spread) and gain the ability to *predict*: what fraction of orders will arrive late? How rare is this sales spike? This lesson introduces the handful of distributions that power data science — when to use each, and how to work with them in SciPy.

## Key Concepts

### 1. Discrete distributions: counting events

**Bernoulli(1 trial, 2 outcomes).** Models a single yes/no event — "will this user click?" `P(1) = p`, `P(0) = 1-p`.

**Binomial(n trials, p).** Counts the number of successes in n *independent* Bernoulli trials — "how many of 1,000 emails will be opened if each opens with probability 0.2?" Mean = np, variance = np(1−p).

**Poisson(λ).** Counts events in a fixed interval when events are rare and independent — "how many support tickets arrive per hour?" The signature property: **mean = variance = λ**. When a count variable's variance is much larger than its mean (overdispersion), the Poisson assumption is wrong — a classic data-science red flag.

### 2. Continuous distributions: measuring values

**Uniform(a, b).** Every value in an interval is equally likely. Used for random sampling and as an "ignorance" prior.

**Normal(μ, σ).** The bell curve — measurements of natural quantities (heights, errors, test scores). Governed by the Central Limit Theorem for averages.

**Exponential(λ).** Models *time between events* in a Poisson process — "how long until the next request?" Memoryless: the expected remaining wait doesn't depend on how long you've already waited.

```python
from scipy import stats
import numpy as np

rng = np.random.default_rng(42)
x = stats.poisson.rvs(mu=3, size=1000, random_state=rng)   # tickets/hour, mean 3
print(x.mean(), x.var())                                    # ~3, ~3
```

### 3. The normal family: why it dominates

Any process that sums many small independent effects becomes normal — that is the Central Limit Theorem's practical meaning. Consequences for data science:

- **Errors** of a well-specified model are often roughly normal → residual plots that look like a bell confirm model assumptions.
- **Log-normal data**: prices and incomes are often right-skewed; taking the log makes them normal-ish. This single trick (log transform) unlocks linear models on data that would otherwise violate assumptions.
- **Standardizing** `z = (x − μ)/σ` converts any normal to the standard normal — the basis for z-tests and confidence intervals.

### 4. Choosing a distribution for real data

The practical workflow is: **look, hypothesize, check.**

```python
import seaborn as sns

sns.histplot(data=df, x="tickets", discrete=True)   # look at the shape
print(df["tickets"].mean(), df["tickets"].var())    # ~equal? Poisson candidate
```

- Count data → try Poisson or negative binomial.
- Positive continuous, skewed → log-normal or exponential.
- Bell-shaped, symmetric → normal.
- Bounded [0,1] (probabilities, rates) → beta distribution.

### 5. From distribution to decision

Distributions let you answer *"how unusual is this?"* — the essence of anomaly detection and hypothesis testing. Example: if support tickets are Poisson(3) per hour and this hour had 9 tickets, how surprising is that?

```python
from scipy import stats
p_9_or_more = 1 - stats.poisson.cdf(8, mu=3)   # P(X >= 9)
print(f"{p_9_or_more:.4f}")                     # ~0.0038 — quite unusual!
```

This "tail probability" is exactly the logic behind p-values, which you'll formalize next lesson.

## Practice Questions

1. A call center gets an average of 5 calls per 10 minutes. What distribution models the count, and what's the variance?
2. You measure delivery times (always positive, right-skewed). Which distribution family would you try, and what transform might help?
3. Using SciPy, compute the probability of 3 or fewer successes in 20 trials with p=0.25.
4. Why is the normal distribution central to model *errors*?

## LLM Prompts for Deeper Understanding

1. "Explain Poisson vs negative binomial and when overdispersion matters."
2. "Show me a decision tree for picking a probability distribution for a variable."
3. "How do distributions connect to anomaly detection in real systems?"

## Key Takeaways

- Distributions compress uncertainty into parameters and enable prediction.
- Bernoulli/binomial count successes; Poisson counts rare events (mean = variance).
- Uniform, normal, and exponential cover the continuous workhorses.
- Log transforms tame right-skewed data; standardized normals power inference.
- Tail probabilities ("how unusual is this?") are the seed of hypothesis testing.

## Footnotes & Attribution

1. Brown University, *Seeing Theory*. Interactive distributions. [https://seeing-theory.brown.edu/](https://seeing-theory.brown.edu/)
2. Diez, Barr, Çetinkaya-Rundel, *OpenIntro Statistics* (Ch. 3). [https://www.openintro.org/book/os/](https://www.openintro.org/book/os/)
3. Khan Academy, *Random Variables & Distributions*. [https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library)
4. SciPy documentation, *Statistics (scipy.stats)*. [https://docs.scipy.org/doc/scipy/reference/stats.html](https://docs.scipy.org/doc/scipy/reference/stats.html)
