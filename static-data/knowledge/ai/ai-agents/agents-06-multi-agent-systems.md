---
slug: agents-06-multi-agent-systems
title: "Multi-Agent Systems"
description: "How multiple AI agents collaborate, communicate, and coordinate to solve complex problems beyond single-agent capabilities."
order: 6
tags:
  - ai-agents
  - multi-agent
  - collaboration
  - communication
  - swarm-intelligence
prerequisites:
  - agents-02-agent-architecture
  - agents-05-memory-systems
references:
  - title: "Multi-Agent Systems: A Survey"
    author: "Da Xu et al."
    url: "https://arxiv.org/abs/2502.07373"
    type: "paper"
    description: "Comprehensive survey of multi-agent system architectures and design patterns."
  - title: "Cognitive Architectures for Language Agents"
    author: "Theodore Sumers et al."
    url: "https://arxiv.org/abs/2309.02427"
    type: "paper"
    description: "Proposes cognitive architecture framework including multi-agent coordination."
  - title: "LangGraph Multi-Agent Systems Documentation"
    author: "LangChain"
    url: "https://langchain-ai.github.io/langgraph/concepts/multi_agent/"
    type: "docs"
    description: "Practical guide to implementing multi-agent systems with LangGraph."
  - title: "Building Effective Agents"
    author: "Anthropic Engineering"
    url: "https://www.anthropic.com/engineering/building-effective-agents"
    type: "article"
    description: "Covers orchestrator-workers pattern and multi-agent coordination."
  - title: "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation"
    author: "Qingyun Wu et al. (Microsoft)"
    url: "https://arxiv.org/abs/2308.08155"
    type: "paper"
    description: "Framework for multi-agent conversation and collaborative problem-solving."
related_knowledge:
  - slug: agents-02-agent-architecture
    title: "Agent Architecture"
    lesson_number: 2
  - slug: agents-05-memory-systems
    title: "Memory Systems"
    lesson_number: 5
  - slug: agents-17-agent-design-patterns
    title: "Agent Design Patterns"
    lesson_number: 17
knowledge_refs:
  - slug: "genai-12-multiple-models"
    title: "Multiple Models"
  - slug: "dl-19-model-compression"
    title: "Model Compression"
  - slug: "llm-03-tokenization"
    title: "Tokenization"
---

# Multi-Agent Systems

When a single agent hits complexity bottlenecks — context limits, domain expertise requirements, or coordination challenges — multi-agent systems distribute the workload across specialized agents that collaborate to achieve shared goals.

## Why Multi-Agent?

Single-agent systems face inherent limitations:
- **Context Window Constraints:** A single agent's context fills quickly with tool outputs, code, and reasoning traces.
- **Domain Expertise:** One agent trying to be an expert in everything becomes a generalist at nothing.
- **Parallelism:** Many tasks can execute simultaneously if distributed across agents.
- **Reliability:** Multiple agents can cross-check each other's work, catching errors a single agent might miss.

## Architecture Patterns

### Sequential Pipeline
Agents process tasks in a linear chain, each specializing in one step:
```
User Request → Research Agent → Writing Agent → Review Agent → Final Output
```
Each agent receives the output of the previous one and adds its expertise.

### Parallel Workers
Multiple agents work simultaneously on independent subtasks:
```
User Request → Orchestrator
                 ├── Agent A: Research topic X
                 ├── Agent B: Research topic Y
                 └── Agent C: Research topic Z
              → Merge Results → Final Output
```
The orchestrator delegates, collects, and synthesizes results.

### Evaluator-Optimizer (Generator-Critic)
One agent generates, another critiques, iterating until quality thresholds are met:
```
Generator Agent → Output → Critic Agent → Feedback
       ↑                              │
       └──────────────────────────────┘
              (repeat until satisfied)
```
This pattern is effective for tasks requiring iterative refinement — writing, code review, or design.

### Hierarchical (Orchestrator-Workers)
A coordinator agent dynamically breaks down goals and delegates to specialized workers:
```
Orchestrator
  ├── Worker Agent (Research)
  ├── Worker Agent (Data Analysis)
  ├── Worker Agent (Code Writing)
  └── Worker Agent (Verification)
```
The orchestrator maintains the overall plan while workers focus on execution.

## Communication Patterns

### Direct Communication
Agents talk to each other directly, sharing information as needed. Simple but can become chaotic with many agents.

### Shared State
All agents read and write to a shared memory or state store. Enables loose coupling but requires careful conflict resolution.

### Message Passing
Agents communicate through structured messages, often mediated by an orchestrator. Provides clear boundaries and audit trails.

### Blackboard Architecture
A shared "blackboard" where agents post observations and solutions. Any agent can read the blackboard and contribute based on its expertise.

## The Supervisor Pattern

In production multi-agent systems, the **supervisor** pattern is dominant:
- A central agent (the supervisor) manages the workflow
- It decides which worker agents to invoke and when
- It handles error recovery and task reassignment
- It synthesizes final results from worker outputs

This mirrors how human teams operate: a project manager coordinates specialists rather than everyone trying to do everything.

## Challenges in Multi-Agent Systems

### Coordination Overhead
More agents mean more communication, which consumes tokens and adds latency. The overhead can outweigh benefits for simple tasks.

### Consistency
Ensuring agents don't contradict each other or produce conflicting outputs requires careful design of shared state and communication protocols.

### Error Propagation
A mistake by one agent can cascade through the system. Robust multi-agent systems include verification steps and cross-checking mechanisms.

### Debugging Complexity
When multiple agents interact, tracing the source of an error becomes significantly harder. Comprehensive logging and observability are essential.

## When to Use Multi-Agent

**Use multi-agent when:**
- Tasks are naturally decomposable into independent subtasks
- Different parts require different expertise
- Parallelism would significantly reduce latency
- Cross-validation improves reliability

**Stick with single-agent when:**
- Tasks are simple and linear
- Latency is critical
- The overhead of coordination outweighs benefits
- The problem doesn't benefit from domain specialization

---

*References:*
1. Da Xu et al., "Multi-Agent Systems: A Survey," 2025. [Link](https://arxiv.org/abs/2502.07373)
2. Theodore Sumers et al., "Cognitive Architectures for Language Agents," 2023. [Link](https://arxiv.org/abs/2309.02427)
3. LangChain, "LangGraph Multi-Agent Systems." [Link](https://langchain-ai.github.io/langgraph/concepts/multi_agent/)
4. Anthropic Engineering, "Building Effective Agents." [Link](https://www.anthropic.com/engineering/building-effective-agents)
5. Qingyun Wu et al., "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation," Microsoft, 2023. [Link](https://arxiv.org/abs/2308.08155)
