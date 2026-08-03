---
{
  "title": "Agent Design Patterns",
  "description": "Reusable blueprints: reflection, tool use, planning, multi-agent collaboration.",
  "type": "lesson",
  "order": 17,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Identify the core agent patterns",
    "Apply reflection for self-improvement",
    "Use planner-executor separation",
    "Choose a pattern by task type"
  ],
  "knowledge_refs": [
    "ai-agents/agents-17-agent-design-patterns"
  ],
  "prerequisites": [
    "AGENTS-06: Multi-Agent Systems"
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

# AGENTS-17-AGENT-DESIGN-PATTERNS: Agent Design Patterns

## Introduction

Reusable blueprints: reflection, tool use, planning, multi-agent collaboration. By the end of this lesson you will be able to: Identify the core agent patterns; Apply reflection for self-improvement; Use planner-executor separation; Choose a pattern by task type.

## Key Concepts

### 1. Identify the core agent patterns

Target: Identify the core agent patterns. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
patterns = ["reflection", "tool use", "planning", "multi-agent", "evaluator-optimizer"]
for p in patterns:
    print(f"- {p}")
```
### 2. Apply reflection for self-improvement

Target: Apply reflection for self-improvement. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("reflection: generate, critique, regenerate")
```
### 3. Use planner-executor separation

Target: Use planner-executor separation. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("planner: plan steps, executor: run them")
```
### 4. Choose a pattern by task type

Target: Choose a pattern by task type. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("match the pattern to the task's uncertainty")
```

## Practice Questions

1. What is the key idea behind "Agent Design Patterns"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Agent Design Patterns with analogies and real-world examples"
1. "Show me common mistakes beginners make with Agent Design Patterns"
1. "Provide advanced patterns and performance considerations for Agent Design Patterns"

## Key Takeaways

- Master the core ideas of Agent Design Patterns through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
