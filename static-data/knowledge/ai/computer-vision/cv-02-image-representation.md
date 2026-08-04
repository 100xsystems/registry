---
slug: cv-02-image-representation
title: "Image Representation"
description: "How computers see images — pixels, color spaces, tensors, and the battle between HWC and CHW."
order: 2
tags:
  - computer-vision
  - pixels
  - color-spaces
  - tensors
  - preprocessing
prerequisites:
  - cv-01-what-is-computer-vision
  - dl-08-pytorch-tensors-and-autograd
references:
  - title: "Learn PyTorch: PyTorch Computer Vision"
    url: "https://www.learnpytorch.io/03_pytorch_computer_vision/"
    description: "Hands-on PyTorch tutorial for image tensors"
  - title: "OpenCV Color Spaces"
    url: "https://opencv.org/color-spaces-in-opencv/"
    description: "Official OpenCV guide to color space conversions"
  - title: "Roboflow: OpenCV Color Spaces Guide"
    url: "https://blog.roboflow.com/opencv-color-spaces/"
    description: "Practical guide to color space selection"
  - title: "PyTorch Forums: Why NCHW?"
    url: "https://discuss.pytorch.org/t/why-does-pytorch-prefer-using-nchw/83637"
    description: "Technical discussion on channel ordering"
  - title: "PIL Documentation"
    url: "https://pillow.readthedocs.io/"
    description: "Python Imaging Library documentation"
knowledge_refs:
  - cv-01-what-is-computer-vision
  - dl-08-pytorch-tensors-and-autograd
  - cv-03-image-processing
---

# Image Representation

At the most fundamental level, a digital image is a grid of numbers. Understanding how images are represented — as pixels, color channels, and tensors — is essential for all computer vision work.

## Pixels: The Building Blocks

An image is a 2D grid of **pixels** (picture elements), each containing numerical values:

```python
import numpy as np
from PIL import Image

# Load image as numpy array
img = np.array(Image.open("photo.jpg"))
print(img.shape)  # (480, 640, 3) — height, width, channels
print(img.dtype)  # uint8 (0-255)
print(img[0, 0])  # [142, 108, 73] — RGB values of top-left pixel
```

**Grayscale images**: Single channel (2D array)
```python
gray = np.array(Image.open("photo.jpg").convert("L"))
print(gray.shape)  # (480, 640) — height, width
print(gray.dtype)  # uint8 (0-255)
```

**Color images**: Three channels (3D array)
```python
color = np.array(Image.open("photo.jpg"))
print(color.shape)  # (480, 640, 3) — height, width, channels
```

## Color Spaces

### RGB (Red, Green, Blue)
The standard additive color model:
- 3 channels: Red, Green, Blue
- Each channel: 0-255 (uint8) or 0.0-1.0 (float)
- Used by: PIL, Matplotlib, PyTorch, most displays

```python
# RGB channels
r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
```

### BGR (Blue, Green, Red)
- **OpenCV's default** color format
- Same data, different channel order
- **Critical**: Always convert when mixing OpenCV with other libraries

```python
import cv2

# OpenCV reads as BGR
img_bgr = cv2.imread("photo.jpg")

# Convert to RGB for display with Matplotlib
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
```

### HSV (Hue, Saturation, Value)
Separates color from brightness:
- **Hue (H)**: Color wavelength (0-179 in OpenCV)
- **Saturation (S)**: Color purity (0-255)
- **Value (V)**: Brightness (0-255)

**Use cases**: Color segmentation, object tracking (hue is invariant to lighting)

```python
hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

# Segment red objects (two ranges due to hue wraparound)
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
red_mask = mask1 | mask2
```

### LAB (Lightness, A, B)
Perceptually uniform color space:
- **L**: Lightness (0-100)
- **A**: Green to Red (-128 to 127)
- **B**: Blue to Yellow (-128 to 127)

**Use cases**: Color correction, illumination-invariant features

## Tensor Formats: HWC vs CHW

### HWC (Height, Width, Channels)
- **Default for**: NumPy, PIL, Matplotlib, OpenCV
- Shape: (H, W, C)
- Used by: TensorFlow, Keras

### CHW (Channels, Height, Width)
- **Default for**: PyTorch, Caffe
- Shape: (C, H, W)
- Used by: Most vision models in PyTorch

```python
import torch

# NumPy (HWC)
img_np = np.array(Image.open("photo.jpg"))  # (480, 640, 3)

# PyTorch (CHW)
img_tensor = torch.from_numpy(img_np).permute(2, 0, 1)  # (3, 480, 640)

# Or using torchvision
from torchvision import transforms
to_tensor = transforms.ToTensor()  # Converts HWC uint8 → CHW float [0,1]
img_tensor = to_tensor(Image.open("photo.jpg"))  # (3, 480, 640)
```

### Batch Dimension (N)
Multiple images are stacked with a batch dimension:
- **NCHW**: (Batch, Channels, Height, Width) — PyTorch
- **NHWC**: (Batch, Height, Width, Channels) — TensorFlow

```python
# Batch of 32 images, 3 channels, 224x224
batch = torch.randn(32, 3, 224, 224)  # PyTorch NCHW
batch = tf.random.normal((32, 224, 224, 3))  # TensorFlow NHWC
```

## Why Channel Order Matters

Different frameworks expect different formats:
| Framework | Format | Notes |
|---|---|---|
| PyTorch | NCHW | Conv2d expects this |
| TensorFlow | NHWC | Default in TF2 |
| OpenCV | HWC (BGR) | BGR not RGB! |
| PIL/NumPy | HWC (RGB) | Standard Python |
| ONNX | NCHW | For inference |
| TensorRT | NHWC | For GPU inference |

**Common bug**: Passing wrong format causes errors or wrong results silently.

## Normalization

Models expect normalized inputs:
```python
# ImageNet normalization (standard for pretrained models)
mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]

# Apply to tensor
normalized = (tensor - torch.tensor(mean).view(3, 1, 1)) / torch.tensor(std).view(3, 1, 1)
```

**Why normalize?**
- Pretrained models expect this specific normalization
- Helps training convergence
- Makes gradient magnitudes more uniform

## Data Types

| Type | Range | Use Case |
|---|---|---|
| uint8 | 0-255 | Storage, display |
| float32 | 0.0-1.0 | PyTorch (after ToTensor) |
| float32 | -1.0 to 1.0 | Some models (e.g., StyleGAN) |
| float16 | Half precision | Mixed precision training |

```python
# uint8 to float32
img_float = img.astype(np.float32) / 255.0  # [0, 1]

# float32 to normalized
img_norm = (img_float - mean) / std  # ImageNet normalization
```

## Practical Tips

1. **Always check channel order**: RGB vs BGR is the #1 source of bugs
2. **Use ToTensor()**: Handles conversion automatically in PyTorch
3. **Normalize consistently**: Use the same normalization for train/test
4. **Keep original for display**: Convert back to uint8 before showing
5. **Match model expectations**: Check what format the model was trained with

## Further Reading

- Learn PyTorch tutorial provides hands-on practice
- OpenCV color spaces guide explains when to use HSV/LAB
- The PyTorch forums discussion explains why CHW is preferred
- PIL documentation covers image loading and basic operations
