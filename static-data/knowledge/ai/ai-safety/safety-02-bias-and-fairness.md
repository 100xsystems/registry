---
slug: safety-02-bias-and-fairness
title: "Bias & Fairness"
description: "How discrimination becomes encoded in machine learning systems, the mathematical definitions of fairness, and strategies for mitigation."
order: 2
tags:
  - ai-safety
  - bias
  - fairness
  - algorithmic-bias
  - discrimination
prerequisites:
  - safety-01-why-ai-safety
knowledge_refs:
  - slug: safety-01-why-ai-safety
    title: "Why AI Safety Matters"
  - slug: safety-06-privacy
    title: "Privacy & Data Protection"
  - slug: safety-14-societal-impact
    title: "Societal Impact of AI"
references:
  - title: "Google ML Crash Course — Fairness: Types of Bias"
    url: "https://developers.google.com/machine-learning/crash-course/fairness/types-of-bias"
  - title: "Algorithmic Fairness in Computational Medicine"
    url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC9463525/"
  - title: "Fairness (Machine Learning) — Wikipedia"
    url: "https://en.wikipedia.org/wiki/Fairness_(machine_learning)"
  - title: "Fairness-Aware Machine Learning Engineering"
    url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC10673752/"
  - title: "ProPublica — Machine Bias: There's Software Used Across the Country to Predict Future Criminals"
    url: "https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing"
---
## Bias & Fairness

Bias in AI isn't a bug — it's a feature of how data reflects the world as it is, not as it should be. Fairness engineering is the discipline of detecting, measuring, and mitigating these biases before they cause harm.

### Sources of Bias

Bias enters the ML pipeline at every stage:

**Historical bias:** Past social inequities are embedded in training data. A hiring model trained on 20 years of data will learn that "successful" employees are mostly men — because that's what the historical data shows.

**Representation bias:** Training data doesn't adequately represent certain groups. Facial recognition systems perform worse on dark-skinned faces because benchmark datasets are dominated by lighter-skinned individuals.

**Measurement bias:** The way you measure the target variable introduces bias. Using healthcare costs as a proxy for healthcare needs undercounts minorities who have less access to care.

**Reporting bias:** Unusual events get documented more. People report rare diseases more than common colds, skewing disease prevalence data.

**Aggregation bias:** Group-level metrics mask poor performance on subgroups. A model with 95% overall accuracy might have 60% accuracy for a minority group.

### Fairness Definitions

Fairness has multiple mathematical definitions, and Kleinberg's impossibility theorem proves they can't all be satisfied simultaneously:

**Demographic parity:** The proportion of positive predictions should be equal across groups. If 30% of Group A gets approved for loans, 30% of Group B should too — regardless of base rates.

**Equalized odds:** True positive rates and false positive rates should be equal across groups. The model should make errors at the same rate regardless of group membership.

**Calibration:** A prediction score means the same thing across groups. If the model assigns 70% risk to someone in Group A, roughly 70% of people in Group A with that score should actually be high-risk.

**Equal opportunity:** Equal true positive rates across groups. Everyone who deserves a positive outcome has the same chance of getting it.

### Real-World Failures

- **COMPAS (2016):** Recidivism prediction software disproportionately flagged Black defendants as high-risk false positives compared to white defendants.
- **Healthcare algorithm (2019):** A widely deployed algorithm assigned lower health risk scores to Black patients than sicker white patients because it used healthcare costs as a proxy.
- **Amazon hiring tool (2018):** Scrapped after discovering it penalized resumes containing words associated with women's colleges.

### Mitigation Strategies

**Pre-processing:** Modify training data before model training — reweighting, resampling, or removing features that correlate with protected attributes.

**In-processing:** Add fairness constraints to the training objective. Adversarial debiasing trains the model to be accurate while preventing a secondary model from predicting protected attributes from the output.

**Post-processing:** Adjust decision thresholds after training. Apply different thresholds for different groups to achieve equalized odds.

### Common Mistakes

- **Ignoring protected attributes:** Removing gender from data doesn't remove gender bias — proxy variables like name, education, or zip code still correlate.
- **Optimizing for one fairness metric:** No single metric captures all dimensions of fairness. Use multiple metrics.
- **One-time auditing:** Bias is dynamic. Model behavior changes as data and usage patterns evolve.

---

*Continue to learn about interpretability — how to understand what AI systems are actually doing.*
