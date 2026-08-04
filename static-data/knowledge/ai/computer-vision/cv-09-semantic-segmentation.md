---
slug: cv-09-semantic-segmentation
title: "Semantic Segmentation"
description: "Classifying every pixel in an image — FCN, U-Net, DeepLab, and the mIoU metric."
order: 9
tags:
  - computer-vision
  - segmentation
  - u-net
  - deeplab
  - fcn
prerequisites:
  - cv-06-cnns-for-vision
  - cv-08-object-detection
  - dl-12-convolutional-networks
references:
  - title: "Fully Convolutional Networks for Semantic Segmentation (Long et al.)"
    url: "https://arxiv.org/abs/1411.4038"
    description: "The foundational FCN paper that started semantic segmentation"
  - title: "U-Net: Convolutional Networks for Biomedical Image Segmentation"
    url: "https://arxiv.org/abs/1505.04597"
    description: "Ronneberger et al.'s U-Net paper for medical image segmentation"
  - title: "DeepLab: Semantic Image Segmentation with Deep Convolutional Nets"
    url: "https://arxiv.org/abs/1606.00915"
    description: "Chen et al.'s DeepLab series with atrous convolution"
  - title: "PyTorch Segmentation Tutorial"
    url: "https://pytorch.org/tutorials/intermediate/torchvision_tutorial.html"
    description: "Official PyTorch segmentation tutorial"
  - title: "MMSegmentation Documentation"
    url: "https://mmsegmentation.readthedocs.io/"
    description: "Open-source segmentation toolbox"
knowledge_refs:
  - cv-06-cnns-for-vision
  - cv-08-object-detection
  - cv-10-instance-segmentation
---

# Semantic Segmentation

Semantic segmentation classifies **every pixel** in an image into a category — creating a pixel-level map of what's in the scene.

## Segmentation Output

```
Input: Street scene image (H×W×3)
Output: Label map (H×W) where each pixel = class ID
  0 = background
  1 = road
  2 = car
  3 = person
  4 = building
  ...
```

## FCN (Fully Convolutional Network)

The first successful segmentation CNN — replaces fully connected layers with 1×1 convolutions:

```
Input → [Conv layers] → [Upsample] → Pixel predictions
```

**Upsampling**: Deconvolution (transposed convolution) recovers spatial resolution.

## U-Net: The Segmentation Workhorse

Encoder-decoder with skip connections:

```
Encoder (downsampling):
  [Conv→Conv→Pool] × 4
  Features: 64→128→256→512→1024

Decoder (upsampling):
  [Upsample→Concat→Conv→Conv] × 4
  Skip connections from encoder

Output: Per-pixel class predictions
```

```python
class UNet(nn.Module):
    def __init__(self, in_channels=3, num_classes=21):
        super().__init__()
        # Encoder
        self.enc1 = self._block(in_channels, 64)
        self.enc2 = self._block(64, 128)
        self.enc3 = self._block(128, 256)
        self.enc4 = self._block(256, 512)
        
        self.pool = nn.MaxPool2d(2)
        
        # Bottleneck
        self.bottleneck = self._block(512, 1024)
        
        # Decoder
        self.up4 = nn.ConvTranspose2d(1024, 512, 2, stride=2)
        self.dec4 = self._block(1024, 512)  # 1024 because of skip concat
        self.up3 = nn.ConvTranspose2d(512, 256, 2, stride=2)
        self.dec3 = self._block(512, 256)
        self.up2 = nn.ConvTranspose2d(256, 128, 2, stride=2)
        self.dec2 = self._block(256, 128)
        self.up1 = nn.ConvTranspose2d(128, 64, 2, stride=2)
        self.dec1 = self._block(128, 64)
        
        self.out = nn.Conv2d(64, num_classes, 1)
    
    def _block(self, in_ch, out_ch):
        return nn.Sequential(
            nn.Conv2d(in_ch, out_ch, 3, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(),
            nn.Conv2d(out_ch, out_ch, 3, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(),
        )
    
    def forward(self, x):
        # Encoder
        e1 = self.enc1(x)
        e2 = self.enc2(self.pool(e1))
        e3 = self.enc3(self.pool(e2))
        e4 = self.enc4(self.pool(e3))
        
        # Bottleneck
        b = self.bottleneck(self.pool(e4))
        
        # Decoder with skip connections
        d4 = self.dec4(torch.cat([self.up4(b), e4], dim=1))
        d3 = self.dec3(torch.cat([self.up3(d4), e3], dim=1))
        d2 = self.dec2(torch.cat([self.up2(d3), e2], dim=1))
        d1 = self.dec1(torch.cat([self.up1(d2), e1], dim=1))
        
        return self.out(d1)
```

**Why skip connections matter**: They preserve fine spatial details lost during downsampling.

## DeepLab Series

### DeepLab v3+
Key innovations:
- **Atrous (dilated) convolution**: Larger receptive field without pooling
- **ASPP (Atrous Spatial Pyramid Pooling)**: Multi-scale feature extraction
- **Encoder-decoder structure**: Refines boundaries

```python
# Atrous convolution: dilated convolution
dilated_conv = nn.Conv2d(64, 64, 3, padding=2, dilation=2)
# Same parameters as 5×5 receptive field, but only 3×3 weights
```

## Evaluation: mIoU

**Intersection over Union (IoU)** per class:
$$\text{IoU} = \frac{\text{TP}}{\text{TP} + \text{FP} + \text{FN}}$$

**Mean IoU (mIoU)**: Average IoU across all classes.

```python
def compute_miou(pred, target, num_classes):
    ious = []
    for cls in range(num_classes):
        pred_mask = (pred == cls)
        target_mask = (target == cls)
        intersection = (pred_mask & target_mask).sum()
        union = (pred_mask | target_mask).sum()
        if union > 0:
            ious.append(intersection / union)
    return np.mean(ious)
```

## Loss Functions for Segmentation

### Cross-Entropy (Pixel-wise)
$$\mathcal{L} = -\sum_{i} y_i \log(\hat{y}_i)$$

### Dice Loss
Handles class imbalance:
$$\mathcal{L} = 1 - \frac{2 \sum_i y_i \hat{y}_i}{\sum_i y_i + \sum_i \hat{y}_i}$$

### Combined Loss
```python
criterion = nn.CrossEntropyLoss() + dice_loss  # Common practice
```

## Practical Tips

1. **Use U-Net** for medical/biomedical segmentation
2. **Use DeepLab v3+** for general semantic segmentation
3. **Dice loss** helps with class imbalance
4. **Data augmentation** is critical ( flips, scales, color jitter)
5. **Test-time augmentation**: Average predictions over flipped/scaled versions

## Further Reading

- FCN paper started the deep learning segmentation revolution
- U-Net is the gold standard for biomedical segmentation
- DeepLab series pushed the state-of-the-art on PASCAL VOC and ADE20K
- MMSegmentation provides implementations of all major architectures
