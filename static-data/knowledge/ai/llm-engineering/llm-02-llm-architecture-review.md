---
slug: llm-02-llm-architecture-review
title: "LLM Architecture Review"
description: "The transformer decoder under the hood — attention mechanisms, KV cache, positional encoding, and Mixture of Experts."
order: 2
tags:
  - llm-engineering
  - transformer
  - attention
  - architecture
prerequisites:
  - llm-01-what-is-llm-engineering
knowledge_refs:
  - llm-01-what-is-llm-engineering
  - llm-03-llm-apis
references:
  - title: "Attention Is All You Need"
    url: "https://arxiv.org/abs/1706.03762"
    notes: "The original transformer paper"
  - title: "FlashAttention: Fast and Memory-Efficient Exact Attention"
    url: "https://arxiv.org/abs/2205.14135"
    notes: "IO-aware attention algorithm"
  - title: "Llama 3 Herd of Models"
    url: "https://arxiv.org/abs/2407.21783"
    notes: "Modern LLM architecture details"
  - title: "The Illustrated Transformer"
    url: "https://jalammar.github.io/illustrated-transformer/"
    notes: "Visual guide to transformer internals"
  - title: "Mixture of Experts Explained"
    url: "https://huggingface.co/blog/moe"
    notes: "How MoE architectures work"
---

# LLM Architecture Review

Modern LLMs are built on the **transformer decoder** architecture. Understanding the key components helps LLM engineers make better decisions about model selection, prompting, and system design.

## The Transformer Decoder

All modern LLMs (GPT-4, Claude, Llama, Gemini) use a **decoder-only** transformer:

```
Input Tokens → Embedding → [Decoder Block × N] → Linear → Softmax → Output Tokens

Each Decoder Block:
  ├── Masked Multi-Head Self-Attention
  ├── Add & Layer Norm
  ├── Feed-Forward Network (MLP)
  └── Add & Layer Norm
```

## Self-Attention Mechanism

Self-attention lets each token attend to all previous tokens:

```
Attention(Q, K, V) = softmax(QK^T / √d_k) V
```

- **Q (Query)**: "What am I looking for?"
- **K (Key)**: "What do I contain?"
- **V (Value)**: "What information do I provide?"
- **√d_k**: Scaling factor to prevent softmax saturation

### Multi-Head Attention
Multiple attention heads capture different types of relationships:
- Head 1 might capture syntactic relationships
- Head 2 might capture semantic similarity
- Head 3 might capture long-range dependencies

## KV Cache

During autoregressive generation, we compute attention for each new token against all previous tokens. The **KV cache** stores previously computed Key and Value matrices:

- Without cache: O(n²) computation per token
- With cache: O(n) computation per token (only new Q, K, V computed)
- Trade-off: memory proportional to sequence length × number of layers × heads

## Positional Encoding

Transformers have no inherent notion of order. Positional encoding injects sequence position:

### RoPE (Rotary Position Embeddings)
- Used by: Llama, Mistral, Qwen, DeepSeek
- Encodes position as rotation in embedding space
- Naturally handles relative positions
- Extends to longer contexts via NTK-aware scaling

### ALiBi (Attention with Linear Biases)
- Used by: BLOOM, MPT
- Adds linear bias to attention scores based on distance
- Simpler than RoPE, good for length generalization

## Mixture of Experts (MoE)

Instead of a single large feed-forward network, MoE uses multiple specialized "expert" networks:

- **Router**: decides which experts to activate per token
- **Top-k routing**: typically top-2 experts per token
- **Sparse activation**: only k out of N experts run per token
- **Benefits**: larger total model capacity with lower inference cost

Example: Mixtral 8x7B has 8 experts, activates 2 per token → 47B active parameters but 13B effective per token.

## Key Numbers

| Model | Parameters | Context | Architecture |
|-------|-----------|---------|--------------|
| GPT-4 | ~1.8T (MoE) | 128K | Transformer decoder |
| Claude 3.5 | Unknown | 200K | Transformer decoder |
| Llama 3.1 405B | 405B | 128K | Dense transformer |
| Mixtral 8x22B | 141B (39B active) | 64K | MoE transformer |
| DeepSeek-V3 | 671B (37B active) | 128K | MoE + MLA |

## Practical Implications for LLM Engineers

1. **Context window limits** → design retrieval strategies to stay within bounds
2. **KV cache memory** → understand why long contexts are expensive
3. **Attention patterns** → "lost in the middle" is a real phenomenon
4. **MoE routing** → some models may be inconsistent across calls
5. **Positional encoding** → affects length generalization and extrapolation

## Key Takeaways

1. Modern LLMs are decoder-only transformers with self-attention
2. KV cache makes autoregressive generation efficient
3. RoPE is the dominant positional encoding for long-context models
4. MoE architectures offer larger capacity with lower inference cost
5. Understanding architecture helps explain model behaviors and limitations
