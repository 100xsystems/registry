---
{
  "title": "Agent Architecture",
  "description": "The anatomy of an agent: model, tools, memory, planner and executor.",
  "type": "lesson",
  "order": 2,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Decompose an agent into components",
    "Describe the controller pattern",
    "Explain tool registries",
    "Choose when to use simple vs complex architectures"
  ],
  "knowledge_refs": [
    "ai-agents/agents-02-agent-architecture"
  ],
  "prerequisites": [
    "AGENTS-01: What Are AI Agents?"
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

# AGENTS-02-AGENT-ARCHITECTURE: Agent Architecture

## Introduction

The anatomy of an agent: model, tools, memory, planner and executor. By the end of this lesson you will be able to: Decompose an agent into components; Describe the controller pattern; Explain tool registries; Choose when to use simple vs complex architectures.

## Key Concepts

### 1. Decompose an agent into components

Target: Decompose an agent into components. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
components = {
    "model": "decides actions",
    "tools": "capabilities",
    "memory": "state across steps",
    "planner": "breaks down goals",
}
print(components)
```
### 2. Describe the controller pattern

Target: Describe the controller pattern. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import json

# Tool registry: name -> function
tools = {"search": search_fn, "calc": calc_fn}
print("registered:", list(tools))
```
### 3. Explain tool registries

Target: Explain tool registries. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("start simple: one model + few tools")
```
### 4. Choose when to use simple vs complex architectures

Target: Choose when to use simple vs complex architectures. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("controller: the model decides, the code executes")
```

## Practice Questions

1. What is the key idea behind "Agent Architecture"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Agent Architecture with analogies and real-world examples"
1. "Show me common mistakes beginners make with Agent Architecture"
1. "Provide advanced patterns and performance considerations for Agent Architecture"

## Key Takeaways

- Master the core ideas of Agent Architecture through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
