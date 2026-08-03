---
{
  "title": "Working with LLM APIs",
  "description": "Chat completions, parameters, streaming and structured outputs — the daily API toolkit.",
  "type": "lesson",
  "order": 3,
  "duration": "55 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Call chat completion APIs",
    "Tune temperature, max tokens and top-p",
    "Stream responses",
    "Parse structured outputs"
  ],
  "knowledge_refs": [
    "llm-engineering/llm-02-llm-architecture-review",
    "generative-ai/genai-06-llm-architecture",
    "mlops/mlops-10-model-serving"
  ],
  "prerequisites": [
    "LLM-01: What Is LLM Engineering?"
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

# LLM-03-LLM-APIS: Working with LLM APIs

## Introduction

Chat completions, parameters, streaming and structured outputs — the daily API toolkit. By the end of this lesson you will be able to: Call chat completion APIs; Tune temperature, max tokens and top-p; Stream responses; Parse structured outputs.

## Key Concepts

### 1. Call chat completion APIs

Target: Call chat completion APIs. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from openai import OpenAI

client = OpenAI()
res = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say hello in one word"}],
    max_tokens=10,
)
print(res.choices[0].message.content)
```
### 2. Tune temperature, max tokens and top-p

Target: Tune temperature, max tokens and top-p. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from openai import OpenAI

client = OpenAI()
stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Count 1 to 3"}],
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
print()
```
### 3. Stream responses

Target: Stream responses. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import json

# Request JSON output
prompt = 'Return JSON: {"city": string, "temp": number}'
print(prompt)
```
### 4. Parse structured outputs

Target: Parse structured outputs. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
from openai import OpenAI

client = OpenAI()
res = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Summarize in one sentence: ML is hard"}],
    temperature=0.2,
)
print(res.choices[0].message.content)
```

## Practice Questions

1. What is the key idea behind "Working with LLM APIs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Working with LLM APIs with analogies and real-world examples"
1. "Show me common mistakes beginners make with Working with LLM APIs"
1. "Provide advanced patterns and performance considerations for Working with LLM APIs"

## Key Takeaways

- Master the core ideas of Working with LLM APIs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
