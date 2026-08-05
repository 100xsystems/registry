---
slug: agents-01-what-are-ai-agents
title: "What Are AI Agents?"
description: "Understanding the fundamental concept of AI agents — autonomous systems that perceive, reason, and act to accomplish goals."
order: 1
tags:
  - ai-agents
  - agent-fundamentals
  - llm-agents
  - autonomous-systems
  - perception-action-loop
prerequisites: []
references:
  - title: "LLM Powered Autonomous Agents"
    author: "Lilian Weng"
    url: "https://lilianweng.github.io/posts/2023-06-23-agent/"
    type: "article"
    description: "Foundational taxonomy of LLM agent systems covering planning, memory, and tool use."
  - title: "Building Effective Agents"
    author: "Anthropic Engineering"
    url: "https://www.anthropic.com/engineering/building-effective-agents"
    type: "article"
    description: "Practical guide to agentic design patterns and workflows vs. agents."
  - title: "Agentic AI Course"
    author: "DeepLearning.AI"
    url: "https://www.deeplearning.ai/courses/agentic-ai"
    type: "course"
    description: "Core design patterns for agentic AI systems."
  - title: "LangChain Deep Agents"
    author: "LangChain"
    url: "https://docs.langchain.com/oss/python/deepagents/overview"
    type: "docs"
    description: "Advanced agent runtime with virtual filesystems and subagents."
  - title: "Human Compatible: Artificial Intelligence and the Problem of Control"
    author: "Stuart Russell"
    url: "https://www.amazon.com/Human-Compatible-Artificial-Intelligence-Problem-Control/dp/0525558616"
    type: "book"
    description: "Foundational text on AI alignment and the design of beneficial AI systems."
related_knowledge:
  - slug: agents-02-agent-architecture
    title: "Agent Architecture"
    lesson_number: 2
  - slug: agents-03-tool-use
    title: "Tool Use"
    lesson_number: 3
  - slug: agents-04-reasoning-and-planning
    title: "Reasoning and Planning"
    lesson_number: 4
knowledge_refs:
  - slug: "ml-01-what-is-machine-learning"
    title: "What Is Machine Learning?"
  - slug: "llm-01-what-is-llm-engineering"
    title: "Fundamentals of LLMs"
  - slug: "dl-01-what-is-deep-learning"
    title: "Neural Network Foundations"
---

# What Are AI Agents?

An AI agent is an autonomous software system powered by a large language model (LLM) that can perceive its environment, reason about goals, use external tools, and execute multi-step tasks — all without requiring continuous human intervention for every decision.

## The Core Equation

As articulated by Lilian Weng at OpenAI, an autonomous agent system can be formalized as:

**Agent = LLM (Brain) + Planning + Memory + Tool Use**

This equation captures the four essential components that distinguish agents from simple chatbots or static pipelines:

- **LLM (Brain):** The language model serves as the central reasoning engine, interpreting inputs, generating plans, and deciding actions.
- **Planning:** The ability to decompose complex goals into manageable subtasks, sequence them logically, and adapt when things go wrong.
- **Memory:** Both short-term (conversation context) and long-term (persistent knowledge) storage that enables continuity across interactions.
- **Tool Use:** The capacity to interact with external systems — APIs, databases, file systems, web browsers — to gather information and take actions in the real world.

## How Agents Interact with Their Environment

Agents operate through a continuous **Perception-Action Loop**, often structured as the ReAct framework (Reasoning + Acting):

1. **Perception:** The agent receives input from the environment — user prompts, tool outputs, error messages, or file contents.
2. **Reasoning:** The LLM processes the input, reflects on current progress, and determines what needs to happen next.
3. **Action:** The agent invokes a specific action — calling an API, writing a file, running a shell command, or searching the web.
4. **Observation:** The environment returns results — success, data, or error — which feeds back into the next reasoning cycle.

This loop continues until the agent determines the goal has been achieved or a stopping condition is met.

## Types of Agents

### Reactive Agents
Respond directly to stimuli using condition-action rules without maintaining deep internal models or complex multi-step plans. They are fast and predictable but limited in handling novel situations.

### Deliberative Agents
Maintain internal state, engage in explicit planning, break down large goals into subgoals, and evaluate consequences before acting. Examples include Plan-and-Solve and Tree of Thoughts patterns.

### Learning Agents
Improve performance over time through feedback loops, reflection (such as Reflexion or Chain of Hindsight), or fine-tuning based on past successes and failures.

### Hybrid Agents
Combine reactive speed for immediate triggers with deliberative planning for complex, long-horizon tasks. This is the dominant pattern in modern frameworks like LangChain and Anthropic's agent architectures.

## Agents vs. Traditional Software

| Dimension | Traditional Software | AI Agents |
|---|---|---|
| Execution Path | Deterministic, hardcoded control flows | Non-deterministic, model-driven pathways |
| Handling Ambiguity | Fails on unstructured inputs | Interprets ambiguous natural language |
| Error Handling | Requires explicit exception catchers | Self-reflects and retries with alternatives |
| Task Scope | Routine, repetitive automation | Open-ended, multi-step problem solving |
| Verification | Easy to unit test | Requires probabilistic evaluation and monitoring |

## Key Applications

**Customer Support:** Agents check order statuses, pull customer data, process refunds, and verify resolutions autonomously by blending conversation with backend tool integrations.

**Software Engineering:** Agents parse pull requests, locate relevant source files across repositories, write code edits, run tests, and iterate based on failures — as demonstrated by SWE-bench solvers.

**Deep Research:** Agents execute multi-step web searches, crawl pages, extract data, synthesize conflicting information, and compile comprehensive structured reports.

**Data Analysis:** Automated data wrangling, Python script execution in sandboxed interpreters, database queries, and on-the-fly visualization dashboards.

## The Agent-Computer Interface

Anthropic's research on "Building Effective Agents" draws an important distinction between **workflows** and **agents**:

- **Workflows** are systems where LLMs and tools are orchestrated through predefined, hardcoded code paths — providing predictability and consistency.
- **Agents** are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

Most production systems use a spectrum between these extremes, choosing the right level of autonomy for each task.

---

*References:*
1. Lilian Weng, "LLM Powered Autonomous Agents," OpenAI Blog, 2023. [Link](https://lilianweng.github.io/posts/2023-06-23-agent/)
2. Anthropic Engineering, "Building Effective Agents," 2024. [Link](https://www.anthropic.com/engineering/building-effective-agents)
3. DeepLearning.AI, "Agentic AI Course." [Link](https://www.deeplearning.ai/courses/agentic-ai)
4. LangChain, "Deep Agents Overview." [Link](https://docs.langchain.com/oss/python/deepagents/overview)
5. Stuart Russell, *Human Compatible: Artificial Intelligence and the Problem of Control*, Viking, 2019. [Link](https://www.amazon.com/Human-Compatible-Artificial-Intelligence-Problem-Control/dp/0525558616)
