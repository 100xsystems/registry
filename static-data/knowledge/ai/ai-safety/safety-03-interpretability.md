---
{
  "title": "Interpretability & Explainability",
  "description": "Understand why models decide: feature importance, saliency and post-hoc explanations.",
  "type": "lesson",
  "order": 3,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain local vs global interpretability",
    "Use SHAP and LIME",
    "Read saliency maps",
    "Know the limits of explanations"
  ],
  "knowledge_refs": [
    "ai-safety/safety-02-bias-and-fairness",
    "generative-ai/genai-19-ethical-ai-and-safety",
    "llm-engineering/llm-14-guardrails-and-safety"
  ],
  "prerequisites": [
    "SAFETY-02: Bias & Fairness"
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

# SAFETY-03-INTERPRETABILITY: Interpretability & Explainability

## Introduction

Understand why models decide: feature importance, saliency and post-hoc explanations. By the end of this lesson you will be able to: Explain local vs global interpretability; Use SHAP and LIME; Read saliency maps; Know the limits of explanations.

## Key Concepts

### 1. Explain local vs global interpretability

Target: Explain local vs global interpretability. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import shap

# SHAP: how much each feature pushed the prediction
print("shap values ready")
```
### 2. Use SHAP and LIME

Target: Use SHAP and LIME. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# Saliency: gradient magnitude per pixel
saliency = np.random.default_rng(0).normal(size=(224, 224))
print("saliency map:", saliency.shape)
```
### 3. Read saliency maps

Target: Read saliency maps. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("local: why this prediction? global: how does the model work?")
```
### 4. Know the limits of explanations

Target: Know the limits of explanations. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("explanations are approximations, not ground truth")
```

## Practice Questions

1. What is the key idea behind "Interpretability & Explainability"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Interpretability & Explainability with analogies and real-world examples"
1. "Show me common mistakes beginners make with Interpretability & Explainability"
1. "Provide advanced patterns and performance considerations for Interpretability & Explainability"

## Key Takeaways

- Master the core ideas of Interpretability & Explainability through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
