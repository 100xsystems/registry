---
{
  "title": "Model Serving APIs",
  "description": "Expose models over HTTP with FastAPI and MLflow serving — with proper request validation.",
  "type": "lesson",
  "order": 10,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Build a FastAPI inference endpoint",
    "Define request and response schemas",
    "Handle batching and timeouts",
    "Measure latency correctly"
  ],
  "knowledge_refs": [
    "mlops/mlops-09-model-packaging",
    "llm-engineering/llm-15-llm-serving",
    "generative-ai/genai-18-llmops"
  ],
  "prerequisites": [
    "MLOPS-09: Model Packaging & Serialization"
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

# MLOPS-10-MODEL-SERVING: Model Serving APIs

## Introduction

Expose models over HTTP with FastAPI and MLflow serving — with proper request validation. By the end of this lesson you will be able to: Build a FastAPI inference endpoint; Define request and response schemas; Handle batching and timeouts; Measure latency correctly.

## Key Concepts

### 1. Build a FastAPI inference endpoint

Target: Build a FastAPI inference endpoint. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PredictRequest(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(req: PredictRequest):
    return {"score": sum(req.features) * 0.5}

print("endpoint ready")
```
### 2. Define request and response schemas

Target: Define request and response schemas. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# Batch: process many requests in one model call
batch = np.array([[1.0, 2.0], [3.0, 4.0]])
print("batch shape:", batch.shape)
```
### 3. Handle batching and timeouts

Target: Handle batching and timeouts. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import time

# Latency percentiles matter more than the mean
lat = [10, 12, 90, 11, 13]
print("p50:", sorted(lat)[len(lat) // 2], "p95:", sorted(lat)[int(0.95 * len(lat))])
```
### 4. Measure latency correctly

Target: Measure latency correctly. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("timeout + retry logic protects the service")
```

## Practice Questions

1. What is the key idea behind "Model Serving APIs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Model Serving APIs with analogies and real-world examples"
1. "Show me common mistakes beginners make with Model Serving APIs"
1. "Provide advanced patterns and performance considerations for Model Serving APIs"

## Key Takeaways

- Master the core ideas of Model Serving APIs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
