---
{
  "title": "Deploying Agents",
  "description": "Run agents as services: queues, timeouts, scaling and versioning.",
  "type": "lesson",
  "order": 16,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Serve agents via APIs",
    "Use task queues for long runs",
    "Set timeouts and retries",
    "Version agents with prompts and tools"
  ],
  "knowledge_refs": [
    "ai-agents/agents-15-agent-observability",
    "llm-engineering/llm-11-llm-agents",
    "generative-ai/genai-12-agents-and-tool-use"
  ],
  "prerequisites": [
    "AGENTS-15: Agent Observability"
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

# AGENTS-16-DEPLOYING-AGENTS: Deploying Agents

## Introduction

Run agents as services: queues, timeouts, scaling and versioning. By the end of this lesson you will be able to: Serve agents via APIs; Use task queues for long runs; Set timeouts and retries; Version agents with prompts and tools.

## Key Concepts

### 1. Serve agents via APIs

Target: Serve agents via APIs. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/agent")
def run_agent(task: str):
    return {"status": "queued", "task": task}

print("agent API ready")
```
### 2. Use task queues for long runs

Target: Use task queues for long runs. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import asyncio

# Long tasks belong in a queue, not a request
print("worker: consume tasks -> run agent -> store result")
```
### 3. Set timeouts and retries

Target: Set timeouts and retries. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import time

# Hard timeout beats an infinite loop
start = time.perf_counter()
while time.perf_counter() - start < 30:
    pass
print("timeout enforced")
```
### 4. Version agents with prompts and tools

Target: Version agents with prompts and tools. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("version: prompt + tools + model = the agent artifact")
```

## Practice Questions

1. What is the key idea behind "Deploying Agents"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Deploying Agents with analogies and real-world examples"
1. "Show me common mistakes beginners make with Deploying Agents"
1. "Provide advanced patterns and performance considerations for Deploying Agents"

## Key Takeaways

- Master the core ideas of Deploying Agents through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
