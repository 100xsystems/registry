---
slug: dl-16-lstm-and-gru
title: "LSTM & GRU"
description: "Gated architectures that solved the vanishing gradient problem — enabling RNNs to learn long-range dependencies."
order: 16
tags:
  - deep-learning
  - lstm
  - gru
  - gating
  - sequences
prerequisites:
  - dl-15-recurrent-networks
  - dl-05-backpropagation
references:
  - title: "Long Short-Term Memory (Hochreiter & Schmidhuber, 1997)"
    url: "https://doi.org/10.1162/neco.1997.9.8.1735"
    description: "The original LSTM paper — one of the most cited in deep learning"
  - title: "Learning Phrase Representations using RNN Encoder-Decoder (GRU)"
    url: "https://arxiv.org/abs/1406.1078"
    description: "Cho et al.'s GRU paper — simpler alternative to LSTM"
  - title: "Understanding LSTM Networks (Colah)"
    url: "https://colah.github.io/posts/2015-08-Understanding-LSTMs/"
    description: "The definitive visual guide to LSTM gates"
  - title: "An Empirical Exploration of RNN Architectures (Jozefowicz et al.)"
    url: "https://arxiv.org/abs/1502.04759"
    description: "Systematic study of which gates matter in LSTMs and GRUs"
  - title: "Sequence Modeling with GRUs and LSTMs (distill.pub)"
    url: "https://distill.pub/2019/memorization-in-rnns/"
    description: "Interactive exploration of how gated RNNs remember and forget"
knowledge_refs:
  - dl-15-recurrent-networks
  - dl-17-transformers
  - dl-07-optimizers
---

# LSTM & GRU

Vanilla RNNs can't learn long-range dependencies due to vanishing gradients. LSTMs and GRUs solve this with **gating mechanisms** that control what information flows through the network over time.

## The Problem with Vanilla RNNs

In a vanilla RNN, the hidden state is updated as:
$$\mathbf{h}_t = \tanh(W_{hh}\mathbf{h}_{t-1} + W_{xh}\mathbf{x}_t + \mathbf{b})$$

The same $\tanh$ is applied at every step. Over many steps, gradients shrink exponentially:
$$\frac{\partial \mathbf{h}_T}{\partial \mathbf{h}_1} = \prod_{t=2}^{T} \tanh'(W_{hh}\mathbf{h}_{t-1} + \ldots) \cdot W_{hh}$$

With $\tanh' \leq 1$ and typical weight values, the product → 0 rapidly.

## LSTM: Long Short-Term Memory

LSTMs (Hochreiter & Schmidhuber, 1997) introduce a **cell state** $\mathbf{c}_t$ that acts as a highway for information, controlled by three gates:

### The Three Gates

