---
{
  "title": "Image Augmentation",
  "description": "Synthesize training variety: flips, rotations, crops and color jitter to make models robust.",
  "type": "lesson",
  "order": 4,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain why augmentation regularizes vision models",
    "Apply geometric and photometric transforms",
    "Build a torchvision augmentation pipeline",
    "Avoid augmentations that break label meaning"
  ],
  "knowledge_refs": [
    "computer-vision/cv-04-image-augmentation"
  ],
  "prerequisites": [
    "CV-02: Image Representation"
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

# CV-04-IMAGE-AUGMENTATION: Image Augmentation

## Introduction

Synthesize training variety: flips, rotations, crops and color jitter to make models robust. By the end of this lesson you will be able to: Explain why augmentation regularizes vision models; Apply geometric and photometric transforms; Build a torchvision augmentation pipeline; Avoid augmentations that break label meaning.

## Key Concepts

### 1. Explain why augmentation regularizes vision models

Target: Explain why augmentation regularizes vision models. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from torchvision import transforms

t = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(15),
    transforms.ColorJitter(brightness=0.2, contrast=0.2),
    transforms.ToTensor(),
])
print("augmentation pipeline ready")
```
### 2. Apply geometric and photometric transforms

Target: Apply geometric and photometric transforms. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from torchvision import transforms

crop = transforms.RandomResizedCrop(224, scale=(0.7, 1.0))
print("random-resized-crop for scale invariance")
```
### 3. Build a torchvision augmentation pipeline

Target: Build a torchvision augmentation pipeline. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torchvision.transforms.functional as F
import torch

x = torch.rand(3, 32, 32)
flipped = F.hflip(x)
print("flip keeps shape:", flipped.shape)
```
### 4. Avoid augmentations that break label meaning

Target: Avoid augmentations that break label meaning. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
from torchvision import transforms

# Label-preserving: never flip text or digits that flip meaning
print("rule: think about what the label means under each transform")
```

## Practice Questions

1. What is the key idea behind "Image Augmentation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Image Augmentation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Image Augmentation"
1. "Provide advanced patterns and performance considerations for Image Augmentation"

## Key Takeaways

- Master the core ideas of Image Augmentation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
