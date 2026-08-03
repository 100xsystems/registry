---
{
  "title": "Building LLM Agents",
  "description": "Connect models to tools and loops: the agent pattern in production.",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define the agent loop",
    "Give agents tools and constraints",
    "Cap iterations for safety",
    "Trace agent behavior"
  ],
  "knowledge_refs": [
    "llm-engineering/llm-10-function-calling",
    "ai-agents/agents-01-what-are-ai-agents",
    "ai-agents/agents-21-roadmap"
  ],
  "prerequisites": [
    "LLM-10: Function Calling & Structured Outputs"
  ],
  "references": [
    {
      "title": "OpenAI Platform Docs",
      "url": "https://platform.openai.com/docs",
      "description": "API reference for chat, embeddings, function calling and vision."
    },
    {
      "title": "Anthropic Documentation",
      "url": "https://docs.anthropic.com/",
      "description": "Claude API docs including prompt engineering guides."
    },
    {
      "title": "Hugging Face Transformers",
      "url": "https://huggingface.co/docs/transformers",
      "description": "Models, tokenizers and pipelines for LLM work."
    },
    {
      "title": "LangChain Documentation",
      "url": "https://python.langchain.com/docs",
      "description": "Frameworks for RAG, agents and LLM applications."
    },
    {
      "title": "vLLM Documentation",
      "url": "https://docs.vllm.ai/",
      "description": "High-throughput LLM serving and inference."
    }
  ]
}
---

# LLM-11-LLM-AGENTS: Building LLM Agents

## Introduction

Connect models to tools and loops: the agent pattern in production. By the end of this lesson you will be able to: Define the agent loop; Give agents tools and constraints; Cap iterations for safety; Trace agent behavior.

## Key Concepts

### 1. Define the agent loop

Target: Define the agent loop. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
def agent_loop(task, tools, max_steps=5):
    messages = [{"role": "user", "content": task}]
    for step in range(max_steps):
        reply = call_model(messages, tools)
        if reply.finished:
            return reply.answer
        messages.append(reply.as_message())
        messages.append(run_tool(reply.tool_call))
    return "reached step limit"

print(agent_loop)
```
### 2. Give agents tools and constraints

Target: Give agents tools and constraints. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import time

for step in range(3):
    print(f"step {step}: model -> tool -> observe")
    time.sleep(0.05)
```
### 3. Cap iterations for safety

Target: Cap iterations for safety. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
guardrails = {"max_steps": 5, "tool_allowlist": ["search"], "timeout": 30}
print(guardrails)
```
### 4. Trace agent behavior

Target: Trace agent behavior. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("log every step: reasoning, tool call, result")
```

## Practice Questions

1. What is the key idea behind "Building LLM Agents"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Building LLM Agents with analogies and real-world examples"
1. "Show me common mistakes beginners make with Building LLM Agents"
1. "Provide advanced patterns and performance considerations for Building LLM Agents"

## Key Takeaways

- Master the core ideas of Building LLM Agents through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
