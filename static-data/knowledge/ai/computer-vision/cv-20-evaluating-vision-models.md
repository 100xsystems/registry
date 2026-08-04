---
slug: cv-20-evaluating-vision-models
title: "Evaluating Vision Models"
description: "Metrics, benchmarks, and best practices for assessing computer vision model quality."
order: 20
tags:
  - computer-vision
  - evaluation
  - metrics
  - benchmarks
  - map
  - miou
prerequisites:
  - cv-08-object-detection
  - cv-09-semantic-segmentation
  - cv-05-image-classification
references:
  - title: "COCO Detection Challenge"
    url: "https://cocodataset.org/#detection-eval"
    description: "Official COCO evaluation metrics documentation"
  - title: "PASCAL VOC Challenge"
    url: "http://host.robots.ox.ac.uk/pascal/VOC/"
    description: "PASCAL VOC benchmark for detection and segmentation"
  - title: "ImageNet Large Scale Visual Recognition Challenge"
    url: "https://www.image-net.org/challenges/LSVRC/"
    description: "The benchmark that drove CV progress"
  - title: "Papers With Code: Computer Vision"
    url: "https://paperswithcode.com/area/computer-vision"
    description: "State-of-the-art results for CV tasks"
  - title: "torchmetrics Documentation"
    url: "https://torchmetrics.readthedocs.io/"
    description: "PyTorch metrics library for evaluation"
knowledge_refs:
  - cv-05-image-classification
  - cv-08-object-detection
  - cv-09-semantic-segmentation
---

# Evaluating Vision Models

Choosing the right evaluation metric is essential — accuracy alone is insufficient for most vision tasks. Different tasks require different metrics.

## Classification Metrics

| Metric | Description | When to Use |
|---|---|---|
| **Top-1 Accuracy** | Correct class is the prediction | Most tasks |
| **Top-5 Accuracy** | Correct class in top 5 | ImageNet |
| **F1 Score** | Harmonic mean of precision/recall | Imbalanced classes |
| **AUC-ROC** | Area under ROC curve | Binary classification |

```python
from torchmetrics import Accuracy, F1Score

acc = Accuracy(task="multiclass", num_classes=10)
f1 = F1Score(task="multiclass", num_classes=10, average="macro")

accuracy = acc(predictions, labels)
f1_score = f1(predictions, labels)
```

## Detection Metrics (mAP)

### IoU (Intersection over Union)
$$\text{IoU} = \frac{\text{Area of Intersection}}{\text{Area of Union}}$$

A detection is correct if IoU ≥ threshold (typically 0.5).

### Average Precision (AP)
Area under the precision-recall curve for one class.

### mAP (mean Average Precision)
Average AP across all classes:
- **mAP@0.5**: AP at IoU=0.5 (PASCAL VOC style)
- **mAP@0.5:0.95**: Average AP across IoU 0.5 to 0.95 (COCO style)

```python
from torchmetrics.detection.mean_ap import MeanAveragePrecision

metric = MeanAveragePrecision()
metric.update(preds, targets)
result = metric.compute()
# result['map'] — mAP@0.5:0.95
# result['map_50'] — mAP@0.5
# result['map_75'] — mAP@0.75
```

## Segmentation Metrics

### mIoU (mean Intersection over Union)
Per-class IoU averaged across classes:
$$\text{mIoU} = \frac{1}{K}\sum_{k=1}^{K}\text{IoU}_k$$

```python
from torchmetrics import JaccardIndex

jaccard = JaccardIndex(task="multiclass", num_classes=21, average="macro")
miou = jaccard(preds, labels)
```

### Pixel Accuracy
Percentage of correctly classified pixels (can be misleading with class imbalance).

### Dice Score
$$\text{Dice} = \frac{2 \times \text{TP}}{\text{TP} + \text{FP} + \text{TP} + \text{FN}}$$

## Common Benchmarks

| Benchmark | Task | Metric | SOTA |
|---|---|---|---|
| **ImageNet** | Classification | Top-1 | ~91% |
| **COCO** | Detection | mAP@0.5:0.95 | ~60% |
| **ADE20K** | Semantic Seg | mIoU | ~60% |
| **Cityscapes** | Driving Seg | mIoU | ~85% |
| **LFW** | Face Recognition | Accuracy | ~99.8% |

## Evaluation Best Practices

1. **Use standard metrics**: mAP for detection, mIoU for segmentation
2. **Report confidence intervals**: Run multiple times, report mean ± std
3. **Evaluate on test set**: Never evaluate on training data
4. **Check per-class performance**: Some classes may perform poorly
5. **Consider computational cost**: Latency and memory matter for deployment

## Common Mistakes

1. **Using accuracy for imbalanced data**: Use F1 or AUC instead
2. **Ignoring false positives**: mAP accounts for this
3. **Wrong IoU threshold**: 0.5 is easy, 0.75 is strict
4. **Not using official evaluation tools**: COCOeval, VOCeval
5. **Evaluating on augmented test data**: Test on clean data only

## Further Reading

- COCO evaluation is the standard for detection/segmentation
- ImageNet drove the deep learning revolution in CV
- Papers With Code tracks state-of-the-art results
- torchmetrics provides PyTorch-native evaluation metrics
