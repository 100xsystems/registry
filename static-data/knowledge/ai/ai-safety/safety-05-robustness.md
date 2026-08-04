---
slug: safety-05-robustness
title: "Robustness & Adversarial Examples"
description: "Making AI systems reliable under attack — adversarial examples, adversarial training, certified robustness, and out-of-distribution detection."
order: 5
tags:
  - ai-safety
  - robustness
  - adversarial-examples
  - adversarial-training
  - ood-detection
prerequisites:
  - safety-03-interpretability
knowledge_refs:
  - safety-03-interpretability
    title: "Interpretability & Explainability"
  - safety-07-hallucination
    title: "Hallucination & Factualness"
  - safety-10-safety-evaluations
    title: "Safety Evaluations"
references:
  - title: "Adversarial Machine Learning — Wikipedia"
    url: "https://en.wikipedia.org/wiki/Adversarial_machine_learning"
  - title: "AI Safety — Wikipedia"
    url: "https://en.wikipedia.org/wiki/AI_safety"
  - title: "AI Alignment — Wikipedia"
    url: "https://en.wikipedia.org/wiki/AI_alignment"
  - title: "Anomaly Detection — Wikipedia"
    url: "https://en.wikipedia.org/wiki/Anomaly_detection"
  - title: "Towards Deep Learning Models Resistant to Adversarial Attacks (Madry et al., 2018)"
    url: "https://arxiv.org/abs/1706.06083"
---

## Robustness & Adversarial Examples

A model that works perfectly on test data can fail catastrophically when the input is slightly perturbed. Robustness is about ensuring AI systems remain reliable under adversarial attack, distributional shift, and unexpected inputs.

### Adversarial Examples

Adversarial examples are inputs purposefully modified with small, often imperceptible perturbations that cause the model to make confident wrong predictions.

**How they work:** Neural networks learn decision boundaries that are locally smooth but globally complex. Small perturbations in high-dimensional space can cross these boundaries, even though the perturbation is invisible to humans.

**Real-world implications:**
- A stop sign modified with stickers is misclassified by a self-driving car
- A 3D-printed object fools facial recognition systems
- Slight audio perturbations cause speech-to-text to transcribe wrong words
- Text-based prompt injections can manipulate LLM behavior

### Attack Types

**White-box attacks:** The attacker has full access to model weights and gradients.
- **FGSM (Fast Gradient Sign Method):** Adds noise in the direction of the gradient — fast but limited.
- **PGD (Projected Gradient Descent):** Iterative FGSM with projection — stronger, considered the gold standard for evaluating defenses.
- **C&W (Carlini & Wagner):** Optimization-based attacks that find minimal perturbations.

**Black-box attacks:** The attacker only has query access. They often exploit **transferability** — adversarial examples generated for one model often fool other models trained on similar data.

### Defenses

**Adversarial training:** The most effective defense. Generate adversarial examples during training and include them in the training set. This teaches the model to be robust to perturbations.

The core trade-off: adversarial training costs 2–10× more compute and often reduces clean accuracy by 5–15%. Robustness comes at a price.

**Certified robustness:** Mathematical guarantees that predictions won't change within a specified perturbation region.
- **Randomized smoothing:** Adds Gaussian noise to inputs and takes majority vote over multiple noisy versions
- **Interval bound propagation:** Computes worst-case outputs over input regions

**Input validation:** Detect and reject inputs that look adversarial before they reach the model.

### Out-of-Distribution Detection

Standard ML assumes training and test data come from the same distribution. In reality, deployed models encounter data far outside their training distribution.

**OOD detection techniques:**
- Energy-based scoring
- Maximum softmax probability
- Density estimation
- Vision-language alignment (using CLIP-like models to detect semantic outliers)

Without OOD detection, models produce overconfident wrong predictions on novel inputs. In safety-critical applications, the ability to say "I don't know" is as important as getting the right answer.

### Common Mistakes

- **Assuming adversarial robustness transfers:** Defenses against one attack type don't necessarily protect against others.
- **Ignoring the accuracy-robustness trade-off:** Making models more robust often reduces their accuracy on clean data.
- **Testing with weak attacks:** Evaluating robustness against FGSM but not PGD gives false confidence.
- **No OOD detection:** Deploying without the ability to detect unusual inputs is dangerous.

---

*Continue to learn about privacy — protecting data and preventing information leakage in AI systems.*
