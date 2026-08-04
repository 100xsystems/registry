---
slug: mlops-05-feature-stores
title: "Feature Stores"
description: "Serving features consistently across training and inference — Feast, Tecton, online vs offline stores, and point-in-time correctness."
order: 5
tags:
  - mlops
  - feature-stores
  - feast
  - feature-engineering
  - point-in-time
prerequisites:
  - mlops-04-data-pipelines
knowledge_refs:
  - mlops-04-data-pipelines
    title: "Data Pipelines"
  - mlops-06-experiment-tracking
    title: "Experiment Tracking"
  - mlops-10-model-serving
    title: "Model Serving APIs"
references:
  - title: "Feast — Point-in-Time Joins"
    url: "https://docs.feast.dev/getting-started/concepts/point-in-time-joins"
  - title: "Feast — Introduction"
    url: "https://docs.feast.dev/"
  - title: "Tecton Concepts"
    url: "https://docs.tecton.ai/docs/0.9/introduction/tecton-concepts"
  - title: "Databricks — Point-in-Time Feature Joins"
    url: "https://docs.databricks.com/aws/en/machine-learning/feature-store/time-series"
  - title: "Databricks Blog — What Is a Feature Store?"
    url: "https://www.databricks.com/blog/what-feature-store-complete-guide-ml-feature-engineering"
---

## Feature Stores

A feature store is the centralized infrastructure layer that provides a single source of truth for defining, storing, and serving ML features. It eliminates feature duplication, prevents train-serve skew, and enables feature reuse across teams and models.

### The Problem Feature Stores Solve

Without a feature store:
- Data scientists write custom feature extraction code for each model
- Training uses one feature computation; serving uses another
- Feature logic is duplicated across notebooks and production code
- No one knows which features exist or how they're computed

A feature store standardizes feature definitions as code, stores them centrally, and serves them consistently for both training and real-time inference.

### Online vs. Offline Features

**Offline feature store:** Optimized for batch processing and historical analytics. Stores months or years of historical feature data for model training and backfilling. Powered by data warehouses (Snowflake, BigQuery, Delta Lake).

**Online feature store:** Designed for real-time, low-latency lookups (<10ms). Holds the latest pre-computed feature values for production inference. Powered by key-value stores (Redis, DynamoDB).

Most feature stores maintain both, with automatic synchronization between them.

### Point-in-Time Correctness

Point-in-time correctness ensures training data reflects the exact feature values available at the moment each observation was recorded. Without this, future values leak into training data (data leakage), creating overly optimistic metrics that collapse in production.

Feature stores execute temporal joins that look backward from each event timestamp to find the most recent valid feature state — preventing leakage automatically.

### Leading Tools

**Feast:** Open-source, lightweight, works on top of existing data infrastructure. Good for teams with existing data warehouses.

**Tecton:** Enterprise-grade, manages full feature pipelines as code, includes streaming and batch orchestration, lineage tracking, and monitoring.

### Common Mistakes

- **No feature store:** Teams duplicate feature logic across models, creating inconsistency and technical debt.
- **Ignoring online/offline parity:** Features computed differently in training vs. serving cause silent model failures.
- **No point-in-time correctness:** Training on future data produces models that fail in production.
- **Not versioning features:** Feature definitions should be versioned like code.

---

*Continue to learn about experiment tracking — logging every training run's parameters and metrics.*
