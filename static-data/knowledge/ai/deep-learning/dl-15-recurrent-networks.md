---
slug: dl-15-recurrent-networks
title: "Recurrent Neural Networks"
description: "Networks with memory — how RNNs process sequential data one timestep at a time."
order: 15
tags:
  - deep-learning
  - rnn
  - sequences
  - time-series
  - nlp
prerequisites:
  - dl-09-building-an-mlp-in-pytorch
  - dl-05-backpropagation
  - dl-06-loss-functions
references:
  - title: "Deep Learning Book: Chapter 10 — Sequence Modeling"
    url: "https://www.deeplearningbook.org/contents/rnn.html"
    description: "Goodfellow et al.'s comprehensive treatment of RNNs and sequence models"
  - title: "Understanding LSTM Networks (Colah)"
    url: "https://colah.github.io/posts/2015-08-Understanding-LSTMs/"
    description: "The definitive visual explanation of LSTMs"
  - title: "Sequence to Sequence Learning with Neural Networks"
    url: "https://arxiv.org/abs/1409.3215"
    description: "Sutskever et al.'s seq2seq paper — foundational for machine translation"
  - title: "The Unreasonable Effectiveness of RNNs (Karpathy)"
    url: "https://karpathy.github.io/2015/05/21/rnn-effectiveness/"
    description: "Karpathy's famous blog post on generating text with RNNs"
  - title: "PyTorch RNN Tutorial"
    url: "https://pytorch.org/docs/stable/generated/torch.nn.RNN.html"
    description: "Official PyTorch documentation for RNN layers"
knowledge_refs:
  - dl-16-lstm-and-gru
  - dl-17-transformers
  - dl-04-forward-propagation
---

# Recurrent Neural Networks

RNNs process **sequences** — text, time series, audio, video — by maintaining a hidden state that evolves over time. They were the dominant architecture for sequential data before transformers took over.

## The Sequential Problem

Standard neural networks process each input independently. But sequences have order:
- "The cat sat on the mat" ≠ "The mat sat on the cat"
- Tomorrow's stock price depends on today's prices
- Each frame of a video depends on previous frames

RNNs solve this by maintaining a **hidden state** that carries information from previous timesteps.

## How RNNs Work

At each timestep $t$, the RNN:
1. Takes current input $\mathbf{x}_t$ and previous hidden state $\mathbf{h}_{t-1}$
2. Computes new hidden state: $\mathbf{h}_t = f(W_{hh} \mathbf{h}_{t-1} + W_{xh} \mathbf{x}_t + \mathbf{b})$
3. Optionally produces output: $\mathbf{y}_t = W_{hy} \mathbf{h}_t$

```python
import torch.nn as nn

rnn = nn.RNN(input_size=10, hidden_size=64, num_layers=1, batch_first=True)

# Input: (batch, seq_len, features)
x = torch.randn(32, 50, 10)  # 32 sequences, 50 timesteps, 10 features

# Output: (batch, seq_len, hidden_size), hidden: (num_layers, batch, hidden_size)
output, hidden = rnn(x)
print(output.shape)  # (32, 50, 64)
print(hidden.shape)  # (1, 32, 64) — final hidden state
```

**Weight sharing**: The same $W_{hh}$ and $W_{xh}$ are used at every timestep. This means RNNs can handle sequences of any length.

## Types of RNN Architectures

```
One-to-Many:    Input → [RNN] → [RNN] → [RNN] → Output sequence
                (e.g., image captioning)

Many-to-One:    [RNN] → [RNN] → [RNN] → Input sequence → Output
                (e.g., sentiment analysis)

Many-to-Many:   [RNN] → [RNN] → [RNN] → [RNN] → Input → Output sequence
                (e.g., named entity recognition, same length)

Seq-to-Seq:     Encoder: [RNN] → [RNN] → context vector
                Decoder: → [RNN] → [RNN] → [RNN] → Output sequence
                (e.g., machine translation)
```

## Backpropagation Through Time (BPTT)

RNNs are unrolled through time and trained with standard backpropagation:

```
h₀ → h₁ → h₂ → ... → hₜ
       ↓       ↓             ↓
      y₁      y₂            yₜ
```

The loss is summed over all timesteps:
$$\mathcal{L} = \sum_{t=1}^{T} \mathcal{L}_t(\hat{y}_t, y_t)$$

Gradients flow backward through the entire unrolled network.

## The Vanishing/Exploding Gradient Problem

Through many timesteps, gradients multiply repeatedly:

$$\frac{\partial h_T}{\partial h_1} = \prod_{t=2}^{T} \frac{\partial h_t}{\partial h_{t-1}}$$

If the Jacobian has eigenvalues < 1, gradients vanish exponentially. If > 1, they explode.

**Consequences:**
- **Vanishing**: RNN can't learn long-range dependencies (forgetting early information)
- **Exploding**: Training diverges, NaN losses

**Solutions:**
- **Gradient clipping**: Prevents explosion
- **LSTM/GRU gates**: Prevent vanishing (next lesson)
- **Truncated BPTT**: Limit the unroll length

```python
# Gradient clipping
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=5.0)
```

## PyTorch RNN Variants

```python
# Vanilla RNN
rnn = nn.RNN(input_size=10, hidden_size=64, batch_first=True)

# LSTM (Long Short-Term Memory)
lstm = nn.LSTM(input_size=10, hidden_size=64, num_layers=2, 
               batch_first=True, dropout=0.2, bidirectional=True)

# GRU (Gated Recurrent Unit)
gru = nn.GRU(input_size=10, hidden_size=64, batch_first=True)
```

## RNN for Text Classification

```python
class TextRNN(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, num_classes):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, num_layers=2, 
                           batch_first=True, bidirectional=True, dropout=0.3)
        self.fc = nn.Linear(hidden_dim * 2, num_classes)  # *2 for bidirectional
    
    def forward(self, x):
        embeds = self.embedding(x)           # (B, seq_len, embed_dim)
        output, (hidden, cell) = self.lstm(embeds)
        
        # Concatenate final forward and backward hidden states
        hidden = torch.cat([hidden[-2], hidden[-1]], dim=1)  # (B, hidden*2)
        return self.fc(hidden)
```

## RNN for Time Series

```python
class TimeSeriesRNN(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers=1, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)
    
    def forward(self, x):
        # x: (B, seq_len, features)
        lstm_out, _ = self.lstm(x)
        # Take the last timestep's output
        last_output = lstm_out[:, -1, :]
        return self.fc(last_output)
```

## Why RNNs Were Replaced

Despite their elegance, RNNs have fundamental limitations:

1. **Sequential computation**: Can't parallelize across timesteps (slow on GPUs)
2. **Short memory**: Even LSTMs struggle with > 1000 timestep dependencies
3. **Training instability**: Vanishing/exploding gradients, sensitive to hyperparameters
4. **Transformers are better**: Self-attention handles long-range dependencies in parallel

**When RNNs are still useful:**
- Streaming/online processing (one timestep at a time)
- Very long sequences where transformers are memory-prohibitive
- Simple sequence tasks where transformers are overkill
- Edge devices with limited compute

## Further Reading

- Colah's LSTM post is the best visual explanation ever written
- Karpathy's "Unreasonable Effectiveness" post is essential reading
- For modern sequence modeling: the next lesson covers LSTMs/GRUs, then transformers
- For time series: N-BEATS, TFT, and PatchTST are current state-of-the-art