**Forget gate**: What to remove from cell state
$$\mathbf{f}_t = \sigma(W_f[\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_f)$$

**Input gate**: What new information to store
$$\mathbf{i}_t = \sigma(W_i[\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_i)$$
$$\tilde{\mathbf{c}}_t = \tanh(W_c[\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_c)$$

**Output gate**: What to output from cell state
$$\mathbf{o}_t = \sigma(W_o[\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_o)$$

### Cell State Update

$$\mathbf{c}_t = \mathbf{f}_t \odot \mathbf{c}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{c}}_t$$

**Key insight**: The cell state is updated via **addition**, not multiplication. This creates a gradient highway — gradients flow through the cell state with minimal degradation.

### Hidden State Output

$$\mathbf{h}_t = \mathbf{o}_t \odot \tanh(\mathbf{c}_t)$$

```python
import torch.nn as nn

lstm = nn.LSTM(input_size=10, hidden_size=64, num_layers=2, 
               batch_first=True, bidirectional=True, dropout=0.2)

x = torch.randn(32, 50, 10)  # (batch, seq_len, features)
output, (h_n, c_n) = lstm(x)

print(output.shape)  # (32, 50, 128) — 64*2 for bidirectional
print(h_n.shape)     # (4, 32, 64) — 2 layers × 2 directions
print(c_n.shape)     # (4, 32, 64) — cell states
```

## GRU: Gated Recurrent Unit

GRUs (Cho et al., 2014) simplify LSTMs by merging the forget and input gates:

### Reset Gate (controls how much past to forget)
$$\mathbf{r}_t = \sigma(W_r[\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_r)$$

### Update Gate (controls how much past to keep)
$$\mathbf{z}_t = \sigma(W_z[\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_z)$$

### New Candidate
$$\tilde{\mathbf{h}}_t = \tanh(W[\mathbf{r}_t \odot \mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b})$$

### Hidden State Update
$$\mathbf{h}_t = (1 - \mathbf{z}_t) \odot \mathbf{h}_{t-1} + \mathbf{z}_t \odot \tilde{\mathbf{h}}_t$$

```python
gru = nn.GRU(input_size=10, hidden_size=64, num_layers=2, 
              batch_first=True, bidirectional=True)

x = torch.randn(32, 50, 10)
output, h_n = gru(x)  # No cell state!

print(output.shape)  # (32, 50, 128)
print(h_n.shape)     # (4, 32, 64)
```

## LSTM vs GRU

| Aspect | LSTM | GRU |
|---|---|---|
| Parameters | More (4 gates) | Fewer (2 gates) |
| Training speed | Slower | Faster |
| Cell state | Yes (separate highway) | No (merged) |
| Performance | Slightly better on long sequences | Comparable on many tasks |
| When to use | Long sequences, complex patterns | Shorter sequences, faster training |

**Practical recommendation**: Try GRU first (faster, simpler). Switch to LSTM if performance is insufficient.

## Bidirectional RNNs

Process sequence in both directions to capture context from past AND future:

```python
bi_lstm = nn.LSTM(input_size=10, hidden_size=64, bidirectional=True, batch_first=True)

x = torch.randn(32, 50, 10)
output, (h_n, c_n) = bi_lstm(x)

# Forward: h_n[0] (layer 0, forward)
# Backward: h_n[1] (layer 0, backward)
# Output: concatenation of forward and backward at each timestep
```

**When to use bidirectional**: When the entire sequence is available (classification, NER). **Not for**: autoregressive generation (can't see the future).

## Complete Text Classification Model

```python
class LSTMClassifier(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, num_classes, num_layers=2):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, num_layers=num_layers,
                           batch_first=True, bidirectional=True, dropout=0.3)
        self.attention = nn.Linear(hidden_dim * 2, 1)
        self.fc = nn.Sequential(
            nn.Dropout(0.3),
            nn.Linear(hidden_dim * 2, num_classes)
        )
    
    def forward(self, x):
        embeds = self.embedding(x)
        lstm_out, _ = self.lstm(embeds)  # (B, seq_len, hidden*2)
        
        # Attention mechanism
        attn_weights = torch.softmax(self.attention(lstm_out).squeeze(-1), dim=1)
        context = torch.bmm(attn_weights.unsqueeze(1), lstm_out).squeeze(1)
        
        return self.fc(context)
```

## Stacking Layers

```python
# Multi-layer LSTM
lstm = nn.LSTM(input_size=100, hidden_size=256, num_layers=3,
               batch_first=True, dropout=0.2)

# Each layer processes the output of the previous layer
# Layer 1: processes input
# Layer 2: processes layer 1 output
# Layer 3: processes layer 2 output
```

## Practical Tips

1. **Gradient clipping is essential**: `clip_grad_norm_(5.0)` prevents explosion
2. **Pack padded sequences**: For variable-length inputs:
   ```python
   from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence
   lengths = torch.tensor([50, 30, 45])
   packed = pack_padded_sequence(embeds, lengths, batch_first=True, enforce_sorted=False)
   output, _ = lstm(packed)
   output, _ = pad_packed_sequence(output, batch_first=True)
   ```
3. **Teacher forcing**: During training, feed ground truth as next input
4. **Use `batch_first=True`**: Makes the API more intuitive (B, seq, features)

## When to Use LSTMs/GRUs vs. Transformers

| Task | LSTM/GRU | Transformer |
|---|---|---|
| Online/streaming | ✅ Great | ❌ Needs context |
| Very long sequences (>10K) | ✅ Linear memory | ❌ Quadratic attention |
| Small datasets | ✅ Less overfitting | ❌ Needs more data |
| Parallel training | ❌ Sequential | ✅ Parallel |
| Long-range dependencies | ⚠️ Struggles | ✅ Excellent |
| State of the art | ❌ No | ✅ Yes |

## Further Reading

- Hochreiter & Schmidhuber (1997) is one of the most impactful ML papers
- Cho et al. (2014) introduced GRUs as a simpler alternative
- Colah's visual guide remains the best learning resource
- For modern sequence modeling, the next lesson covers transformers
