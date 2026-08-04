---
slug: genai-06-llm-architecture
title: "LLM Architecture & Scaling"
description: "From transformer blocks to mixture of experts — understanding the architectures and scaling laws behind modern LLMs."
order: 6
tags:
  - generative-ai
  - llm
  - architecture
  - scaling
  - mixture-of-experts
prerequisites:
  - dl-17-transformers
  - genai-03-text-generation-basics
references:
  - title: "Scaling Laws for Neural Language Models (Kaplan et al.)"
    url: "https://arxiv.org/abs/2001.08361"
    description: "Foundational scaling laws showing predictable performance improvement with compute"
  - title: "Training Compute-Optimal Large Language Models (Chinchilla)"
    url: "https://arxiv.org/abs/2203.15556"
    description: "Hoffmann et al.'s Chinchilla paper — optimal model size vs training data ratio"
  - title: "Switch Transformers: Scaling to Trillion Parameter Models"
    url: "https://arxiv.org/abs/2101.03961"
    description: "Fedus et al.'s mixture of experts architecture for efficient scaling"
  - title: "A Survey of Large Language Models (Zhao et al.)"
    url: "https://arxiv.org/abs/2303.18223"
    description: "Comprehensive survey of LLM architectures, training, and capabilities"
  - title: "Llama 2: Open Foundation and Fine-Tuned Chat Models"
    url: "https://arxiv.org/abs/2307.09288"
    description: "Meta's Llama 2 paper with architecture details and training methodology"
knowledge_refs:
  - dl-17-transformers
  - dl-19-training-at-scale
  - genai-03-text-generation-basics
---

# LLM Architecture & Scaling

Modern LLMs are built on the transformer decoder architecture, but with critical modifications that enable scaling to billions of parameters. Understanding these architectures and scaling laws is essential for working with frontier models.

## The Transformer Decoder Stack

All modern LLMs (GPT, LLaMA, Claude) use a decoder-only transformer:

```
Input Tokens
    ↓
Token Embedding + RoPE Positional Encoding
    ↓
┌─────────────────────────────┐
│  RMSNorm                      │
│  Masked Multi-Head Attention  │
│  RMSNorm                      │
│  Feed-Forward Network (SwiGLU)│
└─────────────────────────────┘  × N layers
    ↓
RMSNorm → Linear Head → Softmax
```

**Key modifications from original transformer:**
- **RMSNorm** instead of LayerNorm (faster, simpler)
- **RoPE** (Rotary Position Embeddings) instead of sinusoidal
- **SwiGLU** activation in feed-forward layers
- **GQA** (Grouped-Query Attention) for efficient inference

## Model Sizes and Parameters

| Model | Parameters | Layers | Hidden Dim | Heads | Context |
|---|---|---|---|---|---|
| GPT-3 | 175B | 96 | 12,288 | 96 | 2K |
| LLaMA-2 7B | 7B | 32 | 4,096 | 32 | 4K |
| LLaMA-2 70B | 70B | 80 | 8,192 | 64 | 4K |
| LLaMA-3 8B | 8B | 32 | 4,096 | 32 | 8K |
| LLaMA-3 70B | 70B | 80 | 8,192 | 64 | 8K |
| GPT-4 (est.) | ~1.8T | ~120 | ~12,288 | ~96 | 8-128K |
| Claude 3 Opus | ~2T (est.) | unknown | unknown | unknown | 200K |
| Gemini 1.5 Pro | ~1.5T (est.) | unknown | unknown | unknown | 1M |

## Key Architectural Components

### Rotary Position Embeddings (RoPE)
Encodes position by rotating query/key vectors:
- Relative positions naturally captured
- Extends to longer contexts via interpolation
- Used by: LLaMA, Mistral, Qwen, most open-source models

### Grouped-Query Attention (GQA)
Multiple query heads share key-value heads:
- Reduces KV-cache memory by 4-8x
- Slight quality trade-off for major inference speedup
- Used by: LLaMA 2 70B, LLaMA 3, Mistral, Gemini

### SwiGLU Activation
$$\text{SwiGLU}(x) = \text{Swish}(xW_1) \odot (xW_2)$$

Better than ReLU/GELU in transformer feed-forward layers. Used by: LLaMA, PaLM, Mistral.

### Sliding Window Attention
Mistral uses local attention with a window size:
- Each token attends to only $W$ previous tokens
- Reduces attention complexity from $O(N^2)$ to $O(N \times W)$
- Combined with global attention at every few layers

## Scaling Laws

Kaplan et al. (2020) discovered that LLM performance follows power laws:

$$L(N) = \left(\frac{N_c}{N}\right)^{\alpha_N}$$
$$L(D) = \left(\frac{D_c}{D}\right)^{\alpha_D}$$
$$L(C) = \left(\frac{C_c}{C}\right)^{\alpha_C}$$

where $L$ is loss, $N$ = parameters, $D$ = data tokens, $C$ = compute.

**Key insight**: Performance improves predictably with scale — no sudden jumps, no plateaus.

### Chinchilla Optimal Scaling

Hoffmann et al. (2022) showed that for optimal performance given a compute budget:
- Model size and training data should scale **together**
- Rule of thumb: 20 tokens per parameter
- GPT-3 (175B params, 300B tokens) was **over-parameterized, under-trained**
- Chinchilla (70B params, 1.4T tokens) matched GPT-3 performance at 4x less compute

```
Chinchilla optimal:
  7B params → 140B tokens
  70B params → 1.4T tokens
  175B params → 3.5T tokens
```

## Mixture of Experts (MoE)

Instead of one large dense model, use many small expert networks:

```
Input → Router → Select top-K experts → Combine outputs
         ↓
    Expert 1 (inactive)
    Expert 2 (active)  ←── selected
    Expert 3 (inactive)
    Expert 4 (active)  ←── selected
    ...
    Expert N (inactive)
```

**Benefits:**
- 8x more parameters but only 2x compute per token
- Each token activates only 2 of 8 experts
- Better performance at same compute budget

**Examples:**
- Mixtral 8x7B: 47B params, 12.9B active per token
- Switch Transformer: Up to 1.6T params
- GPT-4 (rumored): 8x220B MoE

## Training Infrastructure

| Scale | Hardware | Duration | Cost |
|---|---|---|---|
| 7B | 8× A100 80GB | 1-2 weeks | ~$10K |
| 70B | 256× A100 | 2-4 weeks | ~$500K |
| 175B | 1024× A100 | 3-4 weeks | ~$2-5M |
| 1T+ | 16K+ H100 | Months | $50-100M+ |

## Common Training Data

| Dataset | Size | Source |
|---|---|---|
| Common Crawl | 5PB | Web crawl |
| C4 | 750GB | Cleaned Common Crawl |
| The Pile | 825GB | 22 diverse sources |
| RedPajama | 1.2T tokens | Reproduction of LLaMA data |
| FineWeb | 15T tokens | Hugging Face cleaned web data |
| LLaMA training data | 2T tokens | Web, code, Wikipedia, books |

## Practical Implications

1. **For inference**: Smaller models with more training data can match larger under-trained models
2. **For fine-tuning**: Full fine-tuning of 70B needs ~8× A100; LoRA needs 1× A100
3. **For deployment**: GQA + quantization (INT4/INT8) dramatically reduce memory
4. **For cost**: MoE models offer better performance per FLOP than dense models

## Further Reading

- Kaplan et al. and Chinchilla papers are foundational for understanding scaling
- LLaMA papers provide the most detailed open-source architecture descriptions
- Switch Transformers showed MoE can scale efficiently
- For practical deployment: vLLM and TGI optimize inference for these architectures
