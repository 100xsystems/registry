---
slug: agents-05-memory-systems
title: "Memory Systems"
description: "How AI agents store, retrieve, and manage information across short-term, long-term, episodic, and semantic memory."
order: 5
tags:
  - ai-agents
  - memory
  - vector-databases
  - retrieval
  - episodic-memory
  - semantic-memory
prerequisites:
  - agents-01-what-are-ai-agents
  - agents-04-reasoning-and-planning
references:
  - title: "Cognitive Architectures for Language Agents"
    author: "Theodore Sumers et al."
    url: "https://arxiv.org/abs/2309.02427"
    type: "paper"
    description: "Proposes cognitive architecture framework for language agents including memory systems."
  - title: "Generative Agents: Interactive Simulacra of Human Behavior"
    author: "Joon Sung Park et al. (Stanford)"
    url: "https://arxiv.org/abs/2304.03442"
    type: "paper"
    description: "Seminal paper on generative agents with memory, reflection, and planning."
  - title: "LLM Powered Autonomous Agents"
    author: "Lilian Weng"
    url: "https://lilianweng.github.io/posts/2023-06-23-agent/"
    type: "article"
    description: "Comprehensive overview of agent memory systems and retrieval."
  - title: "LangChain Memory Documentation"
    author: "LangChain"
    url: "https://python.langchain.com/docs/concepts/memory/"
    type: "docs"
    description: "Practical guide to implementing memory in LLM agents."
  - title: "Letta: Stateful LLM Agents"
    author: "Letta (formerly MemGPT)"
    url: "https://docs.letta.com/"
    type: "docs"
    description: "Framework for stateful agents with persistent memory management."
related_knowledge:
  - slug: agents-04-reasoning-and-planning
    title: "Reasoning and Planning"
    lesson_number: 4
  - slug: agents-06-multi-agent-systems
    title: "Multi-Agent Systems"
    lesson_number: 6
  - slug: agents-07-langchain-agents
    title: "Building Agents with LangChain"
    lesson_number: 7
knowledge_refs:
  - slug: "llm-01-what-is-llm-engineering"
    title: "Fundamentals of LLMs"
  - slug: "genai-05-in-context-learning"
    title: "In-Context Learning"
  - slug: "llm-07-rag-engineering"
    title: "Information Retrieval"
---

# Memory Systems

Memory is what transforms an LLM from a stateless text generator into an agent that learns, adapts, and maintains context across interactions. Effective memory systems enable agents to recall past decisions, learn from experience, and build coherent understanding over time.

## The Memory Spectrum

Agent memory mirrors human cognitive architecture, organized into distinct but interacting systems:

### Working Memory (Context Window)
The agent's immediate working space — what's currently in the LLM's context window. This includes:
- The current conversation
- Recent tool outputs
- Active plans and goals
- System prompts and instructions

**Limitation:** Context windows are finite (typically 8K-200K tokens). Older information gets displaced as new information arrives.

### Short-Term Memory
Recent interactions and tool results that haven't yet been committed to long-term storage. Implemented through:
- Conversation buffers (keeping the last N messages)
- Sliding window approaches (keeping messages within a token budget)
- Summarization (compressing older messages into summaries)

### Long-Term Memory
Persistent information that survives across sessions and conversations. This is where the real power lies:
- **Episodic Memory:** Specific past experiences and interactions ("When the user asked about Python debugging last Tuesday, I found that...")
- **Semantic Memory:** General knowledge and learned patterns ("This codebase uses TypeScript with strict mode enabled")
- **Procedural Memory:** Learned workflows and procedures ("The deployment process requires running tests first, then building, then pushing")

## Implementing Agent Memory

### Vector Database Storage
The most common approach for long-term memory uses vector databases to store and retrieve information:

1. **Storage:** Text chunks, conversation summaries, or structured facts are embedded using a text embedding model and stored in a vector database (Chroma, Pinecone, Weaviate, etc.).

2. **Retrieval:** When the agent needs relevant context, it queries the vector database with the current situation, retrieving the most semantically similar memories.

3. **Consolidation:** Periodically, raw memories are summarized, deduplicated, or reorganized to maintain quality.

### The Generative Agents Approach
Stanford's landmark "Generative Agents" paper introduced a comprehensive memory architecture:

1. **Memory Stream:** A chronological log of all observations, reflections, and actions.
2. **Retrieval:** Uses recency (recent memories are more relevant), importance (higher-importance memories are more relevant), and relevance (semantically similar memories are more relevant) to score and retrieve memories.
3. **Reflection:** Periodically, the agent synthesizes recent memories into higher-level insights ("I've been helping this user with Python debugging a lot — they seem to prefer pytest over unittest").
4. **Planning:** Uses memories and reflections to generate and refine plans for future actions.

### Letta (formerly MemGPT)
Letta implements a "memory hierarchy" inspired by operating systems, where the agent manages its own memory:
- **Core Memory:** Always in context (user preferences, critical facts)
- **Archival Memory:** Stored in external database, retrieved on demand
- **Recall Memory:** Conversation history with search capabilities

The key innovation is that the agent itself decides when to save, retrieve, or forget information — rather than relying on fixed heuristics.

## Memory Challenges

### Context Window Management
As conversations grow, agents must decide what to keep in working memory and what to archive:
- **Summarization:** Compress older messages into concise summaries
- **Priority-based retention:** Keep high-relevance information, drop low-relevance
- **Sliding window:** Fixed-size buffer of recent messages

### Memory Retrieval Quality
Retrieving the right memories is crucial. Common issues:
- **Semantic drift:** Vector similarity doesn't always capture true relevance
- **Information overload:** Too many retrieved memories clutter the context
- **Stale information:** Memories that were true before but are no longer accurate

### Cross-Session Persistence
Agents need to maintain state across sessions without requiring users to repeat context:
- User preferences and history
- Project-specific knowledge
- Learned patterns and corrections

## Best Practices

**Layer Your Memory:** Use working memory for immediate context, short-term for recent history, and long-term for persistent knowledge. Each layer serves a different purpose.

**Index by Multiple Dimensions:** Store memories with timestamps (for recency), importance scores (for relevance), and semantic embeddings (for similarity).

**Implement Forgetting:** Not all memories are worth keeping. Agents should be able to forget low-value information to prevent noise accumulation.

**Make Memory Editable:** Allow the agent (or user) to update, correct, or delete stored memories. Stale or incorrect memories can cause cascading errors.

---

*References:*
1. Theodore Sumers et al., "Cognitive Architectures for Language Agents," 2023. [Link](https://arxiv.org/abs/2309.02427)
2. Joon Sung Park et al., "Generative Agents: Interactive Simulacra of Human Behavior," Stanford, 2023. [Link](https://arxiv.org/abs/2304.03442)
3. Lilian Weng, "LLM Powered Autonomous Agents," OpenAI Blog. [Link](https://lilianweng.github.io/posts/2023-06-23-agent/)
4. LangChain, "Memory Documentation." [Link](https://python.langchain.com/docs/concepts/memory/)
5. Letta, "Stateful LLM Agents." [Link](https://docs.letta.com/)
