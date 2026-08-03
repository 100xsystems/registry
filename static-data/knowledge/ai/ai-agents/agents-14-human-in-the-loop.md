---
{
  "title": "Human-in-the-Loop Patterns",
  "description": "Design agents that escalate and collaborate with people instead of acting alone.",
  "type": "lesson",
  "order": 14,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Design escalation triggers",
    "Support approval workflows",
    "Collect corrections",
    "Learn from human feedback"
  ],
  "knowledge_refs": [
    "ai-agents/agents-13-safety-and-control",
    "llm-engineering/llm-11-llm-agents",
    "generative-ai/genai-12-agents-and-tool-use"
  ],
  "prerequisites": [
    "AGENTS-13: Agent Safety & Control"
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

# AGENTS-14-HUMAN-IN-THE-LOOP: Human-in-the-Loop Patterns

## Introduction

Design agents that escalate and collaborate with people instead of acting alone. By the end of this lesson you will be able to: Design escalation triggers; Support approval workflows; Collect corrections; Learn from human feedback.

## Key Concepts

### 1. Design escalation triggers

Target: Design escalation triggers. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
def maybe_escalate(confidence):
    return "human" if confidence < 0.7 else "agent"

print(maybe_escalate(0.5))
```
### 2. Support approval workflows

Target: Support approval workflows. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("corrections become training data and eval cases")
```
### 3. Collect corrections

Target: Collect corrections. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("approval: agent proposes, human disposes")
```
### 4. Learn from human feedback

Target: Learn from human feedback. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("feedback loop: every escalation is a reviewable event")
```

## Practice Questions

1. What is the key idea behind "Human-in-the-Loop Patterns"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Human-in-the-Loop Patterns with analogies and real-world examples"
1. "Show me common mistakes beginners make with Human-in-the-Loop Patterns"
1. "Provide advanced patterns and performance considerations for Human-in-the-Loop Patterns"

## Key Takeaways

- Master the core ideas of Human-in-the-Loop Patterns through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
