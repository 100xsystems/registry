---
{
  "title": "Experiment Tracking",
  "description": "Log every run: metrics, hyperparameters and artifacts with MLflow.",
  "type": "lesson",
  "order": 6,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Log runs with MLflow",
    "Compare experiments",
    "Track hyperparameters and metrics",
    "Search and organize runs"
  ],
  "knowledge_refs": [
    "mlops/mlops-05-feature-stores",
    "generative-ai/genai-18-llmops",
    "llm-engineering/llm-20-llmops-tooling"
  ],
  "prerequisites": [
    "MLOPS-03: Reproducibility & Versioning"
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

# MLOPS-06-EXPERIMENT-TRACKING: Experiment Tracking

## Introduction

Log every run: metrics, hyperparameters and artifacts with MLflow. By the end of this lesson you will be able to: Log runs with MLflow; Compare experiments; Track hyperparameters and metrics; Search and organize runs.

## Key Concepts

### 1. Log runs with MLflow

Target: Log runs with MLflow. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import mlflow

with mlflow.start_run():
    mlflow.log_param("lr", 0.01)
    mlflow.log_metric("accuracy", 0.93)
print("run logged")
```
### 2. Compare experiments

Target: Compare experiments. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import mlflow

# Nested structure: params, metrics, tags
mlflow.set_tag("team", "fraud")
print("tags set")
```
### 3. Track hyperparameters and metrics

Target: Track hyperparameters and metrics. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import mlflow

# Log artifacts: model files, plots
mlflow.log_artifact("confusion_matrix.png")
print("artifact logged")
```
### 4. Search and organize runs

Target: Search and organize runs. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import mlflow

runs = mlflow.search_runs(experiment_names=["default"])
print("runs found:", len(runs))
```

## Practice Questions

1. What is the key idea behind "Experiment Tracking"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Experiment Tracking with analogies and real-world examples"
1. "Show me common mistakes beginners make with Experiment Tracking"
1. "Provide advanced patterns and performance considerations for Experiment Tracking"

## Key Takeaways

- Master the core ideas of Experiment Tracking through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
