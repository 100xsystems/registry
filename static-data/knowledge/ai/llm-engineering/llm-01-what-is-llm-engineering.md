---
{
  "title": "What Is LLM Engineering?",
  "description": "The discipline of building systems on top of large language models — and where it differs from classic ML.",
  "type": "lesson",
  "order": 1,
  "duration": "40 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define LLM engineering and its scope",
    "Contrast LLM apps with traditional ML services",
    "List the core building blocks (prompts, RAG, agents, evals)",
    "Identify when an LLM is the right tool"
  ],
  "knowledge_refs": [
    "generative-ai/genai-06-llm-architecture",
    "prompt-engineering/pe-01-what-is-prompt-engineering",
    "prompt-engineering/pe-21-roadmap"
  ],
  "prerequisites": [
    "GENAI-01: What Is Generative AI?"
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

# LLM-01-WHAT-IS-LLM-ENGINEERING: What Is LLM Engineering?

## Introduction

The discipline of building systems on top of large language models — and where it differs from classic ML. By the end of this lesson you will be able to: Define LLM engineering and its scope; Contrast LLM apps with traditional ML services; List the core building blocks (prompts, RAG, agents, evals); Identify when an LLM is the right tool.

## Key Concepts

### 1. Define LLM engineering and its scope

Target: Define LLM engineering and its scope. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
stack = ["models", "prompts", "retrieval", "agents", "evals", "guardrails"]
for s in stack:
    print(f"- {s}")
```
### 2. Contrast LLM apps with traditional ML services

Target: Contrast LLM apps with traditional ML services. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("LLM apps: mostly orchestration + evaluation, less training")
```
### 3. List the core building blocks (prompts, RAG, agents, evals)

Target: List the core building blocks (prompts, RAG, agents, evals). Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from openai import OpenAI

client = OpenAI()
res = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "hi"}],
)
print("first call:", res.choices[0].message.content)
```
### 4. Identify when an LLM is the right tool

Target: Identify when an LLM is the right tool. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
wrong_tools = ["precise math", "low latency at scale", "deterministic rules"]
for w in wrong_tools:
    print(f"- avoid LLMs for: {w}")
```

## Practice Questions

1. What is the key idea behind "What Is LLM Engineering?"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain What Is LLM Engineering? with analogies and real-world examples"
1. "Show me common mistakes beginners make with What Is LLM Engineering?"
1. "Provide advanced patterns and performance considerations for What Is LLM Engineering?"

## Key Takeaways

- Master the core ideas of What Is LLM Engineering? through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
