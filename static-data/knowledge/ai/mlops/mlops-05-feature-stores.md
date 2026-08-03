---
{
  "title": "Feature Stores",
  "description": "One source of truth for features: consistent online and offline features.",
  "type": "lesson",
  "order": 5,
  "duration": "50 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Explain the feature store concept",
    "Describe online vs offline features",
    "Avoid train-serve skew",
    "Register and reuse features"
  ],
  "knowledge_refs": [
    "mlops/mlops-04-data-pipelines",
    "generative-ai/genai-18-llmops",
    "llm-engineering/llm-20-llmops-tooling"
  ],
  "prerequisites": [
    "MLOPS-04: Data Pipelines"
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

# MLOPS-05-FEATURE-STORES: Feature Stores

## Introduction

One source of truth for features: consistent online and offline features. By the end of this lesson you will be able to: Explain the feature store concept; Describe online vs offline features; Avoid train-serve skew; Register and reuse features.

## Key Concepts

### 1. Explain the feature store concept

Target: Explain the feature store concept. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
feature = {
    "name": "user_7d_spend",
    "offline": "batch job",
    "online": "redis lookup",
}
print(feature)
```
### 2. Describe online vs offline features

Target: Describe online vs offline features. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import redis

r = redis.Redis()
r.set("user:42:7d_spend", "129.5")
print("online feature:", r.get("user:42:7d_spend"))
```
### 3. Avoid train-serve skew

Target: Avoid train-serve skew. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("same code computes offline and online features -> no skew")
```
### 4. Register and reuse features

Target: Register and reuse features. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import feast

store = feast.FeatureStore("feature_repo")
print("feature store ready")
```

## Practice Questions

1. What is the key idea behind "Feature Stores"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Feature Stores with analogies and real-world examples"
1. "Show me common mistakes beginners make with Feature Stores"
1. "Provide advanced patterns and performance considerations for Feature Stores"

## Key Takeaways

- Master the core ideas of Feature Stores through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
