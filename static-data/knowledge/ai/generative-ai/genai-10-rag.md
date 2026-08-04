---
slug: genai-10-rag
title: "Retrieval-Augmented Generation (RAG)"
description: "Connecting LLMs to external knowledge — the architecture that grounds AI responses in real documents."
order: 10
tags:
  - generative-ai
  - rag
  - retrieval
  - vector-databases
  - embeddings
prerequisites:
  - genai-06-llm-architecture
  - genai-11-embeddings-and-vector-databases
  - genai-04-prompt-engineering
references:
  - title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
    url: "https://arxiv.org/abs/2005.11401"
    description: "Lewis et al.'s original RAG paper from Meta AI"
  - title: "Building RAG Applications (LangChain)"
    url: "https://python.langchain.com/docs/tutorials/rag/"
    description: "Practical tutorial on building RAG systems with LangChain"
  - title: "Advanced RAG Techniques (Pinecone)"
    url: "https://www.pinecone.io/learn/series/langchain/langchain-retrieval-augmentation/"
    description: "Comprehensive guide to advanced RAG architectures"
  - title: "Chunking Strategies for RAG (LangChain)"
    url: "https://python.langchain.com/docs/how_to/recursive_text_splitter/"
    description: "Guide to document chunking strategies for optimal retrieval"
  - title: "Evaluation of RAG Systems"
    url: "https://docs.ragas.io/"
    description: "RAGAS framework for evaluating RAG pipeline quality"
knowledge_refs:
  - genai-11-embeddings-and-vector-databases
  - genai-04-prompt-engineering
  - genai-03-text-generation-basics
---

# Retrieval-Augmented Generation (RAG)

RAG connects LLMs to external knowledge sources, grounding their responses in real documents rather than relying solely on training data. It's the most practical solution for building accurate, up-to-date AI applications.

## The Problem RAG Solves

LLMs have three fundamental limitations:
1. **Knowledge cutoff**: Training data has a cutoff date
2. **Hallucination**: Confidently state false information
3. **No proprietary data**: Can't access your company's documents

RAG addresses all three by retrieving relevant documents before generating a response.

## RAG Architecture

```
User Query
    ↓
┌─────────────────┐
│  Query Embedding  │  Convert query to vector
└─────────────────┘
    ↓
┌─────────────────┐
│  Vector Search    │  Find similar documents
└─────────────────┘
    ↓
┌─────────────────┐
│  Retrieved Docs   │  Top-K relevant chunks
└─────────────────┘
    ↓
┌─────────────────┐
│  Prompt Assembly  │  Combine query + context
└─────────────────┘
    ↓
┌─────────────────┐
│  LLM Generation   │  Generate grounded response
└─────────────────┘
    ↓
Response with citations
```

## Step 1: Document Processing

### Loading Documents
```python
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    CSVLoader,
    WebBaseLoader,
)

# Load PDFs
loader = PyPDFLoader("document.pdf")
documents = loader.load()

# Load web pages
loader = WebBaseLoader("https://example.com/article")
documents = loader.load()
```

### Chunking Strategies

Documents must be split into chunks for retrieval:

| Strategy | Description | Best For |
|---|---|---|
| **Fixed-size** | Split every N characters | Simple, fast |
| **Recursive** | Split on paragraph/sentence boundaries | General use |
| **Semantic** | Split on topic changes | Complex documents |
| **Document-aware** | Split respecting document structure | PDFs, code |
| **Agentic** | Use LLM to determine split points | High-quality retrieval |

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,       # characters per chunk
    chunk_overlap=200,     # overlap between chunks
    separators=["\n\n", "\n", ". ", " "],
)
chunks = splitter.split_documents(documents)
```

**Chunk size guidelines:**
- **500-1000 chars**: Good for factual retrieval
- **1000-2000 chars**: Good for contextual understanding
- **2000+ chars**: Risk of losing focus, but more context

## Step 2: Embedding and Indexing

Convert chunks to vectors and store in a vector database:

```python
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(chunks, embeddings)
```

## Step 3: Retrieval

Find the most relevant chunks for a query:

```python
# Basic similarity search
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}  # return top 5 chunks
)
docs = retriever.invoke("What is RAG?")
```

### Advanced Retrieval Techniques

**Hybrid Search** (combines semantic + keyword):
```python
from langchain.retrievers import EnsembleRetriever
from langchain.retrievers import BM25Retriever

bm25_retriever = BM25Retriever.from_documents(chunks)
vector_retriever = vectorstore.as_retriever()

ensemble = EnsembleRetriever(
    retrievers=[bm25_retriever, vector_retriever],
    weights=[0.3, 0.7]  # 30% keyword, 70% semantic
)
```

**Reranking**: Use a cross-encoder to rerank retrieved results:
```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain_cohere import CohereRerank

compressor = CohereRerank(model="rerank-v3.5", top_n=3)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=retriever
)
```

**Multi-Query Retrieval**: Generate multiple query variations:
```python
from langchain.retrievers.multi_query import MultiQueryRetriever

mq_retriever = MultiQueryRetriever.from_llm(
    retriever=retriever,
    llm=ChatOpenAI(model="gpt-4"),
)
```

## Step 4: Generation

Combine retrieved context with the user query:

```python
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

llm = ChatOpenAI(model="gpt-4", temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # combine all docs into one prompt
    retriever=retriever,
)
answer = qa_chain.invoke("What is RAG?")
```

### Prompt Template for RAG
```
Use the following context to answer the question. If the answer is not 
in the context, say "I don't have enough information to answer this."

Context:
{context}

Question: {question}

Answer:
```

## RAG Evaluation

Key metrics for RAG quality:

| Metric | What It Measures |
|---|---|
| **Faithfulness** | Does the answer follow from the context? |
| **Answer relevance** | Does the answer address the question? |
| **Context relevance** | Are the retrieved documents relevant? |
| **Context recall** | Does the context contain the answer? |

```python
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision

result = evaluate(
    dataset=test_dataset,
    metrics=[faithfulness, answer_relevancy, context_precision],
)
```

## Common RAG Patterns

### Naive RAG
```
Query → Embed → Search → Retrieve → Generate
```
Simple but limited.

### Advanced RAG
```
Query → Rewrite → Embed → Hybrid Search → Rerank → Generate
```
Better retrieval quality.

### Modular RAG
```
Query → Router → [Different pipelines per domain] → Generate
```
Domain-specific routing.

### Agentic RAG
```
Query → Agent → Decide: search, calculate, or generate → Tool use → Response
```
LLM decides when and how to retrieve.

## RAG vs. Fine-Tuning

| Aspect | RAG | Fine-Tuning |
|---|---|---|
| Knowledge | External documents | Encoded in weights |
| Updates | Instant (update docs) | Retrain required |
| Cost | Lower (no training) | Higher (training compute) |
| Hallucination | Reduced (grounded in docs) | Can still hallucinate |
| Latency | Higher (retrieval step) | Lower (direct generation) |
| Best for | Knowledge-intensive tasks | Style/format/behavior |

## Further Reading

- Lewis et al.'s original RAG paper is foundational
- LangChain's tutorials are the best practical starting point
- RAGAS provides comprehensive evaluation metrics
- For production: Pinecone, Weaviate, Qdrant are production-ready vector databases
