---
slug: agents-01-what-are-ai-agents
title: "What Are AI Agents?"
description: "Defining AI agents — autonomous systems that perceive, reason, and act — from reactive reflex agents to modern LLM-powered agents."
order: 1
tags:
  - ai-agents
  - foundations
  - autonomy
prerequisites: []
knowledge_refs:
  - agents-02-agent-architecture
  - agents-03-tool-use
references:
  - title: "What Are AI Agents? (AWS)"
    url: "https://aws.amazon.com/what-is/ai-agents/"
    notes: "AWS overview of AI agents"
  - title: "Types of AI Agents (IBM)"
    url: "https://www.ibm.com/think/topics/ai-agent-types"
    notes: "Classification of agent types"
  - title: "The Evolution of AI Agents (IBM)"
    url: "https://www.ibm.com/think/topics/evolution-of-ai-agents"
    notes: "Historical development of agents"
  - title: "AI: A Modern Approach (Russell & Norvig)"
    url: "https://aima.cs.berkeley.edu/"
    notes: "Foundational AI textbook"
  - title: "Understanding AI Agent Types (Red Hat)"
    url: "https://www.redhat.com/en/blog/understanding-ai-agent-types-simple-complex"
    notes: "Categorizing agent complexity"
---

# What Are AI Agents?

An AI agent is a system that **perceives** its environment, **reasons** about what to do, and **acts** to achieve goals — with some degree of autonomy. Unlike simple chatbots that respond to prompts, agents take initiative.

## Core Properties

| Property | Description |
|----------|-------------|
| **Autonomy** | Operates without constant human direction |
| **Perception** | Gathers information from its environment |
| **Reasoning** | Analyzes situations and plans actions |
| **Action** | Executes tools, APIs, or commands |
| **Goal-oriented** | Works toward specific objectives |
| **Adaptive** | Learns and adjusts from feedback |

## Agent Taxonomy

### Reactive Agents
Respond directly to stimuli with no internal state:
```
Input → Condition-Action Rule → Output
```
- Example: thermostat, spam filter
- Simple but limited

### Deliberative Agents
Maintain internal models and plan ahead:
```
Perception → World Model → Planning → Action
```
- Goal-based: evaluate action sequences toward objectives
- Utility-based: optimize trade-offs (speed vs. cost vs. safety)

### Learning Agents
Improve over time via feedback:
```
Action → Critic Evaluation → Learning Element → Improved Policy
```
- Use reinforcement learning, human feedback, or experience

### LLM-Powered Agents
Use language models as the cognitive core:
```
Goal → LLM Reasoning → Tool Calls → Observations → LLM Reasoning → ...
```
- Natural language as the interface
- Flexible, general-purpose reasoning
- Can use any tool via function calling

## Autonomous vs. Assistive

| Dimension | Assistive Agent | Autonomous Agent |
|-----------|----------------|------------------|
| **Initiative** | Waits for user input | Proactively takes action |
| **Scope** | Single-turn assistance | Multi-step workflows |
| **Control** | Human approves all actions | Executes independently |
| **Example** | ChatGPT, GitHub Copilot | Devin, AutoGPT, Claude Code |

## Historical Evolution

1. **1950s-1970s**: Expert systems (MYCIN) — hand-coded rules
2. **1980s-1990s**: BDI architectures — belief-desire-intention models
3. **2000s-2010s**: Reinforcement learning agents — Atari, Go
4. **2020s**: LLM agents — GPT-4, Claude with tool use, ReAct, planning

## The Agent Loop

```
1. Observe: gather information
2. Think: reason about the situation
3. Decide: choose an action
4. Act: execute the action
5. Reflect: evaluate the outcome
6. Repeat until goal achieved
```

## Key Takeaways

1. Agents perceive, reason, and act — not just respond
2. LLM agents use language models as the reasoning engine
3. Agents range from simple reactive to complex autonomous systems
4. The key distinction is autonomy — how much the agent acts without human direction
5. Modern agents combine LLM reasoning with tool use and memory
