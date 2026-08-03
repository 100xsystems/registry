---
{
  "title": "Transfer Learning for Vision",
  "description": "Pretrained backbones are the default starting point — swap the head, keep the features.",
  "type": "lesson",
  "order": 7,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Load a torchvision backbone",
    "Replace the classifier for custom classes",
    "Fine-tune features selectively",
    "Use augmentation with pretrained pipelines"
  ],
  "knowledge_refs": [
    "computer-vision/cv-07-transfer-learning-for-vision"
  ],
  "prerequisites": [
    "DL-14: Transfer Learning"
  ],
  "references": [
    {
      "title": "OpenCV Documentation",
      "url": "https://docs.opencv.org/4.x/index.html",
      "description": "The reference for classic image processing in Python."
    },
    {
      "title": "PyTorch Vision Docs",
      "url": "https://pytorch.org/vision/stable/index.html",
      "description": "Datasets, transforms and model zoo for vision."
    },
    {
      "title": "Stanford CS231n",
      "url": "http://cs231n.stanford.edu/",
      "description": "The classic university course on CNNs for visual recognition."
    },
    {
      "title": "YOLO Papers & Implementations",
      "url": "https://docs.ultralytics.com/",
      "description": "Real-time object detection with YOLOv8 (Ultralytics)."
    },
    {
      "title": "Torchvision Models",
      "url": "https://pytorch.org/vision/stable/models.html",
      "description": "Pretrained model catalog for transfer learning."
    }
  ]
}
---

# CV-07-TRANSFER-LEARNING-FOR-VISION: Transfer Learning for Vision

## Introduction

Pretrained backbones are the default starting point — swap the head, keep the features. By the end of this lesson you will be able to: Load a torchvision backbone; Replace the classifier for custom classes; Fine-tune features selectively; Use augmentation with pretrained pipelines.

## Key Concepts

### 1. Load a torchvision backbone

Target: Load a torchvision backbone. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torchvision.models as models
import torch.nn as nn

m = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
m.fc = nn.Linear(m.fc.in_features, 3)
print(m.fc)
```
### 2. Replace the classifier for custom classes

Target: Replace the classifier for custom classes. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch

for p in m.parameters():
    p.requires_grad = False
for p in m.fc.parameters():
    p.requires_grad = True
print("head-only training")
```
### 3. Fine-tune features selectively

Target: Fine-tune features selectively. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from torchvision import transforms

# Pretrained models expect ImageNet normalization
pre = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
print("use ImageNet stats")
```
### 4. Use augmentation with pretrained pipelines

Target: Use augmentation with pretrained pipelines. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch

# Two-stage: train head, then unfreeze and fine-tune
opt1 = torch.optim.Adam(m.fc.parameters(), lr=1e-3)
print("stage 1 optimizer ready")
```

## Practice Questions

1. What is the key idea behind "Transfer Learning for Vision"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Transfer Learning for Vision with analogies and real-world examples"
1. "Show me common mistakes beginners make with Transfer Learning for Vision"
1. "Provide advanced patterns and performance considerations for Transfer Learning for Vision"

## Key Takeaways

- Master the core ideas of Transfer Learning for Vision through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
