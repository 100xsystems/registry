---
slug: mlops-01-what-is-mlops
title: "What Is MLOps?"
description: "The engineering discipline that bridges ML research and production — automating the end-to-end machine learning lifecycle."
order: 1
tags:
  - mlops
  - ml-engineering
  - devops
  - production-ml
prerequisites: []
knowledge_refs:
  - slug: mlops-02-the-ml-lifecycle
    title: "The ML Lifecycle"
  - slug: mlops-16-cicd-for-ml
    title: "CI/CD for Machine Learning"
references:
  - title: "Google Cloud — MLOps: Continuous Delivery and Automation Pipelines"
    url: "https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning"
  - title: "AWS — MLOps Best Practices"
    url: "https://docs.aws.amazon.com/whitepapers/latest/ml-best-practices-public-sector-organizations/mlops.html"
  - title: "Microsoft Azure — MLOps Maturity Model"
    url: "https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/mlops-maturity-model"
  - title: "Hidden Technical Debt in Machine Learning Systems (Sculley et al., 2015)"
    url: "https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html"
  - title: "MLOps: Overview, Definition, and Architecture (IEEE Access)"
    url: "https://en.wikipedia.org/wiki/MLOps"
---

## What Is MLOps?

MLOps (Machine Learning Operations) is the engineering discipline that makes machine learning work in production. It combines ML, software engineering, and data engineering to automate and govern the entire lifecycle — from data collection and model training to deployment and monitoring.

### Why MLOps Exists

Most ML projects never reach production. Studies show up to 87% of ML models fail to deploy. The reason isn't poor model quality — it's poor engineering.

Google's landmark 2015 paper "Hidden Technical Debt in Machine Learning Systems" revealed that actual ML code accounts for only a tiny fraction of a production system. The vast majority is data collection, feature extraction, monitoring, configuration, and serving infrastructure.

MLOps exists to build and manage that infrastructure systematically.

### From DevOps to MLOps

**DevOps** bridged the gap between developers and operations through CI/CD, version control, and automation. It works for traditional software.

**MLOps** extends DevOps with ML-specific challenges:
- **Data is part of the product** — code + data = behavior
- **Models decay silently** — performance degrades as data distributions shift
- **Reproducibility is hard** — randomness in training, large datasets, complex environments
- **Multiple artifacts to track** — code, data, models, features, configs, environments

### The MLOps Maturity Model

Microsoft and Google define MLOps maturity in levels:

**Level 0 — Manual:** Data scientists work in notebooks, hand off models manually, releases happen a few times a year. No CI/CD, no monitoring.

**Level 1 — Pipeline Automation:** Training is automated into pipelines. Data validation, model validation, and automatic retraining are introduced.

**Level 2 — CI/CD:** Full integration of continuous integration and deployment for both code and models. Automated testing, canary deployments, A/B testing.

**Level 3 — Full Automation:** The entire system operates with maximum automation. Drift detection triggers retraining. Policy-based model promotion. Near-zero manual intervention.

### Core Practices

- **Continuous Training (CT):** Automatically retrain models on fresh data
- **Experiment Tracking:** Log every training run's parameters, metrics, and artifacts
- **Model Registry:** Version and govern model artifacts centrally
- **Feature Stores:** Ensure consistent feature computation across training and serving
- **Monitoring:** Track model performance and data drift in production
- **CI/CD for ML:** Automate testing and deployment of data pipelines and models

### Common Mistakes

- **Treating ML like traditional software:** ML systems need data pipelines, not just code pipelines.
- **Skipping monitoring:** Models decay silently without monitoring.
- **Manual deployment:** Hand-off between data scientists and engineers creates bottlenecks.
- **No reproducibility:** Without versioning, you can't debug or reproduce model behavior.

---

*Continue to learn about the ML lifecycle — the stages from problem framing to production monitoring.*
