---
{
  "title": "Containerization with Docker",
  "description": "Package the model, code and dependencies into one portable image.",
  "type": "lesson",
  "order": 11,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write a production Dockerfile",
    "Keep images small and layered",
    "Run containers locally",
    "Understand security basics"
  ],
  "knowledge_refs": [
    "mlops/mlops-11-containerization"
  ],
  "prerequisites": [
    "MLOPS-10: Model Serving APIs"
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

# MLOPS-11-CONTAINERIZATION: Containerization with Docker

## Introduction

Package the model, code and dependencies into one portable image. By the end of this lesson you will be able to: Write a production Dockerfile; Keep images small and layered; Run containers locally; Understand security basics.

## Key Concepts

### 1. Write a production Dockerfile

Target: Write a production Dockerfile. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
dockerfile = """FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
"""
print(dockerfile)
```
### 2. Keep images small and layered

Target: Keep images small and layered. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import subprocess

print("docker build -t my-model .")
```
### 3. Run containers locally

Target: Run containers locally. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("slim base + pinned deps = smaller, reproducible image")
```
### 4. Understand security basics

Target: Understand security basics. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("never bake secrets into images")
```

## Practice Questions

1. What is the key idea behind "Containerization with Docker"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Containerization with Docker with analogies and real-world examples"
1. "Show me common mistakes beginners make with Containerization with Docker"
1. "Provide advanced patterns and performance considerations for Containerization with Docker"

## Key Takeaways

- Master the core ideas of Containerization with Docker through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
