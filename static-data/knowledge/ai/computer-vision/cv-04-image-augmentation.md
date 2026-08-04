---
slug: cv-04-image-augmentation
title: "Image Augmentation"
description: "Artificially expanding your training data — from basic flips to advanced techniques like Mixup and CutMix."
order: 4
tags:
  - computer-vision
  - augmentation
  - data-augmentation
  - regularization
  - albumentations
prerequisites:
  - cv-02-image-representation
  - cv-05-image-classification
  - dl-11-regularization-for-deep-learning
references:
  - title: "Torchvision v2 Transforms"
    url: "https://docs.pytorch.org/vision/0.21/transforms.html"
    description: "PyTorch's official augmentation documentation"
  - title: "Torchvision CutMix and MixUp Tutorial"
    url: "https://docs.pytorch.org/vision/main/auto_examples/transforms/plot_cutmix_mixup.html"
    description: "Step-by-step guide to batch-level augmentations"
  - title: "Albumentations Documentation"
    url: "https://albumentations.ai/docs/"
    description: "High-performance augmentation library with OpenCV backend"
  - title: "RandAugment: Practical automated data augmentation"
    url: "https://arxiv.org/abs/1909.13719"
    description: "Cubuk et al.'s RandAugment paper"
  - title: "timm Mixup & CutMix"
    url: "https://timm.fast.ai/mixup_cutmix"
    description: "State-of-the-art augmentation configurations"
knowledge_refs:
  - cv-05-image-classification
  - dl-11-regularization-for-deep-learning
  - cv-02-image-representation
---

# Image Augmentation

Data augmentation is the most effective regularization technique for vision models. By creating modified versions of training images, you teach the model to be invariant to irrelevant variations while learning the essential patterns.

## Why Augmentation Matters

A model trained on only clean, centered images will fail on real-world data:
- **Flipped images**: Cars face both directions
- **Cropped images**: Objects appear at different scales
- **Noisy images**: Camera sensors add noise
- **Color-shifted images**: Different lighting conditions

Augmentation artificially expands your dataset and teaches invariance.

## Basic Augmentations

### PyTorch Torchvision
```python
from torchvision import transforms

train_transform = transforms.Compose([
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomVerticalFlip(p=0.1),
    transforms.RandomRotation(15),
    transforms.RandomResizedCrop(224, scale=(0.8, 1.0)),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
    transforms.RandomGrayscale(p=0.1),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
```

### Albumentations (Faster, More Flexible)
```python
import albumentations as A
from albumentations.pytorch import ToTensorV2

train_transform = A.Compose([
    A.RandomResizedCrop(height=224, width=224, scale=(0.8, 1.0)),
    A.HorizontalFlip(p=0.5),
    A.VerticalFlip(p=0.1),
    A.Rotate(limit=15, p=0.5),
    A.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1, p=0.5),
    A.GaussNoise(var_limit=(10.0, 50.0), p=0.3),
    A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ToTensorV2(),
])

# Apply to image and mask (for segmentation)
transformed = train_transform(image=img, mask=mask)
img_tensor = transformed['image']
mask_tensor = transformed['mask']
```

## Augmentation Catalog

| Augmentation | What It Does | When to Use |
|---|---|---|
| **RandomHorizontalFlip** | Mirror left-right | Almost always (p=0.5) |
| **RandomVerticalFlip** | Mirror up-down | Medical, satellite (not natural) |
| **RandomRotation** | Rotate by angle | Orientation varies |
| **RandomResizedCrop** | Crop + resize | Scale invariance |
| **ColorJitter** | Change brightness/contrast/saturation/hue | Lighting variation |
| **RandomGrayscale** | Convert to grayscale | Color isn't essential |
| **GaussianBlur** | Add blur | Different focus levels |
| **GaussNoise** | Add Gaussian noise | Sensor noise robustness |
| **RandomErasing** | Mask random rectangle | Occlusion robustness |

## Advanced Augmentations

