---
{
  "title": "Fine-Tuning LLMs",
  "description": "Adapt a foundation model to a domain with supervised fine-tuning and parameter-efficient methods (LoRA).",
  "type": "lesson",
  "order": 8,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain supervised fine-tuning (SFT)",
    "Prepare instruction datasets",
    "Use LoRA for efficient fine-tuning",
    "Know when fine-tuning beats prompting"
  ],
  "knowledge_refs": [
    "generative-ai/genai-08-fine-tuning-llms"
  ],
  "prerequisites": [
    "GENAI-06: LLM Architecture & Scaling"
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

# GENAI-08-FINE-TUNING-LLMS: Fine-Tuning LLMs

## Introduction

Adapt a foundation model to a domain with supervised fine-tuning and parameter-efficient methods (LoRA). By the end of this lesson you will be able to: Explain supervised fine-tuning (SFT); Prepare instruction datasets; Use LoRA for efficient fine-tuning; Know when fine-tuning beats prompting.

## Key Concepts

### 1. Explain supervised fine-tuning (SFT)

Target: Explain supervised fine-tuning (SFT). Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
dataset = [
    {"instruction": "Translate to French", "input": "hello", "output": "bonjour"},
    {"instruction": "Translate to French", "input": "goodbye", "output": "au revoir"},
]
print(dataset)
```
### 2. Prepare instruction datasets

Target: Prepare instruction datasets. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("gpt2")
print("loaded for SFT")
```
### 3. Use LoRA for efficient fine-tuning

Target: Use LoRA for efficient fine-tuning. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from peft import LoraConfig, get_peft_model

config = LoraConfig(r=8, lora_alpha=16, target_modules=["c_attn"])
peft_model = get_peft_model(model, config)
print("trainable params:", sum(p.numel() for p in peft_model.parameters() if p.requires_grad))
```
### 4. Know when fine-tuning beats prompting

Target: Know when fine-tuning beats prompting. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("prompt first; RAG second; fine-tune only when needed")
```

## Practice Questions

1. What is the key idea behind "Fine-Tuning LLMs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Fine-Tuning LLMs with analogies and real-world examples"
1. "Show me common mistakes beginners make with Fine-Tuning LLMs"
1. "Provide advanced patterns and performance considerations for Fine-Tuning LLMs"

## Key Takeaways

- Master the core ideas of Fine-Tuning LLMs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
