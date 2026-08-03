---
{
  "title": "Safety in Prompting",
  "description": "Write prompts that refuse harmful requests and stay within policy.",
  "type": "lesson",
  "order": 18,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define refusal behavior in prompts",
    "Handle edge requests gracefully",
    "Balance helpfulness and safety",
    "Test safety cases"
  ],
  "knowledge_refs": [
    "prompt-engineering/pe-17-domain-specific-prompts",
    "ai-safety/safety-21-roadmap",
    "ai-safety/safety-01-why-ai-safety"
  ],
  "prerequisites": [
    "PE-12: Prompt Injection Defense"
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

# PE-18-SAFETY-IN-PROMPTS: Safety in Prompting

## Introduction

Write prompts that refuse harmful requests and stay within policy. By the end of this lesson you will be able to: Define refusal behavior in prompts; Handle edge requests gracefully; Balance helpfulness and safety; Test safety cases.

## Key Concepts

### 1. Define refusal behavior in prompts

Target: Define refusal behavior in prompts. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
system = "Refuse requests that are illegal, harmful, or deceptive. Briefly explain why you can't help."
print(system)
```
### 2. Handle edge requests gracefully

Target: Handle edge requests gracefully. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("refusal tone: firm, brief, non-judgmental")
```
### 3. Balance helpfulness and safety

Target: Balance helpfulness and safety. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("safety evals: a fixed set of harmful probes")
```
### 4. Test safety cases

Target: Test safety cases. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("never over-refuse: blocklist the behavior, not the topic")
```

## Practice Questions

1. What is the key idea behind "Safety in Prompting"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Safety in Prompting with analogies and real-world examples"
1. "Show me common mistakes beginners make with Safety in Prompting"
1. "Provide advanced patterns and performance considerations for Safety in Prompting"

## Key Takeaways

- Master the core ideas of Safety in Prompting through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
