---
{
  "title": "Advanced RAG",
  "description": "Hybrid search, reranking, query rewriting and contextual compression for better answers.",
  "type": "lesson",
  "order": 8,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Combine keyword and vector search (hybrid)",
    "Rerank candidates with cross-encoders",
    "Rewrite queries before retrieval",
    "Compress retrieved context"
  ],
  "knowledge_refs": [
    "llm-engineering/llm-08-advanced-rag"
  ],
  "prerequisites": [
    "LLM-07: RAG Engineering"
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

# LLM-08-ADVANCED-RAG: Advanced RAG

## Introduction

Hybrid search, reranking, query rewriting and contextual compression for better answers. By the end of this lesson you will be able to: Combine keyword and vector search (hybrid); Rerank candidates with cross-encoders; Rewrite queries before retrieval; Compress retrieved context.

## Key Concepts

### 1. Combine keyword and vector search (hybrid)

Target: Combine keyword and vector search (hybrid). Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

# Hybrid: blend BM25 + vector scores
bm25 = np.array([0.6, 0.2, 0.1])
vector = np.array([0.4, 0.8, 0.3])
hybrid = 0.5 * bm25 + 0.5 * vector
print("hybrid scores:", hybrid.round(2))
```
### 2. Rerank candidates with cross-encoders

Target: Rerank candidates with cross-encoders. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from sentence_transformers import CrossEncoder

reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
print("reranker ready")
```
### 3. Rewrite queries before retrieval

Target: Rewrite queries before retrieval. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("query rewriting: turn a vague question into a searchable one")
```
### 4. Compress retrieved context

Target: Compress retrieved context. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("compression: keep only the sentences that answer the question")
```

## Practice Questions

1. What is the key idea behind "Advanced RAG"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Advanced RAG with analogies and real-world examples"
1. "Show me common mistakes beginners make with Advanced RAG"
1. "Provide advanced patterns and performance considerations for Advanced RAG"

## Key Takeaways

- Master the core ideas of Advanced RAG through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
