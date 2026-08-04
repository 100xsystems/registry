---
slug: genai-03-text-generation-basics
title: "Text Generation Fundamentals"
description: "How decoder-only transformers generate text token by token — from GPT-1 to modern LLMs."
order: 3
tags:
  - generative-ai
  - text-generation
  - decoder
  - autoregressive
  - gpt
prerequisites:
  - genai-02-probabilistic-generation
  - dl-17-transformers
references:
  - title: "Language Models are Unsupervised Multitask Learners (GPT-2)"
    url: "https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf"
    description: "Radford et al.'s GPT-2 paper showing zero-shot task completion"
  - title: "Language Models are Few-Shot Learners (GPT-3)"
    url: "https://arxiv.org/abs/2005.14165"
    description: "Brown et al.'s GPT-3 paper — in-context learning and scaling laws"
  - title: "Scaling Laws for Neural Language Models (Kaplan et al.)"
    url: "https://arxiv.org/abs/2001.08361"
    description: "Kaplan et al.'s scaling laws showing predictable performance improvement"
  - title: "Text Generation with Hugging Face Transformers"
    url: "https://huggingface.co/docs/transformers/en/generation_strategies"
    description: "Practical guide to text generation parameters and strategies"
  - title: "A Survey of Large Language Models (Zhao et al.)"
    url: "https://arxiv.org/abs/2303.18223"
    description: "Comprehensive survey of LLM architectures, training, and capabilities"
knowledge_refs:
  - genai-02-probabilistic-generation
  - dl-17-transformers
  - dl-18-attention-mechanisms
---

# Text Generation Fundamentals

Modern text generation is powered by **decoder-only transformers** — a specific architecture that generates one token at a time, conditioned on everything that came before.

## The Decoder-Only Architecture

Unlike the original transformer (encoder-decoder), decoder-only models use a single stack of transformer layers with **causal masking**:

```
Input: "The cat sat"
         ↓
[Token Embedding] + [Positional Encoding]
         ↓
┌─────────────────────┐
│  Causal Self-Attention  │  ← Can only attend to past tokens
│  Feed-Forward Network   │
│  Layer Normalization    │
└─────────────────────┘  × N layers
         ↓
[Linear Head] → [Softmax] → Probability over vocabulary
         ↓
Sample next token
```

**Causal masking** prevents tokens from attending to future tokens:
```
Attention mask for "The cat sat":
     The  cat  sat
The  [1]  [0]  [0]    ← "The" sees only itself
cat  [1]  [1]  [0]    ← "cat" sees "The" and itself
sat  [1]  [1]  [1]    ← "sat" sees everything before
```

## GPT: The Generative Pre-trained Transformer

### GPT-1 (2018)
- 12 layers, 117M parameters
- Pretrained on BookCorpus (7K books)
- Fine-tuned on downstream tasks
- Showed transfer learning works for NLP

### GPT-2 (2019)
- 48 layers, 1.5B parameters
- Pretrained on WebText (40GB)
- Zero-shot task completion (no fine-tuning needed)
- "Language models are unsupervised multitask learners"

### GPT-3 (2020)
- 96 layers, 175B parameters
- Pretrained on 300B tokens
- **In-context learning**: Learn from examples in the prompt
- Few-shot, one-shot, zero-shot capabilities
- Scaling laws: performance improves predictably with size

### GPT-4 (2023)
- ~1.8T parameters (estimated, mixture of experts)
- Multimodal (text + images)
- Improved reasoning and safety
- Longer context window (8K-128K tokens)

