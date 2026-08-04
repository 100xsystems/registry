---
slug: llm-09-fine-tuning-practice
title: "Fine-Tuning LLMs in Practice"
description: "When and how to fine-tune — LoRA, QLoRA, data preparation, evaluation, and the decision framework for prompt vs fine-tune."
order: 9
tags:
  - llm-engineering
  - fine-tuning
  - lora
  - qlora
  - peft
prerequisites:
  - llm-03-llm-apis
  - llm-04-prompting-systems
knowledge_refs:
  - llm-03-llm-apis
  - llm-04-prompting-systems
  - llm-07-rag-engineering
references:
  - title: "Hugging Face PEFT Documentation"
    url: "https://huggingface.co/docs/peft/en/index"
    notes: "Parameter-Efficient Fine-Tuning library"
  - title: "Guide to Fine-Tuning LLMs with LoRA and QLoRA"
    url: "https://www.mercity.ai/blog-post/guide-to-fine-tuning-llms-with-lora-and-qlora/"
    notes: "Practical LoRA/QLoRA tutorial"
  - title: "Fine-Tuning vs Prompt Engineering"
    url: "https://aishwaryasrinivasan.substack.com/p/fine-tuning-vs-prompt-engineering"
    notes: "Decision framework for when to fine-tune"
  - title: "TRL Fine-Tuning Documentation"
    url: "https://huggingface.co/docs/trl/main/en/sft_trainer"
    notes: "Supervised fine-tuning with TRL"
  - title: "Unsloth Fine-Tuning"
    url: "https://github.com/unslothai/unsloth"
    notes: "Fast LoRA fine-tuning library"
---

# Fine-Tuning LLMs in Practice

Fine-tuning adapts a pre-trained model to your specific task. But when should you fine-tune vs. prompt? And how do you do it efficiently?

## Decision Framework: Prompt vs. Fine-Tune

| Problem | Solution | Why |
|---------|----------|-----|
| Unstable formatting | Prompt engineering | Add format instructions |
| Missing knowledge | RAG | Retrieve relevant docs |
| Wrong tone/style | Fine-tune | Model needs to learn new behavior |
| Domain reasoning | Fine-tune | Deep expertise requires weight updates |
| Cost optimization | Fine-tune smaller model | Distill large model → small model |

**Start with prompting (solves ~70% of issues), then RAG, then fine-tune.**

## Fine-Tuning Approaches

### Full Fine-Tuning
- Update all model parameters
- Requires multi-GPU setup
- Risk of catastrophic forgetting
- Best for: when you have lots of data and compute

### LoRA (Low-Rank Adaptation)
- Freeze base model, train small adapter matrices
- Rank r << model dimensions (typically r=8-64)
- Adapters: 10-100 MB vs. multi-GB full model
- **Zero inference latency** (adapters merge into weights)

```python
from peft import LoraConfig, get_peft_model

config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    task_type="CAUSAL_LM"
)
model = get_peft_model(base_model, config)
model.print_trainable_parameters()
# trainable: 0.1% of total params
```

### QLoRA (Quantized LoRA)
- LoRA + 4-bit quantization
- Fine-tune 70B models on a single GPU
- 4-bit NF4 quantization + double quantization
- Paged optimizers handle memory spikes

## Data Preparation

### Format
```json
{"messages": [
  {"role": "system", "content": "You are a medical assistant."},
  {"role": "user", "content": "What is hypertension?"},
  {"role": "assistant", "content": "Hypertension is..."}
]}
```

### Quality Guidelines
- 100-1000 high-quality examples often beat 10,000 noisy ones
- Remove duplicates and low-quality samples
- Balance domain distribution
- Use consistent formatting and tone

## Training Setup

```python
from trl import SFTTrainer
from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir="./output",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    fp16=True,
    logging_steps=10,
    save_strategy="epoch",
)

trainer = SFTTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    max_seq_length=2048,
)
trainer.train()
```

## Evaluation

- **Validation loss**: monitor for overfitting
- **Benchmarks**: MMLU, GSM8K, HumanEval
- **LLM-as-judge**: GPT-4 scores outputs against references
- **Human evaluation**: blind A/B testing for production

## When NOT to Fine-Tune

- You have fewer than 100 examples
- The task changes frequently
- Prompt engineering + RAG works well enough
- You need the latest model's knowledge
- Cost and latency constraints prohibit it

## Key Takeaways

1. Always try prompting and RAG before fine-tuning
2. LoRA is the standard approach — trains <1% of parameters
3. QLoRA enables fine-tuning large models on consumer GPUs
4. Data quality matters more than quantity
5. Evaluate with benchmarks, LLM-as-judge, and human evaluation
