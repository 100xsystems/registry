---
{
  "title": "Guardrails & Safety for LLM Apps",
  "description": "Prompt injection, moderation, PII redaction and output filtering.",
  "type": "lesson",
  "order": 14,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand prompt injection attacks",
    "Apply input and output moderation",
    "Redact PII",
    "Sandbox tool execution"
  ],
  "knowledge_refs": [
    "llm-engineering/llm-13-evaluating-llm-systems",
    "ai-safety/safety-21-roadmap",
    "ai-safety/safety-12-guardrails"
  ],
  "prerequisites": [
    "LLM-10: Function Calling & Structured Outputs"
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

# LLM-14-GUARDRAILS-AND-SAFETY: Guardrails & Safety for LLM Apps

## Introduction

Prompt injection, moderation, PII redaction and output filtering. By the end of this lesson you will be able to: Understand prompt injection attacks; Apply input and output moderation; Redact PII; Sandbox tool execution.

## Key Concepts

### 1. Understand prompt injection attacks

Target: Understand prompt injection attacks. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from openai import OpenAI

client = OpenAI()
res = client.moderations.create(input="user content here")
print("flagged:", res.results[0].flagged)
```
### 2. Apply input and output moderation

Target: Apply input and output moderation. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import re

text = "email: john@example.com"
redacted = re.sub(r"[\w.+-]+@[\w-]+\.[\w.]+", "[REDACTED]", text)
print(redacted)
```
### 3. Redact PII

Target: Redact PII. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("instruction hierarchy: system > user > tool")
```
### 4. Sandbox tool execution

Target: Sandbox tool execution. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("run tools in sandboxes with timeouts and allowlists")
```

## Practice Questions

1. What is the key idea behind "Guardrails & Safety for LLM Apps"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Guardrails & Safety for LLM Apps with analogies and real-world examples"
1. "Show me common mistakes beginners make with Guardrails & Safety for LLM Apps"
1. "Provide advanced patterns and performance considerations for Guardrails & Safety for LLM Apps"

## Key Takeaways

- Master the core ideas of Guardrails & Safety for LLM Apps through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
