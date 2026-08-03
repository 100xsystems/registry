---
{
  "title": "RAG Agents",
  "description": "Agents that decide when and what to retrieve — retrieval as a tool, not a fixed step.",
  "type": "lesson",
  "order": 11,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Expose retrieval as an agent tool",
    "Let the agent plan searches",
    "Iterate on queries",
    "Ground answers in retrieved content"
  ],
  "knowledge_refs": [
    "ai-agents/agents-11-rag-agents"
  ],
  "prerequisites": [
    "LLM-08: Advanced RAG"
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

# AGENTS-11-RAG-AGENTS: RAG Agents

## Introduction

Agents that decide when and what to retrieve — retrieval as a tool, not a fixed step. By the end of this lesson you will be able to: Expose retrieval as an agent tool; Let the agent plan searches; Iterate on queries; Ground answers in retrieved content.

## Key Concepts

### 1. Expose retrieval as an agent tool

Target: Expose retrieval as an agent tool. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
def retrieve(query: str) -> list[dict]:
    return [{"title": "doc1", "text": "..."}]

print("retrieval tool ready")
```
### 2. Let the agent plan searches

Target: Let the agent plan searches. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("agent asks: do I need to search? what should I search for?")
```
### 3. Iterate on queries

Target: Iterate on queries. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("multiple searches beat one big query")
```
### 4. Ground answers in retrieved content

Target: Ground answers in retrieved content. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("final answer cites retrieved chunks")
```

## Practice Questions

1. What is the key idea behind "RAG Agents"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain RAG Agents with analogies and real-world examples"
1. "Show me common mistakes beginners make with RAG Agents"
1. "Provide advanced patterns and performance considerations for RAG Agents"

## Key Takeaways

- Master the core ideas of RAG Agents through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
