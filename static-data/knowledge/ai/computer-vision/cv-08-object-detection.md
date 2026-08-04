---
slug: cv-08-object-detection
title: "Object Detection"
description: "Locating and classifying objects with bounding boxes — YOLO, Faster R-CNN, anchor-free methods, and mAP evaluation."
order: 8
tags:
  - computer-vision
  - object-detection
  - yolo
  - faster-rcnn
  - map
  - nms
prerequisites:
  - cv-06-cnns-for-vision
  - cv-05-image-classification
  - dl-13-cnn-architectures
references:
  - title: "Faster R-CNN: Towards Real-Time Object Detection"
    url: "https://arxiv.org/abs/1506.01497"
    description: "Ren et al.'s Faster R-CNN paper with Region Proposal Networks"
  - title: "You Only Look Once (YOLO)"
    url: "https://arxiv.org/abs/1506.02640"
    description: "Redmon et al.'s original YOLO paper"
  - title: "YOLOv8 Documentation (Ultralytics)"
    url: "https://docs.ultralytics.com/"
    description: "Ultralytics' YOLOv8 documentation and tutorials"
  - title: "CS231n: Object Detection"
    url: "https://cs231n.stanford.edu/slides/2023/lecture_11.pdf"
    description: "Stanford's object detection lecture"
  - title: "Detectron2 (Meta AI)"
    url: "https://detectron2.readthedocs.io/"
    description: "Meta's detection framework with Mask R-CNN"
knowledge_refs:
  - cv-06-cnns-for-vision
  - cv-09-semantic-segmentation
  - cv-10-instance-segmentation
---

# Object Detection

Object detection locates and classifies multiple objects in an image, outputting bounding boxes with class labels and confidence scores.

## Two-Stage vs. One-Stage Detection

| Approach | Example | Speed | Accuracy |
|---|---|---|---|
| **Two-stage** | Faster R-CNN | Slower | Higher |
| **One-stage** | YOLO, SSD | Faster | Slightly lower |
| **Anchor-free** | FCOS, CenterNet | Fast | Competitive |

## The Detection Output

```
Input: Image
Output: [
  {"bbox": [x1, y1, x2, y2], "class": "car", "score": 0.95},
  {"bbox": [x1, y1, x2, y2], "class": "person", "score": 0.88},
  ...
]
```

## Faster R-CNN (Two-Stage)

```
Image → Backbone (ResNet) → Feature Map
    ↓
Region Proposal Network (RPN) → Region proposals
    ↓
RoI Pooling → Fixed-size features
    ↓
Classifier + Bounding Box Regressor
```

**Key components:**
1. **Backbone**: Extracts features (ResNet + FPN)
2. **RPN**: Proposes regions that might contain objects
3. **RoI Pooling**: Extracts fixed-size features per proposal
4. **Head**: Classifies and refines bounding boxes

## YOLO (One-Stage)

YOLO treats detection as a single regression problem:
1. Divide image into grid cells
2. Each cell predicts bounding boxes + classes directly
3. No region proposals — one forward pass

```python
from ultralytics import YOLO

# Load pretrained YOLOv8
model = YOLO('yolov8n.pt')

# Detect
results = model('image.jpg')
for box in results[0].boxes:
    print(f"Class: {box.cls}, Confidence: {box.conf:.2f}, Box: {box.xyxy}")
```

**YOLO versions**: v1→v8 (Ultralytics), YOLOv5, YOLOv7, YOLOv8, YOLO-NAS

## Anchor-Free Detection

Instead of predefined anchors, predict center points and sizes:
- **FCOS**: Fully Convolutional One-Stage detection
- **CenterNet**: Detect objects as center points
- **ATSS**: Adaptive Training Sample Selection

## Non-Maximum Suppression (NMS)

Remove duplicate detections:
```python
def nms(boxes, scores, iou_threshold=0.5):
    # Sort by confidence
    sorted_idx = scores.argsort(descending=True)
    keep = []
    
    while len(sorted_idx) > 0:
        idx = sorted_idx[0]
        keep.append(idx)
        
        # Compute IoU with remaining boxes
        ious = compute_iou(boxes[idx], boxes[sorted_idx[1:]])
        
        # Keep only boxes with low IoU
        sorted_idx = sorted_idx[1:][ious < iou_threshold]
    
    return keep
```

## Evaluation: mAP (mean Average Precision)

### IoU (Intersection over Union)
$$\text{IoU} = \frac{\text{Area of Intersection}}{\text{Area of Union}}$$

A detection is correct if IoU ≥ threshold (typically 0.5).

### Precision-Recall Curve
- **Precision**: Of detected objects, how many are correct?
- **Recall**: Of all objects, how many were detected?

### Average Precision (AP)
Area under the precision-recall curve for a single class.

### mAP
Mean AP across all classes:
- **mAP@0.5**: AP with IoU threshold 0.5
- **mAP@0.5:0.95**: Average AP across IoU thresholds 0.5 to 0.95 (COCO standard)

```python
from pycocotools.cocoeval import COCOeval

coco_eval = COCOeval(coco_gt, coco_dt, 'bbox')
coco_eval.evaluate()
coco_eval.accumulate()
coco_eval.summarize()
# Prints: AP, AP50, AP75, APs, APm, APl
```

## Feature Pyramid Network (FPN)

Detect objects at multiple scales:
```
Backbone: C2, C3, C4, C5 (different resolutions)
    ↓ FPN
P2, P3, P4, P5 (multi-scale features)
    ↓
Detection head at each scale
```

**Why FPN matters**: Small objects need high-resolution features; large objects need semantic features.

## Practical Tips

1. **Start with YOLOv8**: Best speed-accuracy tradeoff
2. **Use pretrained weights**: Always start from COCO pretrained
3. **Data augmentation**: Mosaic, mixup work well for detection
4. **NMS threshold**: 0.5 is standard; adjust for dense scenes
5. **Confidence threshold**: 0.25-0.5 depending on recall needs

## Further Reading

- Faster R-CNN paper is foundational for modern detection
- YOLO series is the practical choice for real-time detection
- Ultralytics' documentation is the best starting point for YOLOv8
- Detectron2 provides production-quality implementations
