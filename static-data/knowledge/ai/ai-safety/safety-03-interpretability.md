---
slug: safety-03-interpretability
title: "Interpretability & Explainability"
description: "Opening the black box — mechanistic interpretability, SHAP, LIME, attention visualization, and why understanding AI decisions matters."
order: 3
tags:
  - ai-safety
  - interpretability
  - explainability
  - shap
  - lime
  - mechanistic-interpretability
prerequisites:
  - safety-01-why-ai-safety
knowledge_refs:
  - slug: safety-01-why-ai-safety
    title: "Why AI Safety Matters"
  - slug: safety-05-robustness
    title: "Robustness & Adversarial Examples"
  - slug: safety-10-safety-evaluations
    title: "Safety Evaluations"
references:
  - title: "Interpretable Machine Learning — Christoph Molnar"
    url: "https://christophm.github.io/interpretable-ml-book/"
  - title: "A Mathematical Framework for Transformer Circuits"
    url: "https://transformer-circuits.pub/2021/framework/index.html"
  - title: "LIME — Interpretable Machine Learning"
    url: "https://christophm.github.io/interpretable-ml-book/lime.html"
  - title: "SHAP — Interpretable Machine Learning"
    url: "https://christophm.github.io/interpretable-ml-book/shap.html"
  - title: "Partial Dependence Plot — Interpretable Machine Learning"
    url: "https://christophm.github.io/interpretable-ml-book/pdp.html"
---
## Interpretability & Explainability

You can't fix what you can't see. Interpretability is the ability to understand *why* a model made a specific decision. Explainability is communicating that understanding to humans. Both are essential for AI safety.

### Why Interpretability Matters

**Trust:** If a doctor can't understand why an AI recommended a treatment, they shouldn't trust it.

**Debugging:** When a model fails, interpretability helps identify whether it learned the right patterns or shortcuts.

**Regulation:** GDPR gives citizens the "right to explanation" for automated decisions. Financial regulators require model explainability.

**Safety:** If an AI system behaves unexpectedly, you need to understand its internal reasoning to predict and prevent future failures.

### Two Approaches

**Post-hoc explainability:** Explaining a trained model after the fact. These methods treat the model as a black box and probe its behavior from the outside.

**Mechanistic interpretability:** Reverse-engineering the model's internal components — individual neurons, circuits, attention heads — into human-understandable algorithms.

### Post-Hoc Methods

**LIME (Local Interpretable Model-agnostic Explanations):** Fits a simple, interpretable model (like a linear regression) around a single prediction by perturbing the input and observing how the output changes. It tells you which features mattered most for *this specific* prediction.

**SHAP (SHapley Additive exPlanations):** Based on cooperative game theory, SHAP fairly distributes the "payout" (model prediction) among features. It satisfies mathematical properties like local accuracy, missingness, and consistency. SHAP values tell you how much each feature contributed to a specific prediction.

**Partial Dependence Plots:** Show how the model's prediction changes as a single feature varies, averaging over all other features. They reveal the global relationship between features and predictions.

### Mechanistic Interpretability

This field asks: what algorithms do neural networks actually learn?

**Transformer Circuits (Anthropic):** Researchers have discovered specific circuits in transformers responsible for in-context learning, induction heads (copying patterns), and indirect object identification. Tools like `TransformerLens` let researchers inspect these circuits.

**Feature Visualization:** Generate synthetic inputs that maximally activate a specific neuron. This reveals what each neuron "looks for" — edges, textures, concepts, or abstract patterns.

**Probing:** Train a small classifier on intermediate representations to test whether specific concepts (syntactic structure, truthfulness, sentiment) are linearly encoded in the model's hidden states.

**Superposition:** Neural networks pack more features than they have dimensions, overlapping multiple concepts in the same space. Understanding superposition is key to interpreting what models actually know.

### Attention Is Not Explanation

A common mistake is interpreting attention weights as explanations. Attention shows where the model *focuses*, not necessarily what it *decides*. Attention weights alone don't capture the full information flow through a transformer. Use attention visualization as one signal among many, not as a complete explanation.

### Common Mistakes

- **Treating attention as explanation:** Attention weights are correlation, not causation.
- **Over-relying on one method:** LIME and SHAP can give contradictory explanations. Use multiple methods.
- **Ignoring confidence:** An explanation for a low-confidence prediction is less meaningful than one for a high-confidence prediction.
- **Assuming interpretability is free:** Mechanistic interpretability requires significant research investment and specialized tools.

---

*Continue to learn about alignment — ensuring AI systems pursue goals that match human intent.*
