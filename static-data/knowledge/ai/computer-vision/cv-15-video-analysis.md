---
slug: cv-15-video-analysis
title: "Video Analysis & Tracking"
description: "Processing video streams — object tracking, action recognition, and real-time video analysis with OpenCV."
order: 15
tags:
  - computer-vision
  - video
  - tracking
  - action-recognition
  - optical-flow
prerequisites:
  - cv-08-object-detection
  - cv-11-pose-estimation
  - cv-12-opencv-fundamentals
references:
  - title: "OpenCV Video Analysis"
    url: "https://docs.opencv.org/4.x/d4/d27/tutorial_py_video_background_subtraction.html"
    description: "Official OpenCV video processing tutorials"
  - title: "DeepSORT: Simple Online and Realtime Tracking"
    url: "https://arxiv.org/abs/1703.07402"
    description: "Wojke et al.'s DeepSORT multi-object tracker"
  - title: "ByteTrack: Multi-Object Tracking by Associating Every Detection"
    url: "https://arxiv.org/abs/2110.02033"
    description: "Zhang et al.'s ByteTrack for robust MOT"
  - title: "MediaPipe Holistic"
    url: "https://ai.google.dev/edge/mediapipe/solutions/vision/holistic_landmarker"
    description: "Google's combined face, pose, and hand landmark detection"
  - title: "PyPose: Pose Estimation Library"
    url: "https://pypose.org/"
    description: "PyTorch-based library for pose estimation and tracking"
knowledge_refs:
  - cv-08-object-detection
  - cv-11-pose-estimation
  - cv-12-opencv-fundamentals
---

# Video Analysis & Tracking

Video analysis extends single-image CV to temporal sequences — tracking objects across frames, recognizing actions, and understanding motion.

## Reading Video with OpenCV

```python
import cv2

cap = cv2.VideoCapture("video.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Process frame
    processed = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Display
    cv2.imshow("Video", processed)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

## Object Tracking

### Detection + Tracking Pipeline
```
Frame → Detector → Bounding Boxes → Tracker → Tracked IDs
```

### DeepSORT
Multi-object tracking with deep appearance features:
```python
from deep_sort_realtime.deepsort_tracker import DeepSort

tracker = DeepSort(max_age=30, n_init=3)

while True:
    ret, frame = cap.read()
    
    # Detect objects
    detections = detector(frame)
    
    # Update tracker
    tracks = tracker.update_tracks(detections, frame=frame)
    
    for track in tracks:
        if track.is_confirmed():
            bbox = track.to_ltrb()
            track_id = track.track_id
            cv2.rectangle(frame, (int(bbox[0]), int(bbox[1])), 
                         (int(bbox[2]), int(bbox[3])), (0, 255, 0), 2)
            cv2.putText(frame, f"ID: {track_id}", 
                       (int(bbox[0]), int(bbox[1])-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
```

## Optical Flow

Tracks pixel motion between frames:

### Lucas-Kanade (Sparse)
Track specific features:
```python
# Parameters for Shi-Tomasi corner detection
feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7)
lk_params = dict(winSize=(15, 15), maxLevel=2,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Detect features to track
old_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

# Track features
new_gray = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)
p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, new_gray, p0, None, **lk_params)
```

### Farneback (Dense)
Compute flow for every pixel:
```python
flow = cv2.calcOpticalFlowFarneback(prev_gray, curr_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
```

## Action Recognition

### Two-Stream Networks
- **Spatial stream**: Single frame classification
- **Temporal stream**: Optical flow classification
- **Fusion**: Combine both streams

### 3D CNNs
Process video directly as spatio-temporal volumes:
```python
# SlowFast Networks
# Slow pathway: low frame rate, high resolution
# Fast pathway: high frame rate, low resolution
```

### Video Transformers
- TimeSformer: Divided space-time attention
- ViViT: Video Vision Transformer

## Background Subtraction

Detect moving objects by modeling background:
```python
bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50)

while True:
    ret, frame = cap.read()
    mask = bg_subtractor.apply(frame)
    cv2.imshow("Background Subtraction", mask)
```

## Practical Tips

1. **Use YOLO + DeepSORT** for real-time multi-object tracking
2. **Process every Nth frame** for speed (reduce frame rate)
3. **Resize frames** before detection
4. **Use GPU** for real-time processing
5. **Temporal smoothing** prevents ID switching

## Further Reading

- OpenCV video tutorials cover basic video I/O
- DeepSORT is the standard for multi-object tracking
- ByteTrack improved MOT by using every detection
- For action recognition: SlowFast and TimeSformer are state-of-the-art
