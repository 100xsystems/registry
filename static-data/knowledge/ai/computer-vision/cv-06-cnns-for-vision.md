---
slug: cv-06-cnns-for-vision
title: "CNNs for Vision"
description: "The convolution operation, pooling, feature maps, and how CNNs learn hierarchical visual representations."
order: 6
tags:
  - computer-vision
  - cnn
  - convolution
  - pooling
  - feature-maps
prerequisites:
  - cv-05-image-classification
  - dl-12-convolutional-networks
  - cv-02-image-representation
references:
  - title: "CS231n: Convolutional Neural Networks"
    url: "https://cs231n.github.io/convolutional-networks/"
    description: "Stanford's definitive CNN lecture notes"
  - title: "Understanding CNNs (LearnOpenCV)"
    url: "https://learnopencv.com/understanding-convolutional-neural-networks-cnn/"
    description: "Comprehensive CNN guide with visualizations"
  - title: "Dive into Deep Learning: ResNet"
    url: "https://d2l.ai/chapter_convolutional-modern/resnet.html"
    description: "Residual network architecture explained"
  - title: "TensorFlow CNN Tutorial"
    url: "https://www.tensorflow.org/tutorials/images/cnn"
    description: "Hands-on CNN implementation in TensorFlow"
  - title: "PyTorch CIFAR-10 Tutorial"
    url: "https://docs.pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html"
    description: "Building and training a CNN in PyTorch"
knowledge_refs:
  - dl-12-convolutional-networks
  - cv-05-image-classification
  - dl-13-cnn-architectures
---

# CNNs for Vision

Convolutional Neural Networks are the backbone of computer vision. They learn hierarchical feature representations — from simple edges to complex object parts — through parameter sharing and local connectivity.

## The Convolution Operation

A small filter (kernel) slides over the input, computing dot products at each position:

$$\text{Output Size} = \frac{W - F + 2P}{S} + 1$$

where $W$ = input width, $F$ = filter size, $P$ = padding, $S$ = stride.

```python
import torch.nn as nn

# Conv layer: 3 input channels → 32 output channels, 3×3 kernel
conv = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, stride=1, padding=1)
output = conv(input_tensor)  # (B, 3, 224, 224) → (B, 32, 224, 224)
```

## Feature Maps and Hierarchical Features

Each convolutional layer produces **feature maps** — activations that detect specific patterns:

| Layer | Features Detected | Example |
|---|---|---|
| Conv1 | Edges, colors | Horizontal/vertical edges |
| Conv2 | Textures, corners | Checkerboard patterns |
| Conv3 | Parts | Eyes, wheels, windows |
| Conv4 | Objects | Faces, cars, buildings |
| Conv5 | Scenes | Indoor/outdoor, landscape |

**Key insight**: Deeper layers capture increasingly abstract concepts. This hierarchy is learned automatically from data.

## Pooling Layers

Downsample spatial dimensions and provide translation invariance:

```python
# Max pooling: takes maximum in each window
pool = nn.MaxPool2d(kernel_size=2, stride=2)  # Reduces H,W by 2x

# Average pooling
avg_pool = nn.AvgPool2d(kernel_size=2, stride=2)

# Global average pooling: reduces each feature map to a single value
gap = nn.AdaptiveAvgPool2d(1)  # (B, C, H, W) → (B, C, 1, 1)
```

**Max pooling** preserves the strongest activations and is the standard choice.

## Parameter Sharing and Translation Invariance

**Parameter sharing**: The same filter is applied across all spatial positions:
- A 3×3 filter has 9 weights (plus bias)
- Applied to a 224×224 image → uses the same 9 weights everywhere
- Dramatic parameter reduction vs. fully connected layers

**Translation invariance**: If a cat moves in the image, the same filters still detect it.

## Modern CNN Blocks

### Residual Block (ResNet)
Skip connections solve the degradation problem:
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

### Depthwise Separable Convolution (MobileNet)
Factorize standard convolution for efficiency:
```python
# Standard: O(K² × Cin × Cout × H × W)
# Depthwise separable: O(K² × Cin × H × W + Cin × Cout × H × W)

depthwise = nn.Conv2d(64, 64, 3, padding=1, groups=64)  # per-channel
pointwise = nn.Conv2d(64, 128, 1)  # 1×1 to mix channels
```

## Building a Complete CNN

```python
class CNN(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1), nn.BatchNorm2d(32), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding=1), nn.BatchNorm2d(64), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(64, 128, 3, padding=1), nn.BatchNorm2d(128), nn.ReLU(), nn.AdaptiveAvgPool2d(1),
        )
        self.classifier = nn.Linear(128, num_classes)
    
    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        return self.classifier(x)
```

## Visualizing What CNNs Learn

```python
# Hook to extract activations
activations = {}
def hook_fn(module, input, output):
    activations[module] = output

for name, layer in model.named_modules():
    if isinstance(layer, nn.Conv2d):
        layer.register_forward_hook(hook_fn)

# Visualize feature maps
for layer, act in activations.items():
    fig, axes = plt.subplots(1, 8, figsize=(16, 2))
    for i in range(8):
        axes[i].imshow(act[0, i].cpu().detach(), cmap='viridis')
        axes[i].axis('off')
```

## Further Reading

- CS231n notes are the definitive CNN reference
- LearnOpenCV provides excellent visualizations
- D2L covers residual networks mathematically
- For efficient CNNs: MobileNet, EfficientNet papers
