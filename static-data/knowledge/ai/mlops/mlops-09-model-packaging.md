---
{
  "title": "Model Packaging & Serialization",
  "description": "Wrap models into portable artifacts: pickle, ONNX, and MLflow models.",
  "type": "lesson",
  "order": 9,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Serialize models safely",
    "Export to ONNX for portability",
    "Define a serving signature",
    "Avoid pickle pitfalls"
  ],
  "knowledge_refs": [
    "mlops/mlops-08-training-at-scale",
    "generative-ai/genai-18-llmops",
    "llm-engineering/llm-20-llmops-tooling"
  ],
  "prerequisites": [
    "MLOPS-07: Model Registry"
  ],
  "references": [
    {
      "title": "MLflow Documentation",
      "url": "https://mlflow.org/docs/latest/index.html",
      "description": "Tracking, registries and serving for the ML lifecycle."
    },
    {
      "title": "Kubeflow Documentation",
      "url": "https://www.kubeflow.org/docs/",
      "description": "Kubernetes-native ML workflows."
    },
    {
      "title": "DVC Documentation",
      "url": "https://dvc.org/doc",
      "description": "Data version control for reproducible ML pipelines."
    },
    {
      "title": "The ML Engineer — Chip Huyen",
      "url": "https://www.oreilly.com/library/view/introduction-to-machine/9781098119478/",
      "description": "The reference book on building ML systems in production."
    },
    {
      "title": "Google MLOps Whitepaper",
      "url": "https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning",
      "description": "The canonical description of MLOps levels and practices."
    }
  ]
}
---

# MLOPS-09-MODEL-PACKAGING: Model Packaging & Serialization

## Introduction

Wrap models into portable artifacts: pickle, ONNX, and MLflow models. By the end of this lesson you will be able to: Serialize models safely; Export to ONNX for portability; Define a serving signature; Avoid pickle pitfalls.

## Key Concepts

### 1. Serialize models safely

Target: Serialize models safely. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import pickle

model = {"type": "linear", "weights": [0.5, -0.2]}
with open("model.pkl", "wb") as fh:
    pickle.dump(model, fh)
print("pickled")
```
### 2. Export to ONNX for portability

Target: Export to ONNX for portability. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch
import torch.onnx

model = torch.nn.Linear(4, 2)
torch.onnx.export(model, torch.randn(1, 4), "model.onnx")
print("exported to ONNX")
```
### 3. Define a serving signature

Target: Define a serving signature. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import mlflow

mlflow.sklearn.save_model(model, "model_dir", input_example=[1.0, 2.0])
print("mlflow model with signature")
```
### 4. Avoid pickle pitfalls

Target: Avoid pickle pitfalls. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

print("pickle runs arbitrary code on load: only trust your own artifacts")
```

## Practice Questions

1. What is the key idea behind "Model Packaging & Serialization"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Model Packaging & Serialization with analogies and real-world examples"
1. "Show me common mistakes beginners make with Model Packaging & Serialization"
1. "Provide advanced patterns and performance considerations for Model Packaging & Serialization"

## Key Takeaways

- Master the core ideas of Model Packaging & Serialization through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
