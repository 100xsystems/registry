---
slug: cv-21-roadmap
title: "Computer Vision Roadmap"
description: "Where to go after this course — specializing in detection, segmentation, generative vision, or 3D understanding."
order: 21
tags:
  - computer-vision
  - roadmap
  - career
  - learning-path
prerequisites:
  - cv-20-evaluating-vision-models
  - cv-19-vision-transformers
references:
  - title: "CS231n: Deep Learning for Computer Vision"
    url: "https://cs231n.stanford.edu/"
    description: "Stanford's foundational CV course"
  - title: "Papers With Code: Computer Vision"
    url: "https://paperswithcode.com/area/computer-vision"
    description: "State-of-the-art results for all CV tasks"
  - title: "PyTorch Vision Documentation"
    url: "https://pytorch.org/vision/"
    description: "Official PyTorch computer vision library"
  - title: "Hugging Face Vision Models"
    url: "https://huggingface.co/models?pipeline_tag=image-classification"
    description: "Hugging Face's vision model hub"
  - title: "OpenCV Tutorials"
    url: "https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html"
    description: "Official OpenCV Python tutorials"
knowledge_refs:
  - cv-01-what-is-computer-vision
  - dl-17-transformers
  - cv-19-vision-transformers
---

# Computer Vision Roadmap

You've covered the fundamentals of computer vision — from image processing to deep learning, from classification to 3D reconstruction. This roadmap shows where to specialize.

## What You've Learned

By completing this course, you understand:
- ✅ Image fundamentals (representation, processing, augmentation)
- ✅ Classification (CNNs, transfer learning, evaluation)
- ✅ Object detection (YOLO, Faster R-CNN, mAP)
- ✅ Segmentation (semantic, instance, panoptic)
- ✅ Pose estimation and face recognition
- ✅ Classical CV (OpenCV, features, stitching)
- ✅ Video analysis and tracking
- ✅ OCR and document AI
- ✅ 3D vision (depth, NeRFs, point clouds)
- ✅ Vision Transformers (ViT, Swin)

## Specialization Tracks

### Track 1: Autonomous Driving

**Focus**: Understanding and navigating the real world.

**Key tasks:**
- 3D object detection (LiDAR + camera fusion)
- Semantic segmentation (drivable area, lanes)
- Depth estimation (monocular and stereo)
- Motion prediction (trajectory forecasting)

**Key models:**
- PointPillars, CenterPoint (3D detection)
- BEVFormer (bird's-eye view)
- UniAD (unified autonomous driving)

**Career paths**: Autonomous driving engineer, robotics perception

### Track 2: Medical Imaging

**Focus**: Analyzing medical scans for diagnosis.

**Key tasks:**
- Tumor segmentation (brain, lung, liver)
- Disease classification (X-ray, MRI, CT)
- Organ detection and measurement
- Surgical planning and navigation

**Key models:**
- U-Net and variants (segmentation)
- nnU-Net (automated segmentation)
- Medical Foundation Models (MedSAM, BiomedCLIP)

**Career paths**: Medical imaging AI engineer, healthcare AI

### Track 3: Generative Vision

**Focus**: Creating visual content with AI.

**Key tasks:**
- Image generation (diffusion models)
- Image editing (inpainting, style transfer)
- Video generation (Sora, Runway)
- 3D generation (NeRF, Gaussian Splatting)

**Key models:**
- Stable Diffusion, DALL-E 3
- ControlNet, IP-Adapter
- SVD (Stable Video Diffusion)

**Career paths**: Creative AI engineer, visual effects

### Track 4: Robotics Vision

**Focus**: Enabling robots to see and interact.

**Key tasks:**
- Grasp detection (where to pick objects)
- 6D pose estimation (object orientation)
- Scene understanding (what's where)
- Visual navigation (SLAM)

**Key models:**
- Foundation Models for robotics
- Segment Anything (SAM) for robotics
- 3D vision transformers

**Career paths**: Robotics engineer, perception engineer

### Track 5: Surveillance & Security

**Focus**: Monitoring and understanding scenes.

**Key tasks:**
- Anomaly detection
- Activity recognition
- People counting and tracking
- License plate recognition

**Career paths**: Security AI engineer, smart city engineer

## Advanced Topics to Explore

### Foundation Models
- **SAM (Segment Anything)**: Segment anything with prompts
- **DINOv2**: Self-supervised vision features
- **CLIP**: Vision-language understanding
- **Grounding DINO**: Open-vocabulary detection

### Efficient Vision
- **Model pruning**: Remove redundant parameters
- **Quantization**: INT8/INT4 inference
- **Knowledge distillation**: Train small from large
- **Neural architecture search**: AutoML for vision

### Video Understanding
- **Action recognition**: SlowFast, TimeSformer
- **Video object segmentation**: Track objects across frames
- **Video captioning**: Describe video content

## The Learning Mindset

1. **Build projects**: The best way to learn is by doing
2. **Read papers**: Follow CVPR, ICCV, ECCV proceedings
3. **Join communities**: CV Discord servers, Reddit r/computervision
4. **Contribute to open source**: MMDetection, Detectron2, torchvision
5. **Stay current**: The field evolves monthly

## Staying Current

| Source | What It Covers |
|---|---|
| **Papers With Code** | Latest research and benchmarks |
| **arXiv cs.CV** | New papers daily |
| **Twitter/X** | Real-time developments |
| **CVPR/ICCV/ECCV** | Top conferences |
| **Hugging Face** | New models and demos |

## Recommended Resources by Level

### Beginner (Start Here)
- CS231n (Stanford course)
- OpenCV tutorials (practical skills)
- PyTorch Vision tutorials (implementation)

### Intermediate
- Detectron2 / MMDetection (production detection)
- Papers With Code (track SOTA)
- Kaggle CV competitions (practice)

### Advanced
- Papers from top conferences
- Reproduce papers from scratch
- Contribute to major open-source projects

## What's Next in This Course

After this roadmap, continue to:
- **Generative AI** course — image generation, diffusion models
- **Deep Learning** course — advanced architectures
- **AI Agents** course — building autonomous systems

Every course builds on the foundations you've established here. The computer vision landscape is vast and evolving rapidly, but you now have the tools to navigate it.

## Further Reading

- CS231n is the definitive course for learning CV
- Papers With Code tracks progress across all CV tasks
- PyTorch Vision provides the standard tools
- For production: OpenCV + ONNX Runtime + TensorRT
