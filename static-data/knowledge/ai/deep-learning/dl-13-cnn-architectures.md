---
{
  "title": "Classic CNN Architectures",
  "description": "LeNet, VGG, ResNet — the ideas (depth, skip connections) that shaped modern vision models.",
  "type": "lesson",
  "order": 13,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Trace LeNet and VGG design patterns",
    "Explain residual/skip connections",
    "Understand why depth needs ResNets",
    "Load a pretrained ResNet from torchvision"
  ],
  "knowledge_refs": [
    "deep-learning/dl-13-cnn-architectures"
  ],
  "prerequisites": [
    "DL-12: Convolutional Networks"
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

# DL-13-CNN-ARCHITECTURES: Classic CNN Architectures

## Introduction

LeNet, VGG, ResNet — the ideas (depth, skip connections) that shaped modern vision models. By the end of this lesson you will be able to: Trace LeNet and VGG design patterns; Explain residual/skip connections; Understand why depth needs ResNets; Load a pretrained ResNet from torchvision.

## Key Concepts

### 1. Trace LeNet and VGG design patterns

Target: Trace LeNet and VGG design patterns. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torchvision.models as models

resnet = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
print(resnet)
```
### 2. Explain residual/skip connections

Target: Explain residual/skip connections. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch

x = torch.randn(2, 3, 224, 224)
print("resnet out:", resnet(x).shape)  # (2, 1000)
```
### 3. Understand why depth needs ResNets

Target: Understand why depth needs ResNets. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch.nn as nn

# A residual block: y = F(x) + x
class ResidualBlock(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.f = nn.Sequential(nn.Conv2d(dim, dim, 3, padding=1), nn.ReLU(), nn.Conv2d(dim, dim, 3, padding=1))
    def forward(self, x):
        return nn.functional.relu(self.f(x) + x)
```
### 4. Load a pretrained ResNet from torchvision

Target: Load a pretrained ResNet from torchvision. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torchvision.models as models

vgg = models.vgg16(weights=models.VGG16_Weights.DEFAULT)
print("vgg conv layers:", len(list(vgg.features)))
```

## Practice Questions

1. What is the key idea behind "Classic CNN Architectures"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Classic CNN Architectures with analogies and real-world examples"
1. "Show me common mistakes beginners make with Classic CNN Architectures"
1. "Provide advanced patterns and performance considerations for Classic CNN Architectures"

## Key Takeaways

- Master the core ideas of Classic CNN Architectures through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
