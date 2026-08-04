---
slug: cv-10-instance-segmentation
title: "Instance Segmentation"
description: "Detecting individual object instances and their pixel masks — Mask R-CNN, SOLO, and panoptic segmentation."
order: 10
tags:
  - computer-vision
  - instance-segmentation
  - mask-rcnn
  - panoptic
  - coco-metrics
prerequisites:
  - cv-08-object-detection
  - cv-09-semantic-segmentation
  - cv-06-cnns-for-vision
references:
  - title: "Mask R-CNN (He et al., ICCV 2017)"
    url: "https://arxiv.org/abs/1703.06870"
    description: "He et al.'s Mask R-CNN paper — the foundation of instance segmentation"
  - title: "SOLO: Segmenting Objects by Locations"
    url: "https://arxiv.org/abs/1912.04488"
    description: "Wang et al.'s SOLO — direct single-stage instance segmentation"
  - title: "Panoptic Segmentation (Kirillov et al.)"
    url: "https://arxiv.org/abs/1801.00868"
    description: "Kirillov et al.'s panoptic segmentation unifying semantic + instance"
  - title: "Detectron2 Documentation"
    url: "https://detectron2.readthedocs.io/"
    description: "Meta's detection framework with Mask R-CNN implementation"
  - title: "COCO Evaluation Metrics"
    url: "https://cocodataset.org/#detection-eval"
    description: "Official COCO detection and segmentation evaluation"
knowledge_refs:
  - cv-08-object-detection
  - cv-09-semantic-segmentation
  - cv-06-cnns-for-vision
---

# Instance Segmentation

Instance segmentation combines object detection and semantic segmentation — it detects individual object instances AND predicts their pixel-level masks.

## Semantic vs. Instance vs. Panoptic

| Task | What It Does | Example |
|---|---|---|
| **Semantic** | Classify every pixel | All "car" pixels labeled the same |
| **Instance** | Detect + segment each object | Each car gets a separate mask |
| **Panoptic** | Both semantic + instance | Things (instances) + Stuff (regions) |

## Mask R-CNN

Extends Faster R-CNN with a mask prediction branch:

```
Image → Backbone (ResNet+FPN) → Feature Maps
    ↓
Region Proposal Network (RPN) → Proposals
    ↓
RoIAlign → Fixed-size features (no quantization!)
    ↓
┌─────────────────────────────┐
│  Classification Head        │ → Class label
│  Bounding Box Head          │ → Box coordinates
│  Mask Head (FCN)            │ → Binary mask per class
└─────────────────────────────┘
```

### RoIAlign (Key Innovation)
Replaces RoIPool with bilinear interpolation — eliminates quantization error for pixel-accurate masks.

```python
import torchvision

model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)
model.eval()

predictions = model(images)
# predictions[i]['masks'] — (N, 1, H, W) binary masks
# predictions[i]['boxes'] — (N, 4) bounding boxes
# predictions[i]['labels'] — (N,) class labels
# predictions[i]['scores'] — (N,) confidence scores
```

## SOLO (Segmenting Objects by Locations)

Single-stage instance segmentation — no region proposals:

```
Image → Backbone → Feature Pyramid
    ↓
┌──────────────────────┐
│  Category Branch      │ → Class prediction per grid cell
│  Mask Branch          │ → Instance mask per grid cell
└──────────────────────┘
```

**Key idea**: Divide image into S×S grid. Each cell responsible for objects whose center falls within it.

## Panoptic Segmentation

Unifies semantic (stuff) and instance (things) segmentation:

**Things**: Countable objects (cars, persons, dogs)
**Stuff**: Uncountable regions (sky, road, grass)

```
Panoptic Quality (PQ) = Segmentation Quality (SQ) × Recognition Quality (RQ)
```

```python
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg

cfg = get_cfg()
cfg.merge_from_file("COCO-PanopticSegmentation/panoptic_fpn_R_101_3x.yaml")
cfg.MODEL.WEIGHTS = "model_final_c10459.pkl"
predictor = DefaultPredictor(cfg)

outputs = predictor(image)
# outputs["panoptic_seg"] — (H, W) tensor with segment IDs
# outputs["segments_info"] — list of segment metadata
```

## COCO Evaluation Metrics

### For Detection/Instance Segmentation
| Metric | Description |
|---|---|
| **AP** | mAP@0.5:0.95 (main metric) |
| **AP50** | mAP at IoU=0.5 |
| **AP75** | mAP at IoU=0.75 (strict) |
| **APs/APm/APl** | AP for small/medium/large objects |

### For Panoptic Segmentation
| Metric | Description |
|---|---|
| **PQ** | Panoptic Quality (main metric) |
| **SQ** | Segmentation Quality (IoU of matched segments) |
| **RQ** | Recognition Quality (F1 of matching) |

## Training Tips

1. **Use FPN**: Multi-scale features are essential
2. **RoIAlign > RoIPool**: Always use RoIAlign for masks
3. **Loss balance**: Classification + Box + Mask losses need weighting
4. **Data augmentation**: Horizontal flips, scale jitter
5. **COCO-style augmentation**: Copy-paste augmentation helps significantly

## Practical Usage

```python
# Using torchvision for inference
import torchvision
from torchvision.models.detection import maskrcnn_resnet50_fpn

model = maskrcnn_resnet50_fpn(pretrained=True)
model.eval()

with torch.no_grad():
    predictions = model([image_tensor])

# Process results
for pred in predictions:
    masks = pred['masks'] > 0.5  # Binarize
    boxes = pred['boxes']
    labels = pred['labels']
    scores = pred['scores']
    
    # Filter by confidence
    keep = scores > 0.5
    masks, boxes, labels, scores = masks[keep], boxes[keep], labels[keep], scores[keep]
```

## Further Reading

- Mask R-CNN is the foundational architecture for instance segmentation
- SOLO showed single-stage instance segmentation is viable
- Panoptic segmentation provides the complete scene understanding
- Detectron2 is the production framework for all these tasks
