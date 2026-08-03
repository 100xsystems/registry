---
{
  "title": "Cost Optimization for LLM Apps",
  "description": "Cut spend without cutting quality: caching, smaller models, and smart routing.",
  "type": "lesson",
  "order": 16,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Model cost per request",
    "Use prompt and completion caching",
    "Route simple queries to small models",
    "Budget by feature"
  ],
  "knowledge_refs": [
    "llm-engineering/llm-16-cost-optimization"
  ],
  "prerequisites": [
    "LLM-05: Tokenization & Context Management"
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

# LLM-16-COST-OPTIMIZATION: Cost Optimization for LLM Apps

## Introduction

Cut spend without cutting quality: caching, smaller models, and smart routing. By the end of this lesson you will be able to: Model cost per request; Use prompt and completion caching; Route simple queries to small models; Budget by feature.

## Key Concepts

### 1. Model cost per request

Target: Model cost per request. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
in_tok = len(enc.encode("prompt " * 100))
out_tok = 200
cost = in_tok / 1000 * 0.00015 + out_tok / 1000 * 0.0006
print("cost per request:", round(cost, 5))
```
### 2. Use prompt and completion caching

Target: Use prompt and completion caching. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("cache exact prompt matches -> 90% cost cut")
```
### 3. Route simple queries to small models

Target: Route simple queries to small models. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("router: small model for intents, big model for hard cases")
```
### 4. Budget by feature

Target: Budget by feature. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("streaming and trimming inputs also saves tokens")
```

## Practice Questions

1. What is the key idea behind "Cost Optimization for LLM Apps"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Cost Optimization for LLM Apps with analogies and real-world examples"
1. "Show me common mistakes beginners make with Cost Optimization for LLM Apps"
1. "Provide advanced patterns and performance considerations for Cost Optimization for LLM Apps"

## Key Takeaways

- Master the core ideas of Cost Optimization for LLM Apps through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
