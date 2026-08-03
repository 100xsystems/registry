---
{
  "title": "Why AI Safety Matters",
  "description": "The stakes, the risks, and the field that studies how to build AI that behaves.",
  "type": "lesson",
  "order": 1,
  "duration": "40 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define AI safety and its subfields",
    "Identify near-term and long-term risks",
    "Explain why capabilities outpace safety",
    "Recognize safety as an engineering discipline"
  ],
  "knowledge_refs": [
    "ai-safety/safety-01-why-ai-safety"
  ],
  "prerequisites": [
    "GENAI-01: What Is Generative AI?"
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

# SAFETY-01-WHY-AI-SAFETY: Why AI Safety Matters

## Introduction

The stakes, the risks, and the field that studies how to build AI that behaves. By the end of this lesson you will be able to: Define AI safety and its subfields; Identify near-term and long-term risks; Explain why capabilities outpace safety; Recognize safety as an engineering discipline.

## Key Concepts

### 1. Define AI safety and its subfields

Target: Define AI safety and its subfields. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
risks = {
    "near_term": "bias, misinformation, misuse",
    "long_term": "misalignment, loss of control",
}
print(risks)
```
### 2. Identify near-term and long-term risks

Target: Identify near-term and long-term risks. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("capability grows fast; robustness grows slower")
```
### 3. Explain why capabilities outpace safety

Target: Explain why capabilities outpace safety. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("safety = alignment + robustness + governance")
```
### 4. Recognize safety as an engineering discipline

Target: Recognize safety as an engineering discipline. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("you are already building AI systems -> safety is your job")
```

## Practice Questions

1. What is the key idea behind "Why AI Safety Matters"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Why AI Safety Matters with analogies and real-world examples"
1. "Show me common mistakes beginners make with Why AI Safety Matters"
1. "Provide advanced patterns and performance considerations for Why AI Safety Matters"

## Key Takeaways

- Master the core ideas of Why AI Safety Matters through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
