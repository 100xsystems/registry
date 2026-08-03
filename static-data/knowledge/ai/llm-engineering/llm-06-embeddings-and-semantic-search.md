---
{
  "title": "Embeddings & Semantic Search",
  "description": "Turn text into vectors and search by meaning — the retrieval backbone of LLM apps.",
  "type": "lesson",
  "order": 6,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Generate text embeddings",
    "Measure semantic similarity",
    "Index and query vectors",
    "Evaluate retrieval quality"
  ],
  "knowledge_refs": [
    "llm-engineering/llm-06-embeddings-and-semantic-search"
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

# LLM-06-EMBEDDINGS-AND-SEMANTIC-SEARCH: Embeddings & Semantic Search

## Introduction

Turn text into vectors and search by meaning — the retrieval backbone of LLM apps. By the end of this lesson you will be able to: Generate text embeddings; Measure semantic similarity; Index and query vectors; Evaluate retrieval quality.

## Key Concepts

### 1. Generate text embeddings

Target: Generate text embeddings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from openai import OpenAI

client = OpenAI()
vec = client.embeddings.create(model="text-embedding-3-small", input=["deep learning rocks"])
print("dim:", len(vec.data[0].embedding))
```
### 2. Measure semantic similarity

Target: Measure semantic similarity. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

print("similarity:", round(cosine(np.array([1, 0]), np.array([0.99, 0.1])), 3))
```
### 3. Index and query vectors

Target: Index and query vectors. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import faiss

index = faiss.IndexFlatIP(384)
print("vector index ready")
```
### 4. Evaluate retrieval quality

Target: Evaluate retrieval quality. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("evaluate: does the top-5 contain the right document?")
```

## Practice Questions

1. What is the key idea behind "Embeddings & Semantic Search"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Embeddings & Semantic Search with analogies and real-world examples"
1. "Show me common mistakes beginners make with Embeddings & Semantic Search"
1. "Provide advanced patterns and performance considerations for Embeddings & Semantic Search"

## Key Takeaways

- Master the core ideas of Embeddings & Semantic Search through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
