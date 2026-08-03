---
{
  "title": "Data Pipelines",
  "description": "Reliable, repeatable data flow: ingestion, validation, cleaning and feature preparation.",
  "type": "lesson",
  "order": 4,
  "duration": "55 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Design a data ingestion pipeline",
    "Validate data with expectations",
    "Handle incremental updates",
    "Use orchestration tools (Airflow, Prefect)"
  ],
  "knowledge_refs": [
    "mlops/mlops-04-data-pipelines"
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

# MLOPS-04-DATA-PIPELINES: Data Pipelines

## Introduction

Reliable, repeatable data flow: ingestion, validation, cleaning and feature preparation. By the end of this lesson you will be able to: Design a data ingestion pipeline; Validate data with expectations; Handle incremental updates; Use orchestration tools (Airflow, Prefect).

## Key Concepts

### 1. Design a data ingestion pipeline

Target: Design a data ingestion pipeline. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import pandas as pd

# Validate: fail fast on bad data
required = ["user_id", "event_time"]
df = pd.DataFrame({"user_id": [1, 2], "event_time": ["2024-01-01", None]})
missing = [c for c in required if df[c].isna().any()]
print("missing required:", missing)
```
### 2. Validate data with expectations

Target: Validate data with expectations. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
from airflow import DAG

# DAG: define task dependencies declaratively
print("extract -> validate -> transform -> load")
```
### 3. Handle incremental updates

Target: Handle incremental updates. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import pandas as pd

# Incremental: only new rows
def load_new(last_id, source):
    return source[source["id"] > last_id]

print("incremental load ready")
```
### 4. Use orchestration tools (Airflow, Prefect)

Target: Use orchestration tools (Airflow, Prefect). Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import pandera as pa

schema = pa.DataFrameSchema({
    "price": pa.Column(float, pa.Check.ge(0)),
})
print("schema validation ready")
```

## Practice Questions

1. What is the key idea behind "Data Pipelines"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Data Pipelines with analogies and real-world examples"
1. "Show me common mistakes beginners make with Data Pipelines"
1. "Provide advanced patterns and performance considerations for Data Pipelines"

## Key Takeaways

- Master the core ideas of Data Pipelines through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
