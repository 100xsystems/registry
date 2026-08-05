---
slug: mlops-08-training-at-scale
title: "Training at Scale"
description: "Distributed training, GPU clusters, training orchestration, and cost-efficient approaches to large-scale model training."
order: 8
tags:
  - mlops
  - distributed-training
  - gpu
  - kubeflow
  - sagemaker
  - cost-efficiency
prerequisites:
  - mlops-07-model-registry
knowledge_refs:
  - slug: mlops-07-model-registry
    title: "Model Registry"
  - slug: mlops-19-cost-and-performance
    title: "Cost & Performance Optimization"
  - slug: mlops-11-containerization
    title: "Containerization with Docker"
references:
  - title: "AWS SageMaker — Distributed Training"
    url: "https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training.html"
  - title: "AWS SageMaker — Distributed Training Strategies"
    url: "https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training-strategies.html"
  - title: "Kubeflow Trainer Overview"
    url: "https://www.kubeflow.org/docs/components/trainer/overview/"
  - title: "Optimizing Training Workloads for GPU Clusters"
    url: "https://www.together.ai/blog/optimizing-training-workloads-for-gpu-clusters"
  - title: "AWS SageMaker — Distributed Computing Best Practices"
    url: "https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training-options.html"
---
## Training at Scale

When models are too large for a single GPU or datasets too big for one machine, distributed training splits the work across multiple devices. This lesson covers the strategies, infrastructure, and cost considerations for training at scale.

### Distributed Training Strategies

**Data parallelism:** The dataset is split across GPUs. Each worker holds a complete model copy, processes a different mini-batch, and synchronizes gradients via AllReduce. This is the most common strategy and works well when the model fits in a single GPU's memory.

**Model parallelism:** The model itself is split across GPUs. Each worker holds a portion of the model's layers. This is necessary when the model is too large for one GPU (common with large language models).

**Pipeline parallelism:** A form of model parallelism where different model stages run on different GPUs simultaneously using micro-batches, reducing idle time.

### GPU Clusters

**Interconnects matter:** NVLink (intra-node) and InfiniBand (inter-node) determine how fast gradients synchronize. Slow interconnects become the bottleneck.

**Hardware validation:** Before training, verify GPU health (no ECC errors), check communication topology, and run NCCL tests.

**Data pipelines:** Pre-stage datasets to node-local NVMe storage. CPU preprocessing bottlenecks starve GPUs.

### Training Orchestration

**Kubeflow Trainer:** Kubernetes-native. Orchestrates distributed training across PyTorch, TensorFlow, DeepSpeed. Integrates with Kueue for priority scheduling.

**SageMaker Training:** Managed service. Abstracts infrastructure via Deep Learning Containers. Supports data parallelism, model parallelism, and automatic hyperparameter tuning.

### Cost-Efficient Training

**Spot instances:** Use preemptible GPUs (30–50% savings) with robust checkpointing to handle preemptions.

**Mixed precision:** FP16/BF16 training reduces memory and increases throughput via NVIDIA Tensor Cores.

**Right-sizing:** Benchmark on small clusters first. Find optimal batch size and GPU count before scaling up.

### Common Mistakes

- **Ignoring interconnects:** Slow networking makes multi-node training inefficient.
- **No checkpointing:** Spot instances require frequent checkpointing to survive preemptions.
- **Over-provisioning:** More GPUs isn't always faster. Communication overhead can dominate.
- **Skipping mixed precision:** FP16 training is nearly free performance with minimal accuracy loss.

---

*Continue to learn about model packaging — serializing models for deployment.*
