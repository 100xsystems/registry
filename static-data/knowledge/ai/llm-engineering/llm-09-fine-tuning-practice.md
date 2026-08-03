---
{
  "title": "Fine-Tuning LLMs in Practice",
  "description": "LoRA, QLoRA and instruction tuning — adapt open models when prompting is not enough.",
  "type": "lesson",
  "order": 9,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Prepare an instruction dataset",
    "Fine-tune with LoRA",
    "Evaluate the fine-tuned model",
    "Decide when fine-tuning is worth it"
  ],
  "knowledge_refs": [
    "llm-engineering/llm-08-advanced-rag",
    "generative-ai/genai-08-fine-tuning-llms",
    "machine-learning/ml-17-hyperparameter-tuning"
  ],
  "prerequisites": [
    "GENAI-08: Fine-Tuning LLMs"
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

# LLM-09-FINE-TUNING-PRACTICE: Fine-Tuning LLMs in Practice

## Introduction

LoRA, QLoRA and instruction tuning — adapt open models when prompting is not enough. By the end of this lesson you will be able to: Prepare an instruction dataset; Fine-tune with LoRA; Evaluate the fine-tuned model; Decide when fine-tuning is worth it.

## Key Concepts

### 1. Prepare an instruction dataset

Target: Prepare an instruction dataset. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
data = [
    {"prompt": "Define ML", "completion": "Machine learning is..."},
    {"prompt": "Define DL", "completion": "Deep learning is..."},
]
print("instruction pairs:", len(data))
```
### 2. Fine-tune with LoRA

Target: Fine-tune with LoRA. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from peft import LoraConfig, get_peft_model

config = LoraConfig(r=8, lora_alpha=16, target_modules=["q_proj", "v_proj"])
print("LoRA config ready")
```
### 3. Evaluate the fine-tuned model

Target: Evaluate the fine-tuned model. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

# QLoRA: 4-bit base + LoRA adapters on top
print("4-bit quantization keeps memory low")
```
### 4. Decide when fine-tuning is worth it

Target: Decide when fine-tuning is worth it. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("fine-tune to match a style/format, not to add facts")
```

## Practice Questions

1. What is the key idea behind "Fine-Tuning LLMs in Practice"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Fine-Tuning LLMs in Practice with analogies and real-world examples"
1. "Show me common mistakes beginners make with Fine-Tuning LLMs in Practice"
1. "Provide advanced patterns and performance considerations for Fine-Tuning LLMs in Practice"

## Key Takeaways

- Master the core ideas of Fine-Tuning LLMs in Practice through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
