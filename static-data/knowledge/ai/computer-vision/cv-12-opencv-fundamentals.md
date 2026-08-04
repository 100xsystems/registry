---
slug: cv-12-opencv-fundamentals
title: "OpenCV Fundamentals"
description: "The essential computer vision library — image I/O, drawing, color conversion, and basic operations."
order: 12
tags:
  - computer-vision
  - opencv
  - image-io
  - drawing
  - color-conversion
prerequisites:
  - cv-02-image-representation
  - cv-03-image-processing
  - cv-01-what-is-computer-vision
references:
  - title: "OpenCV-Python Tutorials"
    url: "https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html"
    description: "Official OpenCV Python tutorials"
  - title: "LearnOpenCV"
    url: "https://learnopencv.com/"
    description: "Comprehensive OpenCV tutorials and guides"
  - title: "OpenCV Documentation"
    url: "https://docs.opencv.org/"
    description: "Official OpenCV documentation"
  - title: "PyImageSearch OpenCV Guides"
    url: "https://pyimagesearch.com/opencv-tutorials-guides/"
    description: "Adrian Rosebrock's practical OpenCV tutorials"
  - title: "OpenCV GitHub"
    url: "https://github.com/opencv/opencv"
    description: "OpenCV source code and examples"
knowledge_refs:
  - cv-02-image-representation
  - cv-03-image-processing
  - cv-01-what-is-computer-vision
---

# OpenCV Fundamentals

OpenCV (Open Source Computer Vision Library) is the most widely-used CV library. Understanding its core operations is essential for any computer vision practitioner.

## Image I/O

```python
import cv2
import numpy as np

# Read image (BGR format!)
img = cv2.imread("photo.jpg")
img = cv2.imread("photo.jpg", cv2.IMREAD_GRAYSCALE)  # Grayscale

# Write image
cv2.imwrite("output.jpg", img)

# Display image
cv2.imshow("Window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

**Critical**: OpenCV reads images in **BGR** format, not RGB. Convert before using with Matplotlib/PIL:
```python
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

## Drawing Functions

```python
# Create blank image
canvas = np.zeros((512, 512, 3), dtype=np.uint8)

# Line
cv2.line(canvas, (0, 0), (511, 511), (0, 255, 0), 3)

# Rectangle
cv2.rectangle(canvas, (50, 50), (200, 200), (255, 0, 0), 2)

# Circle
cv2.circle(canvas, (300, 300), 50, (0, 0, 255), -1)  # -1 = filled

# Put text
cv2.putText(canvas, "OpenCV", (100, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
```

## Color Conversion

```python
# BGR to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# BGR to RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# All conversion codes: cv2.COLOR_<src>2<dst>
# Common: BGR2GRAY, BGR2HSV, BGR2RGB, GRAY2BGR
```

## Image Transformations

```python
# Resize
resized = cv2.resize(img, (224, 224))
resized = cv2.resize(img, None, fx=0.5, fy=0.5)  # Scale by 0.5

# Rotate
M = cv2.getRotationMatrix2D(center=(cols/2, rows/2), angle=45, scale=1)
rotated = cv2.warpAffine(img, M, (cols, rows))

# Translate
M = np.float32([[1, 0, 50], [0, 1, 100]])  # Shift right 50, down 100
translated = cv2.warpAffine(img, M, (cols, rows))

# Flip
flipped_h = cv2.flip(img, 1)  # Horizontal
flipped_v = cv2.flip(img, 0)  # Vertical
```

## ROI (Region of Interest)

```python
# Crop region
roi = img[100:300, 200:400]  # [y1:y2, x1:x2]

# Paste region elsewhere
img[50:250, 100:300] = roi
```

## Image Arithmetic

```python
# Add images (with saturation)
blended = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

# Bitwise operations (for masks)
mask = cv2.imread("mask.png", 0)
result = cv2.bitwise_and(img, img, mask=mask)
result = cv2.bitwise_or(img, img, mask=mask)
result = cv2.bitwise_not(img)
```

## Common Gotchas

| Issue | Solution |
|---|---|
| Wrong colors | Convert BGR→RGB for display |
| Can't show image | Add `cv2.waitKey(0)` |
| Image too large | Resize before display |
| Grayscale shape | Use `(H, W)` not `(H, W, 1)` |
| Write fails | Check path exists |

## Practical Pipeline

```python
def process_image(path):
    # Read
    img = cv2.imread(path)
    
    # Convert to RGB for processing
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Resize
    resized = cv2.resize(gray, (224, 224))
    
    # Normalize
    normalized = resized.astype(np.float32) / 255.0
    
    return normalized
```

## Further Reading

- OpenCV official tutorials are comprehensive
- LearnOpenCV provides practical guides
- PyImageSearch is excellent for beginners
- For deep learning with OpenCV: use DNN module for inference
