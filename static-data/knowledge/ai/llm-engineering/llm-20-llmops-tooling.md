---
slug: llm-20-llmops-tooling
title: "The LLMOps Tooling Landscape"
description: "Navigating the LLMOps ecosystem — frameworks, platforms, and tools for building, deploying, and monitoring LLM applications."
order: 20
tags:
  - llm-engineering
  - llmops
  - tooling
  - platforms
prerequisites:
  - llm-17-observability
  - llm-15-llm-serving
knowledge_refs:
  - llm-17-observability
  - llm-15-llm-serving
  - llm-16-cost-optimization
references:
  - title: "LLMOPS Community"
    url: "https://github.com/chase0213/llmops"
    notes: "LLMOps resource collection"
  - title: "LangChain Ecosystem"
    url: "https://www.langchain.com/"
    notes: "Framework + platform for LLM apps"
  - title: "LlamaIndex Documentation"
    url: "https://docs.llamaindex.ai/"
    notes: "Data framework for LLM apps"
  - title: "Haystack by deepset"
    url: "https://haystack.deepset.ai/"
    notes: "Production NLP framework"
  - title: "Modal: Serverless LLM Infrastructure"
    url: "https://modal.com/"
    notes: "Cloud GPU infrastructure for LLMs"
---

# The LLMOps Tooling Landscape

The LLMOps ecosystem has exploded. Understanding the layers helps you choose the right tools for your stack.

## Tooling Layers

```
┌─────────────────────────────────────────────┐
│              Application Layer              │
│  LangChain, LlamaIndex, Haystack, Semantic │
├─────────────────────────────────────────────┤
│              Orchestration Layer            │
│  LangGraph, CrewAI, AutoGen, DSPy         │
├─────────────────────────────────────────────┤
│              Observability Layer            │
│  LangSmith, Braintrust, Helicone, Arize    │
├─────────────────────────────────────────────┤
│              Serving Layer                  │
│  vLLM, TGI, TensorRT-LLM, Ollama         │
├─────────────────────────────────────────────┤
│              Infrastructure Layer           │
│  Modal, Replicate, Anyscale, Together AI   │
├─────────────────────────────────────────────┤
│              Model Layer                    │
│  OpenAI, Anthropic, Google, Meta, Mistral  │
└─────────────────────────────────────────────┘
```

## Framework Comparison

### LangChain / LangGraph
- **LangChain**: chain LLM calls with tools and memory
- **LangGraph**: graph-based workflow orchestration
- **LangSmith**: observability and evaluation platform
- **Best for**: complex agent workflows, multi-step pipelines

### LlamaIndex
- **Focus**: data indexing and retrieval (RAG)
- **Features**: document loaders, vector stores, query engines
- **Best for**: RAG-heavy applications, data-intensive workflows

### Haystack
- **Focus**: production NLP pipelines
- **Features**: modular components, evaluation, deployment
- **Best for**: enterprise search, document processing

### Semantic Kernel
- **Focus**: enterprise Microsoft ecosystem
- **Features**: C#/Python SDK, Azure integration
- **Best for**: Microsoft shops, enterprise deployments

## Vector Databases

| Database | Self-Hosted | Managed | Best For |
|----------|-------------|---------|----------|
| Chroma | ✅ | ❌ | Prototyping |
| Pinecone | ❌ | ✅ | Quick production |
| Weaviate | ✅ | ✅ | Hybrid search |
| Qdrant | ✅ | ✅ | Performance |
| Milvus | ✅ | ✅ | Scale |
| pgvector | ✅ | ✅ | Postgres users |

## Serving Platforms

| Platform | Model | GPU | Best For |
|----------|-------|-----|----------|
| OpenAI API | GPT-4 | Managed | No infra |
| Anthropic API | Claude | Managed | No infra |
| Together AI | Open models | Managed | Open models |
| Modal | Any | Serverless | Custom serving |
| Replicate | Many | Serverless | Quick deployment |
| Anyscale | Any | Clustered | Large-scale |

## Evaluation Platforms

| Platform | Focus | Free Tier |
|----------|-------|-----------|
| LangSmith | Tracing + eval | ✅ |
| Braintrust | Eval + prompts | ✅ |
| Helicone | Proxy + analytics | ✅ |
| Arize | Observability | ✅ |
| Inspect AI | Benchmark eval | ✅ |

## Choosing Your Stack

### Simple RAG App
```
OpenAI API + Chroma + LangChain
```

### Production Agent
```
LangGraph + vLLM + LangSmith + Qdrant
```

### Enterprise
```
Semantic Kernel + Azure OpenAI + Weaviate + Azure ML
```

### Open Source Stack
```
LlamaIndex + Ollama + Chroma + Haystack
```

## Key Takeaways

1. The LLMOps stack has clear layers: application → orchestration → observability → serving → infrastructure → models
2. LangChain/LangGraph leads for complex workflows; LlamaIndex for RAG
3. Vector databases range from Chroma (prototyping) to Milvus (enterprise)
4. Serving platforms span managed APIs to self-hosted vLLM
5. Start simple, add complexity as needed
