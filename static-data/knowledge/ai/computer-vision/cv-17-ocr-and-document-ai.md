---
{
  "title": "OCR & Document AI",
  "description": "Turn images of text into machine-readable text: Tesseract, PaddleOCR, and layout understanding.",
  "type": "lesson",
  "order": 17,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain the OCR pipeline",
    "Run Tesseract via pytesseract",
    "Handle document layout and tables",
    "Pair OCR with downstream NLP"
  ],
  "knowledge_refs": [
    "computer-vision/cv-17-ocr-and-document-ai"
  ],
  "prerequisites": [
    "CV-03: Image Processing Fundamentals"
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

# CV-17-OCR-AND-DOCUMENT-AI: OCR & Document AI

## Introduction

Turn images of text into machine-readable text: Tesseract, PaddleOCR, and layout understanding. By the end of this lesson you will be able to: Explain the OCR pipeline; Run Tesseract via pytesseract; Handle document layout and tables; Pair OCR with downstream NLP.

## Key Concepts

### 1. Explain the OCR pipeline

Target: Explain the OCR pipeline. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import pytesseract
from PIL import Image

text = pytesseract.image_to_string(Image.open("receipt.png"))
print(text[:200])
```
### 2. Run Tesseract via pytesseract

Target: Run Tesseract via pytesseract. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import pytesseract

data = pytesseract.image_to_data(Image.open("page.png"), output_type=pytesseract.Output.DICT)
print("words:", len(data["text"]))
```
### 3. Handle document layout and tables

Target: Handle document layout and tables. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import cv2

# Preprocessing helps OCR: grayscale + threshold
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print("otsu threshold applied")
```
### 4. Pair OCR with downstream NLP

Target: Pair OCR with downstream NLP. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import pytesseract

print("OCR -> structured fields via regex or NLP")
```

## Practice Questions

1. What is the key idea behind "OCR & Document AI"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain OCR & Document AI with analogies and real-world examples"
1. "Show me common mistakes beginners make with OCR & Document AI"
1. "Provide advanced patterns and performance considerations for OCR & Document AI"

## Key Takeaways

- Master the core ideas of OCR & Document AI through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
