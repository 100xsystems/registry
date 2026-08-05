---
slug: mlops-16-cicd-for-ml
title: "CI/CD for Machine Learning"
description: "Automating testing and deployment of ML pipelines — continuous integration, continuous deployment, and continuous training for ML."
order: 16
tags:
  - mlops
  - cicd
  - automation
  - pipelines
  - continuous-training
prerequisites:
  - mlops-15-production-evaluation
knowledge_refs:
  - slug: mlops-15-production-evaluation
    title: "Evaluation in Production"
  - slug: mlops-17-testing-ml-systems
    title: "Testing ML Systems"
  - slug: mlops-04-data-pipelines
    title: "Data Pipelines"
references:
  - title: "Google Cloud — MLOps: CI/CD Pipelines"
    url: "https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning"
  - title: "Made With ML — CI/CD for ML"
    url: "https://madewithml.com/"
  - title: "GitHub Actions for ML"
    url: "https://docs.github.com/en/actions"
  - title: "Kubeflow Pipelines"
    url: "https://www.kubeflow.org/docs/components/pipelines/"
  - title: "MLflow — CI/CD Integration"
    url: "https://mlflow.org/docs/latest/ml/projects.html"
---
## CI/CD for Machine Learning

Traditional CI/CD tests code and deploys binaries. ML CI/CD extends this to test data, validate models, and deploy pipelines. It's the automation backbone of MLOps.

### The Three Pillars

**Continuous Integration (CI):** Every code change triggers automated tests. For ML, this includes:
- Code linting and unit tests
- Data validation (schema, quality, freshness)
- Model validation (performance against baseline)
- Pipeline integration tests

**Continuous Deployment (CD):** Automated deployment of validated models to production. Includes:
- Building and pushing container images
- Updating model registry entries
- Deploying to serving infrastructure
- Running smoke tests against the new deployment

**Continuous Training (CT):** Automatically retraining models when triggered by:
- Scheduled intervals (daily, weekly)
- Data drift detection
- Performance degradation alerts
- New data availability

### GitHub Actions for ML

```yaml
name: ML Pipeline
on:
  push:
    branches: [main]
jobs:
  test-data:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: python tests/test_data.py
  train-model:
    needs: test-data
    runs-on: ubuntu-latest
    steps:
      - run: python train.py
      - run: python tests/test_model.py
  deploy:
    needs: train-model
    runs-on: ubuntu-latest
    steps:
      - run: python deploy.py
```

### Pipeline Orchestration

**Kubeflow Pipelines:** Kubernetes-native ML pipelines. Define multi-step workflows with visual DAGs.

**MLflow Projects:** Package ML code as reproducible projects with environment specifications.

**Prefect/Airflow:** General-purpose orchestrators adapted for ML workflows.

### Best Practices

- **Test everything:** Data, code, models, and infrastructure
- **Automate retraining:** Don't rely on manual triggers
- **Use staging environments:** Test deployments before production
- **Implement rollback:** Every deployment should be reversible
- **Monitor after deployment:** CI/CD doesn't end at deployment

### Common Mistakes

- **Only testing code:** ML systems need data and model testing too.
- **No CT pipeline:** Models decay without automatic retraining.
- **Manual deployment:** Human deployment is slow and error-prone.
- **Skipping staging:** Deploying directly to production is gambling.

---

*Continue to learn about testing ML systems — data testing, model testing, and pipeline testing.*