## The Generation Loop

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate(prompt, max_tokens=50, temperature=0.7, top_p=0.9):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    
    for _ in range(max_tokens):
        # Forward pass: get logits for next token
        with torch.no_grad():
            logits = model(input_ids).logits[:, -1, :]
        
        # Apply temperature
        logits = logits / temperature
        
        # Apply top-p filtering
        sorted_logits, sorted_indices = torch.sort(logits, descending=True)
        cumulative_probs = torch.cumsum(torch.softmax(sorted_logits, dim=-1), dim=-1)
        sorted_indices_to_remove = cumulative_probs > top_p
        sorted_indices_to_remove[..., 1:] = sorted_indices_to_remove[..., :-1].clone()
        sorted_indices_to_remove[..., 0] = 0
        indices_to_remove = sorted_indices[sorted_indices_to_remove]
        logits[0, indices_to_remove] = float('-inf')
        
        # Sample
        probs = torch.softmax(logits, dim=-1)
        next_token = torch.multinomial(probs, num_samples=1)
        
        input_ids = torch.cat([input_ids, next_token], dim=-1)
        
        if next_token.item() == tokenizer.eos_token_id:
            break
    
    return tokenizer.decode(input_ids[0])

print(generate("The future of AI is"))
```

## Context Windows

The **context window** is the maximum number of tokens the model can process:

| Model | Context Window | Release |
|---|---|---|
| GPT-3 | 2,048 | 2020 |
| GPT-3.5 | 4,096 | 2022 |
| GPT-4 | 8,192 / 32,768 | 2023 |
| GPT-4 Turbo | 128,000 | 2023 |
| Claude 3 | 200,000 | 2024 |
| Gemini 1.5 | 1,000,000 | 2024 |
| Llama 3.1 | 128,000 | 2024 |

**Longer context = more capability**: Fewer examples needed, longer documents, more complex reasoning.

## Tokenization

Text is split into **tokens** (subwords) before processing:

```python
tokenizer = AutoTokenizer.from_pretrained("gpt2")
tokens = tokenizer.encode("Hello, world!")
print(tokens)  # [15496, 11, 995, 0]
print(tokenizer.decode(tokens))  # "Hello, world!"
```

**Why subwords?**
- Handle any word (even misspellings)
- Balance between character-level (too slow) and word-level (too many rare words)
- BPE (Byte Pair Encoding) is most common

**Token counts** (approximate):
- 1 token ≈ 0.75 words in English
- 1 token ≈ 4 characters
- 1 page ≈ 300-500 tokens
- 1 book ≈ 200K-500K tokens

## Special Tokens

| Token | Purpose | Example |
|---|---|---|
| `<bos>` / `<\|begin_of_text\|>` | Start of sequence | Beginning of generation |
| `<eos>` / `<\|end_of_text\|>` | End of sequence | Stop generation |
| `<pad>` | Padding | Batch processing |
| `<unk>` | Unknown token | Out-of-vocabulary |
| `<\|im_start\|>` | Instruction start | ChatML format |
| `<\|im_end\|>` | Instruction end | ChatML format |

## Chat Format (ChatML)

Modern LLMs use structured chat formats:
```
<|im_start|>system
You are a helpful assistant.<|im_end|>
<|im_start|>user
What is machine learning?<|im_end|>
<|im_start|>assistant
Machine learning is a subset of AI...<|im_end|>
```

Each turn has a role (system, user, assistant) and content.

## The KV Cache

During generation, previously computed key-value pairs are cached to avoid redundant computation:

```python
# Without cache: O(n²) for each new token
# With cache: O(n) for each new token (only compute new token's attention)

# Hugging Face handles this automatically
output = model.generate(input_ids, use_cache=True)
```

This is why LLM inference is fast — each new token only requires one forward pass through the model.

## What Makes Text "Good"?

LLMs optimize for **coherence**, **relevance**, and **fluency**:
- **Coherence**: Text flows logically
- **Relevance**: Response addresses the prompt
- **Fluency**: Grammatically correct, natural language
- **Factual accuracy**: Correct information (improving but imperfect)
- **Safety**: Appropriate, non-harmful content

The sampling strategy determines the balance between these properties.

## Further Reading

- GPT-2 paper showed zero-shot capabilities — a paradigm shift
- GPT-3 paper established in-context learning — the foundation of modern prompting
- Kaplan et al.'s scaling laws predict performance from model size and data
- Zhao et al.'s survey provides a comprehensive overview of the LLM landscape