### RandAugment
Automated augmentation with just 2 hyperparameters:
```python
transform = transforms.Compose([
    transforms.RandAugment(num_ops=2, magnitude=9),
    transforms.ToTensor(),
])
```

**How it works**: Randomly selects N operations from a pool of 14 transforms, each with uniform magnitude M.

### Mixup
Blend pairs of images and labels:
```python
def mixup_data(x, y, alpha=0.2):
    lam = np.random.beta(alpha, alpha)
    batch_size = x.size(0)
    index = torch.randperm(batch_size)
    
    mixed_x = lam * x + (1 - lam) * x[index]
    y_a, y_b = y, y[index]
    return mixed_x, y_a, y_b, lam

# Use with cross-entropy (soft labels)
mixed_x, y_a, y_b, lam = mixup_data(images, labels)
output = model(mixed_x)
loss = lam * criterion(output, y_a) + (1 - lam) * criterion(output, y_b)
```

### CutMix
Cut a patch from one image, paste on another:
```python
def cutmix_data(x, y, alpha=1.0):
    lam = np.random.beta(alpha, alpha)
    batch_size = x.size(0)
    index = torch.randperm(batch_size)
    
    _, _, H, W = x.shape
    
    # Random bounding box
    cut_ratio = np.sqrt(1. - lam)
    cut_h = int(H * cut_ratio)
    cut_w = int(W * cut_ratio)
    
    cx, cy = np.random.randint(W), np.random.randint(H)
    x1 = np.clip(cx - cut_w // 2, 0, W)
    x2 = np.clip(cx + cut_w // 2, 0, W)
    y1 = np.clip(cy - cut_h // 2, 0, H)
    y2 = np.clip(cy + cut_h // 2, 0, H)
    
    x[:, :, y1:y2, x1:x2] = x[index, :, y1:y2, x1:x2]
    lam = 1 - (x2 - x1) * (y2 - y1) / (W * H)
    
    return x, y, y[index], lam
```

### Mixup vs. CutMix

| Method | How It Works | Benefit |
|---|---|---|
| **Mixup** | Linear blend of pixel values | Smooth decision boundaries |
| **CutMix** | Cut-and-paste rectangular patches | Localized features + regularization |

## Augmentation for Specific Tasks

### Object Detection
Must transform boxes consistently with images:
```python
transform = A.Compose([
    A.RandomResizedCrop(224, 224),
    A.HorizontalFlip(p=0.5),
], bbox_params=A.BboxParams(format='pascal_voc', label_fields=['class_labels']))

transformed = transform(image=img, bboxes=bboxes, class_labels=labels)
```

### Semantic Segmentation
Must transform masks consistently with images:
```python
transform = A.Compose([
    A.RandomResizedCrop(224, 224),
    A.HorizontalFlip(p=0.5),
], mask_fields=['mask'])

transformed = transform(image=img, mask=mask)
```

## Augmentation Strategies

### Light Augmentation
For small datasets or pretraining:
```python
transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
])
```

### Standard Augmentation
For most classification tasks:
```python
transforms.Compose([
    transforms.RandomResizedCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.ColorJitter(0.2, 0.2, 0.2),
    transforms.ToTensor(),
    transforms.Normalize(mean, std),
])
```

### Heavy Augmentation
For large datasets, strong regularization:
```python
transforms.Compose([
    transforms.RandAugment(num_ops=2, magnitude=9),
    transforms.RandomErasing(p=0.5),
    transforms.ToTensor(),
])
```

## Practical Tips

1. **Always augment training, never test**: Test on clean, representative data
2. **Flip is almost always useful**: Objects face both directions
3. **Color augmentation helps**: Lighting varies in real scenes
4. **Mixup/CutMix are powerful**: Nearly free regularization
5. **Don't over-augment**: Too much can hurt more than help
6. **Use GPU acceleration**: Albumentations is faster on GPU

## Further Reading

- Torchvision transforms are the standard for PyTorch
- Albumentations is faster and more flexible
- RandAugment simplified automated augmentation
- Mixup and CutMix provide nearly free regularization
