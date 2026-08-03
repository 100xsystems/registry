---
{
  "title": "LLMOps",
  "description": "Operationalize generative AI: prompt management, evals, guardrails and LLM monitoring.",
  "type": "lesson",
  "order": 20,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Track prompts and versions",
    "Evaluate LLM outputs automatically",
    "Add guardrails in production",
    "Monitor tokens, cost and quality"
  ],
  "knowledge_refs": [
    "mlops/mlops-19-cost-and-performance",
    "generative-ai/genai-18-llmops",
    "llm-engineering/llm-20-llmops-tooling"
  ],
  "prerequisites": [
    "MLOPS-14: Monitoring & Drift Detection"
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

# MLOPS-20-LLMOPS: LLMOps

## Introduction

Operationalize generative AI: prompt management, evals, guardrails and LLM monitoring. By the end of this lesson you will be able to: Track prompts and versions; Evaluate LLM outputs automatically; Add guardrails in production; Monitor tokens, cost and quality.

## Key Concepts

### 1. Track prompts and versions

Target: Track prompts and versions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import hashlib

# Version prompts like code
prompt_v3 = "You are a helpful assistant. Answer concisely."
print("prompt hash:", hashlib.sha256(prompt_v3.encode()).hexdigest()[:10])
```
### 2. Evaluate LLM outputs automatically

Target: Evaluate LLM outputs automatically. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

# Auto-eval: LLM-as-judge on a fixed eval set
scores = np.array([4, 5, 3, 5, 4])
print("mean judge score:", scores.mean())
```
### 3. Add guardrails in production

Target: Add guardrails in production. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
print("guardrails: block prompt injection and harmful outputs")
```
### 4. Monitor tokens, cost and quality

Target: Monitor tokens, cost and quality. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
metrics = {"tokens", "cost", "latency", "eval_score", "user_feedback"}
print(metrics)
```

## Practice Questions

1. What is the key idea behind "LLMOps"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain LLMOps with analogies and real-world examples"
1. "Show me common mistakes beginners make with LLMOps"
1. "Provide advanced patterns and performance considerations for LLMOps"

## Key Takeaways

- Master the core ideas of LLMOps through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
