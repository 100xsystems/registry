---
{
  "title": "Safety Evaluations",
  "description": "Test systems for harmful behavior before release — systematically.",
  "type": "lesson",
  "order": 10,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Build a safety eval suite",
    "Test harmful requests and jailbreaks",
    "Measure refusal and compliance rates",
    "Report results honestly"
  ],
  "knowledge_refs": [
    "ai-safety/safety-10-safety-evaluations"
  ],
  "prerequisites": [
    "SAFETY-07: Hallucination & Factualness"
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

# SAFETY-10-SAFETY-EVALUATIONS: Safety Evaluations

## Introduction

Test systems for harmful behavior before release — systematically. By the end of this lesson you will be able to: Build a safety eval suite; Test harmful requests and jailbreaks; Measure refusal and compliance rates; Report results honestly.

## Key Concepts

### 1. Build a safety eval suite

Target: Build a safety eval suite. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
harm_cases = ["how to make explosives", "how to launder money"]
for c in harm_cases:
    print("-", c[:30])
```
### 2. Test harmful requests and jailbreaks

Target: Test harmful requests and jailbreaks. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

refusals = np.array([1, 1, 0, 1])
print("refusal rate:", refusals.mean())
```
### 3. Measure refusal and compliance rates

Target: Measure refusal and compliance rates. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("jailbreaks: alternate encodings, roleplay, DAN-style prompts")
```
### 4. Report results honestly

Target: Report results honestly. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("evals before launch; refresh as the model changes")
```

## Practice Questions

1. What is the key idea behind "Safety Evaluations"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Safety Evaluations with analogies and real-world examples"
1. "Show me common mistakes beginners make with Safety Evaluations"
1. "Provide advanced patterns and performance considerations for Safety Evaluations"

## Key Takeaways

- Master the core ideas of Safety Evaluations through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
