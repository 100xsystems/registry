---
{
  "title": "Feature Detection & Matching",
  "description": "Keypoints and descriptors: SIFT, ORB, and how image matching enables stitching and localization.",
  "type": "lesson",
  "order": 13,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Explain keypoints and descriptors",
    "Detect and match SIFT/ORB features",
    "Filter matches with ratio tests",
    "Use homography for alignment"
  ],
  "knowledge_refs": [
    "computer-vision/cv-13-feature-detection"
  ],
  "prerequisites": [
    "CV-12: OpenCV Fundamentals"
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

# CV-13-FEATURE-DETECTION: Feature Detection & Matching

## Introduction

Keypoints and descriptors: SIFT, ORB, and how image matching enables stitching and localization. By the end of this lesson you will be able to: Explain keypoints and descriptors; Detect and match SIFT/ORB features; Filter matches with ratio tests; Use homography for alignment.

## Key Concepts

### 1. Explain keypoints and descriptors

Target: Explain keypoints and descriptors. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import cv2

sift = cv2.SIFT_create()
kp, des = sift.detectAndCompute(img, None)
print("keypoints:", len(kp), "descriptor dim:", des.shape)
```
### 2. Detect and match SIFT/ORB features

Target: Detect and match SIFT/ORB features. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import cv2

orb = cv2.ORB_create()
kp2, des2 = orb.detectAndCompute(img, None)
print("ORB keypoints:", len(kp2))
```
### 3. Filter matches with ratio tests

Target: Filter matches with ratio tests. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import cv2

bf = cv2.BFMatcher(cv2.NORM_L2)
matches = bf.knnMatch(des, des2, k=2)
good = [m for m, n in matches if m.distance < 0.75 * n.distance]
print("good matches:", len(good))
```
### 4. Use homography for alignment

Target: Use homography for alignment. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import cv2

# Homography aligns matched points between two views
print("findHomography -> 3x3 transform for stitching")
```

## Practice Questions

1. What is the key idea behind "Feature Detection & Matching"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Feature Detection & Matching with analogies and real-world examples"
1. "Show me common mistakes beginners make with Feature Detection & Matching"
1. "Provide advanced patterns and performance considerations for Feature Detection & Matching"

## Key Takeaways

- Master the core ideas of Feature Detection & Matching through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
