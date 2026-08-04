---
slug: cv-11-pose-estimation
title: "Pose Estimation"
description: "Detecting human body keypoints — from OpenPose to MediaPipe and modern bottom-up approaches."
order: 11
tags:
  - computer-vision
  - pose-estimation
  - keypoints
  - openpose
  - mediapipe
prerequisites:
  - cv-06-cnns-for-vision
  - cv-08-object-detection
  - dl-12-convolutional-networks
references:
  - title: "OpenPose: Realtime Multi-Person 2D Pose Estimation"
    url: "https://arxiv.org/abs/1812.08008"
    description: "Cao et al.'s OpenPose paper for multi-person pose estimation"
  - title: "MediaPipe Pose"
    url: "https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker"
    description: "Google's MediaPipe for real-time pose detection"
  - title: "HRNet: Deep High-Resolution Representation Learning"
    url: "https://arxiv.org/abs/1902.09212"
    description: "Sun et al.'s HRNet for high-resolution pose estimation"
  - title: "Bottom-Up Person Pose Estimation"
    url: "https://arxiv.org/abs/2103.14012"
    description: "VPose and bottom-up approaches to pose estimation"
  - title: "Torchvision Keypoint R-CNN"
    url: "https://pytorch.org/vision/main/models/keypoint_rcnn.html"
    description: "PyTorch's built-in keypoint detection model"
knowledge_refs:
  - cv-08-object-detection
  - cv-06-cnns-for-vision
  - cv-16-face-recognition
---

# Pose Estimation

Pose estimation detects body keypoints (joints) — shoulders, elbows, wrists, hips, knees, ankles — enabling human action understanding, animation, and activity recognition.

## Keypoint Detection

Typical human pose = 17 keypoints (COCO format):
```
0: nose, 1: left_eye, 2: right_eye, 3: left_ear, 4: right_ear,
5: left_shoulder, 6: right_shoulder, 7: left_elbow, 8: right_elbow,
9: left_wrist, 10: right_wrist, 11: left_hip, 12: right_hip,
13: left_knee, 14: right_knee, 15: left_ankle, 16: right_ankle
```

## Two Approaches

### Top-Down
1. Detect person bounding boxes (object detector)
2. Crop each person
3. Estimate keypoints per crop

**Pros**: Higher accuracy per person. **Cons**: Slower, depends on detector.

### Bottom-Up
1. Detect ALL keypoints in the image
2. Group them into individual people

**Pros**: Faster for many people. **Cons**: Harder to group correctly.

## MediaPipe Pose (Practical)

Real-time, lightweight pose estimation:
```python
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, model_complexity=1)

# Process frame
results = pose.process(frame_rgb)

# Access keypoints
for landmark in results.pose_landmarks.landmark:
    print(f"Keypoint: {landmark.x}, {landmark.y}, {landmark.z}, visibility: {landmark.visibility}")
```

## PyTorch Keypoint R-CNN

```python
import torchvision
from torchvision.models.detection import keypointrcnn_resnet50_fpn

model = keypointrcnn_resnet50_fpn(pretrained=True)
model.eval()

predictions = model([image_tensor])
# predictions[i]['keypoints'] — (N, 17, 3) — x, y, visibility
# predictions[i]['keypoints_scores'] — (N, 17) — confidence
```

## Applications

| Application | How Pose Helps |
|---|---|
| **Fitness tracking** | Count reps, check form |
| **Sports analysis** | Technique improvement |
| **Animation** | Motion capture for games/movies |
| **Healthcare** | Physical therapy monitoring |
| **AR/VR** | Virtual avatars |
| **Surveillance** | Activity recognition |
| **Driver monitoring** | Drowsiness detection |

## Evaluation Metrics

- **PCK (Percentage of Correct Keypoints)**: Keypoint within threshold of ground truth
- **mAP (COCO-style)**: AP at various OKS (Object Keypoint Similarity) thresholds
- **OKS**: Similar to IoU but for keypoints, accounting for object scale

## Practical Tips

1. **Use MediaPipe** for real-time applications
2. **Use HRNet** for highest accuracy
3. **Multi-person**: Use bottom-up for crowds, top-down for accuracy
4. **Temporal smoothing**: Smooth keypoints across frames for video
5. **Confidence thresholding**: Filter low-confidence keypoints

## Further Reading

- OpenPose pioneered real-time multi-person pose estimation
- MediaPipe is the practical choice for production apps
- HRNet achieved state-of-the-art on COCO keypoints
- For 3D pose: look into VideoPose3D and MotionBERT
