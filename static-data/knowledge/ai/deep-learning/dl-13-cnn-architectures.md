---
slug: dl-13-cnn-architectures
title: "CNN Architectures: AlexNet to EfficientNet"
description: "The evolution of convolutional architectures — from the deep learning breakthrough to modern efficient designs."
order: 13
tags:
  - deep-learning
  - cnn
  - alexnet
  - resnet
  - efficientnet
prerequisites:
  - dl-12-convolutional-networks
  - dl-11-regularization-for-deep-learning
references:
  - title: "Deep Residual Learning for Image Recognition (ResNet)"
    url: "https://arxiv.org/abs/1512.03385"
    description: "He et al.'s ResNet paper — skip connections that enabled 152-layer networks"
  - title: "EfficientNet: Rethinking Model Scaling"
    url: "https://arxiv.org/abs/1905.11946"
    url: "https://arxiv.org/abs/1905.11946"
    description: "Tan & Le's compound scaling method for efficient models"
  - title: "An Intriguing Idea: Batch Normalization (Inception/VGG)"
    url: "https://arxiv.org/abs/1409.1556"
    description: "Batch normalization paper from the Inception/GoogLeNet team"
  - title: "Visual Geometry Group Networks (VGG)"
    url: "https://arxiv.org/abs/1409.1556"
    description: "Simonyan & Zisserman's VGGNet — showing depth matters"
  - title: "A ConvNet for the 2020s (ConvNeXt)"
    url: "https://arxiv.org/abs/2110.01271"
    description: "Liu et al.'s ConvNeXt — modernizing CNNs with transformer design choices"
knowledge_refs:
  - dl-12-convolutional-networks
  - dl-14-transfer-learning
  - dl-11-regularization-for-deep-learning
---

# CNN Architectures: AlexNet to EfficientNet

The history of computer vision is a story of architectures getting deeper, more efficient, and more powerful. Understanding this evolution teaches you not just what works, but why.

## AlexNet (2012) — The Breakthrough

- **Architecture**: 5 conv layers + 3 FC layers, 60M parameters
- **Innovation**: ReLU, dropout, GPU training, data augmentation
- **Result**: 16% top-5 error on ImageNet (vs 26% for 2nd place)
- **Impact**: Launched the deep learning revolution

```
Input → Conv(96, 11, s4) → Pool → Conv(256, 5, p2) → Pool →
Conv(384, 3, p1) → Conv(384, 3, p1) → Conv(256, 3, p1) → Pool →
FC(4096) → FC(4096) → FC(1000)
```

## VGGNet (2014) — Depth Matters

- **Architecture**: 16-19 layers, all 3×3 convolutions, 138M parameters
- **Innovation**: Showed that deeper networks (with same filter size) perform better
- **Design**: Simple and uniform — every conv is 3×3, stride 1, padding 1
- **Limitation**: Very expensive — 138M parameters

```
[Conv(64) × 2] → Pool → [Conv(128) × 2] → Pool →
[Conv(256) × 3] → Pool → [Conv(512) × 3] → Pool →
[Conv(512) × 3] → Pool → FC(4096) × 2 → FC(1000)
```

## GoogLeNet/Inception (2014) — Efficiency Through Width

- **Architecture**: 22 layers, inception modules, 6.8M parameters
- **Innovation**: Inception module (parallel 1×1, 3×3, 5×5 convs + pooling)
- **Key idea**: 1×1 convolutions reduce dimensionality before expensive operations

```python
class InceptionBlock(nn.Module):
    def __init__(self, in_ch, out_1x1, out_3x3_reduce, out_3x3, out_5x5_reduce, out_5x5, pool_proj):
        super().__init__()
        self.branch1 = nn.Sequential(nn.Conv2d(in_ch, out_1x1, 1), nn.ReLU())
        self.branch2 = nn.Sequential(
            nn.Conv2d(in_ch, out_3x3_reduce, 1), nn.ReLU(),
            nn.Conv2d(out_3x3_reduce, out_3x3, 3, padding=1), nn.ReLU()
        )
        self.branch3 = nn.Sequential(
            nn.Conv2d(in_ch, out_5x5_reduce, 1), nn.ReLU(),
            nn.Conv2d(out_5x5_reduce, out_5x5, 5, padding=2), nn.ReLU()
        )
        self.branch4 = nn.Sequential(
            nn.MaxPool2d(3, stride=1, padding=1),
            nn.Conv2d(in_ch, pool_proj, 1), nn.ReLU()
        )
    
    def forward(self, x):
        return torch.cat([self.branch1(x), self.branch2(x), self.branch3(x), self.branch4(x)], dim=1)
```

## ResNet (2015) — Skip Connections

The most influential CNN architecture ever. **Skip connections** solve the degradation problem:

$$\mathbf{y} = \mathcal{F}(\mathbf{x}, \{W_i\}) + \mathbf{x}$$

Instead of learning $\mathcal{H}(\mathbf{x})$ directly, learn the **residual** $\mathcal{F}(\mathbf{x}) = \mathcal{H}(\mathbf{x}) - \mathbf{x}$.

