---
{
  "title": "Agent Safety & Control",
  "description": "Constrain autonomy: limits, approvals, sandboxes and fail-safes.",
  "type": "lesson",
  "order": 13,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Design autonomy limits",
    "Require human approval for risky actions",
    "Sandbox tool execution",
    "Add circuit breakers"
  ],
  "knowledge_refs": [
    "ai-agents/agents-12-evaluating-agents",
    "ai-safety/safety-21-roadmap",
    "ai-safety/safety-01-why-ai-safety"
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

# AGENTS-13-SAFETY-AND-CONTROL: Agent Safety & Control

## Introduction

Constrain autonomy: limits, approvals, sandboxes and fail-safes. By the end of this lesson you will be able to: Design autonomy limits; Require human approval for risky actions; Sandbox tool execution; Add circuit breakers.

## Key Concepts

### 1. Design autonomy limits

Target: Design autonomy limits. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
limits = {"max_steps": 10, "max_cost": 1.0, "approval_required": ["send_email", "delete"]}
print(limits)
```
### 2. Require human approval for risky actions

Target: Require human approval for risky actions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("risky tools: pause and ask the human")
```
### 3. Sandbox tool execution

Target: Sandbox tool execution. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("sandbox: agents run in isolated environments")
```
### 4. Add circuit breakers

Target: Add circuit breakers. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("circuit breaker: stop the loop after repeated failures")
```

## Practice Questions

1. What is the key idea behind "Agent Safety & Control"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Agent Safety & Control with analogies and real-world examples"
1. "Show me common mistakes beginners make with Agent Safety & Control"
1. "Provide advanced patterns and performance considerations for Agent Safety & Control"

## Key Takeaways

- Master the core ideas of Agent Safety & Control through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
