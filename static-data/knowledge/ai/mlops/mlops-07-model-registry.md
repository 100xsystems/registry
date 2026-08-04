---
slug: mlops-07-model-registry
title: "Model Registry"
description: "Centralized model governance — versioning, staging, aliases, champion/challenger patterns, and deployment workflows."
order: 7
tags:
  - mlops
  - model-registry
  - model-versioning
  - governance
  - champion-challenger
prerequisites:
  - mlops-06-experiment-tracking
knowledge_refs:
  - mlops-06-experiment-tracking
    title: "Experiment Tracking"
  - mlops-13-deployment-strategies
    title: "Model Deployment Strategies"
  - mlops-18-governance
    title: "Data & Model Governance"
references:
  - title: "MLflow Model Registry Documentation"
    url: "https://mlflow.org/docs/latest/ml/model-registry/"
  - title: "MLflow Model Registry Workflows"
    url: "https://mlflow.org/docs/latest/ml/model-registry/workflow/"
  - title: "MLflow ML Lifecycle Management"
    url: "https://mlflow.org/articles/ml-lifecycle-management-explained-for-engineers/"
  - title: "Databricks — Model Lifecycle Management"
    url: "https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/"
  - title: "Champion-Challenger Pattern for Model Governance"
    url: "https://stacksimplify.com/blog/ml-governance-model-registry/"
---

## Model Registry

A model registry is the single source of truth for all trained models. It manages versioning, staging, governance, and deployment workflows — bridging the gap between experimentation and production.

### What a Model Registry Does

**Versioning:** Each time a model is registered, it gets an incrementing version number. No more `model_v2_final_final.pt`.

**Lineage:** Every version links back to the exact training run, code commit, data version, and hyperparameters that produced it.

**Staging:** Models move through lifecycle stages: Development → Staging → Production → Archived.

**Governance:** Role-based access controls ensure only authorized users can promote models to production.

### Modern Approach: Aliases Over Stages

Traditional registries used fixed stages (None → Staging → Production). Modern registries like MLflow 3 and Databricks Unity Catalog use **mutable aliases**:

- `@champion` — the model currently serving production traffic
- `@challenger` — the model being tested against the champion
- `@candidate` — a model pending evaluation

Production services reference models by alias (`models:/my_model@champion`), not version number. Updating production requires only reassigning the alias — zero code changes, zero downtime.

### The Champion/Challenger Pattern

The gold standard for high-stakes model deployments:

1. **Champion** serves live traffic
2. **Challenger** runs in shadow mode (generates predictions but doesn't serve users)
3. If challenger outperforms champion, reassign the `@champion` alias
4. If something goes wrong, reassign back to the previous version instantly

### Quality Gates

Before a model version is registered or promoted, automated evaluations verify:
- Performance metrics meet minimum thresholds
- Model signature matches expected input/output schema
- Fairness metrics pass bias checks
- Safety evaluations pass content filtering

### Common Mistakes

- **No registry:** Without centralized model management, you can't track what's in production.
- **Hardcoded versions:** Services that reference `model_v3` instead of `@champion` require code changes to update.
- **No quality gates:** Promoting untested models to production is gambling.
- **Missing lineage:** Without linking models to training data and code, you can't debug production issues.

---

*Continue to learn about training at scale — distributed training and GPU cluster management.*
