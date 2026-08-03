---
{
  "title": "Model Registry",
  "description": "Stage models through lifecycles and keep production versions audit-ready.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Register models with MLflow",
    "Use lifecycle stages (staging, production)",
    "Version models explicitly",
    "Enforce promotion gates"
  ],
  "knowledge_refs": [
    "mlops/mlops-06-experiment-tracking",
    "generative-ai/genai-18-llmops",
    "llm-engineering/llm-20-llmops-tooling"
  ],
  "prerequisites": [
    "MLOPS-06: Experiment Tracking"
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

# MLOPS-07-MODEL-REGISTRY: Model Registry

## Introduction

Stage models through lifecycles and keep production versions audit-ready. By the end of this lesson you will be able to: Register models with MLflow; Use lifecycle stages (staging, production); Version models explicitly; Enforce promotion gates.

## Key Concepts

### 1. Register models with MLflow

Target: Register models with MLflow. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import mlflow

mlflow.register_model("runs:/<run_id>/model", "churn_model")
print("model registered")
```
### 2. Use lifecycle stages (staging, production)

Target: Use lifecycle stages (staging, production). Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from mlflow.tracking import MlflowClient

client = MlflowClient()
client.transition_model_version_stage("churn_model", "2", "Production")
print("promoted to Production")
```
### 3. Version models explicitly

Target: Version models explicitly. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("every promotion is a reviewable event")
```
### 4. Enforce promotion gates

Target: Enforce promotion gates. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import mlflow

model = mlflow.pyfunc.load_model("models:/churn_model/2")
print("loaded production model")
```

## Practice Questions

1. What is the key idea behind "Model Registry"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Model Registry with analogies and real-world examples"
1. "Show me common mistakes beginners make with Model Registry"
1. "Provide advanced patterns and performance considerations for Model Registry"

## Key Takeaways

- Master the core ideas of Model Registry through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
