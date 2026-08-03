---
{
  "title": "What Are AI Agents?",
  "description": "Autonomous systems that perceive, reason, act and observe — the agent loop explained.",
  "type": "lesson",
  "order": 1,
  "duration": "40 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define an AI agent",
    "Describe the perceive-reason-act loop",
    "Contrast agents with plain LLM calls",
    "List where agents add real value"
  ],
  "knowledge_refs": [
    "llm-engineering/llm-11-llm-agents",
    "generative-ai/genai-12-agents-and-tool-use",
    "reinforcement-learning/rl-20-evaluating-rl-agents"
  ],
  "prerequisites": [
    "LLM-01: What Is LLM Engineering?"
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

# AGENTS-01-WHAT-ARE-AI-AGENTS: What Are AI Agents?

## Introduction

Autonomous systems that perceive, reason, act and observe — the agent loop explained. By the end of this lesson you will be able to: Define an AI agent; Describe the perceive-reason-act loop; Contrast agents with plain LLM calls; List where agents add real value.

## Key Concepts

### 1. Define an AI agent

Target: Define an AI agent. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
agent = {
    "perceive": "observe the environment",
    "reason": "decide the next action",
    "act": "call a tool or respond",
    "observe": "read the result and loop",
}
print(agent)
```
### 2. Describe the perceive-reason-act loop

Target: Describe the perceive-reason-act loop. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("LLM call: one-shot. Agent: a loop with tools.")
```
### 3. Contrast agents with plain LLM calls

Target: Contrast agents with plain LLM calls. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
use_cases = ["research", "data analysis", "support triage", "coding"]
for u in use_cases:
    print(f"- {u}")
```
### 4. List where agents add real value

Target: List where agents add real value. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("agents are only as reliable as their tools + evals")
```

## Practice Questions

1. What is the key idea behind "What Are AI Agents?"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain What Are AI Agents? with analogies and real-world examples"
1. "Show me common mistakes beginners make with What Are AI Agents?"
1. "Provide advanced patterns and performance considerations for What Are AI Agents?"

## Key Takeaways

- Master the core ideas of What Are AI Agents? through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
