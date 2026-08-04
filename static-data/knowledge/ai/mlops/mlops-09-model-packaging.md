---
slug: mlops-09-model-packaging
title: "Model Packaging & Serialization"
description: "Converting trained models into deployable artifacts — ONNX, pickle, SavedModel, TorchScript, and containerized serving."
order: 9
tags:
  - mlops
  - model-packaging
  - onnx
  - serialization
  - containerization
prerequisites:
  - mlops-08-training-at-scale
knowledge_refs:
  - mlops-08-training-at-scale
    title: "Training at Scale"
  - mlops-10-model-serving
    title: "Model Serving APIs"
  - mlops-11-containerization
    title: "Containerization with Docker"
references:
  - title: "ONNX Runtime Documentation"
    url: "https://onnxruntime.ai/docs/"
  - title: "PyTorch — TorchScript"
    url: "https://pytorch.org/docs/stable/jit.html"
  - title: "TensorFlow — SavedModel Format"
    url: "https://www.tensorflow.org/guide/saved_model"
  - title: "Scikit-learn — Model Persistence"
    url: "https://scikit-learn.org/stable/model_persistence.html"
  - title: "MLflow — Model Flavor Documentation"
    url: "https://mlflow.org/docs/latest/ml/models.html"
---

## Model Packaging & Serialization

A trained model in memory isn't deployable. Model packaging converts it into a format that can be saved, loaded, transported, and served efficiently across different environments.

### Why Packaging Matters

- **Portability:** The model must run on different hardware and platforms
- **Performance:** Serialized formats enable optimized inference
- **Dependency management:** The package must include everything needed for inference
- **Versioning:** Packages are the artifacts that get versioned and promoted

### Common Formats

**Pickle/joblib (Python):** Simple serialization for scikit-learn models. Quick to implement but Python-specific and not secure against malicious payloads.

**ONNX (Open Neural Network Exchange):** Framework-agnostic format. Train in PyTorch, deploy with ONNX Runtime on any platform. Enables optimization passes and hardware-specific acceleration.

**TensorFlow SavedModel:** Complete TensorFlow model with weights, computation graph, and metadata. Native format for TensorFlow Serving.

**TorchScript:** PyTorch's deployment format. Traces or scripts the model to create a standalone representation that runs without Python dependencies.

**MLflow Model Flavors:** Wraps models with metadata (conda environment, dependencies, signature) for reproducible deployment across platforms.

### Choosing a Format

| Format | Best For | Framework |
|---|---|---|
| **Pickle** | Quick prototyping | scikit-learn |
| **ONNX** | Cross-framework deployment | Any |
| **SavedModel** | TensorFlow Serving | TensorFlow |
| **TorchScript** | PyTorch production | PyTorch |
| **MLflow** | MLOps integration | Any |

### Best Practices

- **Test the packaged model:** Load it in a clean environment and verify predictions match training.
- **Freeze the environment:** Pin all dependencies in the package.
- **Include metadata:** Model signature, training data version, evaluation metrics.
- **Optimize for inference:** Remove training-only layers, quantize weights, optimize graph.

### Common Mistakes

- **Using pickle for production:** Pickle is insecure and not cross-language. Use ONNX or framework-specific formats.
- **Not testing the package:** Models that work in training notebooks may fail when loaded in a different environment.
- **Missing dependencies:** Forgetting to include preprocessing steps or custom layers in the package.

---

*Continue to learn about model serving — deploying models as APIs for real-time and batch inference.*
