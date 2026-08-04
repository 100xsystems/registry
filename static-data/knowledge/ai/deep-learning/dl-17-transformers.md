---
slug: dl-17-transformers
title: "Transformers"
description: "The architecture that changed everything — self-attention, parallelism, and the foundation of GPT, BERT, and modern AI."
order: 17
tags:
  - deep-learning
  - transformers
  - attention
  - bert
  - gpt
prerequisites:
  - dl-18-attention-mechanisms
  - dl-15-recurrent-networks
  - dl-09-building-an-mlp-in-pytorch
references:
  - title: "Attention Is All You Need (Vaswani et al., 2017)"
    url: "https://arxiv.org/abs/1706.03762"
    description: "The transformer paper — arguably the most important ML paper of the decade"
  - title: "The Illustrated Transformer (Jay Alammar)"
    url: "https://jalammar.github.io/illustrated-transformer/"
    description: "The best visual explanation of transformers"
  - title: "BERT: Pre-training of Deep Bidirectional Transformers"
    url: "https://arxiv.org/abs/1810.04805"
    description: "Devlin et al.'s BERT — bidirectional pretraining for NLP"
  - title: "Language Models are Few-Shot Learners (GPT-3)"
    url: "https://arxiv.org/abs/2005.14165"
    description: "Brown et al.'s GPT-3 paper — scaling laws and in-context learning"
  - title: "A Tutorial on the Transformer Architecture"
    url: "https://nlp.seas.harvard.edu/annotated-transformer/"
    description: "Harvard's annotated transformer implementation"
knowledge_refs:
  - dl-18-attention-mechanisms
  - dl-15-recurrent-networks
  - dl-11-regularization-for-deep-learning
---

# Transformers

The transformer (Vaswani et al., 2017) replaced recurrent processing with **self-attention**, enabling massive parallelization and capturing long-range dependencies. It's the foundation of GPT, BERT, vision transformers, and essentially all of modern AI.

## Why Transformers Won

RNNs process tokens sequentially — O(N) steps, no parallelism. Transformers process all tokens simultaneously — O(1) steps, full parallelism.

| Aspect | RNN | Transformer |
|---|---|---|
| Parallelism | Sequential | Fully parallel |
| Long-range dependencies | Vanish over distance | Direct attention |
| Training speed | Slow (GPU underutilized) | Fast (GPU saturated) |
| Memory | O(N) | O(N²) attention matrix |

The trade-off: transformers use O(N²) memory for attention, but this is manageable for most sequence lengths.

## The Transformer Architecture

```
Input Embedding + Positional Encoding
         ↓
┌─────────────────────┐
│  Transformer Block  │ × N layers
│  ┌─────────────────┐│
│  │ Multi-Head       ││
│  │ Self-Attention   ││
│  └─────────────────┘│
│  Add & LayerNorm    │
│  ┌─────────────────┐│
│  │ Feed-Forward     ││
│  │ Network          ││
│  └─────────────────┘│
│  Add & LayerNorm    │
└─────────────────────┘
         ↓
Output (logits / embeddings)
```

## Self-Attention

The core mechanism. Every token attends to every other token:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

where $Q$ (queries), $K$ (keys), $V$ (values) are linear projections of the input.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

def self_attention(x, d_k):
    B, T, D = x.shape
    Q = x[:, :, :d_k]
    K = x[:, :, :d_k:T]
    V = x[:, :, d_k:T*2]
    
    scores = torch.matmul(Q, K.transpose(-2, -1)) / (d_k ** 0.5)
    weights = F.softmax(scores, dim=-1)
    return torch.matmul(weights, V)
```

## Multi-Head Attention

Multiple attention heads learn different relationship patterns:

```python
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)
    
    def forward(self, x):
        B, T, D = x.shape
        
        Q = self.W_q(x).view(B, T, self.num_heads, self.d_k).transpose(1, 2)
        K = self.W_k(x).view(B, T, self.num_heads, self.d_k).transpose(1, 2)
        V = self.W_v(x).view(B, T, self.num_heads, self.d_k).transpose(1, 2)
        
        scores = torch.matmul(Q, K.transpose(-2, -1)) / (self.d_k ** 0.5)
        weights = F.softmax(scores, dim=-1)
        output = torch.matmul(weights, V)
        
        output = output.transpose(1, 2).contiguous().view(B, T, D)
        return self.W_o(output)
```

## Positional Encoding

Transformers have no inherent notion of position. Positional encoding adds position information:

$$PE_{(pos, 2i)} = \sin(pos / 10000^{2i/d_{model}})$$
$$PE_{(pos, 2i+1)} = \cos(pos / 10000^{2i/d_{model}})$$

```python
class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=5000):
        super().__init__()
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len).unsqueeze(1).float()
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * -(math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        self.register_buffer('pe', pe.unsqueeze(0))
    
    def forward(self, x):
        return x + self.pe[:, :x.size(1)]
```

**Learned positional embeddings** (used in GPT, BERT) are often better than sinusoidal.

## Transformer Block

```python
class TransformerBlock(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout=0.1):
        super().__init__()
        self.attention = MultiHeadAttention(d_model, num_heads)
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.ff = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.GELU(),
            nn.Linear(d_ff, d_model)
        )
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, x):
        # Self-attention with residual connection
        x = x + self.dropout(self.attention(self.norm1(x)))
        # Feed-forward with residual connection
        x = x + self.dropout(self.ff(self.norm2(x)))
        return x
```

## Two Transformer Variants

### Encoder-Only (BERT)
- Bidirectional attention (sees both past and future)
- Pretrained on masked language modeling
- Best for: classification, NER, question answering

### Decoder-Only (GPT)
- Causal attention (only sees past tokens)
- Pretrained on next-token prediction
- Best for: text generation, in-context learning

```python
# GPT-style causal mask
def causal_mask(seq_len):
    return torch.triu(torch.ones(seq_len, seq_len), diagonal=1).bool()

# In attention:
scores.masked_fill(causal_mask(T), float('-inf'))
```

## Complete Transformer Model

```python
class TransformerClassifier(nn.Module):
    def __init__(self, vocab_size, d_model=256, num_heads=8, num_layers=4, num_classes=10):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_encoding = PositionalEncoding(d_model)
        self.layers = nn.ModuleList([
            TransformerBlock(d_model, num_heads, d_model * 4) for _ in range(num_layers)
        ])
        self.norm = nn.LayerNorm(d_model)
        self.classifier = nn.Linear(d_model, num_classes)
    
    def forward(self, x):
        x = self.embedding(x) * (x.shape[1] ** 0.5)
        x = self.pos_encoding(x)
        for layer in self.layers:
            x = layer(x)
        x = self.norm(x[:, 0])  # CLS token
        return self.classifier(x)
```

## Scaling Laws

Larger transformers consistently perform better, following predictable power laws:
- Performance scales as a power law with model size, data, and compute
- GPT-3 (175B parameters) demonstrated that scaling enables in-context learning
- Chinchilla (70B) showed that data and model should scale together

## What's Next

The next lesson dives deeper into **attention mechanisms** — the foundation of everything in this lesson.

## Further Reading

- Vaswani et al. (2017) is the most important ML paper of the decade
- Jay Alammar's Illustrated Transformer is the best visual introduction
- Harvard's annotated transformer provides a detailed implementation
- For modern LLMs: see the LLM Engineering course for GPT, BERT, and beyond
