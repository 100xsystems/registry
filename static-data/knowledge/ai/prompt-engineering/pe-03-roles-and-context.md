---
{
  "title": "Roles & Context",
  "description": "System prompts, personas and context injection — set the stage for better outputs.",
  "type": "lesson",
  "order": 3,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write effective system prompts",
    "Use personas deliberately",
    "Inject relevant context",
    "Separate instructions from data"
  ],
  "knowledge_refs": [
    "prompt-engineering/pe-03-roles-and-context"
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

# PE-03-ROLES-AND-CONTEXT: Roles & Context

## Introduction

System prompts, personas and context injection — set the stage for better outputs. By the end of this lesson you will be able to: Write effective system prompts; Use personas deliberately; Inject relevant context; Separate instructions from data.

## Key Concepts

### 1. Write effective system prompts

Target: Write effective system prompts. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
system = "You are a meticulous code reviewer who catches security issues."
print(system)
```
### 2. Use personas deliberately

Target: Use personas deliberately. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from openai import OpenAI

client = OpenAI()
res = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Answer as a friendly mentor."},
        {"role": "user", "content": "Explain recursion."},
    ],
)
print(res.choices[0].message.content[:80])
```
### 3. Inject relevant context

Target: Inject relevant context. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("context: give facts the model needs; don't overload")
```
### 4. Separate instructions from data

Target: Separate instructions from data. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("instructions in the system turn, data in the user turn")
```

## Practice Questions

1. What is the key idea behind "Roles & Context"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Roles & Context with analogies and real-world examples"
1. "Show me common mistakes beginners make with Roles & Context"
1. "Provide advanced patterns and performance considerations for Roles & Context"

## Key Takeaways

- Master the core ideas of Roles & Context through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
