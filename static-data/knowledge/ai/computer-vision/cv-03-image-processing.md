---
{
  "title": "Image Processing Fundamentals",
  "description": "Convolutions, blur, edges and thresholds — the classic toolbox that still powers pipelines today.",
  "type": "lesson",
  "order": 3,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain 2D convolution on images",
    "Apply blur and sharpening filters",
    "Detect edges with Sobel/Canny",
    "Threshold and morph images"
  ],
  "knowledge_refs": [
    "computer-vision/cv-02-image-representation"
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

# CV-03-IMAGE-PROCESSING: Image Processing Fundamentals

## Introduction

Convolutions, blur, edges and thresholds — the classic toolbox that still powers pipelines today. By the end of this lesson you will be able to: Explain 2D convolution on images; Apply blur and sharpening filters; Detect edges with Sobel/Canny; Threshold and morph images.

## Key Concepts

### 1. Explain 2D convolution on images

Target: Explain 2D convolution on images. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import cv2
import numpy as np

img = np.full((8, 8), 50, dtype=np.uint8)
img[3:5, 3:5] = 200
blurred = cv2.GaussianBlur(img, (3, 3), 0)
print("blurred center:", blurred[3:5, 3:5])
```
### 2. Apply blur and sharpening filters

Target: Apply blur and sharpening filters. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import cv2

# Edge detection
edges = cv2.Canny(img, 50, 150)
print("edges shape:", edges.shape)
```
### 3. Detect edges with Sobel/Canny

Target: Detect edges with Sobel/Canny. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import cv2

# Simple box blur via convolution
kernel = np.ones((3, 3), np.float32) / 9
box = cv2.filter2D(img, -1, kernel)
print("box-blurred:", box)
```
### 4. Threshold and morph images

Target: Threshold and morph images. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import cv2

# Thresholding for masks
_, mask = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
print("mask unique values:", np.unique(mask))
```

## Practice Questions

1. What is the key idea behind "Image Processing Fundamentals"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Image Processing Fundamentals with analogies and real-world examples"
1. "Show me common mistakes beginners make with Image Processing Fundamentals"
1. "Provide advanced patterns and performance considerations for Image Processing Fundamentals"

## Key Takeaways

- Master the core ideas of Image Processing Fundamentals through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
