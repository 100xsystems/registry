---
slug: cv-01-what-is-computer-vision
title: "What Is Computer Vision?"
description: "The field that gives machines sight — from early edge detectors to modern vision transformers."
order: 1
tags:
  - computer-vision
  - fundamentals
  - deep-learning
prerequisites:
  - dl-01-what-is-deep-learning
  - ml-01-what-is-machine-learning
references:
  - title: "CS231n: Deep Learning for Computer Vision (Stanford)"
    url: "https://cs231n.stanford.edu/"
    description: "The definitive academic course on computer vision"
  - title: "OpenCV: What Is Computer Vision?"
    url: "https://opencv.org/what-is-computer-vision/"
    description: "Practical overview of CV tasks and applications"
  - title: "PyTorch Computer Vision Tutorial"
    url: "https://www.learnpytorch.io/03_pytorch_computer_vision/"
    description: "Hands-on introduction to CV with PyTorch"
  - title: "Deep Residual Learning for Image Recognition (He et al.)"
    url: "https://arxiv.org/abs/1512.03385"
    description: "ResNet paper that enabled deep vision models"
  - title: "An Image is Worth 16x16 Words (ViT Paper)"
    url: "https://arxiv.org/abs/2010.11929"
    description: "Dosovitskiy et al.'s Vision Transformer paper"
knowledge_refs:
  - dl-12-convolutional-networks
  - dl-13-cnn-architectures
  - cv-05-image-classification
---

# What Is Computer Vision?

Computer vision is a field of AI that enables machines to interpret and understand visual information from the world — images, videos, and real-time visual streams. It's one of the oldest and most impactful areas of artificial intelligence.

## The Goal of Computer Vision

Humans process visual information effortlessly — we can identify faces, read text, navigate rooms, and catch balls without conscious effort. Computer vision aims to replicate this capability in machines, enabling applications from autonomous driving to medical diagnosis.

## Key Computer Vision Tasks

### Image Classification
Assign a single label to an entire image:
```
Input: [Image of a cat]
Output: "Cat" (0.95), "Dog" (0.03), "Bird" (0.02)
```

### Object Detection
Locate and classify multiple objects with bounding boxes:
```
Input: [Street scene]
Output: [
  {"label": "car", "bbox": [100, 200, 300, 400], "conf": 0.92},
  {"label": "person", "bbox": [50, 100, 150, 350], "conf": 0.88}
]
```

### Semantic Segmentation
Classify every pixel in the image:
```
Input: [Street scene]
Output: [Pixel map where road=blue, car=red, person=green, sky=cyan]
```

### Instance Segmentation
Detect individual object instances AND their pixel boundaries:
```
Input: [Two cars]
Output: [Car_1 mask, Car_2 mask] — distinguishes separate instances
```

### Pose Estimation
Detect human body keypoints (joints):
```
Input: [Person standing]
Output: {left_shoulder: (x,y), right_knee: (x,y), ...}
```

## A Brief History

| Year | Milestone | Impact |
|---|---|---|
| 1959 | Hubel & Wiesel: Visual cortex neurons | Biological inspiration for CNNs |
| 1963 | Roberts: 3D from 2D images | First CV thesis |
| 1979 | Fukushima: Neocognitron | Inspired CNN architecture |
| 1998 | LeNet-5 (LeCun) | First practical CNN for digits |
| 2001 | Viola-Jones: Face detection | First real-time face detection |
| 2009 | ImageNet dataset | Enabled deep learning revolution |
| 2012 | AlexNet wins ImageNet | Deep learning takes over CV |
| 2015 | ResNet: 152 layers | Deep networks become trainable |
| 2017 | Faster R-CNN: Real-time detection | Object detection becomes practical |
| 2020 | Vision Transformer (ViT) | Transformers enter computer vision |
| 2023 | SAM: Segment Anything | Foundation model for segmentation |

## The Paradigm Shift

### Pre-Deep Learning (Before 2012)
- **Hand-crafted features**: SIFT, HOG, SURF
- **Manual pipeline**: Feature extraction → Feature selection → Classifier
- **Brittle**: Failed with lighting changes, occlusion, viewpoint variation

### Deep Learning Era (2012–Present)
- **Learned features**: CNNs learn features end-to-end from pixels
- **Single model**: Input pixels → Output predictions
- **Robust**: Handles real-world variation through data augmentation

## Real-World Applications

| Application | CV Tasks Used | Impact |
|---|---|---|
| **Autonomous driving** | Detection, segmentation, depth | Safety-critical, life-saving |
| **Medical imaging** | Classification, segmentation | Early disease detection |
| **Manufacturing** | Defect detection, quality control | Reduce waste, improve quality |
| **Retail** | Face recognition, product detection | Cashier-less stores |
| **Agriculture** | Crop monitoring, disease detection | Precision farming |
| **AR/VR** | Pose estimation, SLAM | Immersive experiences |
| **Security** | Surveillance, anomaly detection | Public safety |
| **Content moderation** | Classification, detection | Platform safety |

## The Modern CV Stack

```
Input Image
    ↓
[Preprocessing] → Resize, normalize, augment
    ↓
[Backbone] → Extract features (ResNet, ViT, EfficientNet)
    ↓
[Neck] → Multi-scale features (FPN, BiFPN)
    ↓
[Head] → Task-specific predictions
    ↓
Output: Class, Box, Mask, Keypoints
```

## What You'll Learn in This Course

1. **Image fundamentals**: Representation, processing, augmentation
2. **Classification**: CNNs, transfer learning, evaluation
3. **Object detection**: YOLO, Faster R-CNN, anchor-free methods
4. **Segmentation**: Semantic, instance, panoptic
5. **Pose estimation**: Human and animal pose
6. **Classical CV**: OpenCV, feature detection, image processing
7. **Video analysis**: Tracking, action recognition
8. **Face analysis**: Detection, recognition, analysis
9. **Document AI**: OCR, document understanding
10. **3D vision**: Depth estimation, point clouds, NeRFs
11. **Vision Transformers**: ViT, DeiT, Swin Transformer

## Further Reading

- CS231n is the definitive course for learning CV
- OpenCV documentation covers practical CV operations
- The ViT paper marks the transformer era in vision
- ResNet enabled deep networks that actually work
