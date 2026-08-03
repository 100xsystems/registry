---
{
  "title": "Data & Model Governance",
  "description": "Auditability, access control and compliance for ML assets.",
  "type": "lesson",
  "order": 18,
  "duration": "50 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Record model cards and lineage",
    "Control access to data and models",
    "Meet audit requirements",
    "Document decisions"
  ],
  "knowledge_refs": [
    "mlops/mlops-18-governance"
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

# MLOPS-18-GOVERNANCE: Data & Model Governance

## Introduction

Auditability, access control and compliance for ML assets. By the end of this lesson you will be able to: Record model cards and lineage; Control access to data and models; Meet audit requirements; Document decisions.

## Key Concepts

### 1. Record model cards and lineage

Target: Record model cards and lineage. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
model_card = {
    "owner": "fraud-team",
    "intended_use": "transaction scoring",
    "limitations": "trained on EU data",
    "version": "2.1.0",
}
print(model_card)
```
### 2. Control access to data and models

Target: Control access to data and models. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
print("every prediction traceable to a model version")
```
### 3. Meet audit requirements

Target: Meet audit requirements. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("role-based access: analysts read, engineers deploy")
```
### 4. Document decisions

Target: Document decisions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
print("audit log: who changed what, when, why")
```

## Practice Questions

1. What is the key idea behind "Data & Model Governance"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Data & Model Governance with analogies and real-world examples"
1. "Show me common mistakes beginners make with Data & Model Governance"
1. "Provide advanced patterns and performance considerations for Data & Model Governance"

## Key Takeaways

- Master the core ideas of Data & Model Governance through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
