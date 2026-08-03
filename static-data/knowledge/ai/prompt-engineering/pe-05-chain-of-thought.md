---
{
  "title": "Chain-of-Thought Reasoning",
  "description": "Prompt the model to reason step by step — dramatically better on math and logic.",
  "type": "lesson",
  "order": 5,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain why CoT improves reasoning",
    "Write step-by-step instructions",
    "Use few-shot CoT examples",
    "Know when to disable reasoning (speed)"
  ],
  "knowledge_refs": [
    "prompt-engineering/pe-05-chain-of-thought"
  ],
  "prerequisites": [
    "PE-02: Prompt Structure"
  ],
  "references": [
    {
      "title": "OpenAI Prompt Engineering Guide",
      "url": "https://platform.openai.com/docs/guides/prompt-engineering",
      "description": "Six strategies for reliable prompting from OpenAI."
    },
    {
      "title": "Anthropic Prompt Engineering Docs",
      "url": "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering",
      "description": "Claude's practical prompt engineering guide."
    },
    {
      "title": "Prompt Engineering Guide (DAIR.AI)",
      "url": "https://www.promptingguide.ai/",
      "description": "A broad open-source guide to prompt techniques."
    },
    {
      "title": "CoT: Chain-of-Thought Prompting",
      "url": "https://arxiv.org/abs/2201.11903",
      "description": "The paper on reasoning via chain-of-thought prompts."
    },
    {
      "title": "ReAct: Reasoning + Acting",
      "url": "https://arxiv.org/abs/2210.03629",
      "description": "Combining reasoning traces with tool actions."
    }
  ]
}
---

# PE-05-CHAIN-OF-THOUGHT: Chain-of-Thought Reasoning

## Introduction

Prompt the model to reason step by step — dramatically better on math and logic. By the end of this lesson you will be able to: Explain why CoT improves reasoning; Write step-by-step instructions; Use few-shot CoT examples; Know when to disable reasoning (speed).

## Key Concepts

### 1. Explain why CoT improves reasoning

Target: Explain why CoT improves reasoning. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
prompt = """Solve step by step:\nA store has 3 shelves with 5 boxes each. How many boxes?\nStep 1: 3 shelves * 5 boxes = 15.\nAnswer: 15"""
print(prompt)
```
### 2. Write step-by-step instructions

Target: Write step-by-step instructions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
prompt2 = "A train travels 60 km/h for 2 hours and 90 km/h for 1 hour. What is the total distance? Show your work step by step."
print(prompt2)
```
### 3. Use few-shot CoT examples

Target: Use few-shot CoT examples. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("CoT shines on arithmetic, logic and planning")
```
### 4. Know when to disable reasoning (speed)

Target: Know when to disable reasoning (speed). Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("for simple tasks, reasoning wastes tokens and latency")
```

## Practice Questions

1. What is the key idea behind "Chain-of-Thought Reasoning"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Chain-of-Thought Reasoning with analogies and real-world examples"
1. "Show me common mistakes beginners make with Chain-of-Thought Reasoning"
1. "Provide advanced patterns and performance considerations for Chain-of-Thought Reasoning"

## Key Takeaways

- Master the core ideas of Chain-of-Thought Reasoning through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
