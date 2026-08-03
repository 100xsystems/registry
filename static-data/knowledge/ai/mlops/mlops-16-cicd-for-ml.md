---
{
  "title": "CI/CD for Machine Learning",
  "description": "Automate testing, training and deployment in pipelines that run on every change.",
  "type": "lesson",
  "order": 16,
  "duration": "55 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define CI and CD for ML",
    "Run unit tests on data and code",
    "Trigger training on data or code changes",
    "Gate deployments on eval thresholds"
  ],
  "knowledge_refs": [
    "mlops/mlops-16-cicd-for-ml"
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

# MLOPS-16-CICD-FOR-ML: CI/CD for Machine Learning

## Introduction

Automate testing, training and deployment in pipelines that run on every change. By the end of this lesson you will be able to: Define CI and CD for ML; Run unit tests on data and code; Trigger training on data or code changes; Gate deployments on eval thresholds.

## Key Concepts

### 1. Define CI and CD for ML

Target: Define CI and CD for ML. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import yaml

workflow = {
    "name": "train",
    "on": ["push"],
    "jobs": {"train": {"steps": ["checkout", "test", "train", "register"]}},
}
print(workflow)
```
### 2. Run unit tests on data and code

Target: Run unit tests on data and code. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
def test_pipeline():
    assert sum([1, 2, 3]) == 6
    return "tests pass"

print(test_pipeline())
```
### 3. Trigger training on data or code changes

Target: Trigger training on data or code changes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("data change -> retrain. code change -> retrain. both audited")
```
### 4. Gate deployments on eval thresholds

Target: Gate deployments on eval thresholds. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("gate: only promote if eval metric beats the champion")
```

## Practice Questions

1. What is the key idea behind "CI/CD for Machine Learning"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain CI/CD for Machine Learning with analogies and real-world examples"
1. "Show me common mistakes beginners make with CI/CD for Machine Learning"
1. "Provide advanced patterns and performance considerations for CI/CD for Machine Learning"

## Key Takeaways

- Master the core ideas of CI/CD for Machine Learning through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
