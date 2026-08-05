---
slug: mlops-12-kubernetes-basics
title: "Kubernetes Basics for ML"
description: "Orchestrating ML workloads with Kubernetes — pods, deployments, services, GPU scheduling, and Helm charts."
order: 12
tags:
  - mlops
  - kubernetes
  - orchestration
  - gpu-scheduling
  - helm
prerequisites:
  - mlops-11-containerization
knowledge_refs:
  - slug: mlops-11-containerization
    title: "Containerization with Docker"
  - slug: mlops-13-deployment-strategies
    title: "Model Deployment Strategies"
  - slug: mlops-18-governance
    title: "Data & Model Governance"
references:
  - title: "Kubernetes Documentation"
    url: "https://kubernetes.io/docs/home/"
  - title: "Kubeflow — ML on Kubernetes"
    url: "https://www.kubeflow.org/docs/"
  - title: "KServe — Kubernetes-based Model Serving"
    url: "https://kserve.github.io/website/"
  - title: "NVIDIA GPU Operator for Kubernetes"
    url: "https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/"
  - title: "Helm — Kubernetes Package Manager"
    url: "https://helm.sh/docs/"
---
## Kubernetes Basics for ML

Kubernetes (K8s) is the industry standard for container orchestration. For ML, it provides scalable, reliable infrastructure for training, serving, and monitoring models.

### Core Kubernetes Concepts

**Pod:** The smallest deployable unit. Contains one or more containers sharing network and storage. An ML serving pod typically runs one model server container.

**Deployment:** Manages pod replicas, rolling updates, and rollouts. Ensures the desired number of pods are running.

**Service:** Provides stable networking for pods. A LoadBalancer service exposes your model API to external traffic.

**Namespace:** Isolates resources within a cluster. Use namespaces to separate training, serving, and monitoring environments.

### GPU Scheduling

Kubernetes can schedule GPU workloads using the NVIDIA GPU Operator:
- Install the GPU Operator to manage NVIDIA drivers and device plugins
- Request GPUs in pod specs: `resources.limits.nvidia.com/gpu: 1`
- Use node selectors to target GPU nodes

### ML-Specific Tools

**Kubeflow:** End-to-end ML platform on Kubernetes. Provides pipelines, training operators, and model serving.

**KServe:** Kubernetes-native model serving. Supports TensorFlow, PyTorch, ONNX, and custom models. Provides canary deployments, autoscaling, and explainability.

### Helm Charts

Helm packages Kubernetes manifests into reusable charts:
- Parameterize deployments (image tags, resource requests, environment variables)
- Version and share configurations
- Deploy complex ML stacks with a single command

### Common Mistakes

- **No resource limits:** Pods without CPU/GPU limits can consume all cluster resources.
- **Ignoring autoscaling:** ML serving workloads are bursty. HPA (Horizontal Pod Autoscaler) handles traffic spikes.
- **No health checks:** Kubernetes can't replace failed pods without liveness and readiness probes.
- **Over-complicating:** Start simple. Not every ML workload needs Kubernetes.

---

*Continue to learn about deployment strategies — canary, blue-green, and shadow deployments.*
