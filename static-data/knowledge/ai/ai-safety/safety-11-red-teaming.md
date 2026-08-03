---
{
  "title": "Red Teaming",
  "description": "Adversarial testing by skilled humans — find failures before users do.",
  "type": "lesson",
  "order": 11,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Design a red-team campaign",
    "Write adversarial test cases",
    "Triage and fix findings",
    "Institutionalize red teaming"
  ],
  "knowledge_refs": [
    "ai-safety/safety-10-safety-evaluations",
    "generative-ai/genai-19-ethical-ai-and-safety",
    "llm-engineering/llm-14-guardrails-and-safety"
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

# SAFETY-11-RED-TEAMING: Red Teaming

## Introduction

Adversarial testing by skilled humans — find failures before users do. By the end of this lesson you will be able to: Design a red-team campaign; Write adversarial test cases; Triage and fix findings; Institutionalize red teaming.

## Key Concepts

### 1. Design a red-team campaign

Target: Design a red-team campaign. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
print("red team: try to make the system fail safely")
```
### 2. Write adversarial test cases

Target: Write adversarial test cases. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
focus = ["injection", "jailbreaks", "bias", "data leakage"]
print(focus)
```
### 3. Triage and fix findings

Target: Triage and fix findings. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("triage: severity x likelihood, then fix + retest")
```
### 4. Institutionalize red teaming

Target: Institutionalize red teaming. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("diverse testers find diverse failures")
```

## Practice Questions

1. What is the key idea behind "Red Teaming"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Red Teaming with analogies and real-world examples"
1. "Show me common mistakes beginners make with Red Teaming"
1. "Provide advanced patterns and performance considerations for Red Teaming"

## Key Takeaways

- Master the core ideas of Red Teaming through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
