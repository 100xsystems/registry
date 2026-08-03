---
{
  "title": "Agent Cost & Scale",
  "description": "Make agents affordable: token budgets, model routing and parallel workers.",
  "type": "lesson",
  "order": 19,
  "duration": "50 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Model agent token cost",
    "Route steps to cheaper models",
    "Parallelize independent tasks",
    "Budget per user or task"
  ],
  "knowledge_refs": [
    "ai-agents/agents-18-enterprise-agents",
    "llm-engineering/llm-11-llm-agents",
    "generative-ai/genai-12-agents-and-tool-use"
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

# AGENTS-19-AGENT-COST-AND-SCALE: Agent Cost & Scale

## Introduction

Make agents affordable: token budgets, model routing and parallel workers. By the end of this lesson you will be able to: Model agent token cost; Route steps to cheaper models; Parallelize independent tasks; Budget per user or task.

## Key Concepts

### 1. Model agent token cost

Target: Model agent token cost. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
steps = 8
tokens_per_step = 800
cost = steps * tokens_per_step / 1000 * 0.00015
print("cost per task:", round(cost, 4))
```
### 2. Route steps to cheaper models

Target: Route steps to cheaper models. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("simple steps: small model. hard steps: big model.")
```
### 3. Parallelize independent tasks

Target: Parallelize independent tasks. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import asyncio

async def run_many(tasks):
    return await asyncio.gather(*[run_agent(t) for t in tasks])

print("parallel workers ready")
```
### 4. Budget per user or task

Target: Budget per user or task. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("per-user budget caps runaway spend")
```

## Practice Questions

1. What is the key idea behind "Agent Cost & Scale"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Agent Cost & Scale with analogies and real-world examples"
1. "Show me common mistakes beginners make with Agent Cost & Scale"
1. "Provide advanced patterns and performance considerations for Agent Cost & Scale"

## Key Takeaways

- Master the core ideas of Agent Cost & Scale through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
