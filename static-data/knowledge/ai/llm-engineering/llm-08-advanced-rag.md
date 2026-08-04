---
slug: llm-08-advanced-rag
title: "Advanced RAG"
description: "Beyond basic RAG — query routing, self-RAG, GraphRAG, multimodal RAG, and agentic retrieval patterns."
order: 8
tags:
  - llm-engineering
  - advanced-rag
  - self-rag
  - graph-rag
prerequisites:
  - llm-07-rag-engineering
  - llm-11-llm-agents
knowledge_refs:
  - llm-07-rag-engineering
  - llm-11-llm-agents
  - llm-06-embeddings-and-semantic-search
references:
  - title: "Self-RAG: Learning to Retrieve, Generate, and Critique"
    url: "https://arxiv.org/abs/2310.11511"
    notes: "Adaptive retrieval with reflection tokens"
  - title: "GraphRAG: Unlocking LLM discovery on narrative private data"
    url: "https://microsoft.github.io/graphrag/"
    notes: "Microsoft's knowledge graph + RAG"
  - title: "CRAG: Corrective Retrieval Augmented Generation"
    url: "https://arxiv.org/abs/2401.15884"
    notes: "Self-correcting retrieval quality"
  - title: "RAGAS Evaluation Framework"
    url: "https://docs.ragas.io/"
    notes: "RAG evaluation metrics and benchmarks"
  - title: "TruLens RAG Triad"
    url: "https://www.trulens.org/getting_started/core_concepts/rag_triad/"
    notes: "Context relevance, groundedness, answer relevance"
---

# Advanced RAG

Basic RAG retrieves top-k chunks and generates an answer. Advanced RAG adds intelligence at every stage — deciding when to retrieve, how to route queries, and how to verify quality.

## Query Routing

Not every query needs retrieval. A router decides the best strategy:

```python
def route_query(query):
    if is_factual(query):
        return "retrieval"      # needs external knowledge
    elif is_conversational(query):
        return "direct"          # model knowledge sufficient
    elif is_complex(query):
        return "multi_step"      # needs iterative retrieval
    else:
        return "summarization"   # needs document processing
```

## Self-RAG

The model decides **when** to retrieve and **critiques** its own outputs:

1. Generate a query analysis
2. Decide: retrieve or not?
3. If retrieved, evaluate document relevance (`IsREL`)
4. Generate answer
5. Critique: is answer supported? (`IsSUP`)
6. Is answer useful? (`IsUSE`)

Uses special **reflection tokens** trained into the model.

## CRAG (Corrective RAG)

Adds a quality gate after retrieval:

```
Retrieve → Evaluate relevance → High confidence? → Generate normally
                                → Low confidence? → Web search fallback
                                → Ambiguous? → Hybrid approach
```

Prevents bad retrieval from poisoning the prompt.

## GraphRAG

Builds a **knowledge graph** from source documents:

1. Extract entities and relationships from text
2. Build entity-relationship graph
3. Detect communities (clusters of related entities)
4. At query time: traverse graph for multi-hop reasoning

### When to Use GraphRAG
- Complex relationship queries ("Which researchers collaborated on X?")
- Multi-document synthesis
- Need for global sensemaking over large corpora

## Multimodal RAG

Handle documents with images, tables, and charts:

```
Document → Parse (text + images + tables) → 
  Text chunks → text embedding
  Images → image embedding (CLIP) + text summary
  Tables → markdown conversion + embedding
→ Unified vector store → retrieval → multimodal LLM generation
```

## Agentic RAG

RAG as a tool within an agent loop:

```python
def agent_loop(query):
    plan = plan_subqueries(query)
    results = []
    for subquery in plan:
        docs = retrieve(subquery)
        answer = generate(subquery, docs)
        results.append(answer)
        if needs_more_info(answer):
            plan.append(follow_up(query, answer))
    return synthesize(results)
```

## Evaluation Frameworks

### RAGAS
- **Faithfulness**: is the answer grounded in context?
- **Answer relevance**: does it address the query?
- **Context precision**: are retrieved docs relevant?
- **Context recall**: are all relevant docs found?

### TruLens RAG Triad
1. **Context relevance**: each chunk relevant to query?
2. **Groundedness**: claims supported by context?
3. **Answer relevance**: response addresses question?

## Key Takeaways

1. Query routing avoids unnecessary retrieval for simple queries
2. Self-RAG and CRAG add self-correction to prevent hallucination
3. GraphRAG excels at relationship and multi-hop queries
4. Multimodal RAG handles documents with images and tables
5. Agentic RAG enables iterative, multi-step retrieval
