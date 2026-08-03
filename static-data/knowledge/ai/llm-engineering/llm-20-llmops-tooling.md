---
{
  "title": "The LLMOps Tooling Landscape",
  "description": "Survey the ecosystem: frameworks, eval platforms, observability and serving.",
  "type": "lesson",
  "order": 20,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Compare LLM frameworks (LangChain, LlamaIndex)",
    "Choose an eval platform",
    "Pick observability tooling",
    "Match tools to team size"
  ],
  "knowledge_refs": [
    "llm-engineering/llm-19-production-case-studies",
    "mlops/mlops-01-what-is-mlops",
    "mlops/mlops-20-llmops"
  ],
  "prerequisites": [
    "LLM-01: What Is LLM Engineering?"
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

# LLM-20-LLMOPS-TOOLING: The LLMOps Tooling Landscape

## Introduction

Survey the ecosystem: frameworks, eval platforms, observability and serving. By the end of this lesson you will be able to: Compare LLM frameworks (LangChain, LlamaIndex); Choose an eval platform; Pick observability tooling; Match tools to team size.

## Key Concepts

### 1. Compare LLM frameworks (LangChain, LlamaIndex)

Target: Compare LLM frameworks (LangChain, LlamaIndex). Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
frameworks = {"langchain": "chains & agents", "llamaindex": "data & RAG"}
print(frameworks)
```
### 2. Choose an eval platform

Target: Choose an eval platform. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("start with plain API calls; add frameworks when they pay for themselves")
```
### 3. Pick observability tooling

Target: Pick observability tooling. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("eval platforms: run golden sets on every commit")
```
### 4. Match tools to team size

Target: Match tools to team size. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("observability: traces, cost, latency, feedback")
```

## Practice Questions

1. What is the key idea behind "The LLMOps Tooling Landscape"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain The LLMOps Tooling Landscape with analogies and real-world examples"
1. "Show me common mistakes beginners make with The LLMOps Tooling Landscape"
1. "Provide advanced patterns and performance considerations for The LLMOps Tooling Landscape"

## Key Takeaways

- Master the core ideas of The LLMOps Tooling Landscape through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
