---
slug: mlops-11-containerization
title: "Containerization with Docker"
description: "Packaging ML applications for reproducible deployment — Dockerfiles, multi-stage builds, GPU containers, and container registries."
order: 11
tags:
  - mlops
  - docker
  - containerization
  - gpu-containers
  - reproducibility
prerequisites:
  - mlops-10-model-serving
knowledge_refs:
  - slug: mlops-10-model-serving
    title: "Model Serving APIs"
  - slug: mlops-12-kubernetes-basics
    title: "Kubernetes Basics for ML"
  - slug: mlops-09-model-packaging
    title: "Model Packaging & Serialization"
references:
  - title: "Docker — Multi-Stage Builds"
    url: "https://docs.docker.com/build/building/multi-stage/"
  - title: "Docker — Model Runner for AI"
    url: "https://docs.docker.com/ai/model-runner/"
  - title: "NVIDIA GPU Support in Docker for AI/ML"
    url: "https://oneuptime.com/blog/post/2026-01-16-docker-nvidia-gpu-ai-ml/view"
  - title: "Docker Documentation"
    url: "https://docs.docker.com/"
  - title: "NVIDIA Container Toolkit"
    url: "https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/"
---
## Containerization with Docker

Docker solves the "it works on my machine" problem by packaging code, dependencies, and runtime into immutable containers. For ML, this means reproducible environments from training to serving.

### Why Docker for ML

ML systems have complex dependencies — Python versions, CUDA drivers, GPU libraries, model files. Docker encapsulates all of this into a single artifact that runs identically everywhere.

### Writing Dockerfiles for ML

**Base image selection:** Start with official framework images (`pytorch/pytorch:2.1-cuda12.1-cudnn8-runtime`) or minimal Python images for smaller footprints.

**Layer caching:** Order instructions strategically — copy `requirements.txt` and run `pip install` before copying source code. This maximizes cache hits.

**Security:** Run containers as non-root users. Avoid storing secrets in images.

### Multi-Stage Builds

Separate build-time dependencies from runtime:

```dockerfile
# Stage 1: Build
FROM python:3.11 AS builder
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . /app
```

This produces images 50–80% smaller by excluding compilers, caches, and build tools.

### GPU Containers

Docker can use NVIDIA GPUs via the NVIDIA Container Toolkit:

```bash
docker run --gpus all my-ml-image
docker run --gpus '"device=0,2"' my-ml-image  # Specific GPUs
```

**Performance tuning:** Set `shm_size: '8gb'` for PyTorch DataLoader workers. Use `ipc: host` for multi-GPU NCCL communication.

### Container Registries

Store and distribute images via:
- Docker Hub (public)
- Amazon ECR, Google Artifact Registry, Azure Container Registry (private)

Tag images with version numbers and push/pull for deployment.

### Common Mistakes

- **Huge images:** Including build tools and unnecessary packages bloats images and slows deployment.
- **No .dockerignore:** Sending the entire build context (including `.git`, `node_modules`) wastes time.
- **Running as root:** Security risk. Always use a non-root user.
- **No multi-stage builds:** Build dependencies in the runtime image wastes space.

---

*Continue to learn about Kubernetes — orchestrating ML workloads at scale.*
