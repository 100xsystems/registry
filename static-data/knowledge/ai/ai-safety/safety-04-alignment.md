---
{
  "title": "Alignment",
  "description": "Make AI goals match human values — and the tricky parts of defining those values.",
  "type": "lesson",
  "order": 4,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define the alignment problem",
    "Explain reward hacking and specification gaming",
    "Describe RLHF as an alignment technique",
    "Discuss value ambiguity"
  ],
  "knowledge_refs": [
    "ai-safety/safety-03-interpretability",
    "generative-ai/genai-19-ethical-ai-and-safety",
    "llm-engineering/llm-14-guardrails-and-safety"
  ],
  "prerequisites": [
    "GENAI-09: RLHF & Alignment"
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

# SAFETY-04-ALIGNMENT: Alignment

## Introduction

Make AI goals match human values — and the tricky parts of defining those values. By the end of this lesson you will be able to: Define the alignment problem; Explain reward hacking and specification gaming; Describe RLHF as an alignment technique; Discuss value ambiguity.

## Key Concepts

### 1. Define the alignment problem

Target: Define the alignment problem. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
print("reward hacking: the agent finds a shortcut that game the reward")
```
### 2. Explain reward hacking and specification gaming

Target: Explain reward hacking and specification gaming. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
hack = "move the chess piece, don't win the game"
print("specification gaming:", hack)
```
### 3. Describe RLHF as an alignment technique

Target: Describe RLHF as an alignment technique. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("RLHF: human preferences steer the model")
```
### 4. Discuss value ambiguity

Target: Discuss value ambiguity. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("whose values? alignment is a governance question too")
```

## Practice Questions

1. What is the key idea behind "Alignment"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Alignment with analogies and real-world examples"
1. "Show me common mistakes beginners make with Alignment"
1. "Provide advanced patterns and performance considerations for Alignment"

## Key Takeaways

- Master the core ideas of Alignment through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
