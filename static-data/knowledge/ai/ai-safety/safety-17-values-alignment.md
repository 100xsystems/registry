---
{
  "title": "Designing for Human Values",
  "description": "Turn values into requirements: privacy, fairness, dignity as design inputs.",
  "type": "lesson",
  "order": 17,
  "duration": "50 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Translate values into product requirements",
    "Run value-sensitive design workshops",
    "Balance competing values",
    "Measure value alignment"
  ],
  "knowledge_refs": [
    "ai-safety/safety-16-data-governance",
    "generative-ai/genai-19-ethical-ai-and-safety",
    "llm-engineering/llm-14-guardrails-and-safety"
  ],
  "prerequisites": [
    "SAFETY-04: Alignment"
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

# SAFETY-17-VALUES-ALIGNMENT: Designing for Human Values

## Introduction

Turn values into requirements: privacy, fairness, dignity as design inputs. By the end of this lesson you will be able to: Translate values into product requirements; Run value-sensitive design workshops; Balance competing values; Measure value alignment.

## Key Concepts

### 1. Translate values into product requirements

Target: Translate values into product requirements. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
values = {"privacy": "no PII in logs", "fairness": "parity on subgroups", "dignity": "humane error messages"}
print(values)
```
### 2. Run value-sensitive design workshops

Target: Run value-sensitive design workshops. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("values -> requirements -> evals -> review")
```
### 3. Balance competing values

Target: Balance competing values. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("conflicts: privacy vs personalization needs trade-offs")
```
### 4. Measure value alignment

Target: Measure value alignment. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("measure: evals for each value requirement")
```

## Practice Questions

1. What is the key idea behind "Designing for Human Values"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Designing for Human Values with analogies and real-world examples"
1. "Show me common mistakes beginners make with Designing for Human Values"
1. "Provide advanced patterns and performance considerations for Designing for Human Values"

## Key Takeaways

- Master the core ideas of Designing for Human Values through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
