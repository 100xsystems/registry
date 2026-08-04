---
slug: cv-03-image-processing
title: "Image Processing Fundamentals"
description: "The classical foundations — filtering, edge detection, morphology, histograms, and thresholding with OpenCV."
order: 3
tags:
  - computer-vision
  - image-processing
  - opencv
  - filtering
  - edge-detection
prerequisites:
  - cv-02-image-representation
  - cv-01-what-is-computer-vision
references:
  - title: "OpenCV Edge Detection Tutorial"
    url: "https://opencv.org/edge-detection-using-opencv/"
    description: "Official OpenCV guide to edge detection algorithms"
  - title: "OpenCV Image Thresholding Tutorial"
    url: "https://opencv.org/image-thresholding-using-opencv/"
    description: "Official OpenCV guide to thresholding methods"
  - title: "OpenCV Histogram Equalization"
    url: "https://docs.opencv.org/3.4.20/d4/d1b/tutorial_histogram_equalization.html"
    description: "Official OpenCV tutorial on histogram equalization"
  - title: "Morphological Operations in Image Processing (GeeksforGeeks)"
    url: "https://www.geeksforgeeks.org/computer-vision/different-morphological-operations-in-image-processing/"
    description: "Comprehensive guide to morphological operations"
  - title: "LearnOpenCV: Image Filtering"
    url: "https://learnopencv.com/image-filtering/"
    description: "Practical guide to convolution and filtering"
knowledge_refs:
  - cv-02-image-representation
  - dl-12-convolutional-networks
  - cv-05-image-classification
---

# Image Processing Fundamentals

Before deep learning, classical image processing provided the tools to manipulate and analyze images. These fundamentals remain essential for preprocessing, debugging, and understanding how visual information is transformed.

## Image Filtering & Convolution

Filtering modifies pixel values based on local neighborhoods using a **kernel** (small matrix):

```python
import cv2
import numpy as np

# Load image
img = cv2.imread("photo.jpg", cv2.IMREAD_GRAYSCALE)

# Gaussian blur (smoothing)
blurred = cv2.GaussianBlur(img, (5, 5), sigmaX=1.5)

# Mean blur
mean_blur = cv2.blur(img, (5, 5))

# Median blur (preserves edges better)
median_blur = cv2.medianBlur(img, 5)

# Custom kernel (sharpening)
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
sharpened = cv2.filter2D(img, -1, kernel)
```

### Common Filters

| Filter | Purpose | Kernel Example |
|---|---|---|
| **Gaussian** | Smooth, reduce noise | $\frac{1}{16}\begin{bmatrix}1&2&1\\2&4&2\\1&2&1\end{bmatrix}$ |
| **Mean** | Simple smoothing | $\frac{1}{9}\begin{bmatrix}1&1&1\\1&1&1\\1&1&1\end{bmatrix}$ |
| **Median** | Salt-and-pepper noise | Median of neighborhood |
| **Laplacian** | Edge detection | $\begin{bmatrix}0&1&0\\1&-4&1\\0&1&0\end{bmatrix}$ |
| **Sharpen** | Enhance edges | $\begin{bmatrix}0&-1&0\\-1&5&-1\\0&-1&0\end{bmatrix}$ |

## Edge Detection

Edges are boundaries where intensity changes abruptly.

### Sobel Operator
Computes horizontal and vertical gradients:
```python
# Sobel gradients
grad_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Gradient magnitude
magnitude = np.sqrt(grad_x**2 + grad_y**2)
```

### Canny Edge Detection
The gold standard — multi-stage algorithm:
```python
# Canny: automatic threshold selection
edges = cv2.Canny(img, threshold1=100, threshold2=200)
```

**Canny pipeline:**
1. Gaussian smoothing (reduce noise)
2. Gradient computation (Sobel)
3. Non-maximum suppression (thin edges)
4. Hysteresis thresholding (connect edges)

### Laplacian
Second-order derivative — detects rapid intensity changes:
```python
laplacian = cv2.Laplacian(img, cv2.CV_64F)
```

## Morphological Operations

Non-linear operations that process image shapes using a **structuring element**:

```python
# Binary image
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Define kernel
kernel = np.ones((5, 5), np.uint8)

# Erosion: shrink bright regions
eroded = cv2.erode(binary, kernel, iterations=1)

# Dilation: expand bright regions
dilated = cv2.dilate(binary, kernel, iterations=1)

# Opening: erosion → dilation (remove noise)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

# Closing: dilation → erosion (fill holes)
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

# Gradient: dilation - erosion (edge detection)
gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)
```

| Operation | Effect | Use Case |
|---|---|---|
| Erosion | Shrink bright regions | Remove small noise |
| Dilation | Expand bright regions | Fill small holes |
| Opening | Remove small bright spots | Noise removal |
| Closing | Fill small dark holes | Gap filling |

## Image Histograms

A histogram shows the distribution of pixel intensities:

```python
import matplotlib.pyplot as plt

# Compute histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Plot
plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.subplot(122)
plt.plot(hist)
plt.title('Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()
```

### Histogram Equalization
Improves contrast by flattening the intensity distribution:
```python
# Global equalization
equalized = cv2.equalizeHist(img)

# CLAHE (adaptive, prevents noise amplification)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_equalized = clahe.apply(img)
```

## Thresholding

Converts grayscale to binary:
```python
# Simple thresholding
_, thresh_binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Otsu's: automatically find optimal threshold
_, thresh_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Adaptive thresholding (handles uneven lighting)
thresh_adaptive = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, blockSize=11, C=2
)
```

| Method | Best For |
|---|---|
| **Global threshold** | Even lighting, clear separation |
| **Otsu's** | Bimodal distribution |
| **Adaptive** | Uneven lighting, varying contrast |

## Practical Pipeline

```python
def preprocess_image(image_path):
    # 1. Load
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # 2. Noise reduction
    denoised = cv2.GaussianBlur(img, (5, 5), 1.5)
    
    # 3. Contrast enhancement
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(denoised)
    
    # 4. Thresholding
    _, binary = cv2.threshold(enhanced, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # 5. Morphological cleanup
    kernel = np.ones((3, 3), np.uint8)
    cleaned = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    
    return cleaned
```

## When to Use Classical vs. Deep Learning

| Use Case | Classical | Deep Learning |
|---|---|---|
| Simple thresholding | ✅ Fast, interpretable | Overkill |
| Barcode reading | ✅ Proven methods | Possible but unnecessary |
| Noise reduction | ✅ Gaussian/median blur | Learned filters (DnCNN) |
| Edge detection | ✅ Canny for simple cases | Learned edges (HED) |
| Complex recognition | ❌ Limited | ✅ CNNs excel |
| Scene understanding | ❌ Not possible | ✅ Deep models |

## Further Reading

- OpenCV's edge detection tutorial covers Canny in depth
- Morphological operations are essential for binary image processing
- CLAHE is a must-know for contrast enhancement
- Classical preprocessing often helps deep learning models