```python
class ResBlock(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv1 = nn.Conv2d(channels, channels, 3, padding=1)
        self.bn1 = nn.BatchNorm2d(channels)
        self.conv2 = nn.Conv2d(channels, channels, 3, padding=1)
        self.bn2 = nn.BatchNorm2d(channels)
    
    def forward(self, x):
        residual = x
        out = F.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out += residual  # Skip connection!
        return F.relu(out)
```

**Why skip connections work:**
- Gradients flow directly through skip connections (no vanishing)
- Network can learn identity mapping trivially
- Enables training 50-152+ layer networks
- Creates an ensemble of shallower networks

**Key variants:**
- ResNet-18/34: Basic blocks (2 conv layers each)
- ResNet-50/101/152: Bottleneck blocks (3 conv layers: 1×1 → 3×3 → 1×1)

## DenseNet (2017) — Feature Reuse

Every layer receives features from ALL preceding layers:

```python
class DenseBlock(nn.Module):
    def __init__(self, in_ch, growth_rate, num_layers):
        super().__init__()
        layers = []
        for i in range(num_layers):
            layers.append(nn.Sequential(
                nn.BatchNorm2d(in_ch + i * growth_rate),
                nn.ReLU(),
                nn.Conv2d(in_ch + i * growth_rate, growth_rate, 3, padding=1)
            ))
        self.layers = nn.ModuleList(layers)
    
    def forward(self, x):
        features = [x]
        for layer in self.layers:
            out = layer(torch.cat(features, dim=1))
            features.append(out)
        return torch.cat(features, dim=1)
```

**DenseNet-121** has 8M parameters (vs ResNet-50's 25M) but comparable accuracy. Very parameter-efficient.

## EfficientNet (2019) — Compound Scaling

Instead of scaling depth, width, or resolution independently, scale all three **together**:

$$\text{depth: } d = \alpha^\phi, \quad \text{width: } w = \beta^\phi, \quad \text{resolution: } r = \gamma^\phi$$

subject to $\alpha \cdot \beta^2 \cdot \gamma^2 \approx 2$.

**EfficientNet-B0 to B7**: A family of models with increasing compute budgets.

```python
# EfficientNet-B0 base architecture (simplified)
# Uses mobile inverted bottleneck (MBConv) blocks
# Compound scaling applies to all three dimensions
```

**Results**: EfficientNet-B7 achieves 84.3% ImageNet top-1 accuracy — state-of-the-art at the time, with 8.4x fewer FLOPs than the previous best.

## ConvNeXt (2022) — Modernizing CNNs

A pure convolution network that matches Vision Transformer performance by adopting transformer design choices:

- Larger kernel size (7×7 instead of 3×3)
- Fewer activation functions (GELU instead of ReLU)
- Layer normalization instead of batch normalization
- Inverted bottleneck design
- Patchify stem (4×4 conv with stride 4)

```python
class ConvNeXtBlock(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dwconv = nn.Conv2d(dim, dim, kernel_size=7, padding=3, groups=dim)  # depthwise
        self.norm = nn.LayerNorm(dim)
        self.pwconv1 = nn.Linear(dim, 4 * dim)
        self.act = nn.GELU()
        self.pwconv2 = nn.Linear(4 * dim, dim)
    
    def forward(self, x):
        residual = x
        x = self.dwconv(x)
        x = x.permute(0, 2, 3, 1)  # (B,C,H,W) → (B,H,W,C)
        x = self.norm(x)
        x = self.pwconv1(x)
        x = self.act(x)
        x = self.pwconv2(x)
        x = x.permute(0, 3, 1, 2)
        return residual + x
```

## Architecture Comparison

| Architecture | Year | Parameters | Top-1 Acc | Key Innovation |
|---|---|---|---|---|
| AlexNet | 2012 | 60M | 63% | ReLU, GPU, dropout |
| VGG-16 | 2014 | 138M | 74% | Depth with 3×3 filters |
| GoogLeNet | 2014 | 6.8M | 74% | Inception modules |
| ResNet-50 | 2015 | 25M | 76% | Skip connections |
| DenseNet-121 | 2017 | 8M | 75% | Feature reuse |
| EfficientNet-B7 | 2019 | 66M | 84% | Compound scaling |
| ConvNeXt-B | 2022 | 89M | 84% | Transformer-style CNN |

## Choosing an Architecture

| Use Case | Recommended |
|---|---|
| Learning/education | ResNet-18 (simple, well-understood) |
| Production (general) | EfficientNet-B3/B4 |
| Mobile/edge | MobileNetV3, EfficientNet-B0 |
| Maximum accuracy | ConvNeXt-L or ViT-L |
| Medical imaging | EfficientNet + transfer learning |
| Fine-grained classification | ResNet + attention |

## Further Reading

- He et al. (2015) ResNet is one of the most important papers in deep learning
- Tan & Le (2019) EfficientNet showed compound scaling is principled
- Liu et al. (2022) ConvNeXt blurred the line between CNNs and transformers
- For efficient inference: TensorRT, ONNX Runtime, MobileNet
