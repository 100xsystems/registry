---
{
  "title": "Reasoning & Planning (ReAct)",
  "description": "Interleave thought, action and observation — the ReAct pattern that powers modern agents.",
  "type": "lesson",
  "order": 4,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain the ReAct loop",
    "Write reasoning prompts",
    "Implement a ReAct-style agent",
    "Plan multi-step tasks"
  ],
  "knowledge_refs": [
    "ai-agents/agents-04-reasoning-and-planning"
  ],
  "prerequisites": [
    "AGENTS-03: Tool Use & Function Calling"
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

# AGENTS-04-REASONING-AND-PLANNING: Reasoning & Planning (ReAct)

## Introduction

Interleave thought, action and observation — the ReAct pattern that powers modern agents. By the end of this lesson you will be able to: Explain the ReAct loop; Write reasoning prompts; Implement a ReAct-style agent; Plan multi-step tasks.

## Key Concepts

### 1. Explain the ReAct loop

Target: Explain the ReAct loop. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
react = ["Thought", "Action", "Observation", "Thought", "Action", "Final"]
print(react)
```
### 2. Write reasoning prompts

Target: Write reasoning prompts. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
prompt = """You answer questions using tools.\n\nThought: what do I need?\nAction: search[query]\nObservation: result\nAnswer: ...\n"""
print(prompt)
```
### 3. Implement a ReAct-style agent

Target: Implement a ReAct-style agent. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import time

state = "need current price"
for step in range(3):
    print(f"Thought -> Action -> Observation (step {step})")
    time.sleep(0.05)
```
### 4. Plan multi-step tasks

Target: Plan multi-step tasks. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("plan-then-execute: decompose a big task into steps")
```

## Practice Questions

1. What is the key idea behind "Reasoning & Planning (ReAct)"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Reasoning & Planning (ReAct) with analogies and real-world examples"
1. "Show me common mistakes beginners make with Reasoning & Planning (ReAct)"
1. "Provide advanced patterns and performance considerations for Reasoning & Planning (ReAct)"

## Key Takeaways

- Master the core ideas of Reasoning & Planning (ReAct) through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
