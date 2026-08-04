---
slug: dl-18-attention-mechanisms
title: "Attention Mechanisms"
description: "The mechanism that enables transformers to focus on relevant parts of the input — from Bahdanau attention to modern efficient variants."
order: 18
tags:
  - deep-learning
  - attention
  - self-attention
  - cross-attention
prerequisites:
  - dl-15-recurrent-networks
  - dl-17-transformers
references:
  - title: "Neural Machine Translation by Jointly Learning to Align and Translate (Bahdanau)"
    url: "https://arxiv.org/abs/1409.0473"
    description: "Bahdanau et al.'s attention paper — the foundation of modern attention"
  - title: "Effective Approaches to Attention-based NMT (Luong)"
    url: "https://arxiv.org/abs/1508.04025"
    description: "Luong's simplified attention mechanisms"
  - title: "Attention Is All You Need (Vaswani et al.)"
    url: "https://arxiv.org/abs/1706.03762"
    description: "Self-attention in transformers"
  - title: "FlashAttention: Fast and Memory-Efficient Exact Attention"
    url: "https://arxiv.org/abs/2205.14135"
    description: "Dao et al.'s IO-aware attention algorithm — 2-4x speedup"
  - title: "Efficient Transformers: A Survey"
    url: "https://arxiv.org/abs/2009.06732"
    description: "Tay et al.'s comprehensive survey of efficient attention variants"
knowledge_refs:
  - dl-17-transformers
  - dl-15-recurrent-networks
  - dl-14-transfer-learning
---

# Attention Mechanisms

Attention lets models dynamically focus on the most relevant parts of the input for each prediction. It's the mechanism that powers transformers, and understanding its variants is key to modern deep learning.

## The Core Idea

Instead of compressing an entire sequence into a single fixed vector, attention creates a **weighted summary** that adapts to each query:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

- **Q (Query)**: What am I looking for?
- **K (Key)**: What do I contain?
- **V (Value)**: What do I provide?
- **$\sqrt{d_k}$**: Scaling factor to prevent dot products from growing too large

## Types of Attention

### Self-Attention
Every token in a sequence attends to every other token in the same sequence:
$$\text{Self-Attn}(X) = \text{softmax}\left(\frac{XW_Q(XW_K)^T}{\sqrt{d_k}}\right)XW_V$$

Used in: Transformer encoder, decoder (masked), BERT, GPT

### Cross-Attention
One sequence attends to another:
$$\text{Cross-Attn}(Q, K, V) = \text{softmax}\left(\frac{QW_Q(KW_K)^T}{\sqrt{d_k}}\right)VW_V$$

Used in: Encoder-decoder models, image captioning, text-to-image

### Causal (Masked) Self-Attention
Tokens can only attend to previous tokens (autoregressive):
$$\text{Causal-Attn}(X) = \text{softmax}\left(\frac{XW_Q(XW_K)^T}{\sqrt{d_k}} + M\right)XW_V$$

where $M$ is a mask that blocks future positions.

```python
# Causal mask
def causal_mask(seq_len):
    mask = torch.triu(torch.ones(seq_len, seq_len), diagonal=1)
    return mask.masked_fill(mask == 1, float('-inf'))
```

## Implementing Attention from Scratch

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class ScaledDotProductAttention(nn.Module):
    def __init__(self, d_k):
        super().__init__()
        self.scale = math.sqrt(d_k)
    
    def forward(self, Q, K, V, mask=None):
        # Q, K, V: (B, H, T, d_k)
        scores = torch.matmul(Q, K.transpose(-2, -1)) / self.scale
        
        if mask is not None:
            scores = scores.masked_fill(mask, float('-inf'))
        
        weights = F.softmax(scores, dim=-1)
        return torch.matmul(weights, V), weights
```

## Multi-Head Attention

Multiple heads capture different relationship patterns:

```python
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        assert d_model % num_heads == 0
        self.d_k = d_model // num_heads
        self.num_heads = num_heads
        
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)
        self.attention = ScaledDotProductAttention(self.d_k)
    
    def forward(self, x, context=None, mask=None):
        B, T, D = x.shape
        
        Q = self.W_q(x).view(B, T, self.num_heads, self.d_k).transpose(1, 2)
        K = self.W_k(context if context else x).view(B, -1, self.num_heads, self.d_k).transpose(1, 2)
        V = self.W_v(context if context else x).view(B, -1, self.num_heads, self.d_k).transpose(1, 2)
        
        output, weights = self.attention(Q, K, V, mask)
        output = output.transpose(1, 2).contiguous().view(B, T, D)
        return self.W_o(output), weights
```

## Efficient Attention Variants

Standard attention is O(N²) in sequence length. Several variants reduce this:

### Linear Attention
Approximates softmax attention with kernel functions:
$$\text{Linear-Attn}(Q, K, V) = \phi(Q)(\phi(K)^T V)$$

O(N) complexity but lower quality.

### Sparse Attention (Longformer, BigBird)
Only attend to local windows + random global tokens:
- Local window: O(N × w) where w is window size
- Global tokens: attend to everything
- Combined: O(N × (w + g))

### Flash Attention
IO-aware exact attention that's 2-4x faster:
- Tiles the computation to fit in GPU SRAM
- Reduces memory access from O(N²) to O(N)
- Same output as standard attention, just faster

```python
# Flash attention is a drop-in replacement
# Available in PyTorch 2.0+
with torch.backends.cuda.sdp_kernel(enable_flash=True):
    output = F.scaled_dot_product_attention(Q, K, V, is_causal=True)
```

### Grouped-Query Attention (GQA)
Used in LLaMA 2 and beyond:
- Multiple query heads share key-value heads
- Reduces KV-cache memory for inference
- 2-3x faster inference with minimal quality loss

### Multi-Query Attention (MQA)
All query heads share one key-value head:
- Maximum memory savings
- Slight quality degradation
- Used in PaLM, Falcon

## Attention Patterns

Different heads learn different patterns:

```
Head 1: Local attention (nearby tokens)
Head 2: Syntactic attention (subject-verb, adjective-noun)
Head 3: Positional attention (same position in different layers)
Head 4: Delimiter attention (attending to [SEP], [CLS])
```

Visualizing attention weights helps interpret model behavior:
```python
import matplotlib.pyplot as plt

def visualize_attention(weights, tokens_x, tokens_y, head=0):
    attn = weights[0, head].detach().cpu()
    plt.figure(figsize=(10, 10))
    plt.imshow(attn, cmap='Blues')
    plt.xticks(range(len(tokens_y)), tokens_y, rotation=90)
    plt.yticks(range(len(tokens_x)), tokens_x)
    plt.colorbar()
    plt.show()
```

## When to Use What

| Scenario | Attention Type |
|---|---|
| Text classification | Self-attention (BERT) |
| Text generation | Causal self-attention (GPT) |
| Translation | Cross-attention (encoder-decoder) |
| Image understanding | Self-attention (ViT) |
| Long documents | Sparse/linear attention |
| Real-time inference | Multi-query/grouped-query |

## Further Reading

- Bahdanau et al. (2014) introduced attention for NMT — foundational
- Flash Attention (Dao et al., 2022) made transformers 2-4x faster
- For efficient attention: Linformer, Performer, and BigBird are all interesting
- For cross-modal attention: see CLIP and DALL-E
