---
{
  "title": "Tool Use & Function Calling",
  "description": "Give agents real capabilities with typed tools and safe execution.",
  "type": "lesson",
  "order": 3,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define tools with schemas",
    "Execute tool calls safely",
    "Handle errors and retries",
    "Restrict tools by allowlist"
  ],
  "knowledge_refs": [
    "ai-agents/agents-03-tool-use"
  ],
  "prerequisites": [
    "LLM-10: Function Calling & Structured Outputs"
  ],
  "references": [
    {
      "title": "LangChain Agents",
      "url": "https://python.langchain.com/docs/how_to/#agents",
      "description": "Agent frameworks, tools and memory patterns."
    },
    {
      "title": "OpenAI Agents Documentation",
      "url": "https://platform.openai.com/docs/guides/agents",
      "description": "Function calling and agent loop patterns."
    },
    {
      "title": "ReAct: Synergizing Reasoning and Acting",
      "url": "https://arxiv.org/abs/2210.03629",
      "description": "The paper behind reasoning-acting agent loops."
    },
    {
      "title": "Anthropic — Building Effective Agents",
      "url": "https://www.anthropic.com/research/building-effective-agents",
      "description": "A practical guide to agent architecture."
    },
    {
      "title": "CrewAI Documentation",
      "url": "https://docs.crewai.com/",
      "description": "Multi-agent orchestration framework."
    }
  ]
}
---

# AGENTS-03-TOOL-USE: Tool Use & Function Calling

## Introduction

Give agents real capabilities with typed tools and safe execution. By the end of this lesson you will be able to: Define tools with schemas; Execute tool calls safely; Handle errors and retries; Restrict tools by allowlist.

## Key Concepts

### 1. Define tools with schemas

Target: Define tools with schemas. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
def get_weather(city: str) -> str:
    return f"Weather for {city}: sunny"

tool_schema = {
    "name": "get_weather",
    "parameters": {"type": "object", "properties": {"city": {"type": "string"}}},
}
print(tool_schema)
```
### 2. Execute tool calls safely

Target: Execute tool calls safely. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import json

args = json.loads('{"city": "Paris"}')
result = get_weather(**args)
print("tool result:", result)
```
### 3. Handle errors and retries

Target: Handle errors and retries. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("wrap tools: try/except, timeout, and a clear error message")
```
### 4. Restrict tools by allowlist

Target: Restrict tools by allowlist. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("allowlist: agents may only call approved tools")
```

## Practice Questions

1. What is the key idea behind "Tool Use & Function Calling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Tool Use & Function Calling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Tool Use & Function Calling"
1. "Provide advanced patterns and performance considerations for Tool Use & Function Calling"

## Key Takeaways

- Master the core ideas of Tool Use & Function Calling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
