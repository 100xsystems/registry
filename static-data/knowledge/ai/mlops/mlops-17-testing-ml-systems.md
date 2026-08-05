---
slug: mlops-17-testing-ml-systems
title: "Testing ML Systems"
description: "Testing beyond code — data testing, model testing, pipeline testing, and integration testing for ML systems."
order: 17
tags:
  - mlops
  - testing
  - data-testing
  - model-testing
  - pipeline-testing
prerequisites:
  - mlops-16-cicd-for-ml
knowledge_refs:
  - slug: mlops-16-cicd-for-ml
    title: "CI/CD for Machine Learning"
  - slug: mlops-14-monitoring-and-drift
    title: "Monitoring & Drift Detection"
  - slug: mlops-03-reproducibility-and-versioning
    title: "Reproducibility & Versioning"
references:
  - title: "Made With ML — Testing ML Systems"
    url: "https://madewithml.com/courses/mlops/testing/"
  - title: "Evidently AI — Evaluation and Observability"
    url: "https://www.evidentlyai.com/"
  - title: "Google Cloud — MLOps CI/CD"
    url: "https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning"
  - title: "Great Expectations — Data Validation"
    url: "https://greatexpectations.io/"
  - title: "Pytest — Python Testing Framework"
    url: "https://docs.pytest.org/"
---
## Testing ML Systems

ML systems are probabilistic, data-dependent, and prone to silent failures. Testing must go beyond traditional unit tests to cover data, models, and pipelines.

### Data Testing

Data is the code of ML systems. Bad data produces bad models regardless of code quality.

**What to test:**
- **Schema:** Column names, data types, nullability
- **Statistics:** Value ranges, distribution bounds, uniqueness
- **Quality:** Missing values, duplicates, formatting errors
- **Drift:** Distribution changes between training and production

**Tools:** Great Expectations, Pandera, Evidently AI

### Model Testing

Models need behavioral testing, not just accuracy metrics.

**What to test:**
- **Performance:** Accuracy, precision, recall, F1 against baseline
- **Invariance:** Changing non-sensitive features shouldn't flip predictions
- **Directional expectations:** Increasing a feature should move predictions in expected direction
- **Slice performance:** Model shouldn't disproportionately fail on subgroups
- **Robustness:** Behavior under adversarial or edge-case inputs

### Pipeline Testing

ML pipelines orchestrate data processing, training, and deployment.

**What to test:**
- **Idempotency:** Running the same pipeline twice produces identical results
- **Trigger conditions:** CT triggers fire correctly (drift, schedule, new data)
- **Data flow:** Features flow correctly between pipeline stages
- **Error handling:** Pipeline fails gracefully on bad data

### Integration Testing

Verify that all components work together end-to-end.

**What to test:**
- **End-to-end flow:** Raw data → features → model → predictions
- **API contracts:** Serving API accepts the same features produced by training
- **Registry integration:** Models register, version, and deploy correctly
- **Monitoring integration:** Monitoring detects injected failures

### Testing Frameworks

- **pytest:** Unit and integration testing for Python code
- **Great Expectations:** Data validation and quality testing
- **Evidently AI:** Data drift, model performance, and monitoring tests
- **Seldon Alibi:** Model explanation and adversarial robustness testing

### Common Mistakes

- **Only unit testing:** Code tests don't catch data or model issues.
- **No data validation:** Assumed-clean data often isn't.
- **Testing on training data:** Always test on held-out data.
- **No integration tests:** Components that work individually may fail together.

---

*Continue to learn about data and model governance — ensuring compliance and accountability.*
