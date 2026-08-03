---
{
  "title": "Image Representation",
  "description": "Pixels, channels, color spaces and the tensor layouts every vision library uses.",
  "type": "lesson",
  "order": 2,
  "duration": "50 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Describe an image as a tensor of pixels",
    "Understand RGB and grayscale channels",
    "Convert between HWC and CHW layouts",
    "Normalize images for model input"
  ],
  "knowledge_refs": [
    "computer-vision/cv-01-what-is-computer-vision",
    "nlp/nlp-02-text-representation"
  ],
  "prerequisites": [
    "CV-01: What Is Computer Vision?"
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

# CV-02-IMAGE-REPRESENTATION: Image Representation

## Introduction

Pixels, channels, color spaces and the tensor layouts every vision library uses. By the end of this lesson you will be able to: Describe an image as a tensor of pixels; Understand RGB and grayscale channels; Convert between HWC and CHW layouts; Normalize images for model input.

## Key Concepts

### 1. Describe an image as a tensor of pixels

Target: Describe an image as a tensor of pixels. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

img = np.zeros((4, 4, 3), dtype=np.uint8)  # HWC
img[1, 1] = [255, 0, 0]  # a red pixel
print("pixel (1,1):", img[1, 1])
```
### 2. Understand RGB and grayscale channels

Target: Understand RGB and grayscale channels. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import cv2

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
print("grayscale shape:", gray.shape)
```
### 3. Convert between HWC and CHW layouts

Target: Convert between HWC and CHW layouts. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

x = torch.tensor(img)  # (H, W, C)
chw = x.permute(2, 0, 1)  # (C, H, W)
print("torch layout:", chw.shape)
```
### 4. Normalize images for model input

Target: Normalize images for model input. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
from torchvision import transforms

t = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
print("normalization pipeline ready")
```

## Practice Questions

1. What is the key idea behind "Image Representation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Image Representation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Image Representation"
1. "Provide advanced patterns and performance considerations for Image Representation"

## Key Takeaways

- Master the core ideas of Image Representation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
