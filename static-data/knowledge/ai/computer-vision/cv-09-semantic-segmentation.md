---
{
  "title": "Semantic Segmentation",
  "description": "Label every pixel: FCNs, U-Net, and the encoder-decoder design for pixel-level tasks.",
  "type": "lesson",
  "order": 9,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define semantic segmentation",
    "Explain encoder-decoder architectures",
    "Build a U-Net-style model",
    "Evaluate with pixel accuracy and IoU"
  ],
  "knowledge_refs": [
    "computer-vision/cv-08-object-detection",
    "llm-engineering/llm-06-embeddings-and-semantic-search"
  ],
  "prerequisites": [
    "CV-08: Object Detection"
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

# CV-09-SEMANTIC-SEGMENTATION: Semantic Segmentation

## Introduction

Label every pixel: FCNs, U-Net, and the encoder-decoder design for pixel-level tasks. By the end of this lesson you will be able to: Define semantic segmentation; Explain encoder-decoder architectures; Build a U-Net-style model; Evaluate with pixel accuracy and IoU.

## Key Concepts

### 1. Define semantic segmentation

Target: Define semantic segmentation. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch

# Input (B, C, H, W) -> output (B, num_classes, H, W)
x = torch.randn(2, 3, 128, 128)
logits = torch.randn(2, 5, 128, 128)
print("per-pixel class logits:", logits.shape)
```
### 2. Explain encoder-decoder architectures

Target: Explain encoder-decoder architectures. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch.nn as nn

# Encoder-decoder: down then up, with skip connections
print("U-Net pattern: contract -> expand -> concatenate skips")
```
### 3. Build a U-Net-style model

Target: Build a U-Net-style model. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

# Pixel accuracy is easy to game; IoU is honest
pred = torch.randint(0, 2, (256, 256))
true = torch.zeros(256, 256, dtype=torch.long)
inter = ((pred == true) & (pred == 1)).sum()
union = ((pred == 1) | (true == 1)).sum()
print("IoU:", round(inter.item() / union.item(), 3))
```
### 4. Evaluate with pixel accuracy and IoU

Target: Evaluate with pixel accuracy and IoU. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
from torchvision.models.segmentation import fcn_resnet50

m = fcn_resnet50(weights=None, num_classes=3)
print(m)
```

## Practice Questions

1. What is the key idea behind "Semantic Segmentation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Semantic Segmentation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Semantic Segmentation"
1. "Provide advanced patterns and performance considerations for Semantic Segmentation"

## Key Takeaways

- Master the core ideas of Semantic Segmentation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
