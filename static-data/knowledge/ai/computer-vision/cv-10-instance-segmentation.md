---
{
  "title": "Instance Segmentation",
  "description": "Separate each object, not just each class: Mask R-CNN and the mask-head idea.",
  "type": "lesson",
  "order": 10,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Distinguish semantic from instance segmentation",
    "Explain the Mask R-CNN two-stage design",
    "Load a pretrained instance segmentation model",
    "Evaluate masks with mask IoU"
  ],
  "knowledge_refs": [
    "computer-vision/cv-10-instance-segmentation"
  ],
  "prerequisites": [
    "CV-09: Semantic Segmentation"
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

# CV-10-INSTANCE-SEGMENTATION: Instance Segmentation

## Introduction

Separate each object, not just each class: Mask R-CNN and the mask-head idea. By the end of this lesson you will be able to: Distinguish semantic from instance segmentation; Explain the Mask R-CNN two-stage design; Load a pretrained instance segmentation model; Evaluate masks with mask IoU.

## Key Concepts

### 1. Distinguish semantic from instance segmentation

Target: Distinguish semantic from instance segmentation. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from torchvision.models.detection import maskrcnn_resnet50_fpn

m = maskrcnn_resnet50_fpn(weights=None, num_classes=91)
print("mask r-cnn ready")
```
### 2. Explain the Mask R-CNN two-stage design

Target: Explain the Mask R-CNN two-stage design. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch

# Output: boxes, labels, scores, masks per instance
out = {"boxes": torch.zeros(3, 4), "masks": torch.zeros(3, 1, 32, 32)}
print("per-instance masks:", out["masks"].shape)
```
### 3. Load a pretrained instance segmentation model

Target: Load a pretrained instance segmentation model. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

# Panoptic: semantic + instance merged into one label per pixel
print("panoptic segmentation unifies both tasks")
```
### 4. Evaluate masks with mask IoU

Target: Evaluate masks with mask IoU. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import torch

def mask_iou(a, b):
    inter = (a & b).sum()
    union = (a | b).sum()
    return inter / union

a = torch.tensor([[True, True], [False, False]])
b = torch.tensor([[True, False], [False, False]])
print("mask IoU:", round(mask_iou(a, b).item(), 2))
```

## Practice Questions

1. What is the key idea behind "Instance Segmentation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Instance Segmentation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Instance Segmentation"
1. "Provide advanced patterns and performance considerations for Instance Segmentation"

## Key Takeaways

- Master the core ideas of Instance Segmentation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
