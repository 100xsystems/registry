---
slug: cv-07-transfer-learning-for-vision
title: "Transfer Learning for Vision"
description: "Don't train from scratch — leverage pretrained models to achieve state-of-the-art with minimal data."
order: 7
tags:
  - computer-vision
  - transfer-learning
  - fine-tuning
  - pretrained-models
  - feature-extraction
prerequisites:
  - cv-06-cnns-for-vision
  - cv-05-image-classification
  - dl-14-transfer-learning
references:
  - title: "PyTorch Transfer Learning Tutorial"
    url: "https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html"
    description: "Official PyTorch transfer learning guide"
  - title: "Dive into Deep Learning: Fine-Tuning"
    url: "https://d2l.ai/chapter_computer-vision/fine-tuning.html"
    description: "D2L's comprehensive fine-tuning chapter"
  - title: "CS231n: Transfer Learning"
    url: "https://cs231n.github.io/transfer-learning/"
    description: "Stanford's practical transfer learning guide"
  - title: "PyTorch Vision Models"
    url: "https://pytorch.org/vision/stable/models.html"
    description: "Official pretrained model zoo"
  - title: "timm: PyTorch Image Models"
    url: "https://github.com/huggingface/pytorch-image-models"
    description: "Comprehensive model library with 1000+ architectures"
knowledge_refs:
  - cv-06-cnns-for-vision
  - dl-14-transfer-learning
  - cv-05-image-classification
---

# Transfer Learning for Vision

Training a deep CNN from scratch requires millions of labeled images. Transfer learning lets you start with a model pretrained on ImageNet and adapt it to your task — often with just hundreds of examples.

## Why Transfer Learning Works

Deep networks learn hierarchical features:
- **Early layers**: Generic features (edges, textures) — transferable across tasks
- **Later layers**: Task-specific features (dog faces, car wheels) — less transferable

Transfer learning reuses the generic features and relearns the task-specific ones.

## Strategy 1: Feature Extraction

Freeze the backbone, train only the classifier head:

```python
import torch
from torchvision import models

model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V2)

# Freeze all layers
for param in model.parameters():
    param.requires_grad = False

# Replace classifier
model.fc = nn.Linear(model.fc.in_features, num_classes)

# Only new layer is trained
optimizer = torch.optim.Adam(model.fc.parameters(), lr=1e-3)
```

**When to use**: Small dataset (< 1000 samples), same domain as ImageNet.

## Strategy 2: Fine-Tuning

Unfreeze some layers and train with small learning rates:

```python
model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V2)

# Discriminative learning rates
optimizer = torch.optim.AdamW([
    {'params': model.layer1.parameters(), 'lr': 1e-6},  # earliest: smallest LR
    {'params': model.layer2.parameters(), 'lr': 1e-6},
    {'params': model.layer3.parameters(), 'lr': 1e-5},
    {'params': model.layer4.parameters(), 'lr': 1e-5},
    {'params': model.fc.parameters(), 'lr': 1e-3},       # head: largest LR
], lr=1e-4)
```

**Discriminative learning rates**: Earlier layers need smaller updates (they contain generic features).

## Strategy 3: Gradual Unfreezing

Progressively unfreeze layers during training:
```python
# Phase 1: Train only head
for param in model.parameters():
    param.requires_grad = False
model.fc.requires_grad_(True)
train(epochs=5)

# Phase 2: Unfreeze last block
model.layer4.requires_grad_(True)
train(epochs=5, lr=1e-4)

# Phase 3: Unfreeze more layers
model.layer3.requires_grad_(True)
train(epochs=5, lr=1e-5)
```

## Strategy 4: Progressive Resizing

Train on small images first, then resize to larger:
```python
# Stage 1: 128×128 (fast, explore)
# Stage 2: 224×224 (standard, refine)
# Stage 3: 384×384 (high-res, final)
```

## When to Use What

| Data Size | Domain Match | Strategy |
|---|---|---|
| Small (< 1K) | Same as ImageNet | Feature extraction |
| Small (< 1K) | Different domain | Feature extraction + data augmentation |
| Medium (1K-10K) | Same | Fine-tune last 2 blocks |
| Medium (1K-10K) | Different | Fine-tune more blocks |
| Large (> 10K) | Same | Fine-tune all layers |
| Large (> 10K) | Different | Fine-tune all layers |

## Common Pitfalls

1. **Forgetting to freeze**: Training all layers on small data → overfitting
2. **Learning rate too high**: Destroys pretrained features
3. **Wrong preprocessing**: Must match ImageNet normalization
4. **Not adjusting batch norm**: Freeze BN during fine-tuning
5. **Wrong input size**: Models expect specific resolutions

```python
# Fix: freeze batch norm during fine-tuning
for m in model.modules():
    if isinstance(m, nn.BatchNorm2d):
        m.eval()  # Use running stats, not batch stats
```

## Pretrained Model Zoo

| Model | Parameters | Top-1 Acc | Speed | Use Case |
|---|---|---|---|---|
| ResNet-50 | 25M | 76% | Fast | General purpose |
| EfficientNet-B3 | 12M | 82% | Medium | Best accuracy/size |
| MobileNetV3 | 5.5M | 75% | Very fast | Mobile/edge |
| ViT-B/16 | 86M | 84% | Slow | When data is abundant |
| ConvNeXt-T | 29M | 84% | Medium | Modern CNN |

## Further Reading

- PyTorch's transfer learning tutorial is the practical starting point
- D2L covers fine-tuning theory comprehensively
- CS231n provides the conceptual foundation
- timm offers 1000+ pretrained models for any use case
