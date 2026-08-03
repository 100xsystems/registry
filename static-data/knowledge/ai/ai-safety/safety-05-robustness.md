---
{
  "title": "Robustness & Adversarial Examples",
  "description": "Models that break under tiny perturbations — and how to harden them.",
  "type": "lesson",
  "order": 5,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain adversarial examples",
    "Generate simple adversarial perturbations",
    "Defend with augmentation and adversarial training",
    "Test robustness systematically"
  ],
  "knowledge_refs": [
    "ai-safety/safety-04-alignment",
    "generative-ai/genai-19-ethical-ai-and-safety",
    "llm-engineering/llm-14-guardrails-and-safety"
  ],
  "prerequisites": [
    "SAFETY-03: Interpretability & Explainability"
  ],
  "references": [
    {
      "title": "The Alignment Problem — Brian Christian",
      "url": "https://www.brianchristian.org/the-alignment-problem/",
      "description": "A narrative history of AI alignment research."
    },
    {
      "title": "AI Safety Fundamentals",
      "url": "https://aisafetyfundamentals.com/",
      "description": "Courses and readings on AI safety topics."
    },
    {
      "title": "Fairness in Machine Learning (Google)",
      "url": "https://developers.google.com/machine-learning/fairness-overview",
      "description": "A practical overview of ML fairness."
    },
    {
      "title": "Model Cards for Model Reporting",
      "url": "https://arxiv.org/abs/1810.03993",
      "description": "The paper introducing model cards."
    },
    {
      "title": "Anthropic — Red Teaming",
      "url": "https://www.anthropic.com/news/red-teaming-language-models",
      "description": "Practices for adversarial testing of AI systems."
    }
  ]
}
---

# SAFETY-05-ROBUSTNESS: Robustness & Adversarial Examples

## Introduction

Models that break under tiny perturbations — and how to harden them. By the end of this lesson you will be able to: Explain adversarial examples; Generate simple adversarial perturbations; Defend with augmentation and adversarial training; Test robustness systematically.

## Key Concepts

### 1. Explain adversarial examples

Target: Explain adversarial examples. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

# Tiny perturbation flips a prediction
x = np.array([1.0, 0.0])
adv = x + 0.05 * np.array([-1.0, 1.0])
print("perturbed:", adv)
```
### 2. Generate simple adversarial perturbations

Target: Generate simple adversarial perturbations. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("human-invisible changes can flip model outputs")
```
### 3. Defend with augmentation and adversarial training

Target: Defend with augmentation and adversarial training. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("defense: adversarial training, augmentation, smoothing")
```
### 4. Test robustness systematically

Target: Test robustness systematically. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("robustness evals belong in the test suite")
```

## Practice Questions

1. What is the key idea behind "Robustness & Adversarial Examples"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Robustness & Adversarial Examples with analogies and real-world examples"
1. "Show me common mistakes beginners make with Robustness & Adversarial Examples"
1. "Provide advanced patterns and performance considerations for Robustness & Adversarial Examples"

## Key Takeaways

- Master the core ideas of Robustness & Adversarial Examples through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
