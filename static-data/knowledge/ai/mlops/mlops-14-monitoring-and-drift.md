---
{
  "title": "Monitoring & Drift Detection",
  "description": "Watch predictions and features: data drift, concept drift and model performance decay.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Monitor feature distributions",
    "Detect data and concept drift",
    "Track prediction drift",
    "Set alert thresholds deliberately"
  ],
  "knowledge_refs": [
    "mlops/mlops-14-monitoring-and-drift"
  ],
  "prerequisites": [
    "MLOPS-13: Model Deployment Strategies"
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

# MLOPS-14-MONITORING-AND-DRIFT: Monitoring & Drift Detection

## Introduction

Watch predictions and features: data drift, concept drift and model performance decay. By the end of this lesson you will be able to: Monitor feature distributions; Detect data and concept drift; Track prediction drift; Set alert thresholds deliberately.

## Key Concepts

### 1. Monitor feature distributions

Target: Monitor feature distributions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np
from scipy import stats

# KS test: did the feature distribution change?
baseline = np.random.default_rng(0).normal(0, 1, 1000)
current = np.random.default_rng(1).normal(0.5, 1, 1000)
print("KS p-value:", round(stats.ks_2samp(baseline, current).pvalue, 4))
```
### 2. Detect data and concept drift

Target: Detect data and concept drift. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# PSI: population stability index
bins = np.linspace(0, 1, 11)
actual = np.histogram(np.random.default_rng(0).uniform(size=1000), bins=bins)[0]
expected = np.histogram(np.random.default_rng(1).uniform(size=1000), bins=bins)[0]
psi = ((actual / actual.sum()) - (expected / expected.sum())) * np.log((actual / actual.sum()) / (expected / expected.sum()))
print("PSI:", round(psi.sum(), 3))
```
### 3. Track prediction drift

Target: Track prediction drift. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

# Concept drift: the relationship changed, not just inputs
print("accuracy drops even when features look the same")
```
### 4. Set alert thresholds deliberately

Target: Set alert thresholds deliberately. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
alerts = {"psi > 0.25", "accuracy -5pp", "empty predictions"}
print(alerts)
```

## Practice Questions

1. What is the key idea behind "Monitoring & Drift Detection"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Monitoring & Drift Detection with analogies and real-world examples"
1. "Show me common mistakes beginners make with Monitoring & Drift Detection"
1. "Provide advanced patterns and performance considerations for Monitoring & Drift Detection"

## Key Takeaways

- Master the core ideas of Monitoring & Drift Detection through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
