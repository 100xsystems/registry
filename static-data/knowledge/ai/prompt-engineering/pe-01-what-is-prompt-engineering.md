---
{
  "title": "What Is Prompt Engineering?",
  "description": "Designing instructions that get reliable model behavior — a discipline, not a parlor trick.",
  "type": "lesson",
  "order": 1,
  "duration": "40 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define prompt engineering and why it matters",
    "Explain the iterative prompt lifecycle",
    "List the levers: wording, examples, format, constraints",
    "Evaluate prompts systematically"
  ],
  "knowledge_refs": [
    "generative-ai/genai-04-prompt-engineering",
    "llm-engineering/llm-17-observability",
    "llm-engineering/llm-04-prompting-systems"
  ],
  "prerequisites": [
    "GENAI-04: Prompt Engineering"
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

# PE-01-WHAT-IS-PROMPT-ENGINEERING: What Is Prompt Engineering?

## Introduction

Designing instructions that get reliable model behavior — a discipline, not a parlor trick. By the end of this lesson you will be able to: Define prompt engineering and why it matters; Explain the iterative prompt lifecycle; List the levers: wording, examples, format, constraints; Evaluate prompts systematically.

## Key Concepts

### 1. Define prompt engineering and why it matters

Target: Define prompt engineering and why it matters. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
v1 = "Write about ML"
v2 = "Explain gradient descent to a 10-year-old in 3 sentences"
print("specific beats vague:") 
print("  ", v1)
print("  ", v2)
```
### 2. Explain the iterative prompt lifecycle

Target: Explain the iterative prompt lifecycle. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from openai import OpenAI

client = OpenAI()
res = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "List 3 pros and 3 cons of Python. One line each."}],
)
print(res.choices[0].message.content)
```
### 3. List the levers: wording, examples, format, constraints

Target: List the levers: wording, examples, format, constraints. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
levers = ["role", "context", "examples", "format", "constraints"]
print(levers)
```
### 4. Evaluate prompts systematically

Target: Evaluate prompts systematically. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("every prompt change is a hypothesis -> measure with evals")
```

## Practice Questions

1. What is the key idea behind "What Is Prompt Engineering?"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain What Is Prompt Engineering? with analogies and real-world examples"
1. "Show me common mistakes beginners make with What Is Prompt Engineering?"
1. "Provide advanced patterns and performance considerations for What Is Prompt Engineering?"

## Key Takeaways

- Master the core ideas of What Is Prompt Engineering? through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
