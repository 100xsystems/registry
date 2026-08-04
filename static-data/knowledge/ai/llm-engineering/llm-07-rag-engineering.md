---
slug: llm-07-rag-engineering
title: "RAG Engineering"
description: "Retrieval-Augmented Generation — building production RAG pipelines with chunking, retrieval, reranking, and faithfulness."
order: 7
tags:
  - llm-engineering
  - rag
  - retrieval
  - chunking
prerequisites:
  - llm-06-embeddings-and-semantic-search
  - llm-04-prompting-systems
knowledge_refs:
  - llm-06-embeddings-and-semantic-search
  - llm-04-prompting-systems
  - llm-08-advanced-rag
references:
  - title: "RAG from Scratch (LangChain)"
    url: "https://github.com/langchain-ai/rag-from-scratch"
    notes: "Step-by-step RAG implementation"
  - title: "Chunking Strategies for LLMs"
    url: "https://www.pinecone.io/learn/chunking-strategies/"
    notes: "Comprehensive chunking comparison"
  - title: "RAGAS Evaluation Framework"
    url: "https://docs.ragas.io/"
    notes: "RAG evaluation metrics"
  - title: "Hybrid Search Explained"
    url: "https://docs.weaviate.io/weaviate/search/hybrid"
    notes: "Combining BM25 and vector search"
  - title: "ColBERT Reranking"
    url: "https://arxiv.org/abs/2004.12832"
    notes: "Neural reranking for improved retrieval"
---

# RAG Engineering

Retrieval-Augmented Generation (RAG) grounds LLM responses in real data by retrieving relevant documents before generating answers. It's the most important pattern in production LLM applications.

## The RAG Pipeline

```
User Query → Embedding → Retrieval → Reranking → Context Assembly → LLM Generation
                ↓            ↓            ↓              ↓                ↓
          Query vector   Top-k docs   Rerank by     Prompt with      Generate
                         from DB      relevance     retrieved docs   answer
```

## Document Processing

### Chunking Strategies

| Strategy | How It Works | Best For |
|----------|-------------|----------|
| **Fixed-size** | Split every N characters/tokens | Simple, predictable |
| **Recursive** | Split on paragraphs, then sentences | Structured documents |
| **Semantic** | Split when topic changes | Varied content |
| **Document-based** | Split on headers, sections | Technical docs |

### Chunk Size Guidelines
- **Small chunks (256 tokens)**: High precision, may lose context
- **Large chunks (1024 tokens)**: Good context, may include noise
- **Optimal**: 512-768 tokens with 50-100 token overlap

### Metadata Enrichment
```python
chunk.metadata = {
    "source": "technical-doc.pdf",
    "page": 42,
    "section": "Configuration",
    "last_updated": "2024-01-15"
}
```

## Retrieval

### Dense Retrieval
- Embed query and documents with same model
- Cosine similarity ranking
- Captures semantic meaning

### Sparse Retrieval (BM25)
- Keyword-based matching
- Handles exact terms well (names, codes, acronyms)

### Hybrid Search
Combine dense + sparse for best results:
```python
results = collection.query(
    query_texts=["Python error handling"],
    vector_search_weight=0.7,  # dense
    bm25_search_weight=0.3     # sparse
)
```

## Reranking

First-pass retrieval finds candidates; reranking refines:

```python
from sentence_transformers import CrossEncoder

reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
scores = reranker.predict([
    (query, doc1), (query, doc2), (query, doc3)
])
# Sort by score for final ranking
```

Rerankers use cross-attention (more accurate but slower) vs bi-encoders (faster but less precise).

## Context Assembly

Combine retrieved chunks into the prompt:

```python
context = "\n\n".join([
    f"Source {i+1}: {chunk.text}"
    for i, chunk in enumerate(retrieved_chunks)
])

prompt = f"""Answer the question based on the provided context.

Context:
{context}

Question: {query}

Answer:"""
```

### Best Practices
- Limit context to stay within token budget
- Include source attribution
- Sort by relevance (most relevant first)
- Add instructions for handling insufficient context

## Evaluation

| Metric | What It Measures |
|--------|-----------------|
| **Context Precision** | Are retrieved docs relevant? |
| **Context Recall** | Are all relevant docs retrieved? |
| **Faithfulness** | Is the answer grounded in context? |
| **Answer Relevance** | Does the answer address the query? |

## Key Takeaways

1. RAG grounds LLM responses in real data, reducing hallucination
2. Chunking strategy significantly impacts retrieval quality
3. Hybrid search (dense + sparse) outperforms either alone
4. Reranking improves precision after initial retrieval
5. Evaluate both retrieval quality and generation faithfulness
