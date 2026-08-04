---
slug: llm-05-tokenization-and-context
title: "Tokenization & Context Management"
description: "Understanding how LLMs process text — BPE tokenization, context windows, and strategies for managing long conversations."
order: 5
tags:
  - llm-engineering
  - tokenization
  - context-window
  - bpe
prerequisites:
  - llm-03-llm-apis
  - llm-02-llm-architecture-review
knowledge_refs:
  - llm-03-llm-apis
  - llm-02-llm-architecture-review
  - llm-06-embeddings-and-semantic-search
references:
  - title: "Hugging Face BPE Tokenization"
    url: "https://huggingface.co/learn/llm-course/en/chapter6/5"
    notes: "In-depth BPE algorithm explanation"
  - title: "tiktoken Repository"
    url: "https://github.com/openai/tiktoken"
    notes: "OpenAI's fast BPE tokenizer"
  - title: "Context Window Management Strategies"
    url: "https://www.getmaxim.ai/articles/context-window-management-strategies-for-long-context-ai-agents-and-chatbots/"
    notes: "Practical context management patterns"
  - title: "Lost in the Middle"
    url: "https://arxiv.org/abs/2307.03172"
    notes: "Research on attention distribution in long contexts"
  - title: "Sebastian Raschka: BPE From Scratch"
    url: "https://sebastianraschka.com/blog/2025/bpe-from-scratch.html"
    notes: "Implementing BPE tokenization"
---

# Tokenization & Context Management

Tokens are the atomic unit of LLM processing. Understanding tokenization and context management is essential for cost control, performance optimization, and building reliable applications.

## What Is a Token?

A token is not a word, character, or byte — it's a **subword unit** determined by the tokenizer:

- "hello" → 1 token
- "unbelievable" → 3 tokens ("un", "believ", "able")
- "🤖" → 1-2 tokens (depending on tokenizer)
- "def function_name():" → 5 tokens

**Rule of thumb**: 1 token ≈ 0.75 English words, or ~4 characters.

## Byte Pair Encoding (BPE)

BPE is the dominant tokenization algorithm:

1. Start with individual bytes as base vocabulary
2. Find most frequent adjacent pair in corpus
3. Merge that pair into a new token
4. Repeat until desired vocabulary size reached

### Why BPE?
- No unknown tokens (every byte sequence is representable)
- Balances character-level (too many tokens) vs word-level (too many words)
- Common words get single tokens; rare words decompose

### tiktoken
OpenAI's fast BPE implementation in Rust:
```python
import tiktoken
enc = tiktoken.encoding_for_model("gpt-4o")
tokens = enc.encode("Hello, world!")
print(len(tokens))  # 6
print(enc.decode(tokens))  # "Hello, world!"
```

## Context Windows

The context window is the maximum tokens a model can process:
- GPT-4o: 128K tokens
- Claude 3.5: 200K tokens
- Llama 3.1: 128K tokens
- Gemini 1.5 Pro: 2M tokens

### Cost Implications
- Input tokens are cheaper than output tokens
- Cache hits reduce cost by up to 90%
- Every token in context costs money

## Context Compression Strategies

### Sliding Window
Keep only the last N messages:
```python
def sliding_window(messages, max_messages=20):
    system = messages[0]  # always keep system prompt
    recent = messages[-max_messages:]
    return [system] + recent
```
- **Pros**: Simple, predictable memory usage
- **Cons**: "Digital amnesia" — old context lost entirely

### Summarization Compression
Periodically summarize older conversation blocks:
```python
def summarize_and_compress(messages, threshold=30):
    if len(messages) > threshold:
        old = messages[1:threshold]
        summary = llm.summarize(old)
        return [messages[0], {"role": "system", "content": summary}] + messages[threshold:]
    return messages
```
- **Pros**: Preserves key information
- **Cons**: Loses fine-grained details

### RAG-Based Memory
Store full conversation in vector database, retrieve relevant turns:
```python
def rag_memory(query, conversation_db):
    relevant = conversation_db.search(query, top_k=5)
    return format_context(relevant)
```
- **Pros**: Full history available, semantic retrieval
- **Cons**: Adds latency and infrastructure complexity

## The "Lost in the Middle" Problem

Research shows LLMs struggle to use information placed in the middle of long contexts. They perform best with information at the beginning or end.

**Mitigation strategies:**
- Put most important information first
- Use retrieval to bring relevant context to the front
- For very long documents, chunk and process separately

## Key Takeaways

1. Tokens are subword units — 1 token ≈ 0.75 words
2. BPE tokenization ensures no unknown tokens
3. Context windows are limited and expensive — manage them carefully
4. Sliding window, summarization, and RAG are the main compression strategies
5. "Lost in the middle" means important context should be placed at the start or end
