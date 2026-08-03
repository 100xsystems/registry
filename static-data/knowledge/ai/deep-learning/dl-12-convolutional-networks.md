---
{
  "title": "Convolutional Networks",
  "description": "Why convolutions beat dense layers for images: local structure, weight sharing, and translation invariance.",
  "type": "lesson",
  "order": 12,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain convolution and pooling",
    "Build a CNN with nn.Conv2d",
    "Compute output shapes",
    "Train a small CNN on MNIST"
  ],
  "knowledge_refs": [
    "deep-learning/dl-11-regularization-for-deep-learning",
    "reinforcement-learning/rl-09-deep-q-networks",
    "generative-ai/genai-14-gans"
  ],
  "prerequisites": [
    "DL-10: The Training Loop"
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

# DL-12-CONVOLUTIONAL-NETWORKS: Convolutional Networks

## Introduction

Why convolutions beat dense layers for images: local structure, weight sharing, and translation invariance. By the end of this lesson you will be able to: Explain convolution and pooling; Build a CNN with nn.Conv2d; Compute output shapes; Train a small CNN on MNIST.

## Key Concepts

### 1. Explain convolution and pooling

Target: Explain convolution and pooling. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch
import torch.nn as nn

conv = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, padding=1)
x = torch.randn(4, 1, 28, 28)
print("conv out:", conv(x).shape)   # (4, 16, 28, 28)
```
### 2. Build a CNN with nn.Conv2d

Target: Build a CNN with nn.Conv2d. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch.nn as nn

pool = nn.MaxPool2d(2)
print("pooled:", pool(torch.randn(4, 16, 28, 28)).shape)  # 14x14
```
### 3. Compute output shapes

Target: Compute output shapes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch
import torch.nn as nn

class TinyCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 16, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(16, 32, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
        )
        self.head = nn.Linear(32 * 7 * 7, 10)
    def forward(self, x):
        return self.head(self.features(x).flatten(1))

model = TinyCNN()
print(model(torch.randn(2, 1, 28, 28)).shape)
```
### 4. Train a small CNN on MNIST

Target: Train a small CNN on MNIST. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch.nn as nn

# Pooling gives local translation invariance
print("MaxPool2d(2) halves spatial dims, keeps channels")
```

## Practice Questions

1. What is the key idea behind "Convolutional Networks"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Convolutional Networks with analogies and real-world examples"
1. "Show me common mistakes beginners make with Convolutional Networks"
1. "Provide advanced patterns and performance considerations for Convolutional Networks"

## Key Takeaways

- Master the core ideas of Convolutional Networks through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
