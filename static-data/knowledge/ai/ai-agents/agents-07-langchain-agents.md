---
{
  "title": "Building Agents with LangChain",
  "description": "Compose agents with the LangChain ecosystem: tools, memory and executors.",
  "type": "lesson",
  "order": 7,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create tools with @tool",
    "Bind tools to a chat model",
    "Run an agent loop",
    "Stream agent steps"
  ],
  "knowledge_refs": [
    "ai-agents/agents-07-langchain-agents"
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

# AGENTS-07-LANGCHAIN-AGENTS: Building Agents with LangChain

## Introduction

Compose agents with the LangChain ecosystem: tools, memory and executors. By the end of this lesson you will be able to: Create tools with @tool; Bind tools to a chat model; Run an agent loop; Stream agent steps.

## Key Concepts

### 1. Create tools with @tool

Target: Create tools with @tool. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from langchain_core.tools import tool

@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

print(multiply.name, "|", multiply.description[:40])
```
### 2. Bind tools to a chat model

Target: Bind tools to a chat model. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
print("model ready")
```
### 3. Run an agent loop

Target: Run an agent loop. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
tools = [multiply]
print("bound tools:", len(tools))
```
### 4. Stream agent steps

Target: Stream agent steps. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("run: model decides tool calls, loop executes them")
```

## Practice Questions

1. What is the key idea behind "Building Agents with LangChain"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Building Agents with LangChain with analogies and real-world examples"
1. "Show me common mistakes beginners make with Building Agents with LangChain"
1. "Provide advanced patterns and performance considerations for Building Agents with LangChain"

## Key Takeaways

- Master the core ideas of Building Agents with LangChain through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
