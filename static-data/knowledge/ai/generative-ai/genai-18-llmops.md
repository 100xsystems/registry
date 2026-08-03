---
{
  "title": "LLMOps: Running GenAI in Production",
  "description": "Prompt management, caching, guardrails, monitoring and cost control for LLM apps.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Version prompts and evals",
    "Cache completions and embeddings",
    "Apply guardrails and moderation",
    "Monitor latency, cost and quality"
  ],
  "knowledge_refs": [
    "generative-ai/genai-17-evaluating-llms",
    "mlops/mlops-01-what-is-mlops",
    "mlops/mlops-20-llmops"
  ],
  "prerequisites": [
    "GENAI-10: Retrieval-Augmented Generation (RAG)"
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

# GENAI-18-LLMOPS: LLMOps: Running GenAI in Production

## Introduction

Prompt management, caching, guardrails, monitoring and cost control for LLM apps. By the end of this lesson you will be able to: Version prompts and evals; Cache completions and embeddings; Apply guardrails and moderation; Monitor latency, cost and quality.

## Key Concepts

### 1. Version prompts and evals

Target: Version prompts and evals. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import hashlib

# Semantic-ish cache key from the prompt
def cache_key(prompt: str) -> str:
    return hashlib.sha256(prompt.encode()).hexdigest()

print(cache_key("summarize this article"))
```
### 2. Cache completions and embeddings

Target: Cache completions and embeddings. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from openai import OpenAI

client = OpenAI()
res = client.moderations.create(input="some user text")
print("flagged:", res.results[0].flagged)
```
### 3. Apply guardrails and moderation

Target: Apply guardrails and moderation. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import time

# Track cost: tokens in/out per request
cost = {
    "prompt_tokens": 120,
    "completion_tokens": 40,
    "price_per_1k": 0.00015,
}
est = (cost["prompt_tokens"] + cost["completion_tokens"]) / 1000 * cost["price_per_1k"]
print("estimated cost:", est)
```
### 4. Monitor latency, cost and quality

Target: Monitor latency, cost and quality. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
metrics = ["latency", "tokens", "cost", "hallucination rate", "user feedback"]
print(metrics)
```

## Practice Questions

1. What is the key idea behind "LLMOps: Running GenAI in Production"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain LLMOps: Running GenAI in Production with analogies and real-world examples"
1. "Show me common mistakes beginners make with LLMOps: Running GenAI in Production"
1. "Provide advanced patterns and performance considerations for LLMOps: Running GenAI in Production"

## Key Takeaways

- Master the core ideas of LLMOps: Running GenAI in Production through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
