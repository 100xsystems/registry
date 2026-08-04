---
slug: mlops-10-model-serving
title: "Model Serving APIs"
description: "Deploying models as APIs — REST vs gRPC, TensorFlow Serving, Triton, BentoML, and batch vs real-time serving."
order: 10
tags:
  - mlops
  - model-serving
  - rest-api
  - grpc
  - tensorflow-serving
  - triton
prerequisites:
  - mlops-09-model-packaging
knowledge_refs:
  - mlops-09-model-packaging
    title: "Model Packaging & Serialization"
  - mlops-13-deployment-strategies
    title: "Model Deployment Strategies"
  - mlops-14-monitoring-and-drift
    title: "Monitoring & Drift Detection"
references:
  - title: "TensorFlow Serving Documentation"
    url: "https://www.tensorflow.org/tfx/guide/serving"
  - title: "NVIDIA Triton Inference Server"
    url: "https://github.com/triton-inference-server/server"
  - title: "BentoML Documentation"
    url: "https://docs.bentoml.com/"
  - title: "Seldon Core Documentation"
    url: "https://docs.seldon.io/projects/seldon-core/en/latest/"
  - title: "Google Cloud — Model Serving"
    url: "https://cloud.google.com/vertex-ai/docs/predictions/getting-predictions"
---

## Model Serving APIs

Model serving is the process of making trained models available for inference via APIs. The serving architecture determines latency, throughput, cost, and reliability.

### Real-Time vs. Batch Serving

**Real-time serving:** Models respond to individual requests within milliseconds. Used for recommendations, search ranking, fraud detection, chatbots. Requires low-latency infrastructure.

**Batch serving:** Models process large datasets offline. Used for nightly scoring, report generation, data enrichment. Can optimize for throughput over latency.

**Streaming serving:** Models process data in real-time streams. Used for live analytics, IoT processing, real-time monitoring.

### Serving Protocols

**REST APIs:** JSON-based, human-readable, widely supported. Easy to debug and test. Higher overhead per request.

**gRPC:** Binary protocol, lower latency, higher throughput. Better for high-performance serving. Uses Protocol Buffers for serialization.

### Serving Platforms

**TensorFlow Serving:** Production-grade server for TensorFlow models. Supports model versioning, batching, and gRPC/REST endpoints. Best for TensorFlow-heavy stacks.

**NVIDIA Triton Inference Server:** Multi-framework (PyTorch, TensorFlow, ONNX, TensorRT). Supports dynamic batching, concurrent model execution, and GPU optimization. The most versatile option.

**BentoML:** Python-first framework for wrapping models as production services. Provides Docker packaging, API definitions, and deployment to Kubernetes or cloud. Best for teams wanting Python-native workflows.

**Seldon Core:** Kubernetes-native platform for deploying ML models. Supports complex inference graphs (multiple models chained together).

### Best Practices

- **Implement health checks:** `/health` endpoints for load balancers
- **Add request validation:** Validate inputs before they reach the model
- **Enable batching:** Batch multiple requests together for GPU efficiency
- **Set timeouts:** Prevent slow requests from blocking the queue
- **Monitor latency:** Track p50, p95, p99 latencies

### Common Mistakes

- **No input validation:** Invalid inputs can crash the server or produce garbage outputs
- **Ignoring batching:** Single-request inference wastes GPU capacity
- **No health checks:** Load balancers can't detect failed instances
- **Over-engineering:** Start with a simple API before building complex inference graphs

---

*Continue to learn about containerization — packaging ML applications with Docker.*
