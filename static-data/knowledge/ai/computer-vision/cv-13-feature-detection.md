---
slug: cv-13-feature-detection
title: "Feature Detection & Matching"
description: "Finding and matching interesting points across images — SIFT, ORB, and their applications in stitching and tracking."
order: 13
tags:
  - computer-vision
  - feature-detection
  - sift
  - orb
  - feature-matching
prerequisites:
  - cv-12-opencv-fundamentals
  - cv-03-image-processing
  - cv-02-image-representation
references:
  - title: "OpenCV Feature Detection Tutorial"
    url: "https://docs.opencv.org/4.x/db/d27/tutorial_py_table_of_contents_features2d.html"
    description: "Official OpenCV feature detection and description guide"
  - title: "SIFT: Distinctive Image Features from Scale-Invariant Keypoints"
    url: "https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf"
    description: "Lowe's original SIFT paper"
  - title: "ORB: An Efficient Alternative to SIFT or SURF"
    url: "https://ieeexplore.ieee.org/document/6126544"
    description: "Rublee et al.'s ORB paper — fast, open-source alternative"
  - title: "Feature Matching with FLANN"
    url: "https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html"
    description: "OpenCV's FLANN-based matcher tutorial"
  - title: "LearnOpenCV: Feature Detection"
    url: "https://learnopencv.com/feature-detection-and-description/"
    description: "Practical guide to feature detection in OpenCV"
knowledge_refs:
  - cv-12-opencv-fundamentals
  - cv-03-image-processing
  - cv-14-image-registration-and-stitching
---

# Feature Detection & Matching

Feature detection finds "interesting" points in images (corners, edges, blobs) that can be reliably found across different views. Feature matching connects these points between images.

## Why Features Matter

- **Image stitching**: Align overlapping images
- **Object recognition**: Match query to database images
- **Motion tracking**: Follow points across video frames
- **3D reconstruction**: Estimate camera poses
- **Augmented reality**: Track real-world features

## Feature Detection Algorithms

### SIFT (Scale-Invariant Feature Transform)
- **Detector + Descriptor**: Finds keypoints and describes them
- **Invariant**: To scale, rotation, illumination
- **Patent expired** (2020): Now freely usable

```python
sift = cv2.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(gray, None)

# Draw keypoints
img_with_kp = cv2.drawKeypoints(img, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
```

### ORB (Oriented FAST and Rotated BRIEF)
- **Fast**: ~100x faster than SIFT
- **Open-source**: No patent issues
- **Binary descriptor**: Hamming distance for matching

```python
orb = cv2.ORB_create(nfeatures=1000)
keypoints, descriptors = orb.detectAndCompute(gray, None)
```

### Feature Comparison

| Algorithm | Speed | Accuracy | Descriptor | Patent |
|---|---|---|---|---|
| SIFT | Slow | Excellent | 128-d float | Expired |
| SURF | Medium | Very good | 64-d float | Patent |
| ORB | Very fast | Good | 256-bit binary | Open |
| AKAZE | Fast | Very good | Binary | Open |

## Feature Matching

### Brute-Force Matcher
```python
# For binary descriptors (ORB)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(desc1, desc2)

# Sort by distance
matches = sorted(matches, key=lambda x: x.distance)

# Draw top matches
result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
```

### FLANN Matcher
Faster for large-scale matching:
```python
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(desc1, desc2, k=2)

# Lowe's ratio test
good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)
```

### Ratio Test (Lowe's Test)
Keep only matches where the best match is significantly better than the second best:
```python
good = [m for m, n in matches if m.distance < 0.75 * n.distance]
```

## Applications

### Homography Estimation
Find the transformation between two images:
```python
src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
# H is the 3×3 homography matrix
```

### Image Alignment
```python
# Warp image to match reference
aligned = cv2.warpPerspective(img1, H, (img2.shape[1], img2.shape[0]))
```

## Practical Tips

1. **Use SIFT** for accuracy, ORB for speed
2. **Always use ratio test** to filter false matches
3. **RANSAC** for robust homography estimation
4. **Resize images** before detection for speed
5. **Good features to track**: For simple corner detection:
```python
corners = cv2.goodFeaturesToTrack(gray, maxCorners=100, qualityLevel=0.01, minDistance=10)
```

## Further Reading

- Lowe's SIFT paper is foundational
- ORB is the practical choice for real-time applications
- OpenCV's feature matching tutorial covers FLANN in depth
- For deep learning features: SuperPoint and SuperGlue replace hand-crafted features
