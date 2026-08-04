---
slug: genai-08-fine-tuning-llms
title: "Fine-Tuning LLMs"
description: "From full fine-tuning to LoRA and QLoRA — practical methods for customizing large language models on your data."
order: 8
tags:
  - generative-ai
  - fine-tuning
  - lora
  - qlora
  - peft
  - instruction-tuning
prerequisites:
  - genai-06-llm-architecture
  - genai-04-prompt-engineering
  - dl-07-optimizers
references:
  - title: "PEFT Documentation (Hugging Face)"
    url: "https://huggingface.co/docs/peft/en/index"
    description: "Official Hugging Face PEFT library documentation"
  - title: "LoRA: Low-Rank Adaptation of Large Language Models"
    url: "https://arxiv.org/abs/2106.09685"
    description: "Hu et al.'s original LoRA paper"
  - title: "QLoRA: Efficient Finetuning of Quantized LLMs"
    url: "https://arxiv.org/abs/2305.14314"
    description: "Dettmers et al.'s QLoRA paper — 4-bit fine-tuning on consumer GPUs"
  - title: "What Is Instruction Tuning? (IBM)"
    url: "https://www.ibm.com/think/topics/instruction-tuning"
    description: "Comprehensive explanation of instruction tuning methodology"
  - title: "PEFT GitHub Repository"
    url: "https://github.com/huggingface/peft"
    description: "State-of-the-art implementations of LoRA, QLoRA, and other PEFT methods"
knowledge_refs:
  - genai-06-llm-architecture
  - dl-10-the-training-loop
  - dl-11-regularization-for-deep-learning
---

# Fine-Tuning LLMs

Fine-tuning adapts a pretrained LLM to your specific task, domain, or style. Modern parameter-efficient methods make this possible on consumer hardware.

## Why Fine-Tune?

| Approach | When to Use |
|---|---|
| **Prompt engineering** | Simple tasks, general knowledge |
| **In-context learning** | Task-specific with few examples |
| **RAG** | Need external knowledge |
| **Fine-tuning** | Specific style, domain, format, or behavior |

**Fine-tuning is best when:**
- You need consistent output format
- The model needs domain-specific knowledge
- Prompt engineering isn't sufficient
- You want to reduce inference costs (smaller fine-tuned model)

## Full Fine-Tuning

Retrain all model parameters on your dataset:
- **Pros**: Maximum adaptation, best performance
- **Cons**: Requires massive compute, overwrites pretrained knowledge
- **Memory**: 7B model needs ~60GB GPU (FP16 + optimizer states)
- **Use case**: Creating a new base model from scratch

```python
from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir="./output",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=8,
    learning_rate=2e-5,
    fp16=True,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
)
trainer.train()
```

## LoRA (Low-Rank Adaptation)

The most popular PEFT method — freezes the base model and trains small adapter matrices:

$$W' = W + \Delta W = W + BA$$

where $B \in \mathbb{R}^{d \times r}$ and $A \in \mathbb{R}^{r \times d}$ with $r \ll d$.

```python
from peft import LoraConfig, get_peft_model

lora_config = LoraConfig(
    r=16,                    # rank (higher = more capacity)
    lora_alpha=32,           # scaling factor
    target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
    lora_dropout=0.05,
    bias="none",
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()
# trainable params: 4,194,304 || all params: 6,742,609,920 || 0.06%
```

**Key benefits:**
- Only 0.1-1% of parameters are trainable
- LoRA weights merge back into base model (zero inference overhead)
- Can fine-tune 7B model on 1× RTX 4090 (24GB)

## QLoRA (Quantized LoRA)

Combines 4-bit quantization with LoRA for extreme memory efficiency:

```python
from transformers import BitsAndBytesConfig
import torch

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-hf",
    quantization_config=bnb_config,
)

# Then apply LoRA on top
model = get_peft_model(model, lora_config)
```

**Memory savings:**
| Method | 7B Model | 70B Model |
|---|---|---|
| Full fine-tuning | ~60GB | ~560GB |
| LoRA (FP16) | ~16GB | ~160GB |
| QLoRA (4-bit) | ~6GB | ~48GB |

## Instruction Tuning

Fine-tuning on instruction-response pairs teaches the model to follow directions:

```json
[
  {
    "instruction": "Summarize the following text in 3 bullet points.",
    "input": "The transformer architecture has revolutionized NLP...",
    "output": "• Transformers use self-attention for parallel processing\n• They replaced RNNs for most NLP tasks\n• GPT and BERT are the two main transformer variants"
  }
]
```

**Key datasets:**
- Alpaca: 52K instruction-following examples
- ShareGPT: User-ChatGPT conversations
- OpenAssistant: Human conversations
- Dolly: Databricks' instruction dataset

## Training Data Quality

**Data quality matters more than quantity:**
- 1,000 high-quality examples > 100,000 low-quality examples
- Diverse instructions cover more use cases
- Consistent format helps the model learn patterns
- Remove duplicates and near-duplicates

## Fine-Tuning Pipeline

```python
# 1. Load base model with QLoRA
model = load_qlora_model("meta-llama/Llama-2-7b-hf")

# 2. Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")
tokenizer.pad_token = tokenizer.eos_token

# 3. Prepare dataset
dataset = load_dataset("json", data_files="train.json")

# 4. Configure LoRA
lora_config = LoraConfig(r=16, lora_alpha=32, target_modules=["q_proj", "v_proj"])

# 5. Train
training_args = TrainingArguments(
    output_dir="./output",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=8,
    learning_rate=2e-4,
    fp16=True,
    logging_steps=10,
    save_strategy="epoch",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    tokenizer=tokenizer,
)
trainer.train()

# 6. Save LoRA adapter
model.save_pretrained("./lora-adapter")

# 7. Merge for inference (optional)
merged_model = model.merge_and_unload()
merged_model.save_pretrained("./merged-model")
```

## When to Fine-Tune vs. RAG vs. Prompt

| Need | Solution |
|---|---|
| New knowledge | RAG (don't fine-tune for knowledge) |
| Specific output format | Fine-tune |
| Domain-specific tone | Fine-tune |
| Real-time data | RAG |
| Complex reasoning | Prompt engineering + CoT |
| Cost reduction | Fine-tune smaller model |

## Common Pitfalls

1. **Overfitting**: Too many epochs on small data → memorizes training examples
2. **Catastrophic forgetting**: Model loses pretrained capabilities
3. **Bad data quality**: Garbage in, garbage out
4. **Wrong hyperparameters**: LR too high destroys weights, too low doesn't learn
5. **Not evaluating properly**: Always hold out test data

## Further Reading

- Hu et al.'s LoRA paper introduced parameter-efficient fine-tuning
- Dettmers et al.'s QLoRA made fine-tuning accessible on consumer hardware
- Hugging Face PEFT library is the standard implementation
- For advanced methods: look into DoRA, AdaLoRA, and (IA)³
