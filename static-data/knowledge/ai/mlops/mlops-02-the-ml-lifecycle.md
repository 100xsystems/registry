---
slug: mlops-02-the-ml-lifecycle
title: "The ML Lifecycle"
description: "The stages from problem framing to production monitoring — and how each stage connects in an end-to-end ML system."
order: 2
tags:
  - mlops
  - ml-lifecycle
  - workflow
  - production-ml
prerequisites:
  - mlops-01-what-is-mlops
knowledge_refs:
  - mlops-01-what-is-mlops
    title: "What Is MLOps?"
  - mlops-04-data-pipelines
    title: "Data Pipelines"
  - mlops-14-monitoring-and-drift
    title: "Monitoring & Drift Detection"
references:
  - title: "Google Cloud — ML Lifecycle"
    url: "https://cloud.google.com/architecture/ml-lifecycle"
  - title: "MLflow — ML Lifecycle Management"
    url: "https://mlflow.org/docs/latest/ml/"
  - title: "AWS — MLOps Lifecycle"
    url: "https://aws.amazon.com/solutions/machine-learning/"
  - title: "The ML Lifecycle — Databricks"
    url: "https://www.databricks.com/discover-pages/ml-lifecycle"
  - title: "Chip Huyen — Designing Machine Learning Systems"
    url: "https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/"
---

## The ML Lifecycle

The ML lifecycle is the end-to-end process of building, deploying, and maintaining machine learning systems. Unlike traditional software, the lifecycle is circular — models need continuous retraining and monitoring.

### Stage 1: Problem Framing

Before writing code, define:
- **Business objective:** What problem are you solving?
- **ML formulation:** Is this classification, regression, ranking, generation?
- **Success metrics:** What accuracy, latency, or business metric defines success?
- **Constraints:** Latency budgets, fairness requirements, regulatory compliance

Skipping this stage is the #1 cause of ML project failure.

### Stage 2: Data Collection and Preparation

- **Data sourcing:** Where does the data come from? Internal databases, APIs, web scraping, sensors?
- **Data quality:** Is the data complete, accurate, and consistent?
- **Data labeling:** For supervised learning, who labels the data and how?
- **Data splits:** Train/validation/test sets with proper separation to prevent leakage

### Stage 3: Feature Engineering

Transform raw data into model-ready features:
- **Feature creation:** Domain-specific transformations (ratios, aggregations, embeddings)
- **Feature selection:** Identify which features matter
- **Feature scaling:** Normalize or standardize numerical features
- **Feature storage:** Store features in a feature store for reuse across models

### Stage 4: Model Development

- **Model selection:** Choose architecture based on problem, data, and constraints
- **Training:** Fit the model to training data
- **Hyperparameter tuning:** Optimize model configuration
- **Evaluation:** Measure performance on held-out data using appropriate metrics

### Stage 5: Deployment

Move the model from notebook to production:
- **Model packaging:** Serialize the model for serving
- **Serving infrastructure:** API endpoints, batch processing, edge deployment
- **Deployment strategy:** Canary, blue-green, shadow deployment
- **Integration:** Connect to downstream applications

### Stage 6: Monitoring and Maintenance

The lifecycle doesn't end at deployment:
- **Performance monitoring:** Track prediction quality over time
- **Data drift detection:** Monitor for changes in input data distribution
- **Concept drift detection:** Monitor for changes in the relationship between inputs and outputs
- **Retraining triggers:** Automatic or manual retraining based on drift signals

### The Feedback Loop

Production monitoring feeds back to data collection. Real-world failures become new training examples. This loop is what makes ML systems continuously improve — or continuously degrade if neglected.

### Common Mistakes

- **Starting with the model, not the problem:** Technology-first thinking wastes resources.
- **Ignoring data quality:** Poor data quality cannot be fixed by better models.
- **Treating deployment as the finish line:** The real work starts after deployment.
- **No feedback loop:** Without monitoring and retraining, models decay silently.

---

*Continue to learn about reproducibility and versioning — ensuring you can recreate any model.*
