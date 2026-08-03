---
{
  "title": "Embeddings & Vector Databases",
  "description": "Semantic search at scale: embedding models, vector indexes, and ANN search.",
  "type": "lesson",
  "order": 11,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Generate text embeddings",
    "Measure semantic similarity",
    "Index vectors with ANN (HNSW, FAISS)",
    "Evaluate retrieval quality"
  ],
  "knowledge_refs": [
    "generative-ai/genai-11-embeddings-and-vector-databases"
  ],
  "prerequisites": [
    "GENAI-10: Retrieval-Augmented Generation (RAG)"
  ],
  "references": [
    {
      "title": "Hugging Face NLP Course",
      "url": "https://huggingface.co/learn/nlp-course",
      "description": "Transformers, fine-tuning and LLM fundamentals with hands-on code."
    },
    {
      "title": "OpenAI Documentation",
      "url": "https://platform.openai.com/docs",
      "description": "API reference for GPT models, embeddings and function calling."
    },
    {
      "title": "Attention Is All You Need",
      "url": "https://arxiv.org/abs/1706.03762",
      "description": "The Transformer paper that made generative AI possible."
    },
    {
      "title": "LangChain Documentation",
      "url": "https://python.langchain.com/docs",
      "description": "Frameworks for RAG, agents and LLM applications."
    },
    {
      "title": "DeepLearning.AI Short Courses",
      "url": "https://www.deeplearning.ai/short-courses/",
      "description": "Practical AI courses from industry experts."
    }
  ]
}
---

# GENAI-11-EMBEDDINGS-AND-VECTOR-DATABASES: Embeddings & Vector Databases

## Introduction

Semantic search at scale: embedding models, vector indexes, and ANN search. By the end of this lesson you will be able to: Generate text embeddings; Measure semantic similarity; Index vectors with ANN (HNSW, FAISS); Evaluate retrieval quality.

## Key Concepts

### 1. Generate text embeddings

Target: Generate text embeddings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from openai import OpenAI

client = OpenAI()
vec = client.embeddings.create(model="text-embedding-3-small", input=["hello world"])
print("embedding dim:", len(vec.data[0].embedding))
```
### 2. Measure semantic similarity

Target: Measure semantic similarity. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

def cos(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

print("similarity:", round(cos(np.array([1, 0]), np.array([0.9, 0.1])), 3))
```
### 3. Index vectors with ANN (HNSW, FAISS)

Target: Index vectors with ANN (HNSW, FAISS). Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import faiss

index = faiss.IndexFlatL2(384)
index.add(np.random.default_rng(0).normal(size=(1000, 384)).astype("float32"))
dists, idxs = index.search(np.random.default_rng(1).normal(size=(1, 384)).astype("float32"), k=5)
print("top-5 ids:", idxs[0])
```
### 4. Evaluate retrieval quality

Target: Evaluate retrieval quality. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Retrieval quality: hits@k on labeled queries
queries = np.random.default_rng(0).normal(size=(10, 384)).astype("float32")
print("evaluate hits@k on a labeled set")
```

## Practice Questions

1. What is the key idea behind "Embeddings & Vector Databases"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Embeddings & Vector Databases with analogies and real-world examples"
1. "Show me common mistakes beginners make with Embeddings & Vector Databases"
1. "Provide advanced patterns and performance considerations for Embeddings & Vector Databases"

## Key Takeaways

- Master the core ideas of Embeddings & Vector Databases through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
