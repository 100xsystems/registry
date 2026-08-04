---
slug: genai-11-embeddings-and-vector-databases
title: "Embeddings & Vector Databases"
description: "Turning text into numbers for similarity search — the infrastructure powering RAG, recommendations, and semantic search."
order: 11
tags:
  - generative-ai
  - embeddings
  - vector-databases
  - similarity-search
  - rag
prerequisites:
  - genai-10-rag
  - genai-06-llm-architecture
references:
  - title: "Understanding Vector Databases (Microsoft Learn)"
    url: "https://learn.microsoft.com/en-us/data-engineering/playbook/solutions/vector-database/"
    description: "Microsoft's comprehensive guide to vector database concepts"
  - title: "Best Vector Databases Comparison (Encore)"
    url: "https://encore.dev/articles/best-vector-databases"
    description: "Detailed comparison of Pinecone, Weaviate, Qdrant, Chroma, Milvus"
  - title: "A Deep Dive Into Vector Databases (SingleStore)"
    url: "https://www.singlestore.com/blog/a-complete-guide-to-vector-databases/"
    description: "Technical deep dive into vector database architectures"
  - title: "Learning Transferable Visual Models (CLIP Paper)"
    url: "https://arxiv.org/abs/2103.00020"
    description: "Radford et al.'s CLIP paper establishing contrastive text-image embeddings"
  - title: "Sentence-BERT: Semantic Embeddings (Reimers & Gurevych)"
    url: "https://arxiv.org/abs/1908.10084"
    description: "The paper that made sentence embeddings practical for semantic search"
knowledge_refs:
  - genai-10-rag
  - genai-06-llm-architecture
  - genai-13-diffusion-models
---

# Embeddings & Vector Databases

Embeddings convert text, images, or other data into dense numerical vectors that capture semantic meaning. Vector databases store and search these embeddings at scale — enabling similarity search, RAG, and recommendations.

## What Are Embeddings?

An embedding maps high-dimensional discrete data (words, sentences, images) to a lower-dimensional continuous vector space where semantic similarity is captured by geometric proximity:

```
"king"   → [0.2, 0.8, -0.1, 0.5, ...]  (768 dimensions)
"queen"  → [0.3, 0.7, -0.2, 0.6, ...]  (close to "king")
"banana" → [-0.5, 0.1, 0.9, -0.3, ...] (far from "king")
```

**Key property**: Similar meanings → nearby vectors. Different meanings → distant vectors.

## Types of Embeddings

| Type | Model | Use Case |
|---|---|---|
| **Text** | OpenAI text-embedding-3, sentence-transformers | Semantic search, RAG |
| **Image** | CLIP ViT, DINOv2 | Image search, multi-modal |
| **Code** | CodeBERT, StarCoder embeddings | Code search |
| **Multimodal** | CLIP, SigLIP | Cross-modal retrieval |

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode([
    "What is machine learning?",
    "How does deep learning work?",
    "Best pizza restaurants in NYC"
])
# First two are close, third is far away
```

## Similarity Metrics

| Metric | Formula | Best For |
|---|---|---|
| **Cosine Similarity** | $\cos(\mathbf{a}, \mathbf{b}) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|}$ | Text search (most common) |
| **Euclidean Distance** | $\|\mathbf{a} - \mathbf{b}\|_2$ | When magnitude matters |
| **Dot Product** | $\mathbf{a} \cdot \mathbf{b}$ | When vectors are normalized |

```python
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
```

## Vector Indexing Algorithms

### Exact Search (KNN)
- Brute-force: compare query against every vector
- $O(N)$ complexity — too slow for millions of vectors
- Only feasible for small datasets (< 100K)

### Approximate Nearest Neighbor (ANN)

**HNSW (Hierarchical Navigable Small World)** — Most popular:
- Multi-layer graph structure
- Fast traversal from coarse to fine layers
- Excellent recall-speed tradeoff
- Used by: Qdrant, Weaviate, Milvus, pgvector

**IVF (Inverted File Index)**:
- Partition vectors into clusters
- Search only relevant clusters
- Often combined with Product Quantization (PQ) for compression
- Used by: Milvus, FAISS

**Product Quantization (PQ)**:
- Compress vectors by splitting into sub-vectors
- Each sub-vector quantized to nearest centroid
- 4-32x memory reduction
- Used by: FAISS, Milvus

## Vector Database Comparison

| Database | Type | Open Source | Best Scale | Standout Feature |
|---|---|---|---|---|
| **Pinecone** | Managed SaaS | No | Billions | Zero-ops serverless |
| **Weaviate** | Self-hosted/Cloud | Yes | 100M+ | Built-in vectorization |
| **Qdrant** | Self-hosted/Cloud | Yes | 100M+ | Rust performance, payload filtering |
| **Milvus** | Distributed | Yes | Billions | Enterprise scale, GPU indexing |
| **Chroma** | Embedded | Yes | 100K+ | Simple, local prototyping |
| **pgvector** | PostgreSQL ext | Yes | Millions | Embeddings alongside SQL data |
| **FAISS** | Library | Yes | Billions | Facebook's research library |

## Building a Vector Search Pipeline

```python
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# 1. Load and chunk documents
loader = PyPDFLoader("docs.pdf")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)

# 2. Create embeddings and store
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(chunks, embeddings)

# 3. Search
results = vectorstore.similarity_search("What is transformer architecture?", k=5)

# 4. Search with scores
results_with_scores = vectorstore.similarity_search_with_score("query", k=5)
```

## Advanced Techniques

### Hybrid Search (Dense + Sparse)
Combine semantic embeddings with keyword search:
```python
from langchain.retrievers import EnsembleRetriever

bm25 = BM25Retriever.from_documents(chunks)
dense = vectorstore.as_retriever()

ensemble = EnsembleRetriever(
    retrievers=[bm25, dense],
    weights=[0.3, 0.7]
)
```

### Reranking
Use a cross-encoder for higher precision:
```python
from sentence_transformers import CrossEncoder

reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
scores = reranker.predict([(query, doc.page_content) for doc in results])
```

### Multi-tenancy
Filter vectors by metadata (user, organization, document type):
```python
results = vectorstore.similarity_search(
    "query",
    filter={"user_id": "user_123"},
    k=5
)
```

## Embedding Model Selection

| Model | Dimensions | Speed | Quality | Cost |
|---|---|---|---|---|
| text-embedding-3-small (OpenAI) | 1536 | Fast | Good | $0.02/1M tokens |
| text-embedding-3-large (OpenAI) | 3072 | Fast | Best | $0.13/1M tokens |
| all-MiniLM-L6-v2 (SBERT) | 384 | Very fast | Good | Free (local) |
| bge-large-en-v1.5 (BAAI) | 1024 | Fast | Excellent | Free (local) |
| cohere-embed-v3 | 1024 | Fast | Excellent | $0.1/1M tokens |

## Practical Tips

1. **Normalize embeddings** for cosine similarity
2. **Chunk size matters**: Too small = no context, too large = diluted relevance
3. **Use hybrid search** for best retrieval quality
4. **Reranking** adds 20-30% precision for 2x latency
5. **Monitor embedding drift** — model updates change embedding space
6. **Start with Chroma** for prototyping, migrate to Qdrant/Pinecone for production

## Further Reading

- Microsoft's vector database guide is the best conceptual introduction
- Encore's comparison helps choose the right database
- CLIP paper established the foundation for multimodal embeddings
- Sentence-BERT made practical semantic search possible
