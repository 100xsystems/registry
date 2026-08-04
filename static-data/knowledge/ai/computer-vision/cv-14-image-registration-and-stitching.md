---
slug: cv-14-image-registration-and-stitching
title: "Image Registration & Stitching"
description: "Aligning and combining multiple images into panoramas — homography, RANSAC, and seamless blending."
order: 14
tags:
  - computer-vision
  - registration
  - stitching
  - panorama
  - homography
prerequisites:
  - cv-13-feature-detection
  - cv-12-opencv-fundamentals
  - cv-03-image-processing
references:
  - title: "OpenCV Panorama Stitching Tutorial"
    url: "https://docs.opencv.org/4.x/da/d1b/tutorial_stitching.html"
    description: "Official OpenCV stitching tutorial"
  - title: "Image Stitching with OpenCV and Python"
    url: "https://pyimagesearch.com/2016/01/11/panorama-with-opencv/"
    description: "PyImageSearch's practical panorama guide"
  - title: "Automatic Panoramic Image Stitching (Brown & Lowe)"
    url: "https://ieeexplore.ieee.org/document/4154845"
    description: "Brown & Lowe's influential panorama stitching paper"
  - title: "OpenCV Stitcher API"
    url: "https://docs.opencv.org/4.x/d3/dfe/classcv_1_1Stitcher.html"
    description: "OpenCV's built-in stitcher class"
  - title: "Image Registration Survey"
    url: "https://ieeexplore.ieee.org/document/5201548"
    description: "Zitová and Flusser's survey of image registration methods"
knowledge_refs:
  - cv-13-feature-detection
  - cv-12-opencv-fundamentals
  - cv-03-image-processing
---

# Image Registration & Stitching

Image registration aligns multiple images of the same scene. Image stitching combines aligned images into a panorama or larger field of view.

## The Stitching Pipeline

```
Input: Multiple overlapping images
    ↓
[Feature Detection] → Find keypoints in each image
    ↓
[Feature Matching] → Match keypoints between image pairs
    ↓
[Homography Estimation] → Find transformation between pairs
    ↓
[Warping] → Transform images to common coordinate system
    ↓
[Blending] → Seamlessly combine warped images
    ↓
Output: Panorama / stitched image
```

## Homography

A 3×3 matrix that maps points from one image to another:
$$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = H \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$$

```python
import cv2
import numpy as np

# Detect features
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# Match features
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# Ratio test
good = [m for m, n in matches if m.distance < 0.75 * n.distance]

# Extract matched points
src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

# Find homography with RANSAC
H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
```

## RANSAC (Random Sample Consensus)

Robustly estimates homography despite outlier matches:
1. Randomly select 4 point correspondences
2. Compute homography from these 4 points
3. Count inliers (points consistent with H)
4. Repeat N times, keep best H

```python
H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
# mask indicates which points are inliers
inliers = mask.ravel().sum()
print(f"Inliers: {inliers}/{len(good)}")
```

## Warping and Stitching

### Manual Approach
```python
# Warp img1 to img2's perspective
h1, w1 = img1.shape[:2]
h2, w2 = img2.shape[:2]

# Warp img1
warped1 = cv2.warpPerspective(img1, H, (w1 + w2, max(h1, h2)))

# Place img2 in the panorama
warped1[0:h2, 0:w2] = img2
```

### OpenCV Stitcher (Automatic)
```python
stitcher = cv2.Stitcher.create(cv2.Stitcher_PANORAMA)
status, panorama = stitcher.stitch([img1, img2, img3])

if status == cv2.Stitcher_OK:
    cv2.imwrite("panorama.jpg", panorama)
else:
    print(f"Stitching failed: {status}")
```

## Blending Techniques

### Direct Copy
Simple but creates visible seams.

### Alpha Blending
```python
# Smooth transition in overlap region
alpha = np.linspace(0, 1, overlap_width).reshape(1, -1, 1)
blended = alpha * warped1 + (1 - alpha) * warped2
```

### Multi-Band Blending (Laplacian Pyramid)
Seamlessly blends at multiple scales — the gold standard.

## Applications

| Application | Description |
|---|---|
| **Panoramas** | Combine photos into wide-angle views |
| **Medical imaging** | Align MRI/CT slices |
| **Satellite imagery** | Mosaic large areas |
| **360° video** | Stitch fisheye camera outputs |
| **Document scanning** | Auto-crop and flatten |
| **Multi-focus** | Combine images with different focus |

## Common Issues

1. **Parallax**: Objects move relative to background — use multi-band blending
2. **Exposure differences**: Use exposure compensation before blending
3. **Moving objects**: Ghosting artifacts — detect and remove
4. **Lens distortion**: Calibrate camera first

## Practical Tips

1. **Use OpenCV Stitcher** for quick panoramas
2. **Overlap ≥ 30%**: Enough features for reliable matching
3. **Sort images**: Provide images in left-to-right order
4. **Use SIFT** for best feature matching
5. **Check inlier count**: Low inliers = bad matching

## Further Reading

- OpenCV's stitching tutorial covers the full pipeline
- Brown & Lowe's paper is the foundational panorama stitching work
- PyImageSearch provides practical step-by-step guides
- For video stabilization: similar techniques with temporal consistency
