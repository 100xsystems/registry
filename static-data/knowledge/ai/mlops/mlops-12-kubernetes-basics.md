---
{
  "title": "Kubernetes Basics for ML",
  "description": "Orchestrate containers: pods, deployments, services and autoscaling.",
  "type": "lesson",
  "order": 12,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Describe pods, deployments and services",
    "Deploy a model service",
    "Autoscale based on load",
    "Manage GPU resources"
  ],
  "knowledge_refs": [
    "mlops/mlops-11-containerization",
    "generative-ai/genai-18-llmops",
    "llm-engineering/llm-20-llmops-tooling"
  ],
  "prerequisites": [
    "MLOPS-11: Containerization with Docker"
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

# MLOPS-12-KUBERNETES-BASICS: Kubernetes Basics for ML

## Introduction

Orchestrate containers: pods, deployments, services and autoscaling. By the end of this lesson you will be able to: Describe pods, deployments and services; Deploy a model service; Autoscale based on load; Manage GPU resources.

## Key Concepts

### 1. Describe pods, deployments and services

Target: Describe pods, deployments and services. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
manifest = {
    "kind": "Deployment",
    "spec": {"replicas": 2, "image": "my-model:1.2"},
}
print(manifest)
```
### 2. Deploy a model service

Target: Deploy a model service. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import yaml

service = {"kind": "Service", "spec": {"selector": {"app": "model"}, "ports": [{"port": 80}]}}
print(service)
```
### 3. Autoscale based on load

Target: Autoscale based on load. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("HorizontalPodAutoscaler scales replicas by CPU")
```
### 4. Manage GPU resources

Target: Manage GPU resources. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("nodeSelector + limits: pin pods to GPU nodes")
```

## Practice Questions

1. What is the key idea behind "Kubernetes Basics for ML"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Kubernetes Basics for ML with analogies and real-world examples"
1. "Show me common mistakes beginners make with Kubernetes Basics for ML"
1. "Provide advanced patterns and performance considerations for Kubernetes Basics for ML"

## Key Takeaways

- Master the core ideas of Kubernetes Basics for ML through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
