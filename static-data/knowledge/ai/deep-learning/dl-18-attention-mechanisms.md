---
{
  "title": "Attention Mechanisms",
  "description": "Query-key-value attention, multi-head splits, and how attention replaced recurrence.",
  "type": "lesson",
  "order": 18,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain Q, K, V roles",
    "Implement multi-head attention",
    "Read attention maps as interpretability",
    "Describe the attention-memory analogy"
  ],
  "knowledge_refs": [
    "deep-learning/dl-17-transformers",
    "nlp/nlp-15-attention-and-transformers",
    "computer-vision/cv-19-vision-transformers"
  ],
  "prerequisites": [
    "DL-17: Transformers"
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

# DL-18-ATTENTION-MECHANISMS: Attention Mechanisms

## Introduction

Query-key-value attention, multi-head splits, and how attention replaced recurrence. By the end of this lesson you will be able to: Explain Q, K, V roles; Implement multi-head attention; Read attention maps as interpretability; Describe the attention-memory analogy.

## Key Concepts

### 1. Explain Q, K, V roles

Target: Explain Q, K, V roles. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch
import torch.nn as nn

mha = nn.MultiheadAttention(embed_dim=64, num_heads=4, batch_first=True)
x = torch.randn(2, 12, 64)
out, attn = mha(x, x, x)
print("out:", out.shape, "attention map:", attn.shape)
```
### 2. Implement multi-head attention

Target: Implement multi-head attention. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch

# Attention as soft lookup: weights sum to 1 per query
attn = torch.softmax(torch.randn(12, 12), dim=-1)
print("row sums ~ 1:", attn.sum(-1).round(3)[:3])
```
### 3. Read attention maps as interpretability

Target: Read attention maps as interpretability. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch.nn as nn

# Head splitting: each head attends to different patterns
print("num_heads=4 -> 4 parallel attention subspaces")
```
### 4. Describe the attention-memory analogy

Target: Describe the attention-memory analogy. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch

# Causal mask: tokens can only attend to the past
mask = torch.triu(torch.ones(8, 8), diagonal=1).bool()
print("causal mask row 3 sees:", (~mask[3]).nonzero().flatten().tolist())
```

## Practice Questions

1. What is the key idea behind "Attention Mechanisms"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Attention Mechanisms with analogies and real-world examples"
1. "Show me common mistakes beginners make with Attention Mechanisms"
1. "Provide advanced patterns and performance considerations for Attention Mechanisms"

## Key Takeaways

- Master the core ideas of Attention Mechanisms through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
