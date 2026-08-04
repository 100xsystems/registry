---
slug: cv-16-face-recognition
title: "Face Detection & Recognition"
description: "Detecting, analyzing, and recognizing faces — from Haar cascades to deep learning-based face recognition."
order: 16
tags:
  - computer-vision
  - face-detection
  - face-recognition
  - facial-analysis
  - arcface
prerequisites:
  - cv-06-cnns-for-vision
  - cv-08-object-detection
  - cv-02-image-representation
references:
  - title: "FaceNet: A Unified Embedding for Face Recognition"
    url: "https://arxiv.org/abs/1503.03832"
    description: "Google's FaceNet paper using triplet loss for face recognition"
  - title: "ArcFace: Additive Angular Margin Loss"
    url: "https://arxiv.org/abs/1801.07698"
    description: "Deng et al.'s ArcFace paper for state-of-the-art face recognition"
  - title: "OpenCV Face Detection"
    url: "https://docs.opencv.org/4.x/db/d28/tutorial_cascade_classifier.html"
    description: "Official OpenCV face detection tutorial"
  - title: "face_recognition Library"
    url: "https://github.com/ageitgey/face_recognition"
    description: "Simple face recognition library using dlib"
  - title: "InsightFace"
    url: "https://github.com/deepinsight/insightface"
    description: "State-of-the-art face analysis toolkit"
knowledge_refs:
  - cv-08-object-detection
  - cv-06-cnns-for-vision
  - cv-11-pose-estimation
---

# Face Detection & Recognition

Face detection locates faces in images. Face recognition identifies who the face belongs to. Face analysis extracts attributes (age, expression, landmarks).

## Face Detection

### Haar Cascades (Classical)
Fast but less accurate:
```python
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
```

### MTCNN (Deep Learning)
Multi-task Cascaded CNN — detects faces + landmarks:
```python
from mtcnn import MTCNN

detector = MTCNN()
results = detector.detect_faces(img)
for face in results:
    bbox = face['box']
    landmarks = face['keypoints']
```

### RetinaFace
State-of-the-art face detector:
```python
from retinaface import RetinaFace
faces = RetinaFace.detect_faces(img)
```

## Face Recognition Pipeline

```
Input Image → Face Detection → Face Alignment → Embedding → Matching
```

### Step 1: Face Detection
Locate face bounding box.

### Step 2: Face Alignment
Align face using landmarks (eyes, nose, mouth):
```python
# Align face based on eye positions
def align_face(img, left_eye, right_eye):
    # Compute angle between eyes
    dy = right_eye[1] - left_eye[1]
    dx = right_eye[0] - left_eye[0]
    angle = np.degrees(np.arctan2(dy, dx))
    
    # Rotate to align eyes horizontally
    center = ((left_eye[0] + right_eye[0]) // 2,
              (left_eye[1] + right_eye[1]) // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    aligned = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return aligned
```

### Step 3: Embedding
Convert face to a fixed-size embedding vector:
```python
import face_recognition

# Get face encoding
face_image = face_recognition.load_image_file("person.jpg")
face_encoding = face_recognition.face_encodings(face_image)[0]
# Returns 128-d vector
```

### Step 4: Matching
Compare embeddings using distance metrics:
```python
# Compare two faces
distance = face_recognition.face_distance([known_encoding], unknown_encoding)
if distance < 0.6:
    print("Match!")
```

## FaceNet and ArcFace

### FaceNet (Google)
- Triplet loss: anchor, positive, negative
- Maps faces to 128-d embedding space
- Same person → close embeddings; different → far

### ArcFace
- Additive angular margin loss
- State-of-the-art accuracy on LFW, MegaFace
- Used in most modern face recognition systems

## Face Analysis

### Facial Landmarks
```python
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

results = face_mesh.process(frame_rgb)
# 468 face landmarks
```

### Attributes
- **Age estimation**: Predict age range
- **Expression recognition**: Happy, sad, angry, etc.
- **Gender classification**: Male/female
- **Head pose estimation**: Pitch, yaw, roll

## Practical Tips

1. **Use RetinaFace** for detection (most accurate)
2. **Use InsightFace** for recognition (state-of-the-art)
3. **Always align faces** before embedding
4. **Threshold matters**: 0.6 is standard for face_recognition
5. **GPU acceleration**: Essential for real-time face recognition

## Ethical Considerations

- **Privacy**: Face recognition raises privacy concerns
- **Bias**: Models may perform differently across demographics
- **Consent**: Always get consent before collecting face data
- **Regulation**: Many jurisdictions regulate face recognition use

## Further Reading

- FaceNet paper introduced the triplet loss paradigm
- ArcFace improved face recognition with angular margins
- InsightFace provides state-of-the-art implementations
- face_recognition library is the easiest to use
