---
slug: agents-05-memory-systems
title: "Agent Memory Systems"
description: "Memory architectures for agents — working memory, episodic memory, long-term storage, and self-editing memory patterns."
order: 5
tags:
  - ai-agents
  - memory
  - working-memory
  - episodic-memory
prerequisites:
  - agents-02-agent-architecture
knowledge_refs:
  - agents-02-agent-architecture
  - agents-04-reasoning-and-planning
references:
  - title: "MemGPT: LLMs as Operating Systems"
    url: "https://research.memgpt.ai/"
    notes: "OS-inspired memory management"
  - title: "Agent Memory Guide (MongoDB)"
    url: "https://www.mongodb.com/resources/basics/artificial-intelligence/agent-memory"
    notes: "Multi-tier memory architecture"
  - title: "LLMs as OS: Agent Memory (DeepLearning.AI)"
    url: "https://www.deeplearning.ai/courses/llms-as-operating-systems-agent-memory"
    notes: "Practical memory patterns"
  - title: "Best AI Agent Memory Frameworks"
    url: "https://machinelearningmastery.com/the-6-best-ai-agent-memory-frameworks-you-try-in-2026/"
    notes: "Comparison of memory frameworks"
  - title: "Letta (MemGPT) Documentation"
    url: "https://docs.letta.com/"
    notes: "Self-editing memory framework"
---

# Agent Memory Systems

LLMs are stateless — they forget everything between calls. Memory systems give agents persistence, enabling them to learn, recall, and maintain context across interactions.

## Memory Taxonomy

| Type | What It Stores | Duration | Example |
|------|---------------|----------|---------|
| **Working** | Current task context | Session | Conversation history |
| **Short-term** | Recent interactions | Minutes-hours | Sliding window |
| **Episodic** | Past experiences | Days-weeks | "What happened yesterday?" |
| **Long-term** | Persistent knowledge | Permanent | User preferences, facts |
| **Procedural** | Learned skills | Permanent | Fine-tuned behaviors |

## Working Memory

The LLM's context window — what the model sees right now:

```python
messages = [
    {"role": "system", "content": "You are a research assistant."},
    {"role": "user", "content": "Find papers on RLHF"},
    {"role": "assistant", "content": "I found 3 relevant papers..."},
    {"role": "user", "content": "Summarize the first one"}
]
```

### Challenges
- Limited token budget
- Oldest messages get forgotten
- Important context may be in the middle

## Scratchpads

Structured notes replacing raw conversation:

```python
scratchpad = {
    "goal": "Write a research report on AI safety",
    "completed": ["Found 5 papers", "Read abstracts"],
    "pending": ["Deep read top 3", "Draft outline", "Write report"],
    "key_findings": ["RLHF is standard", "DPO is simpler"],
    "citations": [" paper1.pdf", " paper2.pdf"]
}
```

More efficient than storing full conversation history.

## Episodic Memory

Chronological records of past experiences:

```python
episodes = [
    {"date": "2024-01-15", "event": "User asked about Python debugging", "resolution": "Provided pdb tutorial"},
    {"date": "2024-01-20", "event": "User had memory leak issue", "resolution": "Identified circular reference"},
]
```

Enables agents to learn from past interactions.

## Long-Term Memory

Persistent storage outside the context window:

### Vector Database Memory
```python
# Store experience
vector_db.store(
    embedding=embed(experience),
    metadata={"type": "episode", "date": today}
)

# Retrieve relevant memories
relevant = vector_db.search(embed(current_query), top_k=5)
```

### Key-Value Memory
```python
memory = {
    "user.name": "Alice",
    "user.preferences.tone": "formal",
    "project.deadline": "2024-03-01"
}
```

## MemGPT Architecture

Inspired by operating systems — treat LLM context as RAM:

| Tier | Analogy | Implementation |
|------|---------|----------------|
| **Core Memory** | RAM | In-context persistent block |
| **Recall Memory** | Searchable history | Conversation log + search |
| **Archival Memory** | Disk storage | Vector database + documents |

### Self-Editing Memory
The agent decides when to update its own memory:
```python
# Agent can call memory tools
memory_tool("core_memory_replace", "persona", "I am a research assistant specializing in AI safety")
memory_tool("archival_memory_insert", "Key finding: DPO outperforms RLHF on several benchmarks")
```

## Design Patterns

### Summary Compression
```python
old_messages = messages[:20]
summary = llm.summarize(old_messages)
messages = [{"role": "system", "content": summary}] + messages[20:]
```

### RAG-Enhanced Memory
```python
def build_context(query):
    past = episodic_memory.search(query, top_k=3)
    docs = rag_memory.search(query, top_k=3)
    return combine(past, docs)
```

### Hierarchical Memory
```python
# Level 1: Working memory (current task)
# Level 2: Session memory (today's interactions)
# Level 3: User memory (preferences, history)
# Level 4: World memory (knowledge base)
```

## Key Takeaways

1. Agents need multiple memory types: working, episodic, long-term
2. Scratchpads are more efficient than raw conversation history
3. Vector databases enable semantic memory retrieval
4. MemGPT treats LLM context as RAM with disk-backed storage
5. Self-editing memory lets agents manage their own context
