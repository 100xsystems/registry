---
{
  "title": "Domain-Specific Prompting",
  "description": "Legal, medical, finance and education: prompts tuned to domain constraints.",
  "type": "lesson",
  "order": 17,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Adapt prompts to domain rules",
    "Handle regulated content",
    "Set disclaimers and limits",
    "Respect domain terminology"
  ],
  "knowledge_refs": [
    "prompt-engineering/pe-16-prompt-caching",
    "generative-ai/genai-04-prompt-engineering",
    "llm-engineering/llm-04-prompting-systems"
  ],
  "prerequisites": [
    "PE-10: System Prompts in Production"
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

# PE-17-DOMAIN-SPECIFIC-PROMPTS: Domain-Specific Prompting

## Introduction

Legal, medical, finance and education: prompts tuned to domain constraints. By the end of this lesson you will be able to: Adapt prompts to domain rules; Handle regulated content; Set disclaimers and limits; Respect domain terminology.

## Key Concepts

### 1. Adapt prompts to domain rules

Target: Adapt prompts to domain rules. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
legal_prompt = "Summarize this contract clause in plain language. Flag anything about liability. Do not give legal advice."
print(legal_prompt)
```
### 2. Handle regulated content

Target: Handle regulated content. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
med_prompt = "Explain this test result simply. State that a doctor must interpret results. Do not diagnose."
print(med_prompt)
```
### 3. Set disclaimers and limits

Target: Set disclaimers and limits. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("domains with risk: refuse > speculate")
```
### 4. Respect domain terminology

Target: Respect domain terminology. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("glossaries and style guides improve consistency")
```

## Practice Questions

1. What is the key idea behind "Domain-Specific Prompting"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Domain-Specific Prompting with analogies and real-world examples"
1. "Show me common mistakes beginners make with Domain-Specific Prompting"
1. "Provide advanced patterns and performance considerations for Domain-Specific Prompting"

## Key Takeaways

- Master the core ideas of Domain-Specific Prompting through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
