---
{
  "title": "Optimizing Prompts for Cost",
  "description": "Shorter prompts, fewer tokens, right-sized models — quality per dollar.",
  "type": "lesson",
  "order": 19,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Trim redundant prompt text",
    "Route by task difficulty",
    "Use compact formats",
    "Track cost per outcome"
  ],
  "knowledge_refs": [
    "prompt-engineering/pe-19-optimizing-for-cost"
  ],
  "prerequisites": [
    "PE-16: Prompt Caching & Cost"
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

# PE-19-OPTIMIZING-FOR-COST: Optimizing Prompts for Cost

## Introduction

Shorter prompts, fewer tokens, right-sized models — quality per dollar. By the end of this lesson you will be able to: Trim redundant prompt text; Route by task difficulty; Use compact formats; Track cost per outcome.

## Key Concepts

### 1. Trim redundant prompt text

Target: Trim redundant prompt text. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
verbose = "Please kindly provide me with a summary of the following text."
concise = "Summarize:"
print("tokens saved:", len(enc.encode(verbose)) - len(enc.encode(concise)))
```
### 2. Route by task difficulty

Target: Route by task difficulty. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("small model for easy tasks, big model for hard ones")
```
### 3. Use compact formats

Target: Use compact formats. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("structured short formats beat prose")
```
### 4. Track cost per outcome

Target: Track cost per outcome. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("optimize for outcome, not just tokens")
```

## Practice Questions

1. What is the key idea behind "Optimizing Prompts for Cost"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Optimizing Prompts for Cost with analogies and real-world examples"
1. "Show me common mistakes beginners make with Optimizing Prompts for Cost"
1. "Provide advanced patterns and performance considerations for Optimizing Prompts for Cost"

## Key Takeaways

- Master the core ideas of Optimizing Prompts for Cost through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
