---
{
  "title": "Face Detection & Recognition",
  "description": "Detect faces, embed them into vectors, and recognize identity — and respect the ethics of it.",
  "type": "lesson",
  "order": 16,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Detect faces with cascades or deep detectors",
    "Explain face embeddings",
    "Compare identities with cosine similarity",
    "Discuss privacy and bias considerations"
  ],
  "knowledge_refs": [
    "computer-vision/cv-15-video-analysis",
    "nlp/nlp-09-named-entity-recognition",
    "mlops/mlops-14-monitoring-and-drift"
  ],
  "prerequisites": [
    "CV-07: Transfer Learning for Vision"
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

# CV-16-FACE-RECOGNITION: Face Detection & Recognition

## Introduction

Detect faces, embed them into vectors, and recognize identity — and respect the ethics of it. By the end of this lesson you will be able to: Detect faces with cascades or deep detectors; Explain face embeddings; Compare identities with cosine similarity; Discuss privacy and bias considerations.

## Key Concepts

### 1. Detect faces with cascades or deep detectors

Target: Detect faces with cascades or deep detectors. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import cv2

cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
print("faces found:", len(faces))
```
### 2. Explain face embeddings

Target: Explain face embeddings. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

a = np.array([1.0, 0.0])
b = np.array([0.95, 0.05])
print("similarity:", round(cosine_sim(a, b), 3))
```
### 3. Compare identities with cosine similarity

Target: Compare identities with cosine similarity. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import torch

# Face embedding: model outputs a fixed-size vector per face
embedding = torch.randn(512)
print("embedding dim:", embedding.shape)
```
### 4. Discuss privacy and bias considerations

Target: Discuss privacy and bias considerations. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
ethics = ["consent", "bias across demographics", "surveillance risk", "retention limits"]
for e in ethics:
    print(f"- {e}")
```

## Practice Questions

1. What is the key idea behind "Face Detection & Recognition"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Face Detection & Recognition with analogies and real-world examples"
1. "Show me common mistakes beginners make with Face Detection & Recognition"
1. "Provide advanced patterns and performance considerations for Face Detection & Recognition"

## Key Takeaways

- Master the core ideas of Face Detection & Recognition through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
