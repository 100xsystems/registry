---
{
  "title": "Video Analysis & Tracking",
  "description": "Optical flow, frame differencing, and object tracking across video streams.",
  "type": "lesson",
  "order": 15,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Compute optical flow between frames",
    "Detect motion with background subtraction",
    "Track objects with trackers",
    "Process video frames in a loop"
  ],
  "knowledge_refs": [
    "computer-vision/cv-15-video-analysis"
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

# CV-15-VIDEO-ANALYSIS: Video Analysis & Tracking

## Introduction

Optical flow, frame differencing, and object tracking across video streams. By the end of this lesson you will be able to: Compute optical flow between frames; Detect motion with background subtraction; Track objects with trackers; Process video frames in a loop.

## Key Concepts

### 1. Compute optical flow between frames

Target: Compute optical flow between frames. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import cv2

cap = cv2.VideoCapture(0)
ok, frame = cap.read()
print("frame:", frame.shape if ok else None)
```
### 2. Detect motion with background subtraction

Target: Detect motion with background subtraction. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import cv2

# Sparse optical flow (Lucas-Kanade)
flow = cv2.calcOpticalFlowFarneback(prev, cur, None, 0.5, 3, 15, 3, 5, 1.2, 0)
print("dense flow:", flow.shape)
```
### 3. Track objects with trackers

Target: Track objects with trackers. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import cv2

subtractor = cv2.createBackgroundSubtractorMOG2()
fg = subtractor.apply(frame)
print("foreground mask unique:", set(fg.flatten().tolist()))
```
### 4. Process video frames in a loop

Target: Process video frames in a loop. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import cv2

tracker = cv2.TrackerKCF_create()
print("tracker initialized; update per frame")
```

## Practice Questions

1. What is the key idea behind "Video Analysis & Tracking"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Video Analysis & Tracking with analogies and real-world examples"
1. "Show me common mistakes beginners make with Video Analysis & Tracking"
1. "Provide advanced patterns and performance considerations for Video Analysis & Tracking"

## Key Takeaways

- Master the core ideas of Video Analysis & Tracking through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
