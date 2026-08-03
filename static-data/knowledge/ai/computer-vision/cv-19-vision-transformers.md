---
{
  "title": "Vision Transformers (ViT)",
  "description": "Patch the image into tokens and let attention do the rest — the modern alternative to CNNs.",
  "type": "lesson",
  "order": 19,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain patch embedding",
    "Add position embeddings to patches",
    "Use pretrained ViT models",
    "Compare ViT and CNN trade-offs"
  ],
  "knowledge_refs": [
    "computer-vision/cv-19-vision-transformers"
  ],
  "prerequisites": [
    "DL-17: Transformers"
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

# CV-19-VISION-TRANSFORMERS: Vision Transformers (ViT)

## Introduction

Patch the image into tokens and let attention do the rest — the modern alternative to CNNs. By the end of this lesson you will be able to: Explain patch embedding; Add position embeddings to patches; Use pretrained ViT models; Compare ViT and CNN trade-offs.

## Key Concepts

### 1. Explain patch embedding

Target: Explain patch embedding. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch

# Image -> sequence of patches
x = torch.randn(2, 3, 224, 224)
patches = x.unfold(2, 16, 16).unfold(3, 16, 16)
print("patch grid:", patches.shape)
```
### 2. Add position embeddings to patches

Target: Add position embeddings to patches. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch.nn as nn

proj = nn.Conv2d(3, 768, kernel_size=16, stride=16)
tokens = proj(torch.randn(2, 3, 224, 224)).flatten(2).transpose(1, 2)
print("tokens:", tokens.shape)  # (2, 196, 768)
```
### 3. Use pretrained ViT models

Target: Use pretrained ViT models. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torchvision.models as models

vit = models.vit_b_16(weights=models.ViT_B_16_Weights.DEFAULT)
print(vit)
```
### 4. Compare ViT and CNN trade-offs

Target: Compare ViT and CNN trade-offs. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch

print("ViT: needs lots of data, excels at scale; CNNs win small-data")
```

## Practice Questions

1. What is the key idea behind "Vision Transformers (ViT)"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Vision Transformers (ViT) with analogies and real-world examples"
1. "Show me common mistakes beginners make with Vision Transformers (ViT)"
1. "Provide advanced patterns and performance considerations for Vision Transformers (ViT)"

## Key Takeaways

- Master the core ideas of Vision Transformers (ViT) through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
