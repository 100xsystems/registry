---
{
  "title": "Hallucination & Factualness",
  "description": "When models make things up — measure it, reduce it, and tell users about it.",
  "type": "lesson",
  "order": 7,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define hallucination and its causes",
    "Measure factual accuracy",
    "Ground models with retrieval",
    "Design honest failure behavior"
  ],
  "knowledge_refs": [
    "ai-safety/safety-06-privacy",
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

# SAFETY-07-HALLUCINATION: Hallucination & Factualness

## Introduction

When models make things up — measure it, reduce it, and tell users about it. By the end of this lesson you will be able to: Define hallucination and its causes; Measure factual accuracy; Ground models with retrieval; Design honest failure behavior.

## Key Concepts

### 1. Define hallucination and its causes

Target: Define hallucination and its causes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

# Factual accuracy on a quiz
correct = np.array([1, 1, 0, 1, 0])
print("factual accuracy:", correct.mean())
```
### 2. Measure factual accuracy

Target: Measure factual accuracy. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("causes: next-token training, weak grounding, no source checking")
```
### 3. Ground models with retrieval

Target: Ground models with retrieval. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("fix: RAG, citations, retrieval verification")
```
### 4. Design honest failure behavior

Target: Design honest failure behavior. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("when unsure: say so instead of inventing")
```

## Practice Questions

1. What is the key idea behind "Hallucination & Factualness"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Hallucination & Factualness with analogies and real-world examples"
1. "Show me common mistakes beginners make with Hallucination & Factualness"
1. "Provide advanced patterns and performance considerations for Hallucination & Factualness"

## Key Takeaways

- Master the core ideas of Hallucination & Factualness through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
