---
slug: mlops-06-experiment-tracking
title: "Experiment Tracking"
description: "Logging every training run's parameters, metrics, and artifacts — MLflow, Weights & Biases, and systematic experiment management."
order: 6
tags:
  - mlops
  - experiment-tracking
  - mlflow
  - weights-biases
  - metrics
prerequisites:
  - mlops-03-reproducibility-and-versioning
knowledge_refs:
  - slug: mlops-03-reproducibility-and-versioning
    title: "Reproducibility & Versioning"
  - slug: mlops-07-model-registry
    title: "Model Registry"
  - slug: mlops-08-training-at-scale
    title: "Training at Scale"
references:
  - title: "MLflow Documentation"
    url: "https://mlflow.org/docs/latest/ml/"
  - title: "Weights & Biases Documentation"
    url: "https://docs.wandb.ai/"
  - title: "MLflow vs W&B Comparison"
    url: "https://neptune.ai/blog/mlflow-vs-weights-and-biases"
  - title: "Google Cloud — Experiment Tracking"
    url: "https://cloud.google.com/vertex-ai/docs/experiments"
  - title: "Neptune.ai — Experiment Tracking Guide"
    url: "https://neptune.ai/blog/experiment-tracking"
---
## Experiment Tracking

Every ML experiment generates data — hyperparameters, metrics, code versions, model artifacts. Without systematic tracking, this knowledge is lost in notebooks, local directories, and memory. Experiment tracking captures everything so you can compare, reproduce, and build on past work.

### What to Track

**Inputs:**
- Hyperparameters (learning rate, batch size, architecture choices)
- Data version (which dataset was used)
- Code version (Git commit hash)
- Environment (library versions, GPU type)

**Outputs:**
- Training/validation metrics over time (loss curves, accuracy)
- Final evaluation metrics on test set
- Model artifacts (weights, checkpoints)
- Generated visualizations (confusion matrices, ROC curves)

**Metadata:**
- Training duration
- GPU utilization
- Experiment name and description
- Tags for organization

### Leading Tools

**MLflow:** Open-source, widely adopted. Provides experiment tracking, model registry, and deployment in one platform. Integrates with any ML framework. Self-hostable.

**Weights & Biases (W&B):** Cloud-native platform with superior visualization, collaborative features, and hyperparameter sweeps. Strong community adoption in research.

**Neptune.ai:** Metadata store focused on experiment tracking with rich visualization and team collaboration.

### Best Practices

- **Log everything automatically:** Don't rely on manual logging. Use API integrations.
- **Use consistent naming:** Establish conventions for experiment names, tags, and descriptions.
- **Link experiments to code:** Always log the Git commit hash with each experiment.
- **Compare systematically:** Use dashboards to compare experiments side-by-side.
- **Clean up:** Archive old experiments to keep the workspace manageable.

### Common Mistakes

- **Manual logging:** Copying metrics by hand is error-prone and incomplete.
- **No code versioning:** Without Git commits, you can't recreate the experiment.
- **Ignoring training curves:** Final metrics don't tell the whole story. Training dynamics matter.
- **Not sharing:** Experiments locked in personal accounts don't help the team.

---

*Continue to learn about model registries — governing and versioning model artifacts.*
