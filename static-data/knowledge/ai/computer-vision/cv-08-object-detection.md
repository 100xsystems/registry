---
{
  "title": "Object Detection",
  "description": "Bounding boxes and classes: two-stage detectors, single-shot detectors, and YOLO in practice.",
  "type": "lesson",
  "order": 8,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Frame detection as boxes + classes",
    "Explain anchor boxes and IoU",
    "Compare two-stage and single-shot designs",
    "Run YOLO with the Ultralytics library"
  ],
  "knowledge_refs": [
    "computer-vision/cv-07-transfer-learning-for-vision",
    "mlops/mlops-14-monitoring-and-drift"
  ],
  "prerequisites": [
    "CV-07: Transfer Learning for Vision"
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

# CV-08-OBJECT-DETECTION: Object Detection

## Introduction

Bounding boxes and classes: two-stage detectors, single-shot detectors, and YOLO in practice. By the end of this lesson you will be able to: Frame detection as boxes + classes; Explain anchor boxes and IoU; Compare two-stage and single-shot designs; Run YOLO with the Ultralytics library.

## Key Concepts

### 1. Frame detection as boxes + classes

Target: Frame detection as boxes + classes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import torch

# Detection output: (boxes, scores, class_ids)
boxes = torch.tensor([[10, 10, 40, 40], [5, 5, 30, 30]])
scores = torch.tensor([0.9, 0.4])
print("keep:", scores > 0.5)
```
### 2. Explain anchor boxes and IoU

Target: Explain anchor boxes and IoU. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch

def iou(a, b):
    x1 = max(a[0], b[0]); y1 = max(a[1], b[1])
    x2 = min(a[2], b[2]); y2 = min(a[3], b[3])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    area_a = (a[2] - a[0]) * (a[3] - a[1])
    area_b = (b[2] - b[0]) * (b[3] - b[1])
    return inter / (area_a + area_b - inter)

print("IoU:", round(iou((0, 0, 10, 10), (5, 5, 15, 15)), 2))
```
### 3. Compare two-stage and single-shot designs

Target: Compare two-stage and single-shot designs. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")   # pretrained nano
print("yolo model ready")
```
### 4. Run YOLO with the Ultralytics library

Target: Run YOLO with the Ultralytics library. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch

# Non-max suppression removes duplicate boxes
from torchvision.ops import nms
boxes = torch.tensor([[10, 10, 40, 40], [12, 12, 42, 42], [80, 80, 120, 120]])
scores = torch.tensor([0.9, 0.85, 0.7])
keep = nms(boxes, scores, iou_threshold=0.5)
print("kept boxes:", keep)
```

## Practice Questions

1. What is the key idea behind "Object Detection"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Object Detection with analogies and real-world examples"
1. "Show me common mistakes beginners make with Object Detection"
1. "Provide advanced patterns and performance considerations for Object Detection"

## Key Takeaways

- Master the core ideas of Object Detection through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
