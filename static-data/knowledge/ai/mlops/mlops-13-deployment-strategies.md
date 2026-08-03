---
{
  "title": "Model Deployment Strategies",
  "description": "Ship models safely: shadow, canary and blue-green deployments with rollbacks.",
  "type": "lesson",
  "order": 13,
  "duration": "50 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Compare shadow, canary and blue-green deploys",
    "Route traffic progressively",
    "Define rollback criteria",
    "Avoid duplicated inference cost"
  ],
  "knowledge_refs": [
    "mlops/mlops-12-kubernetes-basics",
    "llm-engineering/llm-15-llm-serving",
    "generative-ai/genai-18-llmops"
  ],
  "prerequisites": [
    "MLOPS-12: Kubernetes Basics for ML"
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

# MLOPS-13-DEPLOYMENT-STRATEGIES: Model Deployment Strategies

## Introduction

Ship models safely: shadow, canary and blue-green deployments with rollbacks. By the end of this lesson you will be able to: Compare shadow, canary and blue-green deploys; Route traffic progressively; Define rollback criteria; Avoid duplicated inference cost.

## Key Concepts

### 1. Compare shadow, canary and blue-green deploys

Target: Compare shadow, canary and blue-green deploys. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
strategies = {
    "shadow": "mirror traffic, no impact",
    "canary": "5% -> 50% -> 100%",
    "blue-green": "switch whole fleet at once",
}
print(strategies)
```
### 2. Route traffic progressively

Target: Route traffic progressively. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import random

# Canary: send a fraction of traffic to the new model
rng = random.Random(0)
for req in range(1000):
    if rng.random() < 0.05:
        new_model(req)
    else:
        old_model(req)
print("canary traffic split")
```
### 3. Define rollback criteria

Target: Define rollback criteria. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("rollback: revert to previous version on metric drop")
```
### 4. Avoid duplicated inference cost

Target: Avoid duplicated inference cost. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

# Compare old vs new on the same request
print("shadow mode logs both predictions for offline diffing")
```

## Practice Questions

1. What is the key idea behind "Model Deployment Strategies"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Model Deployment Strategies with analogies and real-world examples"
1. "Show me common mistakes beginners make with Model Deployment Strategies"
1. "Provide advanced patterns and performance considerations for Model Deployment Strategies"

## Key Takeaways

- Master the core ideas of Model Deployment Strategies through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
