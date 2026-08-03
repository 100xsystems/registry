---
{
  "title": "Testing ML Systems",
  "description": "Test data, features, models and infrastructure — because ML code is only part of the system.",
  "type": "lesson",
  "order": 17,
  "duration": "50 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write data and schema tests",
    "Test model invariants",
    "Write golden tests for features",
    "Load-test the serving path"
  ],
  "knowledge_refs": [
    "mlops/mlops-17-testing-ml-systems"
  ],
  "prerequisites": [
    "MLOPS-16: CI/CD for Machine Learning"
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

# MLOPS-17-TESTING-ML-SYSTEMS: Testing ML Systems

## Introduction

Test data, features, models and infrastructure — because ML code is only part of the system. By the end of this lesson you will be able to: Write data and schema tests; Test model invariants; Write golden tests for features; Load-test the serving path.

## Key Concepts

### 1. Write data and schema tests

Target: Write data and schema tests. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import pandas as pd

def test_no_nulls(df):
    assert not df.isna().any().any()

print("data test ready")
```
### 2. Test model invariants

Target: Test model invariants. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
def test_probability_range(probs):
    assert ((probs >= 0) & (probs <= 1)).all()

print("model invariant test ready")
```
### 3. Write golden tests for features

Target: Write golden tests for features. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# Golden test: known input -> known output
known = np.array([0.0, 1.0, 0.0])
assert np.allclose(known, [0.0, 1.0, 0.0])
print("golden test passes")
```
### 4. Load-test the serving path

Target: Load-test the serving path. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import time

# Load test: requests per second under target latency
start = time.perf_counter()
for _ in range(100):
    predict([1.0, 2.0])
print("100 calls in", round(time.perf_counter() - start, 3), "s")
```

## Practice Questions

1. What is the key idea behind "Testing ML Systems"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Testing ML Systems with analogies and real-world examples"
1. "Show me common mistakes beginners make with Testing ML Systems"
1. "Provide advanced patterns and performance considerations for Testing ML Systems"

## Key Takeaways

- Master the core ideas of Testing ML Systems through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
