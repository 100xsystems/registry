---
{
  "title": "Building an MLP in PyTorch",
  "description": "Assemble a multi-layer perceptron with nn.Module, layers and activations — the skeleton of every modern net.",
  "type": "lesson",
  "order": 9,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define a model with nn.Module",
    "Stack Linear layers and activations",
    "Understand parameter registration",
    "Build a classifier for a small dataset"
  ],
  "knowledge_refs": [
    "deep-learning/dl-09-building-an-mlp-in-pytorch"
  ],
  "prerequisites": [
    "DL-08: PyTorch Tensors & Autograd"
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

# DL-09-BUILDING-AN-MLP-IN-PYTORCH: Building an MLP in PyTorch

## Introduction

Assemble a multi-layer perceptron with nn.Module, layers and activations — the skeleton of every modern net. By the end of this lesson you will be able to: Define a model with nn.Module; Stack Linear layers and activations; Understand parameter registration; Build a classifier for a small dataset.

## Key Concepts

### 1. Define a model with nn.Module

Target: Define a model with nn.Module. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch
import torch.nn as nn

class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(784, 128),
            nn.ReLU(),
            nn.Linear(128, 10),
        )
    def forward(self, x):
        return self.net(x)

model = MLP()
print(model)
```
### 2. Stack Linear layers and activations

Target: Stack Linear layers and activations. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch

x = torch.randn(8, 784)
print("logits:", model(x).shape)  # (8, 10)
```
### 3. Understand parameter registration

Target: Understand parameter registration. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

print("params:", sum(p.numel() for p in model.parameters()))
```
### 4. Build a classifier for a small dataset

Target: Build a classifier for a small dataset. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch
import torch.nn as nn

class DeepMLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.stack = nn.Sequential(
            nn.Linear(64, 256), nn.ReLU(), nn.Dropout(0.2),
            nn.Linear(256, 256), nn.ReLU(), nn.Dropout(0.2),
            nn.Linear(256, 1),
        )
    def forward(self, x):
        return self.stack(x)

print("deep net ready")
```

## Practice Questions

1. What is the key idea behind "Building an MLP in PyTorch"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Building an MLP in PyTorch with analogies and real-world examples"
1. "Show me common mistakes beginners make with Building an MLP in PyTorch"
1. "Provide advanced patterns and performance considerations for Building an MLP in PyTorch"

## Key Takeaways

- Master the core ideas of Building an MLP in PyTorch through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
