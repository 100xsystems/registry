---
{
  "title": "Prompting for Code",
  "description": "Generate, review and debug code with prompts that describe behavior, not just syntax.",
  "type": "lesson",
  "order": 7,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Specify behavior with examples",
    "Request language and style constraints",
    "Ask for tests alongside code",
    "Review code with targeted prompts"
  ],
  "knowledge_refs": [
    "prompt-engineering/pe-07-prompts-for-code"
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

# PE-07-PROMPTS-FOR-CODE: Prompting for Code

## Introduction

Generate, review and debug code with prompts that describe behavior, not just syntax. By the end of this lesson you will be able to: Specify behavior with examples; Request language and style constraints; Ask for tests alongside code; Review code with targeted prompts.

## Key Concepts

### 1. Specify behavior with examples

Target: Specify behavior with examples. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
prompt = """Write a Python function that: \n- takes a list of ints\n- returns the sum of evens\n- raises ValueError on empty input\nInclude docstring and 2 example calls."""
print(prompt)
```
### 2. Request language and style constraints

Target: Request language and style constraints. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("examples in the prompt pin the contract")
```
### 3. Ask for tests alongside code

Target: Ask for tests alongside code. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
code = "def sum_evens(xs):\n    return sum(x for x in xs if x % 2 == 0)"
print(code)
```
### 4. Review code with targeted prompts

Target: Review code with targeted prompts. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
review = "Review this for: off-by-one errors, null safety, and edge cases. Cite line numbers."
print(review)
```

## Practice Questions

1. What is the key idea behind "Prompting for Code"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Prompting for Code with analogies and real-world examples"
1. "Show me common mistakes beginners make with Prompting for Code"
1. "Provide advanced patterns and performance considerations for Prompting for Code"

## Key Takeaways

- Master the core ideas of Prompting for Code through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
