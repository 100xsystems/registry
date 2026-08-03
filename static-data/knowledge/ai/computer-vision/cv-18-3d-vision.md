---
{
  "title": "3D Vision",
  "description": "Depth, point clouds and stereo: how cameras recover the third dimension.",
  "type": "lesson",
  "order": 18,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain depth from stereo disparity",
    "Read depth maps and point clouds",
    "Use camera intrinsics for projection",
    "Explore LiDAR fusion"
  ],
  "knowledge_refs": [
    "computer-vision/cv-18-3d-vision"
  ],
  "prerequisites": [
    "CV-13: Feature Detection & Matching"
  ],
  "references": [
    {
      "title": "OpenCV Documentation",
      "url": "https://docs.opencv.org/4.x/index.html",
      "description": "The reference for classic image processing in Python."
    },
    {
      "title": "PyTorch Vision Docs",
      "url": "https://pytorch.org/vision/stable/index.html",
      "description": "Datasets, transforms and model zoo for vision."
    },
    {
      "title": "Stanford CS231n",
      "url": "http://cs231n.stanford.edu/",
      "description": "The classic university course on CNNs for visual recognition."
    },
    {
      "title": "YOLO Papers & Implementations",
      "url": "https://docs.ultralytics.com/",
      "description": "Real-time object detection with YOLOv8 (Ultralytics)."
    },
    {
      "title": "Torchvision Models",
      "url": "https://pytorch.org/vision/stable/models.html",
      "description": "Pretrained model catalog for transfer learning."
    }
  ]
}
---

# CV-18-3D-VISION: 3D Vision

## Introduction

Depth, point clouds and stereo: how cameras recover the third dimension. By the end of this lesson you will be able to: Explain depth from stereo disparity; Read depth maps and point clouds; Use camera intrinsics for projection; Explore LiDAR fusion.

## Key Concepts

### 1. Explain depth from stereo disparity

Target: Explain depth from stereo disparity. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

# Disparity: closer objects shift more between left/right
focal, baseline = 500.0, 0.12
disparity = 20.0
depth = focal * baseline / disparity
print("depth (m):", round(depth, 2))
```
### 2. Read depth maps and point clouds

Target: Read depth maps and point clouds. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# Project 3D point to pixel with intrinsics
K = np.array([[500, 0, 320], [0, 500, 240], [0, 0, 1]])
pt3d = np.array([1.0, 2.0, 5.0])
pix = K @ pt3d / pt3d[2]
print("pixel:", pix[:2].round(1))
```
### 3. Use camera intrinsics for projection

Target: Use camera intrinsics for projection. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import open3d as o3d

pcd = o3d.geometry.PointCloud()
print("point cloud object ready")
```
### 4. Explore LiDAR fusion

Target: Explore LiDAR fusion. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Depth maps as 2D arrays of distances
depth = np.zeros((240, 320))
print("depth map:", depth.shape)
```

## Practice Questions

1. What is the key idea behind "3D Vision"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain 3D Vision with analogies and real-world examples"
1. "Show me common mistakes beginners make with 3D Vision"
1. "Provide advanced patterns and performance considerations for 3D Vision"

## Key Takeaways

- Master the core ideas of 3D Vision through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
