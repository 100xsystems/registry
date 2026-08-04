---
slug: llm-06-embeddings-and-semantic-search
title: "Embeddings & Semantic Search"
description: "Converting text to vectors for semantic search — embedding models, similarity metrics, and vector database selection."
order: 6
tags:
  - llm-engineering
  - embeddings
  - semantic-search
  - vector-databases
prerequisites:
  - llm-05-tokenization-and-context
knowledge_refs:
  - llm-05-tokenization-and-context
  - llm-07-rag-engineering
references:
  - title: "OpenAI Embeddings Guide"
    url: "https://platform.openai.com/docs/guides/embeddings"
    notes: "Official guide to text embeddings"
  - title: "Sentence Transformers Documentation"
    url: "https://www.sbert.net/"
    notes: "Open-source embedding models"
  - title: "Weaviate Vector Database"
    url: "https://weaviate.io/"
    notes: "Production vector search engine"
  - title: "Chroma DB"
    url: "https://www.trychroma.com/"
    notes: "Lightweight embedding database"
  - title: "Vector Database Comparison"
    url: "https://superlinked.com/vector-db-comparison"
    notes: "Detailed comparison of vector databases"
---

# Embeddings & Semantic Search

Embeddings convert text into dense numerical vectors that capture meaning. Similar texts produce similar vectors, enabling semantic search that goes beyond keyword matching.

## What Are Embeddings?

An embedding is a fixed-size vector (e.g., 1536 dimensions) that represents the semantic meaning of text:

```python
from openai import OpenAI
client = OpenAI()

response = client.embeddings.create(
    model="text-embedding-3-small",
    input="Machine learning is fascinating"
)
vector = response.data[0].embedding  # 1536 floats
```

### Key Property
Semantic similarity → vector proximity:
- "The cat sat on the mat" → similar vector to "A feline rested on the rug"
- "Python programming" → similar vector to "coding in Python"

## Similarity Metrics

| Metric | Formula | Range | Best For |
|--------|---------|-------|----------|
| Cosine | cos(A,B) = A·B / (‖A‖‖B‖) | [-1, 1] | Most common, normalized vectors |
| Dot Product | A·B | (-∞, ∞) | Pre-normalized vectors |
| Euclidean | ‖A-B‖₂ | [0, ∞) | Geometric distance |

**Cosine similarity** is the default for most vector databases.

## Embedding Models

### OpenAI
- `text-embedding-3-small`: 1536 dims, fast, cheap
- `text-embedding-3-large`: 3072 dims, higher quality
- Supports dimension reduction via `dimensions` parameter

### Open-Source (Sentence Transformers)
- `all-MiniLM-L6-v2`: 384 dims, very fast
- `bge-large-en-v1.5`: 1024 dims, high quality
- `nomic-embed-text-v1`: 768 dims, open-source leader
- Run locally, no API costs

### Cohere
- `embed-english-v3.0`: 1024 dims, optimized for search

## Vector Databases

| Database | Type | Best For |
|----------|------|----------|
| **Chroma** | Embedded | Prototyping, small projects |
| **Pinecone** | Managed | Production, zero-ops |
| **Weaviate** | Self-hosted/managed | Hybrid search, GraphQL API |
| **Qdrant** | Self-hosted | Performance, Rust-based |
| **Milvus** | Self-hosted | Large-scale, distributed |
| **pgvector** | Postgres extension | Teams already using Postgres |

### Choosing a Database
- **Prototype**: Chroma (runs in-process, no setup)
- **Small production**: Pinecone (managed, serverless)
- **Hybrid search**: Weaviate (BM25 + vector)
- **High performance**: Qdrant (Rust, fast)
- **Already have Postgres**: pgvector

## Practical Example

```python
import chromadb

client = chromadb.Client()
collection = client.create_collection("documents")

# Add documents
collection.add(
    documents=["Python is great for ML", "JavaScript powers the web"],
    ids=["doc1", "doc2"]
)

# Semantic search
results = collection.query(
    query_texts=["programming for data science"],
    n_results=1
)
print(results["documents"])  # ["Python is great for ML"]
```

## Key Takeaways

1. Embeddings capture semantic meaning as dense vectors
2. Cosine similarity is the standard metric for comparing embeddings
3. Open-source models (Sentence Transformers) are competitive with commercial APIs
4. Choose vector databases based on scale, features, and existing infrastructure
5. Semantic search goes beyond keyword matching to find conceptually related content
