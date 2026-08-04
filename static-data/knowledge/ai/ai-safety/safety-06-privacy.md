---
slug: safety-06-privacy
title: "Privacy & Data Protection"
description: "Protecting personal data in AI systems — differential privacy, federated learning, membership inference attacks, and GDPR compliance."
order: 6
tags:
  - ai-safety
  - privacy
  - differential-privacy
  - federated-learning
  - gdpr
prerequisites:
  - safety-01-why-ai-safety
knowledge_refs:
  - safety-01-why-ai-safety
    title: "Why AI Safety Matters"
  - safety-02-bias-and-fairness
    title: "Bias & Fairness"
  - safety-16-data-governance
    title: "Data Governance for AI"
references:
  - title: "Protecting Trained Models in Privacy-Preserving Federated Learning"
    url: "https://rtau.blog.gov.uk/2024/07/15/protecting-trained-models-in-privacy-preserving-federated-learning/"
  - title: "NIST — Adversarial Machine Learning: A Taxonomy and Terminology"
    url: "https://csrc.nist.gov/pubs/ai/100/2/e2025/final"
  - title: "ICO — Security and Data Minimisation in AI"
    url: "https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/how-should-we-assess-security-and-data-minimisation-in-ai/"
  - title: "ICO — Introduction to Anonymisation"
    url: "https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/anonymisation/introduction-to-anonymisation/"
  - title: "NIST — Membership-Inference Attack Glossary Definition"
    url: "https://csrc.nist.gov/glossary/term/membership_inference_attack"
---

## Privacy & Data Protection

AI systems consume vast amounts of data — and much of that data is personal. Privacy in AI isn't just a legal requirement; it's a fundamental safety concern. Models that leak personal data, memorize training examples, or enable surveillance pose serious risks.

### Differential Privacy

Differential privacy (DP) provides mathematical guarantees that the inclusion or exclusion of any single individual's data doesn't significantly alter the model's output. It works by adding calibrated random noise to queries, model weights, or training updates.

**Key idea:** If you can't tell whether a specific person's data was used to train the model, their privacy is protected.

**Trade-off:** More privacy (more noise) means less accuracy. Organizations must balance privacy guarantees with model utility.

### Federated Learning

Federated learning trains models across multiple devices without sharing raw data. Each device trains locally and sends only encrypted model updates (gradients) to a central server for aggregation.

**Benefits:** Raw data never leaves the device. This is how Google trains keyboard prediction models on millions of phones without collecting typing data.

**Limitations:** Federated learning doesn't prevent all attacks — gradient updates can still leak information. Combining it with differential privacy provides stronger guarantees.

### Data Minimization

The GDPR principle of data minimization requires that AI systems process only the data strictly necessary for their purpose. In practice:
- Use synthetic data where possible
- Collect only required features
- Delete data when no longer needed
- Implement on-device processing

### Membership Inference Attacks

An adversary can determine whether a specific data sample was in the model's training set by analyzing the model's confidence scores. If the model is more confident on a particular input, it was likely trained on it.

**Risk:** Membership inference can reveal that someone was a patient at a specific clinic, enrolled in a clinical trial, or present in a dataset — even without seeing the actual data.

**Defense:** Differential privacy, regularization, and limiting model overfitting reduce membership inference risk.

### Anonymization vs. Pseudonymization

**Pseudonymization** replaces identifiers with tokens but the data remains personal because re-identification is possible with auxiliary information.

**Anonymization** completely removes the link to individuals. Differential privacy is increasingly recognized as a robust tool for achieving legal anonymization.

### Common Mistakes

- **Assuming deletion is deletion:** Models can memorize training data. Deleting the dataset doesn't delete what the model learned.
- **Ignoring gradient leakage:** In federated learning, gradient updates can reconstruct training data without proper protection.
- **Confusing pseudonymization with anonymization:** Pseudonymized data is still personal data under GDPR.

---

*Continue to learn about hallucination — why AI systems generate false information and how to ground them in reality.*
