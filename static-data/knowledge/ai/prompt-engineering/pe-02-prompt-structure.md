---
{
  "title": "Prompt Structure",
  "description": "The anatomy of a strong prompt: task, context, constraints and output format.",
  "type": "lesson",
  "order": 2,
  "duration": "50 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Structure prompts into clear sections",
    "Write unambiguous task statements",
    "Add constraints that prevent failure modes",
    "Specify output format precisely"
  ],
  "knowledge_refs": [
    "prompt-engineering/pe-01-what-is-prompt-engineering",
    "generative-ai/genai-04-prompt-engineering",
    "llm-engineering/llm-17-observability"
  ],
  "prerequisites": [
    "PE-01: What Is Prompt Engineering?"
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

# PE-02-PROMPT-STRUCTURE: Prompt Structure

## Introduction

The anatomy of a strong prompt: task, context, constraints and output format. By the end of this lesson you will be able to: Structure prompts into clear sections; Write unambiguous task statements; Add constraints that prevent failure modes; Specify output format precisely.

## Key Concepts

### 1. Structure prompts into clear sections

Target: Structure prompts into clear sections. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
prompt = """
TASK: Summarize the article in 3 bullet points.
CONTEXT: The audience is busy engineers.
CONSTRAINTS: Max 12 words per bullet.
OUTPUT:
- ...
- ...
- ...
"""
print(prompt)
```
### 2. Write unambiguous task statements

Target: Write unambiguous task statements. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("one task per prompt beats a multi-task muddle")
```
### 3. Add constraints that prevent failure modes

Target: Add constraints that prevent failure modes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("constraints: length, tone, audience, must/must-not")
```
### 4. Specify output format precisely

Target: Specify output format precisely. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
from openai import OpenAI

client = OpenAI()
res = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Extract the date and amount into JSON."}],
)
print(res.choices[0].message.content)
```

## Practice Questions

1. What is the key idea behind "Prompt Structure"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Prompt Structure with analogies and real-world examples"
1. "Show me common mistakes beginners make with Prompt Structure"
1. "Provide advanced patterns and performance considerations for Prompt Structure"

## Key Takeaways

- Master the core ideas of Prompt Structure through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
