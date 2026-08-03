---
{
  "title": "Agent Observability",
  "description": "Trace every thought, tool call and step — because agents fail in the middle, not the end.",
  "type": "lesson",
  "order": 15,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Log complete agent traces",
    "Visualize trajectories",
    "Alert on stuck loops",
    "Replay failures"
  ],
  "knowledge_refs": [
    "ai-agents/agents-15-agent-observability"
  ],
  "prerequisites": [
    "AGENTS-12: Evaluating Agents"
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

# AGENTS-15-AGENT-OBSERVABILITY: Agent Observability

## Introduction

Trace every thought, tool call and step — because agents fail in the middle, not the end. By the end of this lesson you will be able to: Log complete agent traces; Visualize trajectories; Alert on stuck loops; Replay failures.

## Key Concepts

### 1. Log complete agent traces

Target: Log complete agent traces. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
trace = {
    "steps": [
        {"thought": "...", "tool": "search", "args": "x", "result": "..."},
    ],
    "cost": 0.02,
    "duration_ms": 1800,
}
print(trace)
```
### 2. Visualize trajectories

Target: Visualize trajectories. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import time

for i in range(3):
    print(f"[trace] step {i}")
    time.sleep(0.01)
```
### 3. Alert on stuck loops

Target: Alert on stuck loops. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("alert: no progress after N steps")
```
### 4. Replay failures

Target: Replay failures. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("replay: same task, same version, same failure")
```

## Practice Questions

1. What is the key idea behind "Agent Observability"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Agent Observability with analogies and real-world examples"
1. "Show me common mistakes beginners make with Agent Observability"
1. "Provide advanced patterns and performance considerations for Agent Observability"

## Key Takeaways

- Master the core ideas of Agent Observability through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
