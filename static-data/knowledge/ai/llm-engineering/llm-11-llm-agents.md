---
slug: llm-11-llm-agents
title: "Building LLM Agents"
description: "Agent architectures, tool orchestration, memory systems, and multi-agent patterns — from ReAct to CrewAI."
order: 11
tags:
  - llm-engineering
  - agents
  - react
  - multi-agent
  - orchestration
prerequisites:
  - llm-10-function-calling
  - llm-06-embeddings-and-semantic-search
knowledge_refs:
  - llm-10-function-calling
  - llm-12-context-engineering
  - llm-07-rag-engineering
references:
  - title: "What is a ReAct Agent?"
    url: "https://www.ibm.com/think/topics/react-agent"
    notes: "ReAct architecture explanation"
  - title: "LangChain Plan-and-Execute Agents"
    url: "https://www.langchain.com/blog/planning-agents"
    notes: "Planning-based agent architecture"
  - title: "AutoGen Memory and RAG"
    url: "https://microsoft.github.io/autogen/stable//user-guide/agentchat-user-guide/memory.html"
    notes: "Memory systems for multi-agent workflows"
  - title: "Choosing Multi-Agent Architecture"
    url: "https://www.langchain.com/blog/choosing-the-right-multi-agent-architecture"
    notes: "Design patterns for multi-agent systems"
  - title: "CrewAI Documentation"
    url: "https://docs.crewai.com/"
    notes: "Role-based multi-agent framework"
---

# Building LLM Agents

An LLM agent is a system that uses an LLM as its reasoning engine, combined with tools, memory, and planning capabilities to accomplish tasks autonomously.

## Core Agent Architecture

```
User Goal → Planning → Action Selection → Tool Execution → Observation → Reflection → Repeat
              ↑                                                              ↓
              └──────────────────────────────────────────────────────────────┘
```

## Agent Patterns

### ReAct (Reasoning + Acting)
Alternates between thinking and doing:
```
Thought: I need to find the weather in Tokyo
Action: get_weather(location="Tokyo")
Observation: 22°C, sunny
Thought: Now I can answer the user's question
Answer: It's 22°C and sunny in Tokyo
```
- **Pros**: Transparent reasoning, adaptable
- **Cons**: One LLM call per step, high latency

### Plan-and-Execute
Separate planning from execution:
```python
# Planner generates a plan
plan = [
    {"step": 1, "tool": "search", "args": {"query": "..."}},
    {"step": 2, "tool": "analyze", "args": {"data": "step1_result"}},
    {"step": 3, "tool": "summarize", "args": {"analysis": "step2_result"}}
]
# Executor runs each step
```
- **Pros**: Cost-efficient, parallelizable
- **Cons**: Less adaptable to unexpected results

## Tool Orchestration

Agents need tools to interact with the world:

| Tool Type | Examples | Use Case |
|-----------|----------|----------|
| **Search** | Web search, vector DB | Information retrieval |
| **Code** | Python REPL, shell | Computation, analysis |
| **APIs** | Weather, finance, CRM | External services |
| **Memory** | Vector store, file system | Long-term knowledge |

```python
tools = [
    Tool(name="search", func=web_search, description="Search the web"),
    Tool(name="calculator", func=calculate, description="Do math"),
    Tool(name="python", func=run_python, description="Run Python code"),
]
```

## Memory Systems

| Memory Type | Purpose | Implementation |
|-------------|---------|----------------|
| **Working** | Current task context | Conversation history |
| **Short-term** | Recent interactions | Sliding window |
| **Long-term** | Persistent knowledge | Vector database |
| **Procedural** | Learned skills | Fine-tuned behaviors |

## Multi-Agent Systems

### Supervised (Hub-and-Spoke)
```
Supervisor → Agent 1 (research)
           → Agent 2 (writing)
           → Agent 3 (review)
```
One coordinator manages specialized workers.

### Peer-to-Peer
Agents communicate directly, passing tasks like a relay:
```
Agent A → Agent B → Agent C → Final result
```

### Debate/Consensus
Multiple agents discuss and reach agreement:
```
Agent 1: "I think X because..."
Agent 2: "I disagree, Y is better because..."
Agent 1: "Good point, let's consider Z..."
→ Consensus answer
```

## Frameworks

| Framework | Style | Best For |
|-----------|-------|----------|
| **LangGraph** | Graph-based | Complex workflows |
| **CrewAI** | Role-based | Team collaboration |
| **AutoGen** | Event-driven | Multi-agent conversations |
| **LlamaIndex** | Data-focused | RAG-heavy agents |

## Key Takeaways

1. ReAct is transparent but expensive; Plan-and-Execute is efficient but rigid
2. Tool orchestration via function calling is the standard approach
3. Memory systems enable persistent, stateful agents
4. Multi-agent architectures scale complex tasks across specialized agents
5. Choose frameworks based on your workflow complexity and team structure
