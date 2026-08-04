---
slug: cv-18-3d-vision
title: "3D Vision"
description: "Understanding the third dimension — depth estimation, point clouds, NeRFs, and 3D reconstruction from images."
order: 18
tags:
  - computer-vision
  - 3d-vision
  - depth-estimation
  - point-clouds
  - nerf
prerequisites:
  - cv-06-cnns-for-vision
  - cv-12-opencv-fundamentals
  - dl-17-transformers
references:
  - title: "Monodepth2: Self-Supervised Monocular Depth Estimation"
    url: "https://arxiv.org/abs/1806.01260"
    description: "Godard et al.'s self-supervised depth estimation paper"
  - title: "NeRF: Representing Scenes as Neural Radiance Fields"
    url: "https://arxiv.org/abs/2003.08934"
    description: "Mildenhall et al.'s NeRF paper for novel view synthesis"
  - title: "PointNet: Deep Learning on Point Sets"
    url: "https://arxiv.org/abs/1612.00593"
    description: "Qi et al.'s foundational paper for point cloud processing"
  - title: "Open3D Documentation"
    url: "http://www.open3d.org/docs/"
    description: "Open3D library for 3D data processing"
  - title: "Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data"
    url: "https://arxiv.org/abs/2401.10893"
    description: "Yang et al.'s foundation model for monocular depth estimation"
knowledge_refs:
  - cv-06-cnns-for-vision
  - cv-12-opencv-fundamentals
  - dl-17-transformers
---

# 3D Vision

3D vision recovers the third dimension from 2D images — estimating depth, reconstructing 3D scenes, and understanding spatial relationships.

## Key Tasks

### Monocular Depth Estimation
Predict depth from a single image:
```python
import torch
from transformers import pipeline

depth_pipe = pipeline("depth-estimation", model="depth-anything/Depth-Anything-V2-Small")
result = depth_pipe("photo.jpg")
depth_map = result["depth"]  # H×W depth values
```

### Stereo Depth Estimation
Compute depth from two images (left + right):
- Disparity = horizontal shift between matching pixels
- Depth = baseline × focal_length / disparity

### LiDAR / RGB-D
Direct depth sensors provide accurate 3D data.

## Point Clouds

3D data represented as collections of (x, y, z) points:
```python
import numpy as np

# Simple point cloud: (N, 3)
points = np.random.randn(10000, 3)

# With colors: (N, 6) — xyz + rgb
points_with_color = np.hstack([points, np.random.randint(0, 255, (10000, 3))])
```

### PointNet Architecture
Processes unordered point sets directly:
```python
# PointNet: Per-point features → Global feature → Classification
class PointNet(nn.Module):
    def __init__(self, num_classes=40):
        super().__init__()
        self.mlp = nn.Sequential(
            nn.Linear(3, 64), nn.ReLU(),
            nn.Linear(64, 128), nn.ReLU(),
            nn.Linear(128, 1024)
        )
        self.classifier = nn.Sequential(
            nn.Linear(1024, 512), nn.ReLU(),
            nn.Linear(512, 256), nn.ReLU(),
            nn.Linear(256, num_classes)
        )
    
    def forward(self, x):
        features = self.mlp(x)  # (B, N, 1024)
        global_feat = features.max(dim=1)[0]  # (B, 1024)
        return self.classifier(global_feat)
```

## NeRF (Neural Radiance Fields)

Represent 3D scenes as neural networks:
- Input: (x, y, z, θ, φ) — position + viewing direction
- Output: (r, g, b, σ) — color + density
- Render novel views via volume rendering

```python
# Simplified NeRF concept
def nerf(position, direction):
    # MLP maps 3D position to color and density
    features = mlp(position)
    r, g, b, sigma = features
    return rgb, density
```

### NeRF Applications
- Novel view synthesis from few photos
- 3D scene reconstruction
- Virtual reality content creation
- Digital twins

## 3D Reconstruction

### Multi-View Stereo (MVS)
Reconstruct 3D from multiple images:
1. Detect features in each image
2. Match features across views
3. Triangulate 3D points
4. Build dense point cloud / mesh

### Structure from Motion (SfM)
Estimate camera poses + 3D points:
```python
# OpenCV SfM
points4d = cv2.triangulatePoints(proj_matrix1, proj_matrix2, points1, points2)
points3d = points4d[:3] / points4d[3]  # Convert to Cartesian
```

### SLAM (Simultaneous Localization and Mapping)
Real-time 3D mapping while tracking camera pose.

## Libraries and Tools

| Library | Purpose |
|---|---|
| **Open3D** | Point cloud processing, visualization |
| **PyTorch3D** | Differentiable 3D operations |
| **trimesh** | Mesh processing |
| **Open3D** | 3D reconstruction pipeline |

## Applications

| Application | Technology |
|---|---|
| **Autonomous driving** | LiDAR + depth estimation |
| **AR/VR** | 3D reconstruction, SLAM |
| **Robotics** | 3D perception, grasping |
| **Medical imaging** | 3D organ reconstruction |
| **Cultural heritage** | 3D scanning of artifacts |
| **Construction** | Building information modeling |

## Further Reading

- Depth Anything is the current best for monocular depth
- NeRF revolutionized novel view synthesis
- PointNet established deep learning on point clouds
- Open3D provides the essential 3D processing toolkit
