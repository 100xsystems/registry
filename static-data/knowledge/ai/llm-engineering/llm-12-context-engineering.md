---
slug: llm-12-context-engineering
title: "Context Engineering & Memory"
description: "Designing what the model sees — context management, memory architectures, scratchpads, and working memory for agents."
order: 12
tags:
  - llm-engineering
  - context-engineering
  - memory
  - scratchpads
prerequisites:
  - llm-05-tokenization-and-context
  - llm-11-llm-agents
knowledge_refs:
  - llm-05-tokenization-and-context
  - llm-11-llm-agents
  - llm-06-embeddings-and-semantic-search
references:
  - title: "Context Engineering: The New Skill"
    url: "https://www.latent.space/p/context-engineering"
    notes: "swyx on context engineering as a discipline"
  - title: "Building Effective Agents (Anthropic)"
    url: "https://docs.anthropic.com/en/docs/build-with-claude/agentic"
    notes: "Anthropic's guide to agent design"
  - title: "MemGPT: LLMs with Memory"
    url: "https://arxiv.org/abs/2310.08560"
    notes: "Operating system-inspired memory management"
  - title: "LangGraph Memory Guide"
    url: "https://langchain-ai.github.io/langgraph/concepts/memory/"
    notes: "Memory patterns in LangGraph"
  - title: "Context Window Management"
    url: "https://www.getmaxim.ai/articles/context-window-management-strategies-for-long-context-ai-agents-and-chatbots/"
    notes: "Practical context management strategies"
---

# Context Engineering & Memory

Context engineering is the discipline of designing what information the LLM receives. As Andrej Karpathy noted, it's becoming a core skill — the "new prompt engineering."

## Why Context Engineering Matters

The model can only work with what it sees. Poor context = poor output:
- Too little context → hallucination, generic responses
- Too much context → confusion, cost, latency
- Wrong context → irrelevant or misleading outputs
- Poor ordering → important info lost in the middle

## Context Design Principles

### 1. Information Hierarchy
```
[System instructions]     ← Permanent, highest priority
[Tool results]            ← Dynamic, task-relevant
[Retrieved context]       ← Knowledge from RAG
[Conversation history]    ← Recent interactions
[User query]              ← Current request
```

### 2. Recency and Primacy
Put most important information first and last. The "lost in the middle" problem means middle content gets less attention.

### 3. Compression Over Stuffing
Prefer concise, relevant information over raw dumps. Summarize rather than paste entire documents.

## Memory Architectures

### Stateless (No Memory)
Each request is independent:
```
Request → LLM → Response
```
Simple but can't maintain context across interactions.

### Conversation Memory
Maintain chat history:
```python
messages = [
    {"role": "system", "content": "..."},
    # ... previous turns ...
    {"role": "user", "content": "current query"}
]
```

### Scratchpad Memory
Structured state replacing raw conversation:
```python
scratchpad = {
    "goal": "Book a flight to Tokyo",
    "completed": ["Found flights", "Compared prices"],
    "pending": ["Select seat", "Payment"],
    "context": {"preference": "window seat", "budget": "$1500"}
}
```

### Episodic Memory
Store and retrieve past experiences:
```python
def recall_relevant_memories(query, memory_db):
    memories = memory_db.search(query, top_k=5)
    return format_as_context(memories)
```

## Context Budgeting

Allocate tokens across context components:

| Component | Typical Budget | Notes |
|-----------|---------------|-------|
| System prompt | 500-2000 | Fixed, always included |
| Tool definitions | 500-2000 | Depends on number of tools |
| RAG context | 2000-8000 | Dynamic per query |
| Conversation history | 2000-8000 | Sliding window |
| Scratchpad | 500-2000 | Structured state |
| Output reserve | 1000-4000 | For model response |

## Practical Patterns

### Hierarchical Summarization
```
Full conversation → summarize → compressed summary
                                    ↓
Recent turns (verbatim) + Summary (compressed) = context
```

### RAG-Enhanced Memory
Store past interactions in vector DB, retrieve relevant ones:
```python
def build_context(query, conversation_db, rag_db):
    # Get relevant past interactions
    past = conversation_db.search(query, top_k=3)
    # Get relevant documents
    docs = rag_db.search(query, top_k=3)
    return combine(past, docs)
```

## Key Takeaways

1. Context engineering is designing what the model sees — the new core skill
2. Put important information first and last to avoid "lost in the middle"
3. Scratchpad memory is more efficient than raw conversation history
4. Budget tokens carefully across system, retrieval, history, and output
5. Hierarchical summarization and RAG enable long-running agents
