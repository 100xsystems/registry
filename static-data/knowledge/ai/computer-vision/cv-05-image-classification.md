---
{
  "title": "Image Classification",
  "description": "The canonical vision task: train a classifier on MNIST/CIFAR and read the results.",
  "type": "lesson",
  "order": 5,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Load a vision dataset with torchvision",
    "Train a CNN classifier",
    "Report per-class accuracy",
    "Inspect misclassified examples"
  ],
  "knowledge_refs": [
    "computer-vision/cv-05-image-classification"
  ],
  "prerequisites": [
    "DL-12: Convolutional Networks"
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

# CV-05-IMAGE-CLASSIFICATION: Image Classification

## Introduction

The canonical vision task: train a classifier on MNIST/CIFAR and read the results. By the end of this lesson you will be able to: Load a vision dataset with torchvision; Train a CNN classifier; Report per-class accuracy; Inspect misclassified examples.

## Key Concepts

### 1. Load a vision dataset with torchvision

Target: Load a vision dataset with torchvision. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from torchvision import datasets, transforms

train = datasets.CIFAR10(
    "data", train=True, download=True,
    transform=transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))]),
)
print("classes:", train.classes)
```
### 2. Train a CNN classifier

Target: Train a CNN classifier. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch
import torch.nn as nn

model = nn.Sequential(
    nn.Conv2d(3, 16, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
    nn.Conv2d(16, 32, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
    nn.Flatten(), nn.Linear(32 * 8 * 8, 10),
)
print(model)
```
### 3. Report per-class accuracy

Target: Report per-class accuracy. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

x = torch.randn(4, 3, 32, 32)
print("logits:", model(x).shape)
```
### 4. Inspect misclassified examples

Target: Inspect misclassified examples. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch

# Per-class accuracy matters more than a single number
preds = torch.randint(0, 10, (1000,))
true = torch.randint(0, 10, (1000,))
acc = (preds == true).float().mean()
print("overall:", round(acc.item(), 3))
```

## Practice Questions

1. What is the key idea behind "Image Classification"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Image Classification with analogies and real-world examples"
1. "Show me common mistakes beginners make with Image Classification"
1. "Provide advanced patterns and performance considerations for Image Classification"

## Key Takeaways

- Master the core ideas of Image Classification through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
