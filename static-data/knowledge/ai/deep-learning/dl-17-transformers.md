---
{
  "title": "Transformers",
  "description": "The architecture behind modern AI: self-attention, positional encoding, and parallelized sequence processing.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain self-attention in one sentence",
    "Compute attention weights with scaled dot products",
    "Understand multi-head attention and position encodings",
    "Use nn.TransformerEncoder"
  ],
  "knowledge_refs": [
    "deep-learning/dl-17-transformers"
  ],
  "prerequisites": [
    "DL-16: LSTM & GRU"
  ],
  "references": [
    {
      "title": "PyTorch Documentation",
      "url": "https://pytorch.org/docs/stable/index.html",
      "description": "The official reference for the deep-learning framework used across this course."
    },
    {
      "title": "Deep Learning — Goodfellow, Bengio & Courville",
      "url": "https://www.deeplearningbook.org/",
      "description": "The canonical textbook on deep learning (free HTML)."
    },
    {
      "title": "Dive into Deep Learning (d2l.ai)",
      "url": "https://d2l.ai/",
      "description": "Interactive deep-learning textbook with code in PyTorch."
    },
    {
      "title": "Practical Deep Learning — fast.ai",
      "url": "https://course.fast.ai/",
      "description": "A top-down course that gets you training models quickly."
    },
    {
      "title": "Attention Is All You Need",
      "url": "https://arxiv.org/abs/1706.03762",
      "description": "The paper that introduced the Transformer architecture."
    }
  ]
}
---

# DL-17-TRANSFORMERS: Transformers

## Introduction

The architecture behind modern AI: self-attention, positional encoding, and parallelized sequence processing. By the end of this lesson you will be able to: Explain self-attention in one sentence; Compute attention weights with scaled dot products; Understand multi-head attention and position encodings; Use nn.TransformerEncoder.

## Key Concepts

### 1. Explain self-attention in one sentence

Target: Explain self-attention in one sentence. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch
import torch.nn.functional as F

Q = torch.randn(4, 8)   # 4 tokens, 8-dim
K = torch.randn(4, 8)
V = torch.randn(4, 8)
scores = Q @ K.T / (8 ** 0.5)
weights = F.softmax(scores, dim=-1)
out = weights @ V
print("attention out:", out.shape)
```
### 2. Compute attention weights with scaled dot products

Target: Compute attention weights with scaled dot products. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch

# Scaled dot-product: scale prevents softmax saturation
import math
logits = torch.randn(10, 10)
print("scaled:", (logits / math.sqrt(10)).std().round(3))
```
### 3. Understand multi-head attention and position encodings

Target: Understand multi-head attention and position encodings. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch.nn as nn

encoder = nn.TransformerEncoderLayer(d_model=64, nhead=4, batch_first=True)
x = torch.randn(2, 20, 64)   # batch, seq, dim
print("encoded:", encoder(x).shape)
```
### 4. Use nn.TransformerEncoder

Target: Use nn.TransformerEncoder. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch.nn as nn

class TinyTransformer(nn.Module):
    def __init__(self):
        super().__init__()
        self.emb = nn.Embedding(100, 64)
        self.layers = nn.TransformerEncoder(nn.TransformerEncoderLayer(64, 4, batch_first=True), num_layers=2)
        self.head = nn.Linear(64, 100)
    def forward(self, ids):
        return self.head(self.layers(self.emb(ids)))

print("tiny transformer:", TinyTransformer()(torch.randint(0, 100, (2, 10))).shape)
```

## Practice Questions

1. What is the key idea behind "Transformers"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Transformers with analogies and real-world examples"
1. "Show me common mistakes beginners make with Transformers"
1. "Provide advanced patterns and performance considerations for Transformers"

## Key Takeaways

- Master the core ideas of Transformers through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
