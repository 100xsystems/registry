---
{
  "title": "What Is Computer Vision?",
  "description": "The field, the tasks, and the datasets that drive progress in visual intelligence.",
  "type": "lesson",
  "order": 1,
  "duration": "40 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define computer vision and its core tasks",
    "List the landmark datasets and benchmarks",
    "Contrast classic and deep approaches",
    "Identify real-world vision applications"
  ],
  "knowledge_refs": [
    "computer-vision/cv-01-what-is-computer-vision"
  ],
  "prerequisites": [
    "DL-01: What Is Deep Learning?"
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

# CV-01-WHAT-IS-COMPUTER-VISION: What Is Computer Vision?

## Introduction

The field, the tasks, and the datasets that drive progress in visual intelligence. By the end of this lesson you will be able to: Define computer vision and its core tasks; List the landmark datasets and benchmarks; Contrast classic and deep approaches; Identify real-world vision applications.

## Key Concepts

### 1. Define computer vision and its core tasks

Target: Define computer vision and its core tasks. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
tasks = {
    "classification": "what is in the image?",
    "detection": "where are the objects?",
    "segmentation": "which pixels belong to what?",
    "pose": "where is the person's skeleton?",
}
for task, q in tasks.items():
    print(f"{task:14} {q}")
```
### 2. List the landmark datasets and benchmarks

Target: List the landmark datasets and benchmarks. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from torchvision import datasets

print("MNIST classes:", len(datasets.MNIST("data", download=True, train=True).classes))
```
### 3. Contrast classic and deep approaches

Target: Contrast classic and deep approaches. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

# Images are tensors: (C, H, W) in torch
img = torch.zeros(3, 224, 224)
print("channels, height, width:", img.shape)
```
### 4. Identify real-world vision applications

Target: Identify real-world vision applications. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
apps = ["self-driving", "medical imaging", "retail checkout", "phone camera", "AR filters"]
for a in apps:
    print(f"- {a}")
```

## Practice Questions

1. What is the key idea behind "What Is Computer Vision?"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain What Is Computer Vision? with analogies and real-world examples"
1. "Show me common mistakes beginners make with What Is Computer Vision?"
1. "Provide advanced patterns and performance considerations for What Is Computer Vision?"

## Key Takeaways

- Master the core ideas of What Is Computer Vision? through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
