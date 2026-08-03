---
{
  "title": "Advanced Prompting Techniques",
  "description": "Self-consistency, generated knowledge, tree-of-thought and ReAct-style scaffolding.",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Apply self-consistency sampling",
    "Use generated-knowledge prompting",
    "Describe tree-of-thought search",
    "Combine prompts with tool actions (ReAct)"
  ],
  "knowledge_refs": [
    "prompt-engineering/pe-11-advanced-techniques"
  ],
  "prerequisites": [
    "PE-05: Chain-of-Thought Reasoning"
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

# PE-11-ADVANCED-TECHNIQUES: Advanced Prompting Techniques

## Introduction

Self-consistency, generated knowledge, tree-of-thought and ReAct-style scaffolding. By the end of this lesson you will be able to: Apply self-consistency sampling; Use generated-knowledge prompting; Describe tree-of-thought search; Combine prompts with tool actions (ReAct).

## Key Concepts

### 1. Apply self-consistency sampling

Target: Apply self-consistency sampling. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

# Self-consistency: sample many, take the majority
answers = ["42", "42", "43", "42", "45"]
majority = max(set(answers), key=answers.count)
print("self-consistent answer:", majority)
```
### 2. Use generated-knowledge prompting

Target: Use generated-knowledge prompting. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("generated knowledge: ask the model for facts first, then answer")
```
### 3. Describe tree-of-thought search

Target: Describe tree-of-thought search. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("tree-of-thought: branch and evaluate reasoning paths")
```
### 4. Combine prompts with tool actions (ReAct)

Target: Combine prompts with tool actions (ReAct). Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("ReAct: alternate reasoning with tool use")
```

## Practice Questions

1. What is the key idea behind "Advanced Prompting Techniques"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Advanced Prompting Techniques with analogies and real-world examples"
1. "Show me common mistakes beginners make with Advanced Prompting Techniques"
1. "Provide advanced patterns and performance considerations for Advanced Prompting Techniques"

## Key Takeaways

- Master the core ideas of Advanced Prompting Techniques through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
