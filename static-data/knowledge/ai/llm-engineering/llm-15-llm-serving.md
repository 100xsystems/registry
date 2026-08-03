---
{
  "title": "LLM Serving & Inference",
  "description": "Serve open models: vLLM, quantization, batching and GPU memory management.",
  "type": "lesson",
  "order": 15,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Serve models with vLLM",
    "Quantize for lower memory",
    "Batch requests for throughput",
    "Measure tokens per second"
  ],
  "knowledge_refs": [
    "llm-engineering/llm-14-guardrails-and-safety",
    "mlops/mlops-10-model-serving",
    "mlops/mlops-13-deployment-strategies"
  ],
  "prerequisites": [
    "LLM-09: Fine-Tuning LLMs in Practice"
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

# LLM-15-LLM-SERVING: LLM Serving & Inference

## Introduction

Serve open models: vLLM, quantization, batching and GPU memory management. By the end of this lesson you will be able to: Serve models with vLLM; Quantize for lower memory; Batch requests for throughput; Measure tokens per second.

## Key Concepts

### 1. Serve models with vLLM

Target: Serve models with vLLM. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from vllm import LLM

llm = LLM(model="meta-llama/Llama-3.2-1B-Instruct")
print("vLLM engine ready")
```
### 2. Quantize for lower memory

Target: Quantize for lower memory. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from vllm import SamplingParams

params = SamplingParams(temperature=0.7, max_tokens=100)
print("sampling params set")
```
### 3. Batch requests for throughput

Target: Batch requests for throughput. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

# Quantization: 4-bit weights cut memory ~4x
print("bitsandbytes 4-bit config")
```
### 4. Measure tokens per second

Target: Measure tokens per second. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("continuous batching raises GPU utilization")
```

## Practice Questions

1. What is the key idea behind "LLM Serving & Inference"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain LLM Serving & Inference with analogies and real-world examples"
1. "Show me common mistakes beginners make with LLM Serving & Inference"
1. "Provide advanced patterns and performance considerations for LLM Serving & Inference"

## Key Takeaways

- Master the core ideas of LLM Serving & Inference through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
