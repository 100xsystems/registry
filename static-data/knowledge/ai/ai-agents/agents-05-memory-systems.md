---
{
  "title": "Agent Memory Systems",
  "description": "Working memory, long-term memory and retrieval — state that persists across turns.",
  "type": "lesson",
  "order": 5,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Distinguish short-term and long-term memory",
    "Store conversation state",
    "Retrieve relevant memories",
    "Compress and summarize history"
  ],
  "knowledge_refs": [
    "ai-agents/agents-04-reasoning-and-planning",
    "llm-engineering/llm-11-llm-agents",
    "generative-ai/genai-12-agents-and-tool-use"
  ],
  "prerequisites": [
    "AGENTS-04: Reasoning & Planning (ReAct)"
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

# AGENTS-05-MEMORY-SYSTEMS: Agent Memory Systems

## Introduction

Working memory, long-term memory and retrieval — state that persists across turns. By the end of this lesson you will be able to: Distinguish short-term and long-term memory; Store conversation state; Retrieve relevant memories; Compress and summarize history.

## Key Concepts

### 1. Distinguish short-term and long-term memory

Target: Distinguish short-term and long-term memory. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
memory = {
    "working": "current task context",
    "episodic": "past conversations",
    "semantic": "facts about the user",
}
print(memory)
```
### 2. Store conversation state

Target: Store conversation state. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import redis

r = redis.Redis()
r.set("agent:42:preferences", "prefers concise answers")
print("stored:", r.get("agent:42:preferences"))
```
### 3. Retrieve relevant memories

Target: Retrieve relevant memories. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("retrieve memories semantically, not by recency alone")
```
### 4. Compress and summarize history

Target: Compress and summarize history. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("summarize old turns to keep the window small")
```

## Practice Questions

1. What is the key idea behind "Agent Memory Systems"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Agent Memory Systems with analogies and real-world examples"
1. "Show me common mistakes beginners make with Agent Memory Systems"
1. "Provide advanced patterns and performance considerations for Agent Memory Systems"

## Key Takeaways

- Master the core ideas of Agent Memory Systems through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
