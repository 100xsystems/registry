---
{
  "title": "Agents & Tool Use",
  "description": "Let models call functions, use tools, and loop until the job is done.",
  "type": "lesson",
  "order": 12,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain function calling",
    "Define an agent loop (reason → act → observe)",
    "Build a simple tool-using agent",
    "Manage loops and error cases safely"
  ],
  "knowledge_refs": [
    "generative-ai/genai-11-embeddings-and-vector-databases",
    "ai-agents/agents-01-what-are-ai-agents",
    "ai-agents/agents-21-roadmap"
  ],
  "prerequisites": [
    "GENAI-04: Prompt Engineering"
  ],
  "references": [
    {
      "title": "Hugging Face NLP Course",
      "url": "https://huggingface.co/learn/nlp-course",
      "description": "Transformers, fine-tuning and LLM fundamentals with hands-on code."
    },
    {
      "title": "OpenAI Documentation",
      "url": "https://platform.openai.com/docs",
      "description": "API reference for GPT models, embeddings and function calling."
    },
    {
      "title": "Attention Is All You Need",
      "url": "https://arxiv.org/abs/1706.03762",
      "description": "The Transformer paper that made generative AI possible."
    },
    {
      "title": "LangChain Documentation",
      "url": "https://python.langchain.com/docs",
      "description": "Frameworks for RAG, agents and LLM applications."
    },
    {
      "title": "DeepLearning.AI Short Courses",
      "url": "https://www.deeplearning.ai/short-courses/",
      "description": "Practical AI courses from industry experts."
    }
  ]
}
---

# GENAI-12-AGENTS-AND-TOOL-USE: Agents & Tool Use

## Introduction

Let models call functions, use tools, and loop until the job is done. By the end of this lesson you will be able to: Explain function calling; Define an agent loop (reason → act → observe); Build a simple tool-using agent; Manage loops and error cases safely.

## Key Concepts

### 1. Explain function calling

Target: Explain function calling. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from openai import OpenAI

client = OpenAI()
res = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "What is the weather in Paris?"}],
    tools=[{
        "type": "function",
        "function": {
            "name": "get_weather",
            "parameters": {"type": "object", "properties": {"city": {"type": "string"}}},
        },
    }],
)
print(res.choices[0].message.tool_calls)
```
### 2. Define an agent loop (reason → act → observe)

Target: Define an agent loop (reason → act → observe). Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
tools = {"search": search_fn, "calculator": calc_fn}
print("registered tools:", list(tools))
```
### 3. Build a simple tool-using agent

Target: Build a simple tool-using agent. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import time

# Agent loop: while task not done -> call model -> call tool
for step in range(3):
    print(f"step {step}: reason -> act -> observe")
    time.sleep(0.1)
```
### 4. Manage loops and error cases safely

Target: Manage loops and error cases safely. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
safety = ["max iterations", "timeouts", "tool allow-list", "human approval"]
print(safety)
```

## Practice Questions

1. What is the key idea behind "Agents & Tool Use"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Agents & Tool Use with analogies and real-world examples"
1. "Show me common mistakes beginners make with Agents & Tool Use"
1. "Provide advanced patterns and performance considerations for Agents & Tool Use"

## Key Takeaways

- Master the core ideas of Agents & Tool Use through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
