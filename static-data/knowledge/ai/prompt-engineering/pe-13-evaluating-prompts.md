---
{
  "title": "Evaluating Prompts",
  "description": "Turn prompt tweaks into measured improvements with a fixed eval set.",
  "type": "lesson",
  "order": 13,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Build a prompt eval set",
    "Score outputs automatically",
    "A/B test prompt variants",
    "Guard against overfitting to the eval set"
  ],
  "knowledge_refs": [
    "prompt-engineering/pe-13-evaluating-prompts"
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

# PE-13-EVALUATING-PROMPTS: Evaluating Prompts

## Introduction

Turn prompt tweaks into measured improvements with a fixed eval set. By the end of this lesson you will be able to: Build a prompt eval set; Score outputs automatically; A/B test prompt variants; Guard against overfitting to the eval set.

## Key Concepts

### 1. Build a prompt eval set

Target: Build a prompt eval set. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
evals = [
    {"input": "refund policy?", "expected_keywords": ["30 days"]},
    {"input": "shipping time?", "expected_keywords": ["5-7 days"]},
]
print("eval cases:", len(evals))
```
### 2. Score outputs automatically

Target: Score outputs automatically. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
def passes(output, keywords):
    return all(k in output for k in keywords)

print("passes:", passes("You can refund within 30 days.", ["30 days"]))
```
### 3. A/B test prompt variants

Target: A/B test prompt variants. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("run every variant on the same set, compare scores")
```
### 4. Guard against overfitting to the eval set

Target: Guard against overfitting to the eval set. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("refresh evals with real user queries")
```

## Practice Questions

1. What is the key idea behind "Evaluating Prompts"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Evaluating Prompts with analogies and real-world examples"
1. "Show me common mistakes beginners make with Evaluating Prompts"
1. "Provide advanced patterns and performance considerations for Evaluating Prompts"

## Key Takeaways

- Master the core ideas of Evaluating Prompts through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
