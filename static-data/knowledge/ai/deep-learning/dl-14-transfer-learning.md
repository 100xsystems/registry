---
slug: dl-14-transfer-learning
title: "Transfer Learning & Fine-Tuning"
description: "Don't train from scratch — leverage pretrained models to achieve state-of-the-art with minimal data."
order: 14
tags:
  - deep-learning
  - transfer-learning
  - fine-tuning
  - pretrained-models
  - domain-adaptation
prerequisites:
  - dl-13-cnn-architectures
  - dl-10-the-training-loop
references:
  - title: "How Transferable Are Features in Deep Neural Networks?"
    url: "https://arxiv.org/abs/1411.1792"
    description: "Yosinski et al.'s study of feature transferability across layers"
  - title: "Very Deep Convolutional Networks (VGG) Transfer Learning"
    url: "https://cs231n.github.io/transfer-learning/"
    description: "CS231n's practical guide to transfer learning strategies"
  - title: "ImageNet Pretrained Models (torchvision)"
    url: "https://pytorch.org/vision/stable/models.html"
    description: "PyTorch's official pretrained model zoo"
  - title: "A Comprehensive Study of Transfer Learning"
    url: "https://arxiv.org/abs/1911.02150"
    description: "Survey covering when and how to transfer"
  - title: "Don't Decay the Learning Rate, Increase the Batch Size"
    url: "https://arxiv.org/abs/1711.00489"
    description: "Smith et al. on scaling rules for transfer learning"
knowledge_refs:
  - dl-13-cnn-architectures
  - dl-10-the-training-loop
  - dl-11-regularization-for-deep-learning
---

# Transfer Learning & Fine-Tuning

Training a deep network from scratch requires millions of labeled images. Transfer learning lets you start with a model trained on a large dataset (like ImageNet) and adapt it to your specific task — often with just hundreds of examples.

## The Core Idea

Deep networks learn **hierarchical features**:
- **Early layers**: Generic features (edges, textures) — transferable across tasks
- **Later layers**: Task-specific features (dog faces, car wheels) — less transferable

Transfer learning exploits this: reuse the generic features, retrain the task-specific ones.

## When to Use Transfer Learning

| Source → Target | Data Size | Strategy |
|---|---|---|
| Same domain, more data | Large | Fine-tune all layers |
| Same domain, less data | Small | Freeze feature extractor, train classifier |
| Different domain, large data | Large | Fine-tune all layers (lower LR) |
| Different domain, small data | Small | Feature extraction only |

**Rule of thumb**: If you have < 1000 samples per class, use feature extraction. If > 1000, fine-tune.

## Strategy 1: Feature Extraction

Use the pretrained model as a fixed feature extractor:

```python
import torch
import torch.nn as nn
from torchvision import models

# Load pretrained ResNet50
model = models.resnet50(pretrained=True)

# Freeze all layers
for param in model.parameters():
    param.requires_grad = False

# Replace the final layer
num_classes = 10
model.fc = nn.Linear(model.fc.in_features, num_classes)

# Only the new layer is trained
optimizer = torch.optim.Adam(model.fc.parameters(), lr=1e-3)
```

**When to use**: Small dataset (< 1000 samples), same domain as pretrained model.

## Strategy 2: Fine-Tuning

Unfreeze some or all layers and train with a small learning rate:

```python
model = models.resnet50(pretrained=True)

# Option A: Fine-tune all layers with small LR
optimizer = torch.optim.Adam([
    {'params': model.layer4.parameters(), 'lr': 1e-5},  # last block: small LR
    {'params': model.fc.parameters(), 'lr': 1e-3}       # classifier: normal LR
], lr=1e-4)

# Option B: Gradual unfreezing
# Epoch 1-5: Train only classifier
# Epoch 6-10: Unfreeze last block
# Epoch 11-15: Unfreeze last two blocks
# ...
```

