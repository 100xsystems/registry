---
{
  "title": "Reproducibility & Versioning",
  "description": "Version code, data and models together — the foundation of trustworthy ML.",
  "type": "lesson",
  "order": 3,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Version data with DVC",
    "Lock dependencies and environments",
    "Record model lineage",
    "Reproduce any historical experiment"
  ],
  "knowledge_refs": [
    "mlops/mlops-02-the-ml-lifecycle",
    "generative-ai/genai-18-llmops",
    "llm-engineering/llm-20-llmops-tooling"
  ],
  "prerequisites": [
    "MLOPS-02: The ML Lifecycle"
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

# MLOPS-03-REPRODUCIBILITY-AND-VERSIONING: Reproducibility & Versioning

## Introduction

Version code, data and models together — the foundation of trustworthy ML. By the end of this lesson you will be able to: Version data with DVC; Lock dependencies and environments; Record model lineage; Reproduce any historical experiment.

## Key Concepts

### 1. Version data with DVC

Target: Version data with DVC. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import dvc.api

# DVC: data versioned like code
params = dvc.api.params_show()
print("dvc params:", params)
```
### 2. Lock dependencies and environments

Target: Lock dependencies and environments. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import hashlib

# Content hash: the same data hash means the same data
def data_hash(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()[:12]

print("data hash:", data_hash("train.csv"))
```
### 3. Record model lineage

Target: Record model lineage. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import yaml

env = {"python": "3.11", "packages": {"torch": "2.2.0", "sklearn": "1.4.0"}}
print(env)
```
### 4. Reproduce any historical experiment

Target: Reproduce any historical experiment. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("lineage: code + data + config -> model artifact")
```

## Practice Questions

1. What is the key idea behind "Reproducibility & Versioning"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Reproducibility & Versioning with analogies and real-world examples"
1. "Show me common mistakes beginners make with Reproducibility & Versioning"
1. "Provide advanced patterns and performance considerations for Reproducibility & Versioning"

## Key Takeaways

- Master the core ideas of Reproducibility & Versioning through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
