---
{
  "title": "Function Calling & Structured Outputs",
  "description": "Let the model call your tools with typed arguments — reliably.",
  "type": "lesson",
  "order": 10,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define tools with JSON schemas",
    "Handle tool-call responses",
    "Validate arguments before executing",
    "Use structured output modes"
  ],
  "knowledge_refs": [
    "llm-engineering/llm-09-fine-tuning-practice",
    "prompt-engineering/pe-06-structured-outputs",
    "ai-agents/agents-03-tool-use"
  ],
  "prerequisites": [
    "LLM-03: Working with LLM APIs"
  ],
  "references": [
    {
      "title": "OpenAI Platform Docs",
      "url": "https://platform.openai.com/docs",
      "description": "API reference for chat, embeddings, function calling and vision."
    },
    {
      "title": "Anthropic Documentation",
      "url": "https://docs.anthropic.com/",
      "description": "Claude API docs including prompt engineering guides."
    },
    {
      "title": "Hugging Face Transformers",
      "url": "https://huggingface.co/docs/transformers",
      "description": "Models, tokenizers and pipelines for LLM work."
    },
    {
      "title": "LangChain Documentation",
      "url": "https://python.langchain.com/docs",
      "description": "Frameworks for RAG, agents and LLM applications."
    },
    {
      "title": "vLLM Documentation",
      "url": "https://docs.vllm.ai/",
      "description": "High-throughput LLM serving and inference."
    }
  ]
}
---

# LLM-10-FUNCTION-CALLING: Function Calling & Structured Outputs

## Introduction

Let the model call your tools with typed arguments — reliably. By the end of this lesson you will be able to: Define tools with JSON schemas; Handle tool-call responses; Validate arguments before executing; Use structured output modes.

## Key Concepts

### 1. Define tools with JSON schemas

Target: Define tools with JSON schemas. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from openai import OpenAI

client = OpenAI()
res = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Weather in Paris?"}],
    tools=[{
        "type": "function",
        "function": {
            "name": "get_weather",
            "parameters": {"type": "object", "properties": {"city": {"type": "string"}}, "required": ["city"]},
        },
    }],
)
tool_calls = res.choices[0].message.tool_calls
print("tool call:", tool_calls[0].function.name if tool_calls else None)
```
### 2. Handle tool-call responses

Target: Handle tool-call responses. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import json

args = json.loads('{"city": "Paris"}')
assert isinstance(args["city"], str)
print("validated args:", args)
```
### 3. Validate arguments before executing

Target: Validate arguments before executing. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("execute the tool, then return the result as a message")
```
### 4. Use structured output modes

Target: Use structured output modes. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("structured output: force JSON schema conformance")
```

## Practice Questions

1. What is the key idea behind "Function Calling & Structured Outputs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Function Calling & Structured Outputs with analogies and real-world examples"
1. "Show me common mistakes beginners make with Function Calling & Structured Outputs"
1. "Provide advanced patterns and performance considerations for Function Calling & Structured Outputs"

## Key Takeaways

- Master the core ideas of Function Calling & Structured Outputs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
