---
{
  "title": "Statistics Fundamentals",
  "description": "Descriptive statistics, samples vs populations, and the distributions that data science runs on.",
  "type": "lesson",
  "order": 9,
  "duration": "55 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Summarize data with mean, median, variance and percentiles",
    "Distinguish sample statistics from population parameters",
    "Understand the normal distribution and why it appears everywhere",
    "Use sampling distributions to reason about uncertainty"
  ],
  "knowledge_refs": [
    "data-science/ds-10-probability-distributions",
    "data-science/ds-11-hypothesis-testing",
    "data-science/ds-07-exploratory-data-analysis"
  ],
  "prerequisites": [
    "DS-08: Data Visualization"
  ],
  "references": [
    {
      "title": "OpenIntro Statistics (4th Edition)",
      "url": "https://www.openintro.org/book/os/",
      "description": "Free, university-level statistics textbook — descriptive stats and inference."
    },
    {
      "title": "Khan Academy — Statistics and Probability",
      "url": "https://www.khanacademy.org/math/statistics-probability",
      "description": "Free video course: distributions, sampling, and confidence intervals."
    },
    {
      "title": "Seeing Theory — Brown University",
      "url": "https://seeing-theory.brown.edu/",
      "description": "Interactive visual introduction to probability and statistics."
    },
    {
      "title": "StatQuest with Josh Starmer",
      "url": "https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9",
      "description": "Renowned visual explanations of statistical concepts."
    },
    {
      "title": "Introduction to Probability and Statistics (MIT 18.05)",
      "url": "https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/",
      "description": "Rigorous free university course with full lecture notes and problem sets."
    }
  ]
}
---

# DS-09-STATISTICS-FUNDAMENTALS: Statistics Fundamentals

## Introduction

Statistics is the science of making decisions under uncertainty — and data science is, at its core, applied statistics. This lesson builds the vocabulary you need for everything that follows: how to *summarize* data (descriptive statistics), how to distinguish the *sample* you have from the *population* you care about, and why the *normal distribution* and *sampling distributions* are so central. These ideas are the foundation for hypothesis testing (next lessons) and for understanding what ML models actually guarantee.

## Key Concepts

### 1. Summarizing data: measures of center and spread

- **Mean**: the arithmetic average. Sensitive to outliers.
- **Median**: the middle value. Robust to outliers.
- **Variance / standard deviation**: how spread out the data is. Standard deviation is variance in the original units.
- **Percentiles / quartiles**: shape of the distribution — the interquartile range (IQR = Q3 − Q1) is a robust measure of spread.

```python
import numpy as np

data = np.array([2, 3, 5, 7, 11, 13, 17, 19, 100])   # note the outlier
print(data.mean(), np.median(data))                   # 19.7 vs 11
print(data.std(), np.percentile(data, [25, 50, 75]))
```

Watch the mean (19.7) vs median (11): one extreme value drags the mean. Whenever the two disagree strongly, your distribution is skewed — say so, and consider reporting the median.

### 2. Sample vs population

The **population** is every individual you care about; the **sample** is the subset you can measure. We almost never have the whole population, so we use sample statistics to *estimate* population parameters.

- Sample statistic: `x̄` (sample mean), `s` (sample std)
- Population parameter: `μ` (population mean), `σ` (population std)

The entire logic of statistics — confidence intervals, hypothesis tests, model evaluation — is: "I only have a sample; how much can I trust the estimate I computed from it?"

### 3. The normal distribution: nature's default

The normal (Gaussian) distribution is the famous bell curve, characterized by its mean `μ` and standard deviation `σ`. Its central role comes from the **Central Limit Theorem**: regardless of the original distribution, the *mean of many independent samples* approaches a normal distribution as sample size grows.

```python
rng = np.random.default_rng(42)
# Sample means of a skewed (exponential) distribution become normal-ish:
means = [rng.exponential(1.0, n=50).mean() for _ in range(10000)]
print(np.mean(means), np.std(means))
```

This is why the normal distribution shows up everywhere in inference: even when the raw data is not normal, *averages* are. Practical facts:

- ~68% of data is within ±1σ, ~95% within ±2σ, ~99.7% within ±3σ (the "68-95-99.7 rule").

### 4. Sampling distributions: the uncertainty engine

A **sampling distribution** is the distribution of a statistic (like the mean) over many hypothetical samples. Its standard deviation is called the **standard error**:

```
standard error of the mean ≈ σ / √n
```

Two takeaways you will use constantly:

1. **Larger samples → smaller standard error** → more precise estimates.
2. **Precision grows like √n**, not n — quadrupling the sample only halves the standard error. This is why "just collect more data" is a blunt instrument.

### 5. From statistics to data science

Every ML evaluation you will see later is statistics wearing a costume:

- A model's "accuracy" on a test set is a *sample statistic* estimating how the model will perform in the wild.
- Cross-validation averages test-set scores to build a *sampling distribution* of the metric.
- Confidence intervals around metrics tell you how much to trust a reported improvement.

Understanding this now means you will never treat a single accuracy number as gospel.

## Practice Questions

1. Compute mean, median, std, and IQR for `[1, 2, 3, 4, 5, 100]`. Which summaries does the outlier distort?
2. In your own words: why does the Central Limit Theorem matter for statistics?
3. A study with n=30 finds a mean of 50. Roughly what is the standard error if the population σ is 15?
4. Why does quadrupling the sample size only halve (not quarter) the standard error?

## LLM Prompts for Deeper Understanding

1. "Explain the Central Limit Theorem with three different real-world examples."
2. "When should I report the median instead of the mean, and how do I justify it?"
3. "How do sampling distributions connect to machine learning model evaluation?"

## Key Takeaways

- Center = mean/median; spread = std/IQR; always watch skewed distributions.
- Statistics estimate population parameters from samples — trust is always partial.
- The Central Limit Theorem makes averages normal, which powers all inference.
- Standard error ≈ σ/√n — more data helps, but only as √n.
- Model metrics are sample statistics; treat them with the same skepticism.

## Footnotes & Attribution

1. Diez, Barr, Çetinkaya-Rundel, *OpenIntro Statistics* (4th ed.). Free textbook. [https://www.openintro.org/book/os/](https://www.openintro.org/book/os/)
2. Khan Academy, *Statistics and Probability*. Free course. [https://www.khanacademy.org/math/statistics-probability](https://www.khanacademy.org/math/statistics-probability)
3. Brown University, *Seeing Theory*. Interactive probability/statistics. [https://seeing-theory.brown.edu/](https://seeing-theory.brown.edu/)
4. Josh Starmer, *StatQuest*. Visual statistics fundamentals. [https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9](https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9)
5. MIT OpenCourseWare, *18.05 Introduction to Probability and Statistics*. [https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/)
