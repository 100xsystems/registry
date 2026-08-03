---
{
  "title": "Transfer Learning",
  "description": "Stand on the shoulders of pretrained models: freeze features, swap the head, and fine-tune.",
  "type": "lesson",
  "order": 14,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain feature reuse across tasks",
    "Freeze layers and replace the classifier head",
    "Fine-tune with a low learning rate",
    "Avoid catastrophic forgetting"
  ],
  "knowledge_refs": [
    "deep-learning/dl-13-cnn-architectures",
    "computer-vision/cv-07-transfer-learning-for-vision"
  ],
  "prerequisites": [
    "DL-13: Classic CNN Architectures"
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

# DL-14-TRANSFER-LEARNING: Transfer Learning

## Introduction

Stand on the shoulders of pretrained models: freeze features, swap the head, and fine-tune. By the end of this lesson you will be able to: Explain feature reuse across tasks; Freeze layers and replace the classifier head; Fine-tune with a low learning rate; Avoid catastrophic forgetting.

## Key Concepts

### 1. Explain feature reuse across tasks

Target: Explain feature reuse across tasks. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torchvision.models as models
import torch.nn as nn

backbone = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
backbone.fc = nn.Linear(backbone.fc.in_features, 2)  # swap head
print(backbone.fc)
```
### 2. Freeze layers and replace the classifier head

Target: Freeze layers and replace the classifier head. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch

for p in backbone.parameters():
    p.requires_grad = False
for p in backbone.fc.parameters():
    p.requires_grad = True
print("frozen except head")
```
### 3. Fine-tune with a low learning rate

Target: Fine-tune with a low learning rate. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

# Fine-tune with a small learning rate
opt = torch.optim.Adam(filter(lambda p: p.requires_grad, backbone.parameters()), lr=1e-4)
print("trainable params:", sum(p.numel() for p in backbone.parameters() if p.requires_grad))
```
### 4. Avoid catastrophic forgetting

Target: Avoid catastrophic forgetting. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch

# Progressive unfreezing: start with head, then thaw blocks
print("fine-tune strategy: head first, then last blocks")
```

## Practice Questions

1. What is the key idea behind "Transfer Learning"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Transfer Learning with analogies and real-world examples"
1. "Show me common mistakes beginners make with Transfer Learning"
1. "Provide advanced patterns and performance considerations for Transfer Learning"

## Key Takeaways

- Master the core ideas of Transfer Learning through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
