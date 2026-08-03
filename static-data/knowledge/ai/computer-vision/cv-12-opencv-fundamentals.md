---
{
  "title": "OpenCV Fundamentals",
  "description": "The industrial workhorse: reading, writing, resizing, drawing, and real-time camera capture.",
  "type": "lesson",
  "order": 12,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read and write images with OpenCV",
    "Resize, crop and rotate images",
    "Draw boxes and text for visualization",
    "Capture frames from a webcam"
  ],
  "knowledge_refs": [
    "computer-vision/cv-12-opencv-fundamentals"
  ],
  "prerequisites": [
    "CV-03: Image Processing Fundamentals"
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

# CV-12-OPENCV-FUNDAMENTALS: OpenCV Fundamentals

## Introduction

The industrial workhorse: reading, writing, resizing, drawing, and real-time camera capture. By the end of this lesson you will be able to: Read and write images with OpenCV; Resize, crop and rotate images; Draw boxes and text for visualization; Capture frames from a webcam.

## Key Concepts

### 1. Read and write images with OpenCV

Target: Read and write images with OpenCV. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import cv2

img = cv2.imread("photo.jpg")
print("loaded:", None if img is None else img.shape)
```
### 2. Resize, crop and rotate images

Target: Resize, crop and rotate images. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import cv2

small = cv2.resize(img, (640, 480))
print("resized:", small.shape)
```
### 3. Draw boxes and text for visualization

Target: Draw boxes and text for visualization. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import cv2

# BGR ordering in OpenCV, RGB elsewhere
print("OpenCV uses BGR; convert with cvtColor")
```
### 4. Capture frames from a webcam

Target: Capture frames from a webcam. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import cv2

# Draw a detection box
img = cv2.rectangle(img.copy(), (10, 10), (100, 100), (0, 255, 0), 2)
print("box drawn")
```

## Practice Questions

1. What is the key idea behind "OpenCV Fundamentals"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain OpenCV Fundamentals with analogies and real-world examples"
1. "Show me common mistakes beginners make with OpenCV Fundamentals"
1. "Provide advanced patterns and performance considerations for OpenCV Fundamentals"

## Key Takeaways

- Master the core ideas of OpenCV Fundamentals through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
