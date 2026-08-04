---
slug: agents-04-reasoning-and-planning
title: "Reasoning & Planning (ReAct)"
description: "How agents think — ReAct, Chain-of-Thought, Plan-and-Execute, Tree-of-Thoughts, and reflection patterns."
order: 4
tags:
  - ai-agents
  - reasoning
  - planning
  - react
  - chain-of-thought
prerequisites:
  - agents-03-tool-use
  - agents-02-agent-architecture
knowledge_refs:
  - agents-03-tool-use
  - agents-05-memory-systems
references:
  - title: "ReAct: Synergizing Reasoning and Acting"
    url: "https://arxiv.org/abs/2210.03629"
    notes: "Original ReAct paper"
  - title: "Chain-of-Thought Prompting"
    url: "https://arxiv.org/abs/2201.11903"
    notes: "Wei et al. on reasoning"
  - title: "Tree of Thoughts"
    url: "https://arxiv.org/abs/2305.10601"
    notes: "Exploring multiple reasoning paths"
  - title: "Reflexion: Language Agents with Verbal Reinforcement"
    url: "https://arxiv.org/abs/2303.11366"
    notes: "Self-reflection for agents"
  - title: "Building Effective Agents (Anthropic)"
    url: "https://www.anthropic.com/engineering/building-effective-ai-agents"
    notes: "Practical agent design patterns"
---

# Reasoning & Planning (ReAct)

Agents need to think before they act. This lesson covers the reasoning frameworks that let agents plan, reflect, and iterate toward their goals.

## ReAct (Reasoning + Acting)

The most influential agent framework. Alternates between thinking and doing:

```
Thought: I need to find the population of France
Action: search("population of France 2024")
Observation: France has approximately 68 million people
Thought: Now I can answer the user's question
Answer: France has about 68 million people
```

### Why ReAct Works
- **Transparent**: you can see the agent's reasoning
- **Flexible**: adapts based on observations
- **Grounded**: actions provide real-world information

### Limitations
- One LLM call per step (expensive)
- Can get stuck in loops
- No global planning

## Chain-of-Thought (CoT)

Force step-by-step reasoning before acting:

```python
prompt = """
Let me think through this step by step:

1. First, I need to understand what the user is asking
2. Then, I need to identify what information I'm missing
3. Next, I'll determine the best tool to get that information
4. Finally, I'll synthesize an answer

User question: {question}
"""
```

### CoT Variants
- **Zero-shot CoT**: "Let's think step by step"
- **Few-shot CoT**: exemplars with reasoning traces
- **Self-consistency**: sample multiple CoT paths, majority vote

## Plan-and-Execute

Separate planning from execution:

```python
# Phase 1: Plan
plan = planner_llm.generate("""
Create a step-by-step plan to: {user_goal}

Available tools: {tool_descriptions}
""")
# Returns: [Step1, Step2, Step3]

# Phase 2: Execute
for step in plan:
    result = executor_llm.execute(step)
    context.update(step, result)
```

### Advantages
- Fewer LLM calls (plan once, execute many)
- Parallelizable execution
- Clear progress tracking

### Disadvantages
- Less adaptable if plan is wrong
- Needs re-planning mechanism

## Tree of Thoughts (ToT)

Explore multiple reasoning paths simultaneously:

```
         Root Problem
        /      |      \
    Path A   Path B   Path C
    /    \      |      /    \
  A1    A2     B1    C1    C2
  ✓     ✗      ✓     ✗     ✓
```

- Evaluate each branch
- Prune unpromising paths
- Backtrack when stuck

## Reflection & Self-Critique

Agents that learn from their mistakes:

```python
def reflect_and_improve(task, attempt, feedback):
    reflection = llm.generate(f"""
    I attempted: {attempt}
    The result was: {feedback}
    What went wrong? What should I do differently?
    """)
    improved = llm.generate(f"""
    Based on this reflection: {reflection}
    Try again with: {task}
    """)
    return improved
```

### Reflexion Pattern
1. Execute task
2. Evaluate result
3. Generate verbal reflection
4. Use reflection to improve next attempt
5. Repeat until success

## Choosing a Framework

| Framework | Best For | Complexity |
|-----------|----------|------------|
| **ReAct** | Simple tool-use tasks | Low |
| **CoT** | Reasoning without tools | Low |
| **Plan-and-Execute** | Complex multi-step tasks | Medium |
| **ToT** | Exploration, creative tasks | High |
| **Reflexion** | Tasks requiring self-correction | Medium |

## Key Takeaways

1. ReAct is the most widely used agent reasoning framework
2. Chain-of-Thought enables transparent step-by-step reasoning
3. Plan-and-Execute separates planning from execution for efficiency
4. Tree of Thoughts explores multiple paths for complex problems
5. Reflection helps agents learn from mistakes and improve
