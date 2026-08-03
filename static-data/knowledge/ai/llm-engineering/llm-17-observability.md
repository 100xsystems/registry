---
{
  "title": "Prompt Versioning & Observability",
  "description": "Trace every request: prompt, tokens, latency, cost and outcome.",
  "type": "lesson",
  "order": 17,
  "duration": "50 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Log full request traces",
    "Tag prompts and model versions",
    "Monitor cost and latency",
    "Correlate feedback with versions"
  ],
  "knowledge_refs": [
    "llm-engineering/llm-17-observability"
  ],
  "prerequisites": [
    "LLM-13: Evaluating LLM Systems"
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

# LLM-17-OBSERVABILITY: Prompt Versioning & Observability

## Introduction

Trace every request: prompt, tokens, latency, cost and outcome. By the end of this lesson you will be able to: Log full request traces; Tag prompts and model versions; Monitor cost and latency; Correlate feedback with versions.

## Key Concepts

### 1. Log full request traces

Target: Log full request traces. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import time

trace = {
    "prompt_version": "v3",
    "model": "gpt-4o-mini",
    "tokens_in": 120,
    "tokens_out": 40,
    "latency_ms": 412,
}
print(trace)
```
### 2. Tag prompts and model versions

Target: Tag prompts and model versions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("every request is replayable for debugging")
```
### 3. Monitor cost and latency

Target: Monitor cost and latency. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("dashboards: cost, latency, error rate by prompt version")
```
### 4. Correlate feedback with versions

Target: Correlate feedback with versions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("user feedback attaches to the exact version served")
```

## Practice Questions

1. What is the key idea behind "Prompt Versioning & Observability"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Prompt Versioning & Observability with analogies and real-world examples"
1. "Show me common mistakes beginners make with Prompt Versioning & Observability"
1. "Provide advanced patterns and performance considerations for Prompt Versioning & Observability"

## Key Takeaways

- Master the core ideas of Prompt Versioning & Observability through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
