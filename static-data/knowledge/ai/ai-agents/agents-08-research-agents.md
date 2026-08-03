---
{
  "title": "Building a Research Agent",
  "description": "A practical build: gather sources, synthesize findings, cite everything.",
  "type": "lesson",
  "order": 8,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Plan a research workflow",
    "Query search and fetch pages",
    "Synthesize with citations",
    "Handle unreliable sources"
  ],
  "knowledge_refs": [
    "ai-agents/agents-08-research-agents"
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

# AGENTS-08-RESEARCH-AGENTS: Building a Research Agent

## Introduction

A practical build: gather sources, synthesize findings, cite everything. By the end of this lesson you will be able to: Plan a research workflow; Query search and fetch pages; Synthesize with citations; Handle unreliable sources.

## Key Concepts

### 1. Plan a research workflow

Target: Plan a research workflow. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
workflow = ["query", "fetch", "extract", "synthesize", "cite"]
print(workflow)
```
### 2. Query search and fetch pages

Target: Query search and fetch pages. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
def search(query: str) -> list[str]:
    return ["https://example.com/1", "https://example.com/2"]

print("results:", search("llm agents"))
```
### 3. Synthesize with citations

Target: Synthesize with citations. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import re

# Strip HTML before summarizing
clean = re.sub(r"<[^>]+>", "", "<p>Hello</p>")
print(clean)
```
### 4. Handle unreliable sources

Target: Handle unreliable sources. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("cite sources: every claim links back to a fetched page")
```

## Practice Questions

1. What is the key idea behind "Building a Research Agent"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Building a Research Agent with analogies and real-world examples"
1. "Show me common mistakes beginners make with Building a Research Agent"
1. "Provide advanced patterns and performance considerations for Building a Research Agent"

## Key Takeaways

- Master the core ideas of Building a Research Agent through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
