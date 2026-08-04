---
slug: agents-02-agent-architecture
title: "Agent Architecture"
description: "The building blocks of agent systems — the perception-reasoning-action cycle, BDI models, and modern LLM agent architectures."
order: 2
tags:
  - ai-agents
  - architecture
  - bdi
  - agent-loop
prerequisites:
  - agents-01-what-are-ai-agents
knowledge_refs:
  - agents-01-what-are-ai-agents
  - agents-04-reasoning-and-planning
references:
  - title: "Building Effective Agents (Anthropic)"
    url: "https://docs.anthropic.com/en/docs/build-with-claude/agentic"
    notes: "Anthropic's guide to agent architecture"
  - title: "LLM Agent Architectures (LangChain)"
    url: "https://www.langchain.com/blog/agentic-design-patterns-part-1"
    notes: "Modern agent design patterns"
  - title: "Cognitive Architectures for Language Agents"
    url: "https://arxiv.org/abs/2309.02427"
    notes: "Survey of agent architectures"
  - title: "The Agentic Loop"
    url: "https://www.anthropic.com/engineering/building-effective-ai-agents"
    notes: "Core agent loop patterns"
  - title: "BDI Agent Model"
    url: "https://en.wikipedia.org/wiki/Belief%E2%80%93desire%E2%80%93intention_software_model"
    notes: "Classic BDI architecture"
---

# Agent Architecture

Every agent, from a simple chatbot to a complex multi-agent system, follows an architectural pattern. Understanding these patterns helps you design effective agents.

## The Core Agent Loop

```
┌─────────────────────────────────────┐
│              AGENT LOOP             │
│                                     │
│  Observe → Think → Decide → Act    │
│     ↑                        │     │
│     └────────────────────────┘     │
│              (reflect)              │
└─────────────────────────────────────┘
```

### Components

| Component | Function | Implementation |
|-----------|----------|----------------|
| **Perception** | Gather information | APIs, sensors, user input |
| **Memory** | Store context | Conversation, vector DB |
| **Reasoning** | Analyze and plan | LLM, CoT, ReAct |
| **Decision** | Choose action | Tool selection, response generation |
| **Action** | Execute tool | Function calling, API calls |
| **Reflection** | Evaluate outcome | Self-critique, scoring |

## BDI Architecture

The classic **Belief-Desire-Intention** model:

- **Beliefs**: what the agent knows about the world
- **Desires**: what the agent wants to achieve
- **Intentions**: what the agent commits to doing

```
Beliefs + Desires → Intentions → Actions → Updated Beliefs
```

### Modern LLM Equivalent
- **Beliefs**: context window, RAG retrieval, tool results
- **Desires**: user goal, system instructions
- **Intentions**: planned action sequence (CoT, ReAct)
- **Actions**: function calls, text generation

## LLM Agent Architectures

### Single-Agent (Tool-Using LLM)
```
User → LLM + Tools → Response
```
Simple but limited by single-model reasoning.

### Agent with Planning
```
User → Planner LLM → [Step 1, Step 2, Step 3] → Executor → Response
```
Separates planning from execution.

### Multi-Agent
```
User → Supervisor → Agent 1 (research)
                   → Agent 2 (writing)
                   → Agent 3 (review)
                   → Synthesis
```
Specialized agents for different tasks.

### Hierarchical
```
Manager Agent
├── Worker Agent 1
│   ├── Sub-agent 1a
│   └── Sub-agent 1b
└── Worker Agent 2
```
Recursive decomposition of tasks.

## Design Principles

1. **Separation of concerns**: each agent handles one thing well
2. **Clear interfaces**: agents communicate via well-defined messages
3. **Graceful degradation**: fallback when tools fail
4. **Observability**: every step should be traceable
5. **Human control points**: stop-and-ask for high-risk actions

## Key Takeaways

1. All agents follow the observe-think-decide-act loop
2. BDI is the classic architecture; LLM agents are the modern equivalent
3. Single-agent is simplest; multi-agent scales better for complex tasks
4. Hierarchical architectures enable recursive task decomposition
5. Design for observability and human control points
