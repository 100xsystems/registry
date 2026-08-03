---
{
  "title": "Cost & Performance Optimization",
  "description": "Balance accuracy against inference cost, latency and carbon.",
  "type": "lesson",
  "order": 19,
  "duration": "50 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Profile inference latency",
    "Quantize and distill models",
    "Right-size infrastructure",
    "Track cost per prediction"
  ],
  "knowledge_refs": [
    "mlops/mlops-18-governance",
    "llm-engineering/llm-16-cost-optimization",
    "reinforcement-learning/rl-12-proximal-policy-optimization"
  ],
  "prerequisites": [
    "MLOPS-13: Model Deployment Strategies"
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

# MLOPS-19-COST-AND-PERFORMANCE: Cost & Performance Optimization

## Introduction

Balance accuracy against inference cost, latency and carbon. By the end of this lesson you will be able to: Profile inference latency; Quantize and distill models; Right-size infrastructure; Track cost per prediction.

## Key Concepts

### 1. Profile inference latency

Target: Profile inference latency. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import time

# Profile: find the slow stage
start = time.perf_counter()
predict([1.0] * 10)
print("inference ms:", round((time.perf_counter() - start) * 1000, 2))
```
### 2. Quantize and distill models

Target: Quantize and distill models. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import torch

# Quantization: fp32 -> int8, ~4x smaller
print("torch.quantization ready")
```
### 3. Right-size infrastructure

Target: Right-size infrastructure. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# Cost per prediction
daily_cost = 120.0
predictions = 1_000_000
print("cost per prediction:", daily_cost / predictions)
```
### 4. Track cost per prediction

Target: Track cost per prediction. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("batch requests to amortize GPU cost")
```

## Practice Questions

1. What is the key idea behind "Cost & Performance Optimization"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Cost & Performance Optimization with analogies and real-world examples"
1. "Show me common mistakes beginners make with Cost & Performance Optimization"
1. "Provide advanced patterns and performance considerations for Cost & Performance Optimization"

## Key Takeaways

- Master the core ideas of Cost & Performance Optimization through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
