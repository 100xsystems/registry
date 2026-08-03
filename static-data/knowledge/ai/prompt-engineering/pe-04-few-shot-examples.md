---
{
  "title": "Few-Shot Examples",
  "description": "Teach by demonstration: a handful of examples beat paragraphs of description.",
  "type": "lesson",
  "order": 4,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Choose examples that cover edge cases",
    "Format few-shot pairs correctly",
    "Avoid label leakage",
    "Tune the number of examples"
  ],
  "knowledge_refs": [
    "prompt-engineering/pe-04-few-shot-examples"
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

# PE-04-FEW-SHOT-EXAMPLES: Few-Shot Examples

## Introduction

Teach by demonstration: a handful of examples beat paragraphs of description. By the end of this lesson you will be able to: Choose examples that cover edge cases; Format few-shot pairs correctly; Avoid label leakage; Tune the number of examples.

## Key Concepts

### 1. Choose examples that cover edge cases

Target: Choose examples that cover edge cases. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
examples = """
Input: "I love this"
Label: positive

Input: "hate it"
Label: negative

Input: "meh"
Label: neutral

Input: "fantastic!"
Label:"""
print(examples)
```
### 2. Format few-shot pairs correctly

Target: Format few-shot pairs correctly. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("cover edge cases: ambiguous, short, sarcastic inputs")
```
### 3. Avoid label leakage

Target: Avoid label leakage. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("consistent formatting matters more than perfect wording")
```
### 4. Tune the number of examples

Target: Tune the number of examples. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("too few -> drift. too many -> tokens + confusion")
```

## Practice Questions

1. What is the key idea behind "Few-Shot Examples"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Few-Shot Examples with analogies and real-world examples"
1. "Show me common mistakes beginners make with Few-Shot Examples"
1. "Provide advanced patterns and performance considerations for Few-Shot Examples"

## Key Takeaways

- Master the core ideas of Few-Shot Examples through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
