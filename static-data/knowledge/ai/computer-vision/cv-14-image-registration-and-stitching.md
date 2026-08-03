---
{
  "title": "Image Registration & Stitching",
  "description": "Combine overlapping images into panoramas and align images across time or sensors.",
  "type": "lesson",
  "order": 14,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain registration as a geometric alignment problem",
    "Match features across images",
    "Estimate a homography with RANSAC",
    "Warp and blend into a panorama"
  ],
  "knowledge_refs": [
    "computer-vision/cv-13-feature-detection"
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

# CV-14-IMAGE-REGISTRATION-AND-STITCHING: Image Registration & Stitching

## Introduction

Combine overlapping images into panoramas and align images across time or sensors. By the end of this lesson you will be able to: Explain registration as a geometric alignment problem; Match features across images; Estimate a homography with RANSAC; Warp and blend into a panorama.

## Key Concepts

### 1. Explain registration as a geometric alignment problem

Target: Explain registration as a geometric alignment problem. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import cv2

# RANSAC rejects outlier matches
H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
print("inliers:", mask.sum())
```
### 2. Match features across images

Target: Match features across images. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import cv2

# Warp perspective of image A into image B's plane
warped = cv2.warpPerspective(img_a, H, (w, h))
print("warped:", warped.shape)
```
### 3. Estimate a homography with RANSAC

Target: Estimate a homography with RANSAC. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import cv2

# Blend seam with feathering to hide edges
print("blend: weighted average along the seam")
```
### 4. Warp and blend into a panorama

Target: Warp and blend into a panorama. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import cv2

stitcher = cv2.Stitcher_create()
status, pano = stitcher.stitch([img_a, img_b])
print("stitch status:", status)
```

## Practice Questions

1. What is the key idea behind "Image Registration & Stitching"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Image Registration & Stitching with analogies and real-world examples"
1. "Show me common mistakes beginners make with Image Registration & Stitching"
1. "Provide advanced patterns and performance considerations for Image Registration & Stitching"

## Key Takeaways

- Master the core ideas of Image Registration & Stitching through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
