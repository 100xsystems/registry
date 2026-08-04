---
slug: dl-12-convolutional-networks
title: "Convolutional Neural Networks"
description: "The architecture that revolutionized computer vision — how CNNs learn spatial hierarchies from pixels to objects."
order: 12
tags:
  - deep-learning
  - cnn
  - computer-vision
  - convolution
prerequisites:
  - dl-11-regularization-for-deep-learning
  - dl-09-building-an-mlp-in-pytorch
references:
  - title: "Deep Learning Book: Chapter 9 — Convolutional Networks"
    url: "https://www.deeplearningbook.org/contents/convnets.html"
    description: "Goodfellow et al.'s comprehensive treatment of CNNs"
  - title: "CS231n: Convolutional Neural Networks"
    url: "https://cs231n.github.io/convolutional-networks/"
    description: "Stanford's definitive CNN lecture notes"
  - title: "A Guide to Convolution Arithmetic for Deep Learning"
    url: "https://arxiv.org/abs/1603.07285"
    description: "Dumoulin & Visin's visual guide to convolution arithmetic"
  - title: "PyTorch: Convolution Layers"
    url: "https://pytorch.org/docs/stable/nn.html#convolution-layers"
    description: "Official documentation for all convolution variants"
  - title: "An Intuitive Explanation of Convolutional Neural Networks"
    url: "https://www.datacamp.com/tutorial/introduction-to-cnns"
    description: "Accessible introduction to CNN concepts and visualizations"
knowledge_refs:
  - dl-11-regularization-for-deep-learning
  - dl-13-cnn-architectures
  - dl-14-transfer-learning
---

# Convolutional Neural Networks

CNNs are the backbone of computer vision. They exploit the spatial structure of images through parameter sharing and local connectivity, achieving dramatically better performance than fully-connected networks on visual tasks.

## Why Not Fully Connected for Images?

A 224×224×3 image has 150,528 pixels. A single fully-connected layer to 1000 outputs = 150 million parameters. This is:
- **Too many parameters**: Overfits immediately
- **No spatial awareness**: Treats pixels as an unordered vector
- **Computationally expensive**: Massive matrix multiplication

CNNs solve this with three key ideas: **local receptive fields**, **parameter sharing**, and **translation invariance**.

## The Convolution Operation

A convolution slides a small **filter** (kernel) over the input, computing dot products at each position:

```
Input:     5×5
Filter:    3×3
Output:    3×3 (valid convolution)
```

**Mathematically**:
$$(\mathbf{I} * \mathbf{K})(i,j) = \sum_m \sum_n \mathbf{I}(i+m, j+n) \cdot \mathbf{K}(m,n)$$

**PyTorch implementation**:
```python
import torch.nn as nn

# in_channels=3 (RGB), out_channels=32 (number of filters), kernel_size=3
conv = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, stride=1, padding=1)
x = torch.randn(1, 3, 224, 224)  # batch of 1, 3 channels, 224x224
output = conv(x)                   # shape: (1, 32, 224, 224)
```

## Key Parameters

### Stride
How far the filter moves at each step:
- stride=1: Output size ≈ Input size (with padding)
- stride=2: Output size ≈ Half the input size

### Padding
Add zeros around the input border:
- padding=0 (valid): Output is smaller
- padding=1 (same): Output same size as input (for stride=1)

### Output Size Formula
$$\text{Output} = \frac{\text{Input} - \text{Kernel} + 2 \times \text{Padding}}{\text{Stride}} + 1$$

```python
# For 224x224 input, 3x3 kernel, stride=1, padding=1
# (224 - 3 + 2*1) / 1 + 1 = 224 → same size

# For stride=2
# (224 - 3 + 2*1) / 2 + 1 = 112 → half size
```

## Pooling Layers

Reduce spatial dimensions and provide translation invariance:

