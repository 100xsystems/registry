---
{
  "title": "Evaluating Agents",
  "description": "Measure agent quality: task success, trajectory quality and cost.",
  "type": "lesson",
  "order": 12,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define task success metrics",
    "Evaluate trajectories, not just outcomes",
    "Build a task suite",
    "Track cost per task"
  ],
  "knowledge_refs": [
    "reinforcement-learning/rl-20-evaluating-rl-agents",
    "ai-agents/agents-11-rag-agents",
    "deep-learning/dl-20-evaluating-deep-models"
  ],
  "prerequisites": [
    "AGENTS-07: Building Agents with LangChain"
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

# AGENTS-12-EVALUATING-AGENTS: Evaluating Agents

## Introduction

Measure agent quality: task success, trajectory quality and cost. By the end of this lesson you will be able to: Define task success metrics; Evaluate trajectories, not just outcomes; Build a task suite; Track cost per task.

## Key Concepts

### 1. Define task success metrics

Target: Define task success metrics. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

success = np.array([1, 1, 0, 1, 0])
print("task success rate:", success.mean())
```
### 2. Evaluate trajectories, not just outcomes

Target: Evaluate trajectories, not just outcomes. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("a successful task can still waste 10x the steps")
```
### 3. Build a task suite

Target: Build a task suite. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
tasks = [
    {"goal": "find the CEO of OpenAI", "expected": "Sam Altman"},
    {"goal": "sum 2 and 3", "expected": "5"},
]
print("task suite:", len(tasks))
```
### 4. Track cost per task

Target: Track cost per task. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("cost budget: tokens + tool calls per task")
```

## Practice Questions

1. What is the key idea behind "Evaluating Agents"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Evaluating Agents with analogies and real-world examples"
1. "Show me common mistakes beginners make with Evaluating Agents"
1. "Provide advanced patterns and performance considerations for Evaluating Agents"

## Key Takeaways

- Master the core ideas of Evaluating Agents through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
