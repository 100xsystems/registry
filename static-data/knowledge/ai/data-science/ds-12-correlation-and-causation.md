---
{
  "title": "Correlation & Causation",
  "description": "Measure correlation, then learn why correlation is not causation — and how to actually establish causes.",
  "type": "lesson",
  "order": 12,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Compute and interpret Pearson correlation",
    "Explain why correlation does not imply causation",
    "Identify confounders, reverse causation and spurious correlation",
    "Know when experiments vs observation can establish causality"
  ],
  "knowledge_refs": [
    "data-science/ds-11-hypothesis-testing",
    "data-science/ds-13-feature-engineering",
    "machine-learning/ml-20-dimensionality-reduction"
  ],
  "prerequisites": [
    "DS-11: Hypothesis Testing"
  ],
  "references": [
    {
      "title": "Spurious Correlations — Tyler Vigen",
      "url": "https://www.tylervigen.com/spurious-correlations",
      "description": "The classic gallery of absurd but real correlations."
    },
    {
      "title": "Causal Inference for the Brave and True — Matheus Facure",
      "url": "https://matheusfacure.github.io/python-causality-handbook/landing-page.html",
      "description": "Free, open-source, Python-first introduction to causal inference."
    },
    {
      "title": "Introduction to Causal Inference — Brady Neal",
      "url": "https://www.bradyneal.com/causal-inference-course",
      "description": "Free course connecting causality to machine learning."
    },
    {
      "title": "OpenIntro Statistics — Correlation (Chapter 7)",
      "url": "https://www.openintro.org/book/os/",
      "description": "Linear regression and correlation foundations."
    }
  ]
}
---

# DS-12-CORRELATION-AND-CAUSATION: Correlation & Causation

## Introduction

"Correlation does not imply causation" is the most quoted — and most ignored — sentence in data science. This lesson makes it concrete. First you'll learn to *measure* correlation (Pearson's r) and read it honestly. Then you'll see the three classic ways two things can be correlated without one causing the other: **confounding**, **reverse causation**, and pure **spuriousness**. Finally, you'll learn what *would* establish causation — randomized experiments — and how to get closer with observational data.

## Key Concepts

### 1. Measuring correlation: Pearson's r

Pearson's r measures the strength and direction of a *linear* relationship, from −1 to +1:

- r ≈ +1: strong positive linear relationship
- r ≈ −1: strong negative linear relationship
- r ≈ 0: no linear relationship (curves and non-linear patterns are invisible to r!)

```python
import numpy as np

rng = np.random.default_rng(42)
x = rng.normal(size=100)
y = 2 * x + rng.normal(scale=1.0, size=100)      # strong positive linear
print(np.corrcoef(x, y)[0, 1])                   # ~0.9

z = x ** 2 + rng.normal(scale=0.3, size=100)     # perfect quadratic!
print(np.corrcoef(x, z)[0, 1])                   # ~0 — r misses curves
```

Critical caveat: **r only measures linear association.** A variable that is perfectly (but non-linearly) related to another can still show r ≈ 0. Always pair the correlation matrix with scatter plots.

### 2. Why correlation ≠ causation: the three enemies

**Confounding.** A third variable drives both. Example: ice cream sales and drowning deaths are correlated — but the *confounder* is warm weather, which causes both. In data science, confounders are the #1 reason "the data says X causes Y" is wrong.

**Reverse causation.** The arrow points the wrong way. "Depression is correlated with unemployment" — but does unemployment cause depression, or does depression make employment harder? Likely both; the data alone can't untangle the directions.

**Spurious correlation.** Pure coincidence in noisy data. Tyler Vigen's *Spurious Correlations* site catalogs gems like "US spending on science, space, and technology correlates with suicides by hanging" (r ≈ 0.99) [1]. With enough variables and time, random data produces dazzlingly high r — which is exactly why you must not go fishing without correction.

### 3. The gold standard: randomized experiments

To *establish* causation, you need to intervene: randomly assign subjects to treatment and control, and compare outcomes. Random assignment breaks the link between treatment and confounders, so differences in outcome can be attributed to the treatment. This is what A/B testing is — data science's favorite causal instrument.

Why randomization works: on average, treatment and control groups are *statistically identical* except for the treatment. Any confounder that would have biased an observational comparison is balanced across the groups.

### 4. Observational data: getting closer

When experiments are impossible (you can't randomize users' income), you can still make progress — but honesty about assumptions is required:

- **Stratify / control** for known confounders (e.g., compare within income brackets).
- **Difference-in-differences**: track both groups over time and compare *changes*.
- **Instrumental variables, propensity scores, causal graphs**: the tools of causal inference, covered in depth by Facure's free book [2] and Neal's course [3].
- **Domain reasoning**: state *why* you believe the causal direction is what you think it is.

### 5. The data science habit

Before presenting "X causes Y":

1. State the correlation with its confidence interval.
2. List the plausible confounders and what you did about them.
3. Say whether you ran an experiment or are reasoning from observation.
4. If observational, use causal language ("is associated with") in headlines.

Stakeholders will respect a precise, hedged analysis far more than a confident wrong one.

## Practice Questions

1. Compute Pearson's r for a perfectly quadratic relationship — what do you get, and why?
2. Identify the confounder in: "Schools with more library books have higher test scores."
3. Why does random assignment to treatment fix confounding?
4. You can't run an experiment on price elasticity. Name two observational strategies that move you closer to causality.

## LLM Prompts for Deeper Understanding

1. "Explain Simpson's paradox with a concrete example and what it means for your analysis."
2. "What are instrumental variables, and when would a data scientist use them?"
3. "Show me how to present 'correlated but not causal' findings to an executive."

## Key Takeaways

- Pearson's r measures *linear* association only — pair it with scatter plots.
- Confounders, reverse causation, and spuriousness explain most "magic" correlations.
- Randomized experiments (A/B tests) are the gold standard for causality.
- Observational data needs controls, design, and honest causal language.

## Footnotes & Attribution

1. Tyler Vigen, *Spurious Correlations*. [https://www.tylervigen.com/spurious-correlations](https://www.tylervigen.com/spurious-correlations)
2. Matheus Facure, *Causal Inference for the Brave and True*. Free Python handbook. [https://matheusfacure.github.io/python-causality-handbook/landing-page.html](https://matheusfacure.github.io/python-causality-handbook/landing-page.html)
3. Brady Neal, *Introduction to Causal Inference*. Free course/book. [https://www.bradyneal.com/causal-inference-course](https://www.bradyneal.com/causal-inference-course)
4. Diez, Barr, Çetinkaya-Rundel, *OpenIntro Statistics* (Ch. 7). [https://www.openintro.org/book/os/](https://www.openintro.org/book/os/)
