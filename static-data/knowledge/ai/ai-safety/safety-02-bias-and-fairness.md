---
{
  "title": "Bias & Fairness",
  "description": "Measure and mitigate bias: metrics, audits and the human choices behind them.",
  "type": "lesson",
  "order": 2,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define fairness and its competing metrics",
    "Measure disparate impact",
    "Mitigate bias at data, model and post-processing",
    "Audit models for bias"
  ],
  "knowledge_refs": [
    "ai-safety/safety-01-why-ai-safety",
    "generative-ai/genai-19-ethical-ai-and-safety",
    "llm-engineering/llm-14-guardrails-and-safety"
  ],
  "prerequisites": [
    "SAFETY-01: Why AI Safety Matters"
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

# SAFETY-02-BIAS-AND-FAIRNESS: Bias & Fairness

## Introduction

Measure and mitigate bias: metrics, audits and the human choices behind them. By the end of this lesson you will be able to: Define fairness and its competing metrics; Measure disparate impact; Mitigate bias at data, model and post-processing; Audit models for bias.

## Key Concepts

### 1. Define fairness and its competing metrics

Target: Define fairness and its competing metrics. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

# Disparate impact: approval rate ratio between groups
group_a = np.array([1, 1, 0, 1])
group_b = np.array([0, 0, 1, 0])
ratio = group_a.mean() / group_b.mean()
print("disparate impact:", round(ratio, 2))
```
### 2. Measure disparate impact

Target: Measure disparate impact. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("fairness metrics can conflict: choose deliberately")
```
### 3. Mitigate bias at data, model and post-processing

Target: Mitigate bias at data, model and post-processing. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("mitigate: reweight data, constrain the model, calibrate outputs")
```
### 4. Audit models for bias

Target: Audit models for bias. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("audit: test on subgroups before launch")
```

## Practice Questions

1. What is the key idea behind "Bias & Fairness"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Bias & Fairness with analogies and real-world examples"
1. "Show me common mistakes beginners make with Bias & Fairness"
1. "Provide advanced patterns and performance considerations for Bias & Fairness"

## Key Takeaways

- Master the core ideas of Bias & Fairness through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
