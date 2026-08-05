---
slug: mlops-04-data-pipelines
title: "Data Pipelines"
description: "Building reliable data flows for ML — ETL/ELT, data validation, orchestration with Airflow and Prefect, and data contracts."
order: 4
tags:
  - mlops
  - data-pipelines
  - etl
  - airflow
  - prefect
  - data-contracts
prerequisites:
  - mlops-03-reproducibility-and-versioning
knowledge_refs:
  - slug: mlops-03-reproducibility-and-versioning
    title: "Reproducibility & Versioning"
  - slug: mlops-05-feature-stores
    title: "Feature Stores"
  - slug: mlops-16-cicd-for-ml
    title: "CI/CD for Machine Learning"
references:
  - title: "ZenML — Prefect vs. Airflow Comparison"
    url: "https://www.zenml.io/blog/prefect-vs-airflow"
  - title: "Apache Airflow — MLOps Use Cases"
    url: "https://airflow.apache.org/use-cases/mlops/"
  - title: "Data Contracts: The Essential Guide"
    url: "https://www.ml4devs.com/what-is/data-contracts/"
  - title: "Data Contracts Explained — Atlan"
    url: "https://atlan.com/atlan-com/data-contracts/"
  - title: "Apache Airflow Architecture Overview"
    url: "https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/overview.html"
---
## Data Pipelines

Data pipelines are the circulatory system of ML. They move data from source to feature store to model to monitoring — reliably, efficiently, and with quality guarantees.

### ETL vs. ELT

**ETL (Extract, Transform, Load):** Data is cleaned and transformed before loading into the target system. Good for resource-constrained environments where raw storage is expensive.

**ELT (Extract, Load, Transform):** Raw data lands first, transformations happen in the warehouse. This is the modern standard for ML because it preserves raw data for auditing and feature engineering reproducibility.

### Data Validation

Catching data problems early prevents downstream model failures:

**Schema validation:** Enforce data types, required fields, and structural constraints. Tools like Great Expectations and Pandera automate this.

**Semantic validation:** Check business rules — age should be 0–120, prices shouldn't be negative, required fields shouldn't be null.

**Freshness validation:** Ensure data arrives on time. Stale data produces stale models.

### Orchestration Tools

**Apache Airflow:** The industry standard. Defines workflows as Python DAGs (Directed Acyclic Graphs). Highly extensible with hundreds of operators. Best for large data engineering teams with complex batch workflows.

**Prefect:** Python-native orchestrator using `@flow` and `@task` decorators. Lighter weight, more flexible for dynamic workflows. Best for ML teams wanting a streamlined, code-first experience.

**Key difference:** Airflow requires explicit DAG definitions. Prefect infers the DAG from function calls.

### Data Contracts

Data contracts are formal agreements between data producers and consumers:
- **Schema contracts:** What fields exist and their types
- **Quality contracts:** What values are acceptable
- **SLA contracts:** When data must arrive

Contracts prevent upstream changes from breaking downstream feature pipelines and models. They're enforced in CI/CD — violating a contract blocks deployment.

### Common Mistakes

- **No data validation:** Assuming upstream data is always correct.
- **Tight coupling:** Pipelines that depend on specific infrastructure break when infrastructure changes.
- **No SLAs:** Without freshness guarantees, models train on stale data.
- **Ignoring backfills:** When you fix a pipeline bug, you need to backfill historical data.

---

*Continue to learn about feature stores — serving features consistently across training and inference.*
