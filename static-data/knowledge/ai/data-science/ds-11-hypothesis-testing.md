---
{
  "title": "Hypothesis Testing",
  "description": "Null hypotheses, p-values, t-tests and the statistical decisions that separate real effects from noise.",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Formulate null and alternative hypotheses",
    "Explain what a p-value actually means — and what it doesn't",
    "Run t-tests, chi-square tests and interpret results",
    "Avoid common misinterpretations and p-hacking"
  ],
  "knowledge_refs": [
    "data-science/ds-10-probability-distributions",
    "data-science/ds-09-statistics-fundamentals",
    "data-science/ds-12-correlation-and-causation"
  ],
  "prerequisites": [
    "DS-10: Probability Distributions"
  ],
  "references": [
    {
      "title": "OpenIntro Statistics — Chapters 5–6 (Inference)",
      "url": "https://www.openintro.org/book/os/",
      "description": "Hypothesis testing and t-tests with worked examples."
    },
    {
      "title": "StatQuest — p-values and Hypothesis Testing",
      "url": "https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9",
      "description": "Clear visual explanations of p-values and statistical tests."
    },
    {
      "title": "Khan Academy — Significance Tests",
      "url": "https://www.khanacademy.org/math/statistics-probability/significance-tests-confidence-intervals-two-samples",
      "description": "Step-by-step significance testing course."
    },
    {
      "title": "scipy.stats — Statistical Tests",
      "url": "https://docs.scipy.org/doc/scipy/reference/stats.html",
      "description": "The Python implementations of t-tests, chi-square, ANOVA and more."
    }
  ]
}
---

# DS-11-HYPOTHESIS-TESTING: Hypothesis Testing

## Introduction

When your A/B test shows a 3% lift, is it real or is it noise? **Hypothesis testing** is the formal machinery for answering exactly that. The framework: assume nothing is happening (the *null hypothesis*), then measure how surprising your data is under that assumption. If the data is surprising enough, you reject "nothing is happening." This lesson covers the framework, the infamous **p-value**, the most common tests, and — critically — the ways people abuse it.

## Key Concepts

### 1. The framework: null vs alternative

- **Null hypothesis (H₀)**: the status quo — "no difference," "no effect," "no relationship."
- **Alternative hypothesis (H₁)**: the claim you're testing for — "there is a difference."

Example: you test whether a new checkout page increases conversion.

- H₀: conversion(new) = conversion(old)
- H₁: conversion(new) ≠ conversion(old)

You never *prove* H₁; you gather evidence against H₀ and, if strong enough, **reject** it.

### 2. What a p-value really means

**The p-value is the probability of seeing data at least this extreme, *assuming the null hypothesis is true*.** Two immediate consequences:

- A p-value is NOT the probability that H₀ is true.
- A p-value is NOT the probability the result was "caused by chance."

The decision rule: if `p < α` (typically α = 0.05), the data is too unlikely under H₀, so reject H₀. This means: with α = 0.05, even when H₀ is true, you'll wrongly reject it 5% of the time — the **false positive rate**, by design.

### 3. Type I and Type II errors

| | H₀ true | H₀ false |
| --- | --- | --- |
| You fail to reject H₀ | ✅ Correct | ❌ **Type II error** (missed the effect) |
| You reject H₀ | ❌ **Type I error** (false alarm) | ✅ Correct |

- **Type I error** rate is controlled by α.
- **Type II error** rate is controlled by *sample size and effect size*; 1 − Type II = **statistical power**.

When a study "didn't find an effect," always ask: was it a true null, or just an underpowered sample?

### 4. Running the common tests in Python

**t-test** — comparing means of one or two groups (works when data is roughly normal or n is large):

```python
from scipy import stats
import numpy as np

a = np.array([52, 48, 55, 49, 53, 51])
b = np.array([58, 61, 57, 60, 59, 62])

t_stat, p_value = stats.ttest_ind(a, b)
print(f"t={t_stat:.2f}, p={p_value:.4f}")     # p tiny -> reject H0: means differ
```

**Chi-square test** — association between two categorical variables:

```python
observed = np.array([[120, 80], [90, 110]])   # e.g. plan x converted
chi2, p, dof, expected = stats.chi2_contingency(observed)
print(f"chi2={chi2:.2f}, p={p:.4f}")
```

**ANOVA** — comparing means of 3+ groups (`stats.f_oneway(a, b, c)`).

### 5. The failure modes: what to watch for

1. **p-hacking** — testing many hypotheses and reporting only the significant ones. If you run 20 tests at α=0.05, expect ~1 false positive by chance. Correct it (Bonferroni, FDR) or pre-register hypotheses.
2. **Misreading p** — see section 2. p = 0.04 is not "96% sure it's real."
3. **Ignoring effect size** — with a huge sample, even a 0.1% difference becomes "significant." Always report *how big* the effect is, not just *whether* it exists.
4. **Data snooping** — deciding the test *after* looking at the data. Decide the hypothesis first.

## Practice Questions

1. Write H₀ and H₁ for: "Does adding a loyalty discount increase repeat purchases?"
2. Explain p-value to a non-technical stakeholder in two sentences.
3. You run 10 independent tests at α=0.05 and one is significant. Why is that not strong evidence?
4. When would you use a chi-square test instead of a t-test?

## LLM Prompts for Deeper Understanding

1. "Explain p-values, Type I/II errors, and power with a concrete A/B testing story."
2. "What is multiple comparisons, and what correction methods exist (Bonferroni, Benjamini-Hochberg)?"
3. "How does hypothesis testing relate to model evaluation in machine learning?"

## Key Takeaways

- H₀ = nothing happening; reject it only when data is surprising under H₀.
- p-value = P(data this extreme | H₀ true) — not P(H₀ true).
- α controls Type I (false alarm); power/sample size control Type II (missed effect).
- t-tests compare means, chi-square tests compare categories, ANOVA compares 3+ groups.
- Watch for p-hacking, tiny-but-significant effects, and deciding tests after seeing data.

## Footnotes & Attribution

1. Diez, Barr, Çetinkaya-Rundel, *OpenIntro Statistics* (Chs. 5–6). [https://www.openintro.org/book/os/](https://www.openintro.org/book/os/)
2. Josh Starmer, *StatQuest — Statistics Fundamentals* (p-values and hypothesis testing). [https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9](https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9)
3. Khan Academy, *Significance Tests*. [https://www.khanacademy.org/math/statistics-probability/significance-tests-confidence-intervals-two-samples](https://www.khanacademy.org/math/statistics-probability/significance-tests-confidence-intervals-two-samples)
4. SciPy documentation, *scipy.stats*. [https://docs.scipy.org/doc/scipy/reference/stats.html](https://docs.scipy.org/doc/scipy/reference/stats.html)