**Discriminative learning rates**: Earlier layers get smaller learning rates (they contain generic features that shouldn't change much). Later layers get larger rates.

## Strategy 3: Progressive Resizing

Train on small images first, then resize to larger:
```python
# Stage 1: 128×128 images, fast training
# Stage 2: 224×224 images, slower but more accurate
# Stage 3: 384×384 images, final fine-tuning
```

This works because:
- Small images train fast (explore architecture space)
- Large images capture fine details (refine accuracy)
- Act as data augmentation (the model sees each image at different scales)

## PyTorch Transfer Learning Patterns

### Using torchvision Models

```python
from torchvision import models

# ResNet
model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V2)

# EfficientNet
model = models.efficientnet_b0(weights=models.EfficientNet_B0_Weights.IMAGENET1K_V1)

# Vision Transformer
model = models.vit_b_16(weights=models.ViT_B_16_Weights.IMAGENET1K_V1)
```

### Replacing the Head

```python
# For ResNet-like architectures
model.fc = nn.Sequential(
    nn.Dropout(0.3),
    nn.Linear(model.fc.in_features, 256),
    nn.ReLU(),
    nn.Dropout(0.2),
    nn.Linear(256, num_classes)
)

# For EfficientNet
model.classifier = nn.Sequential(
    nn.Dropout(0.2),
    nn.Linear(model.classifier[1].in_features, num_classes)
)
```

### Custom Feature Extraction

```python
class FeatureExtractor(nn.Module):
    def __init__(self, backbone, output_dim):
        super().__init__()
        self.backbone = backbone
        self.backbone.fc = nn.Identity()  # Remove classifier
        self.projection = nn.Linear(backbone.fc.in_features, output_dim)
    
    def forward(self, x):
        features = self.backbone(x)
        return self.projection(features)
```

## Transfer Learning from NLP

Pretrained language models (BERT, GPT, LLaMA) can be fine-tuned for any NLP task:

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained(
    'bert-base-uncased', num_labels=2
)
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

# Fine-tune on your task
optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5)
```

**NLP transfer learning**: BERT, GPT, and similar models are trained on massive text corpora. Fine-tuning adapts them to specific tasks (sentiment analysis, NER, QA) with minimal labeled data.

## Common Pitfalls

1. **Forgetting to freeze layers**: Training all layers on small data → overfitting
2. **Learning rate too high**: Destroys pretrained features
3. **Not adjusting batch norm**: Use `model.eval()` or freeze BN during fine-tuning
4. **Wrong preprocessing**: Must match the pretrained model's expected input format
5. **Domain mismatch**: ImageNet features may not transfer to medical images or satellite imagery

```python
# Fix: freeze batch norm during fine-tuning
class frozen_bn_model(nn.Module):
    def __init__(self, model):
        super().__init__()
        self.model = model
        # Freeze all BN layers
        for m in self.model.modules():
            if isinstance(m, nn.BatchNorm2d):
                m.eval()  # Uses running stats, not batch stats
    
    def train(self, mode=True):
        super().train(mode)
        # Keep BN in eval mode
        for m in self.model.modules():
            if isinstance(m, nn.BatchNorm2d):
                m.eval()
        return self
```

## When Transfer Learning Doesn't Work

- **Very different domains**: Medical images vs. natural images (though features still help)
- **Very small pretrained models**: Not enough capacity to learn useful features
- **Task requires different input resolution**: May lose spatial information
- **Very different label spaces**: Pretrained features may not capture relevant distinctions

**Alternatives**: Self-supervised pretraining (SimCLR, DINO), domain adaptation, few-shot learning.

## Practical Guidelines

1. **Always start with transfer learning** — training from scratch is a last resort
2. **Start with feature extraction** — add fine-tuning only if needed
3. **Use discriminative learning rates** — smaller for earlier layers
4. **Match preprocessing** — same normalization, input size as pretrained model
5. **Monitor overfitting** — especially when fine-tuning on small data
6. **Try multiple backbones** — ResNet, EfficientNet, ViT may perform differently

## Further Reading

- Yosinski et al. (2014) showed that early layers transfer universally
- CS231n's transfer learning guide is the practical starting point
- Hugging Face's model hub has thousands of pretrained models
- For domain adaptation: look into adversarial training methods
