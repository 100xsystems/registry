---
slug: agents-02-agent-architecture
title: "Agent Architecture"
description: "Understanding the design patterns and architectural decisions behind effective AI agent systems."
order: 2
tags:
  - ai-agents
  - agent-architecture
  - react-pattern
  - design-patterns
  - control-flow
prerequisites:
  - agents-01-what-are-ai-agents
references:
  - title: "What is a ReAct Agent?"
    author: "IBM Think"
    url: "https://www.ibm.com/think/topics/react-agent"
    type: "article"
    description: "Explanation of the ReAct paradigm, prompt structures, and scratchpads."
  - title: "Choose a Design Pattern for Your Agentic AI System"
    author: "Google Cloud Architecture Center"
    url: "https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system"
    type: "docs"
    description: "Evaluation of single-agent vs. multi-agent architectures."
  - title: "Building Effective Agents"
    author: "Anthropic Engineering"
    url: "https://www.anthropic.com/engineering/building-effective-agents"
    type: "article"
    description: "Practical guide to agentic design patterns and production trade-offs."
  - title: "Writing Effective Tools for AI Agents"
    author: "Anthropic Engineering"
    url: "https://www.anthropic.com/engineering/writing-tools-for-agents"
    type: "article"
    description: "Best practices for agent-computer interfaces and tool design."
  - title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
    author: "Patrick Lewis et al."
    url: "https://arxiv.org/abs/2005.11401"
    type: "paper"
    description: "Foundational paper on RAG that underpins many agent architectures."
related_knowledge:
  - slug: agents-01-what-are-ai-agents
    title: "What Are AI Agents?"
    lesson_number: 1
  - slug: agents-03-tool-use
    title: "Tool Use"
    lesson_number: 3
  - slug: agents-06-multi-agent-systems
    title: "Multi-Agent Systems"
    lesson_number: 6
knowledge_refs:
  - slug: "llm-01-what-is-llm-engineering"
    title: "Fundamentals of LLMs"
  - slug: "genai-09-rlhf-and-alignment"
    title: "RLHF"
  - slug: "genai-01-what-is-generative-ai"
    title: "What Is Generative AI?"
---

# Agent Architecture

Agent architecture defines how an AI agent's components — reasoning, tools, memory, and control flow — are organized and coordinated. The right architecture determines whether an agent is reliable, efficient, and capable of handling real-world complexity.

## Workflows vs. Agents

Modern agentic systems exist on a spectrum between two extremes:

### Workflows
Systems where LLMs and tools are orchestrated through **predefined code paths**. The developer controls the flow, deciding when each tool is called and how results are processed. Workflows provide:
- Predictability and consistency
- Lower latency for well-defined tasks
- Easier debugging and testing
- Deterministic behavior for production reliability

### Agents
Systems where LLMs **dynamically direct their own execution**, maintaining control over how they accomplish tasks. Agents provide:
- Flexibility for open-ended problems
- Adaptability to novel situations
- Model-driven decision-making
- Ability to handle ambiguity and edge cases

Most production systems use a hybrid approach, choosing the right level of autonomy for each task.

## The ReAct Pattern

**ReAct (Reasoning + Acting)** is the foundational pattern for agentic systems. It integrates chain-of-thought reasoning with external tool execution through an interleaved loop:

1. **Thought:** The LLM verbalizes its reasoning in a "scratchpad" to decompose the task and plan next steps.
2. **Action:** The agent invokes a specific tool or API with structured inputs.
3. **Observation:** The environment returns a result, which feeds back into the next reasoning cycle.

This loop continues until the agent reaches a conclusion or a stopping condition. ReAct reduces hallucinations by grounding models in real-time data, though it incurs higher token consumption due to iterative reasoning.

### ReAct vs. Pure Function Calling

**Function calling** is a paradigm where LLMs output structured JSON arguments directly when they recognize a tool call is needed. It is fast and efficient for predictable, structured tasks.

**ReAct** adds explicit verbal reasoning before acting, making it superior for complex, dynamic problem-solving where adaptability is required.

In practice, most agent frameworks combine both: function calling for the tool invocation mechanism, ReAct-style reasoning for deciding when and how to use tools.

## Common Architecture Patterns

### Prompt Chaining
A sequence of LLM calls where the output of one becomes the input to the next. Simple but effective for linear pipelines like "extract → transform → summarize."

### Routing
An LLM classifier directs inputs to specialized handlers. Useful for support systems that route tickets by category or content type.

### Parallelization
Multiple LLM calls execute simultaneously for independent subtasks, with results merged afterward. Dramatically reduces latency for multi-step workflows.

### Orchestrator-Workers
A central LLM dynamically breaks down tasks and delegates to worker LLMs. Each worker handles a specific subtask independently. This is the dominant pattern for complex agent systems.

### Evaluator-Optimizer
A generator LLM produces output, and an evaluator LLM critiques it. The cycle repeats until quality thresholds are met. Effective for tasks requiring iterative refinement.

## Tool Design Principles

Anthropic's research on "Writing Effective Tools for AI Agents" identifies key principles:

- **Token Efficiency:** Tools should return high-signal context (summaries, filtered results) rather than raw data dumps.
- **Poka-Yoke (Mistake-Proofing):** Design parameters to minimize errors — for example, enforcing absolute file paths instead of relative ones.
- **Namespacing:** Group related tools under prefixes (e.g., `jira_search`, `github_search`) to prevent confusion when models have access to many tools.
- **Clear Descriptions:** Tool descriptions act as instructions for the model — they must be precise about when and how to use each tool.

---

*References:*
1. IBM Think, "What is a ReAct Agent?" [Link](https://www.ibm.com/think/topics/react-agent)
2. Google Cloud Architecture Center, "Choose a Design Pattern for Your Agentic AI System." [Link](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)
3. Anthropic Engineering, "Building Effective Agents." [Link](https://www.anthropic.com/engineering/building-effective-agents)
4. Anthropic Engineering, "Writing Effective Tools for AI Agents." [Link](https://www.anthropic.com/engineering/writing-tools-for-agents)
5. Patrick Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks," NeurIPS 2020. [Link](https://arxiv.org/abs/2005.11401)
