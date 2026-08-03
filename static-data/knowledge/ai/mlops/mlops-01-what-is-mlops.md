---
{
  "title": "What Is MLOps?",
  "description": "The discipline of operationalizing machine learning: people, pipelines, and platforms.",
  "type": "lesson",
  "order": 1,
  "duration": "40 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define MLOps and why it emerged",
    "Contrast ML development with ML operations",
    "Describe the three MLOps maturity levels",
    "Identify the pillars of production ML systems"
  ],
  "knowledge_refs": [
    "generative-ai/genai-18-llmops",
    "llm-engineering/llm-20-llmops-tooling",
    "llm-engineering/llm-15-llm-serving"
  ],
  "prerequisites": [
    "ML-01: What Is Machine Learning?"
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

# MLOPS-01-WHAT-IS-MLOPS: What Is MLOps?

## Introduction

The discipline of operationalizing machine learning: people, pipelines, and platforms. By the end of this lesson you will be able to: Define MLOps and why it emerged; Contrast ML development with ML operations; Describe the three MLOps maturity levels; Identify the pillars of production ML systems.

## Key Concepts

### 1. Define MLOps and why it emerged

Target: Define MLOps and why it emerged. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
pillars = ["data", "models", "code", "deployment", "monitoring"]
for p in pillars:
    print(f"- {p}")
```
### 2. Contrast ML development with ML operations

Target: Contrast ML development with ML operations. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
levels = {
    1: "manual process",
    2: "automated pipelines",
    3: "continuous delivery + monitoring",
}
print(levels)
```
### 3. Describe the three MLOps maturity levels

Target: Describe the three MLOps maturity levels. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("models decay: data drift makes today's model tomorrow's liability")
```
### 4. Identify the pillars of production ML systems

Target: Identify the pillars of production ML systems. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
components = ["training", "serving", "monitoring", "governance", "retraining"]
print(components)
```

## Practice Questions

1. What is the key idea behind "What Is MLOps?"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain What Is MLOps? with analogies and real-world examples"
1. "Show me common mistakes beginners make with What Is MLOps?"
1. "Provide advanced patterns and performance considerations for What Is MLOps?"

## Key Takeaways

- Master the core ideas of What Is MLOps? through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