```python
# Max pooling: takes maximum in each window
pool = nn.MaxPool2d(kernel_size=2, stride=2)
output = pool(x)  # Reduces spatial dimensions by 2x

# Average pooling: takes mean in each window
pool = nn.AvgPool2d(kernel_size=2, stride=2)

# Global average pooling: reduces each feature map to a single value
pool = nn.AdaptiveAvgPool2d(1)
output = pool(x)  # (B, C, H, W) → (B, C, 1, 1)
```

**Max pooling** is more common — it preserves the strongest activations.

## Building a CNN

```python
class SimpleCNN(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        
        # Feature extractor
        self.features = nn.Sequential(
            # Block 1: 3 → 32 channels
            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2),           # 224 → 112
            
            # Block 2: 32 → 64 channels
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2),           # 112 → 56
            
            # Block 3: 64 → 128 channels
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d(1),   # → (B, 128, 1, 1)
        )
        
        # Classifier
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(64, num_classes)
        )
    
    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x

model = SimpleCNN()
x = torch.randn(2, 3, 224, 224)
print(model(x).shape)  # (2, 10)
```

## The Hierarchy of Features

CNNs learn a hierarchy of visual features:

| Layer | What It Detects | Receptive Field |
|---|---|---|
| Layer 1 | Edges, colors, textures | Small (3×3) |
| Layer 2 | Corners, simple patterns | Medium (5×5) |
| Layer 3 | Parts (eyes, wheels) | Larger (7×7) |
| Layer 4 | Objects (faces, cars) | Full image |
| Layer 5 | Scenes, categories | Global |

**Receptive field**: The region of the input that influences a particular neuron. Deeper neurons see more of the image.

## Parameters Sharing

The same filter is applied across the entire image:
- A 3×3 filter has 9 weights (plus bias)
- Applied to a 224×224 image → uses the same 9 weights everywhere
- Enormous parameter reduction vs. fully connected

**A 3×3 conv with 64 filters** = 64 × (3×3×3 + 1) = 1,792 parameters
**A linear layer from 224²×3 to 224²×3** = (224²×3)² = 95 billion parameters

## 1×1 Convolutions

Used to change the number of channels without changing spatial dimensions:
```python
# Reduce channels: 256 → 64
conv1x1 = nn.Conv2d(256, 64, kernel_size=1)
output = conv1x1(x)  # (B, 256, H, W) → (B, 64, H, W)
```

Used in Inception, ResNet bottleneck blocks, and as a channel-wise linear transformation.

## Depthwise Separable Convolutions

Factorize standard convolution into depthwise + pointwise:
```python
# Standard: O(K² × Cin × Cout × H × W)
# Depthwise separable: O(K² × Cin × H × W + Cin × Cout × H × W)
# ~K² times cheaper!

depthwise = nn.Conv2d(64, 64, kernel_size=3, padding=1, groups=64)  # depthwise
pointwise = nn.Conv2d(64, 128, kernel_size=1)  # pointwise
```

**Used in**: MobileNet, EfficientNet — efficient architectures for mobile/edge devices.

## Visualizing What CNNs Learn

```python
# Hook to extract intermediate activations
activations = {}
def hook_fn(module, input, output):
    activations[module] = output

# Register hooks
for name, layer in model.features.named_modules():
    if isinstance(layer, nn.Conv2d):
        layer.register_forward_hook(hook_fn)

# Run inference
with torch.no_grad():
    output = model(image)

# Visualize activations
for layer, act in activations.items():
    plt.figure(figsize=(12, 3))
    for i in range(min(8, act.shape[1])):
        plt.subplot(1, 8, i+1)
        plt.imshow(act[0, i].cpu(), cmap='viridis')
        plt.axis('off')
    plt.suptitle(f'Layer {layer}')
```

## Further Reading

- CS231n notes are the definitive CNN reference
- Dumoulin & Visin's arithmetic guide is essential for understanding output sizes
- For modern efficient CNNs: EfficientNet (Tan & Le, 2019) and ConvNeXt
- For the transition to transformers: ViT (Dosovitskiy et al., 2020)
