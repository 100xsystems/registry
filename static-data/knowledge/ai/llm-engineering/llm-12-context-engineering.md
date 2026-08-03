---
{
  "title": "Context Engineering & Memory",
  "description": "Manage what the model sees: conversation memory, summarization and caching.",
  "type": "lesson",
  "order": 12,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Design conversation memory",
    "Summarize long histories",
    "Cache prompts and completions",
    "Keep context relevant"
  ],
  "knowledge_refs": [
    "llm-engineering/llm-12-context-engineering"
  ],
  "prerequisites": [
    "LLM-05: Tokenization & Context Management"
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

# LLM-12-CONTEXT-ENGINEERING: Context Engineering & Memory

## Introduction

Manage what the model sees: conversation memory, summarization and caching. By the end of this lesson you will be able to: Design conversation memory; Summarize long histories; Cache prompts and completions; Keep context relevant.

## Key Concepts

### 1. Design conversation memory

Target: Design conversation memory. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
messages = [
    {"role": "user", "content": "I want a refund"}, 
    {"role": "assistant", "content": "Order number?"},
]
print("rolling window:", len(messages), "messages")
```
### 2. Summarize long histories

Target: Summarize long histories. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("summarize old turns when the window fills")
```
### 3. Cache prompts and completions

Target: Cache prompts and completions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import hashlib

cache_key = hashlib.sha256(b"same-prompt").hexdigest()
print("cache key:", cache_key[:10])
```
### 4. Keep context relevant

Target: Keep context relevant. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("retrieval + memory = context that stays on-topic")
```

## Practice Questions

1. What is the key idea behind "Context Engineering & Memory"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Context Engineering & Memory with analogies and real-world examples"
1. "Show me common mistakes beginners make with Context Engineering & Memory"
1. "Provide advanced patterns and performance considerations for Context Engineering & Memory"

## Key Takeaways

- Master the core ideas of Context Engineering & Memory through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
