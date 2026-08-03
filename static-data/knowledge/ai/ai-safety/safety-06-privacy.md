---
{
  "title": "Privacy & Data Protection",
  "description": "PII, memorization and differential privacy in AI systems.",
  "type": "lesson",
  "order": 6,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Identify privacy risks in ML pipelines",
    "Explain model memorization",
    "Apply differential privacy basics",
    "Handle data subject rights"
  ],
  "knowledge_refs": [
    "ai-safety/safety-06-privacy"
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

# SAFETY-06-PRIVACY: Privacy & Data Protection

## Introduction

PII, memorization and differential privacy in AI systems. By the end of this lesson you will be able to: Identify privacy risks in ML pipelines; Explain model memorization; Apply differential privacy basics; Handle data subject rights.

## Key Concepts

### 1. Identify privacy risks in ML pipelines

Target: Identify privacy risks in ML pipelines. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import re

text = "email: ada@example.com"
print(re.sub(r"[\w.+-]+@[\w-]+\.[\w.]+", "[PII]", text))
```
### 2. Explain model memorization

Target: Explain model memorization. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# Differential privacy: add calibrated noise
query = 42.0
noisy = query + np.random.default_rng(0).laplace(0, 1.0)
print("private answer:", round(noisy, 2))
```
### 3. Apply differential privacy basics

Target: Apply differential privacy basics. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("large models can memorize training examples")
```
### 4. Handle data subject rights

Target: Handle data subject rights. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("GDPR/CCPA: right to access, erasure, explanation")
```

## Practice Questions

1. What is the key idea behind "Privacy & Data Protection"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Privacy & Data Protection with analogies and real-world examples"
1. "Show me common mistakes beginners make with Privacy & Data Protection"
1. "Provide advanced patterns and performance considerations for Privacy & Data Protection"

## Key Takeaways

- Master the core ideas of Privacy & Data Protection through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
