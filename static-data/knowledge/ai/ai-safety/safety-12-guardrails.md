---
{
  "title": "Guardrails & Content Moderation",
  "description": "Layer protections on outputs: classifiers, filters and policy enforcement.",
  "type": "lesson",
  "order": 12,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Design layered guardrails",
    "Use moderation classifiers",
    "Implement output filters",
    "Balance safety with usability"
  ],
  "knowledge_refs": [
    "ai-safety/safety-12-guardrails"
  ],
  "prerequisites": [
    "SAFETY-10: Safety Evaluations"
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

# SAFETY-12-GUARDRAILS: Guardrails & Content Moderation

## Introduction

Layer protections on outputs: classifiers, filters and policy enforcement. By the end of this lesson you will be able to: Design layered guardrails; Use moderation classifiers; Implement output filters; Balance safety with usability.

## Key Concepts

### 1. Design layered guardrails

Target: Design layered guardrails. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from openai import OpenAI

client = OpenAI()
res = client.moderations.create(input="some content")
print("flagged:", res.results[0].flagged)
```
### 2. Use moderation classifiers

Target: Use moderation classifiers. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import re

# Output filter: block dangerous patterns
out = "call 1-800-EVIL"
print("blocked" if "EVIL" in out else "allowed")
```
### 3. Implement output filters

Target: Implement output filters. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("layers: input filter -> model -> output filter -> human review")
```
### 4. Balance safety with usability

Target: Balance safety with usability. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("too-strict guardrails frustrate users; tune with evals")
```

## Practice Questions

1. What is the key idea behind "Guardrails & Content Moderation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Guardrails & Content Moderation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Guardrails & Content Moderation"
1. "Provide advanced patterns and performance considerations for Guardrails & Content Moderation"

## Key Takeaways

- Master the core ideas of Guardrails & Content Moderation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
