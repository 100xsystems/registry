---
{
  "title": "Transparency & Disclosure",
  "description": "Tell people when AI is involved: disclosure, provenance and model cards.",
  "type": "lesson",
  "order": 9,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Design user-facing AI disclosure",
    "Use content provenance",
    "Write model cards",
    "Explain system limitations"
  ],
  "knowledge_refs": [
    "ai-safety/safety-08-governance",
    "generative-ai/genai-19-ethical-ai-and-safety",
    "llm-engineering/llm-14-guardrails-and-safety"
  ],
  "prerequisites": [
    "SAFETY-08: AI Governance & Policy"
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

# SAFETY-09-TRANSPARENCY: Transparency & Disclosure

## Introduction

Tell people when AI is involved: disclosure, provenance and model cards. By the end of this lesson you will be able to: Design user-facing AI disclosure; Use content provenance; Write model cards; Explain system limitations.

## Key Concepts

### 1. Design user-facing AI disclosure

Target: Design user-facing AI disclosure. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
model_card = {
    "model": "churn-predictor v2",
    "intended_use": "marketing outreach",
    "limitations": "not for credit decisions",
    "data": "2023 customer data",
}
print(model_card)
```
### 2. Use content provenance

Target: Use content provenance. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("disclosure: users should know they are talking to AI")
```
### 3. Write model cards

Target: Write model cards. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("provenance: labels and watermarks for generated content")
```
### 4. Explain system limitations

Target: Explain system limitations. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("document limitations honestly")
```

## Practice Questions

1. What is the key idea behind "Transparency & Disclosure"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Transparency & Disclosure with analogies and real-world examples"
1. "Show me common mistakes beginners make with Transparency & Disclosure"
1. "Provide advanced patterns and performance considerations for Transparency & Disclosure"

## Key Takeaways

- Master the core ideas of Transparency & Disclosure through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
