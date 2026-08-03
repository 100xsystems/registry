---
{
  "title": "Structured Outputs",
  "description": "Force JSON, enums and schemas — reliable data out of free-form models.",
  "type": "lesson",
  "order": 6,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Request JSON with explicit schemas",
    "Validate and repair outputs",
    "Use constrained decoding where available",
    "Handle malformed responses"
  ],
  "knowledge_refs": [
    "prompt-engineering/pe-06-structured-outputs"
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

# PE-06-STRUCTURED-OUTPUTS: Structured Outputs

## Introduction

Force JSON, enums and schemas — reliable data out of free-form models. By the end of this lesson you will be able to: Request JSON with explicit schemas; Validate and repair outputs; Use constrained decoding where available; Handle malformed responses.

## Key Concepts

### 1. Request JSON with explicit schemas

Target: Request JSON with explicit schemas. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import json

prompt = 'Return JSON: {"name": string, "age": number}'
raw = '{"name": "Ada", "age": 36}'
data = json.loads(raw)
print(data["name"])
```
### 2. Validate and repair outputs

Target: Validate and repair outputs. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import json

# Repair: retry with the error message
bad = "name: Ada, age: 36"
try:
    json.loads(bad)
except json.JSONDecodeError as e:
    print("repairing ->", json.dumps({"name": "Ada", "age": 36}))
```
### 3. Use constrained decoding where available

Target: Use constrained decoding where available. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("constrained decoding guarantees schema conformance")
```
### 4. Handle malformed responses

Target: Handle malformed responses. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("validate types; never trust raw model output")
```

## Practice Questions

1. What is the key idea behind "Structured Outputs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Structured Outputs with analogies and real-world examples"
1. "Show me common mistakes beginners make with Structured Outputs"
1. "Provide advanced patterns and performance considerations for Structured Outputs"

## Key Takeaways

- Master the core ideas of Structured Outputs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
