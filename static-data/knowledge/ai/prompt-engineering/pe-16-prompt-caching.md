---
{
  "title": "Prompt Caching & Cost",
  "description": "Cache long system prompts and reuse embeddings to cut cost and latency.",
  "type": "lesson",
  "order": 16,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Cache static prompt prefixes",
    "Batch similar prompts",
    "Measure tokens saved",
    "Balance cache freshness"
  ],
  "knowledge_refs": [
    "prompt-engineering/pe-16-prompt-caching"
  ],
  "prerequisites": [
    "LLM-16: Cost Optimization for LLM Apps"
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

# PE-16-PROMPT-CACHING: Prompt Caching & Cost

## Introduction

Cache long system prompts and reuse embeddings to cut cost and latency. By the end of this lesson you will be able to: Cache static prompt prefixes; Batch similar prompts; Measure tokens saved; Balance cache freshness.

## Key Concepts

### 1. Cache static prompt prefixes

Target: Cache static prompt prefixes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import hashlib

prefix = "You are a helpful assistant." * 50
print("cache key:", hashlib.sha256(prefix.encode()).hexdigest()[:10])
```
### 2. Batch similar prompts

Target: Batch similar prompts. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("static prefixes (system prompt) are cache-friendly")
```
### 3. Measure tokens saved

Target: Measure tokens saved. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("dynamic parts (user input) are not")
```
### 4. Balance cache freshness

Target: Balance cache freshness. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("measure: tokens saved vs cache hit rate")
```

## Practice Questions

1. What is the key idea behind "Prompt Caching & Cost"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Prompt Caching & Cost with analogies and real-world examples"
1. "Show me common mistakes beginners make with Prompt Caching & Cost"
1. "Provide advanced patterns and performance considerations for Prompt Caching & Cost"

## Key Takeaways

- Master the core ideas of Prompt Caching & Cost through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
