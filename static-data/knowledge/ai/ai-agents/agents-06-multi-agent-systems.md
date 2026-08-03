---
{
  "title": "Multi-Agent Systems",
  "description": "Specialized agents that collaborate: orchestrators, workers and handoffs.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Design an orchestrator-worker pattern",
    "Implement handoffs between agents",
    "Coordinate shared state",
    "Avoid over-engineering with many agents"
  ],
  "knowledge_refs": [
    "ai-agents/agents-05-memory-systems",
    "reinforcement-learning/rl-16-multi-agent-rl",
    "llm-engineering/llm-11-llm-agents"
  ],
  "prerequisites": [
    "AGENTS-05: Agent Memory Systems"
  ],
  "references": [
    {
      "title": "LangChain Agents",
      "url": "https://python.langchain.com/docs/how_to/#agents",
      "description": "Agent frameworks, tools and memory patterns."
    },
    {
      "title": "OpenAI Agents Documentation",
      "url": "https://platform.openai.com/docs/guides/agents",
      "description": "Function calling and agent loop patterns."
    },
    {
      "title": "ReAct: Synergizing Reasoning and Acting",
      "url": "https://arxiv.org/abs/2210.03629",
      "description": "The paper behind reasoning-acting agent loops."
    },
    {
      "title": "Anthropic — Building Effective Agents",
      "url": "https://www.anthropic.com/research/building-effective-agents",
      "description": "A practical guide to agent architecture."
    },
    {
      "title": "CrewAI Documentation",
      "url": "https://docs.crewai.com/",
      "description": "Multi-agent orchestration framework."
    }
  ]
}
---

# AGENTS-06-MULTI-AGENT-SYSTEMS: Multi-Agent Systems

## Introduction

Specialized agents that collaborate: orchestrators, workers and handoffs. By the end of this lesson you will be able to: Design an orchestrator-worker pattern; Implement handoffs between agents; Coordinate shared state; Avoid over-engineering with many agents.

## Key Concepts

### 1. Design an orchestrator-worker pattern

Target: Design an orchestrator-worker pattern. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
roles = {
    "orchestrator": "routes work",
    "researcher": "gathers facts",
    "writer": "produces output",
}
print(roles)
```
### 2. Implement handoffs between agents

Target: Implement handoffs between agents. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from crewai import Agent, Task, Crew

researcher = Agent(role="researcher", goal="find facts", backstory="curious")
crew = Crew(agents=[researcher], tasks=[Task(description="research X", agent=researcher)])
print("crew ready")
```
### 3. Coordinate shared state

Target: Coordinate shared state. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("handoff: one agent delegates to another with context")
```
### 4. Avoid over-engineering with many agents

Target: Avoid over-engineering with many agents. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("more agents = more failure modes; start with one")
```

## Practice Questions

1. What is the key idea behind "Multi-Agent Systems"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Multi-Agent Systems with analogies and real-world examples"
1. "Show me common mistakes beginners make with Multi-Agent Systems"
1. "Provide advanced patterns and performance considerations for Multi-Agent Systems"

## Key Takeaways

- Master the core ideas of Multi-Agent Systems through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
