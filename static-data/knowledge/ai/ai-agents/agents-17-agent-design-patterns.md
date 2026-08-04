---
slug: agents-17-agent-design-patterns
title: "Agent Design Patterns"
description: "Common design patterns for building effective AI agents — from reflection and self-correction to orchestrator-worker architectures."
order: 17
tags:
  - ai-agents
  - design-patterns
  - reflection
  - self-correction
  - orchestrator
prerequisites:
  - agents-02-agent-architecture
  - agents-06-multi-agent-systems
references:
  - title: "Building Effective Agents"
    author: "Anthropic Engineering"
    url: "https://www.anthropic.com/engineering/building-effective-agents"
    type: "article"
    description: "Architectural patterns including prompt chaining, routing, and orchestrator-workers."
  - title: "Agentic Design Patterns"
    author: "Andrew Ng (DeepLearning.AI)"
    url: "https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance"
    type: "article"
    description: "The four core agentic workflows: Reflection, Tool Use, Planning, Multi-Agent."
  - title: "An IBM Guide to Agentic AI Systems"
    author: "IBM"
    url: "https://www.ibm.com/think/architectures/patterns/agentic-ai"
    type: "article"
    description: "Enterprise agent architecture and orchestration strategies."
  - title: "Agentic AI Course"
    author: "DeepLearning.AI"
    url: "https://www.deeplearning.ai/courses/agentic-ai"
    type: "course"
    description: "Practical implementation of multi-step agentic processes."
  - title: "What is AI Agent Orchestration?"
    author: "IBM Think"
    url: "https://www.ibm.com/think/topics/ai-agent-orchestration"
    type: "article"
    description: "Networks of specialized agents automating complex workflows."
related_knowledge:
  - slug: agents-02-agent-architecture
    title: "Agent Architecture"
    lesson_number: 2
  - slug: agents-06-multi-agent-systems
    title: "Multi-Agent Systems"
    lesson_number: 6
  - slug: agents-18-enterprise-agents
    title: "Enterprise Agent Applications"
    lesson_number: 18
knowledge_refs:
  - slug: "genai-09-retrieval-augmented-generation"
    title: "RAG"
  - slug: "ml-15-reinforcement-learning-from-human-feedback"
    title: "RLHF"
  - slug: "dl-09-attention-mechanisms"
    title: "Attention Mechanisms"
---

# Agent Design Patterns

Design patterns provide proven solutions to common problems in agent development. Understanding these patterns helps you choose the right architecture for your use case and avoid reinventing solutions.

## The Four Core Agentic Workflows

Andrew Ng identifies four foundational patterns that underpin all agentic systems:

### 1. Reflection
The agent examines its own output, critiques it against criteria, and iteratively refines:
```
Generate → Evaluate → Critique → Refine → Evaluate → ...
```
**Use cases:** Code review, document drafting, translation quality improvement.

### 2. Tool Use
The agent calls external tools to gather information or take actions:
```
Reason → Select Tool → Execute → Observe → Reason → ...
```
**Use cases:** Web search, database queries, API calls, code execution.

### 3. Planning
The agent breaks down complex goals into sequenced subtasks before execution:
```
Goal → Decompose → Plan → Execute Step 1 → Execute Step 2 → ...
```
**Use cases:** Multi-file code changes, research investigations, project management.

### 4. Multi-Agent Collaboration
Multiple specialized agents work together, each contributing expertise:
```
Orchestrator → Delegate to Agent A → Delegate to Agent B → Synthesize
```
**Use cases:** Complex software projects, cross-domain research, enterprise workflows.

## Anthropic's Workflow Patterns

Anthropic identifies five architectural patterns for production systems:

### Prompt Chaining
Sequential LLM calls where output feeds input:
```
Extract → Transform → Summarize
```
Best for linear pipelines with clear stages.

### Routing
Classifier directs inputs to specialized handlers:
```
Input → Classify → Handler A (technical) / Handler B (billing) / Handler C (general)
```
Best for systems handling diverse request types.

### Parallelization
Multiple LLM calls execute simultaneously:
```
Input → [LLM A: Sentiment] + [LLM B: Category] + [LLM C: Urgency] → Merge
```
Best for independent subtasks that reduce latency through parallelism.

### Orchestrator-Workers
Central LLM dynamically delegates to worker LLMs:
```
Orchestrator → Analyze → Spawn Worker 1 + Worker 2 + Worker 3 → Synthesize
```
Best for complex tasks where subtask structure isn't known in advance.

### Evaluator-Optimizer
Generator produces, evaluator critiques, cycle repeats:
```
Generator → Output → Evaluator → Feedback → Generator → ...
```
Best for tasks requiring iterative quality improvement.

## Reflection and Self-Correction

### Reflexion Pattern
The agent reflects on failures and adjusts strategy:
```
Attempt → Fail → Reflect → Adjust Strategy → Attempt → ...
```
Key insight: Store reflections in memory to avoid repeating mistakes.

### Chain of Verification
The agent generates an answer, then systematically verifies each claim:
```
Answer → List Claims → Verify Each Claim → Correct Errors → Final Answer
```

## Planning Patterns

### Static Planning
Predefined templates where the LLM fills in steps:
```
Template: [Research] → [Analyze] → [Write] → [Review]
LLM fills in specifics for each stage
```

### Dynamic Planning
The model generates and updates its plan based on feedback:
```
Initial Plan → Execute → Discover Issue → Replan → Execute → ...
```

### Plan-and-Solve
Generate a complete plan first, then execute each step sequentially. Reduces errors by front-loading reasoning.

## Orchestrator Topologies

### Centralized
Single controller manages all workers. Simple to trace but potential bottleneck.

### Decentralized
Task-queue or blackboard style where agents pull work and post results. Fault-tolerant but harder to debug.

### Hierarchical
Master orchestrator manages domain-specific sub-orchestrators. Balances control and scalability.

## Choosing the Right Pattern

| Pattern | Best For | Complexity | Cost |
|---|---|---|---|
| Prompt Chaining | Linear pipelines | Low | Low |
| Routing | Diverse inputs | Medium | Medium |
| Parallelization | Independent subtasks | Medium | Medium-High |
| Orchestrator-Workers | Complex, open-ended tasks | High | High |
| Evaluator-Optimizer | Quality-critical outputs | High | High |

Start simple. Only increase complexity when the simpler pattern demonstrably fails.

---

*References:*
1. Anthropic Engineering, "Building Effective Agents." [Link](https://www.anthropic.com/engineering/building-effective-agents)
2. Andrew Ng, "Agentic Design Patterns," DeepLearning.AI. [Link](https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance)
3. IBM, "An IBM Guide to Agentic AI Systems." [Link](https://www.ibm.com/think/architectures/patterns/agentic-ai)
4. DeepLearning.AI, "Agentic AI Course." [Link](https://www.deeplearning.ai/courses/agentic-ai)
5. IBM Think, "What is AI Agent Orchestration?" [Link](https://www.ibm.com/think/topics/ai-agent-orchestration)
