---
slug: mlops-03-reproducibility-and-versioning
title: "Reproducibility & Versioning"
description: "Ensuring you can recreate any model at any time — data versioning, code versioning, experiment tracking, and environment management."
order: 3
tags:
  - mlops
  - reproducibility
  - versioning
  - dvc
  - git
  - experiment-tracking
prerequisites:
  - mlops-02-the-ml-lifecycle
knowledge_refs:
  - mlops-02-the-ml-lifecycle
    title: "The ML Lifecycle"
  - mlops-06-experiment-tracking
    title: "Experiment Tracking"
  - mlops-07-model-registry
    title: "Model Registry"
references:
  - title: "DVC — Get Started with Data Version Control"
    url: "https://doc.dvc.org/start"
  - title: "Reproducibility and Versioning in ML Systems"
    url: "https://www.dailydoseofds.com/mlops-crash-course-part-3/"
  - title: "MLflow Model Registry"
    url: "https://mlflow.org/docs/latest/ml/model-registry/"
  - title: "MLflow Model Registry Workflows"
    url: "https://mlflow.org/docs/latest/ml/model-registry/workflow/"
  - title: "MLflow Documentation"
    url: "https://mlflow.org/docs/latest/ml/"
---

## Reproducibility & Versioning

If you can't reproduce a model's results, you can't debug it, improve it, or trust it. Reproducibility is the foundation of reliable ML systems, and versioning is how you achieve it.

### Why Reproducibility Matters

**Debugging:** When a model fails in production, you need to recreate the exact training conditions to understand why.

**Compliance:** Regulators may require you to demonstrate how a model was trained and what data it used.

**Collaboration:** Team members need to build on each other's work without breaking it.

**Audit trails:** Complete version history enables investigation and accountability.

### Code Versioning with Git

Git tracks every change to your source code, configuration, and pipeline definitions. Best practices:

- Every training run should be tied to a specific Git commit
- Use meaningful commit messages that describe what changed
- Tag releases for deployed models
- Avoid untracked local changes

### Data Versioning with DVC

Git can't handle large datasets (GBs or TBs). DVC (Data Version Control) solves this by:
- Storing small `.dvc` placeholder files in Git (containing MD5 checksums)
- Storing actual data in cloud storage (S3, GCS, Azure)
- Using `dvc add` to track datasets and `dvc push/pull` to sync

```bash
dvc init
dvc add data/training.csv
git add data/training.csv.dvc .gitignore
git commit -m "Track training data v1"
dvc push
```

To switch data versions: `git checkout` + `dvc checkout`.

### Model Versioning

Ad-hoc naming (`model_v2_final_final.pt`) doesn't scale. Model registries provide:
- **Automatic versioning:** v1, v2, v3 on each registration
- **Lineage tracking:** Links model to experiment, data, and code
- **Stage transitions:** Development → Staging → Production
- **Aliases and tags:** `@champion`, `@production`, `approved`

### Environment Management

Reproducible environments require:
- **Dependency pinning:** Lock exact library versions (`requirements.txt`, `poetry.lock`)
- **Containerization:** Docker images package code, runtime, and dependencies
- **Deterministic training:** Set random seeds across all libraries

```python
import random, numpy as np, torch
random.seed(42)
np.random.seed(42)
torch.manual_seed(42)
```

### Common Mistakes

- **Not versioning data:** Code versioning without data versioning gives incomplete reproducibility.
- **Floating dependencies:** Using `pandas>=1.0` instead of `pandas==2.1.0` causes silent breakage.
- **Ignoring randomness:** Without setting seeds, results vary between runs.
- **No model registry:** Without structured model management, you can't track what's in production.

---

*Continue to learn about data pipelines — building reliable data flows for ML.*
