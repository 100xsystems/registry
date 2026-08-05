---
slug: mlops-14-monitoring-and-drift
title: "Monitoring & Drift Detection"
description: "Watching for model decay in production — data drift, concept drift, Evidently AI, dashboards, and alerting."
order: 14
tags:
  - mlops
  - monitoring
  - drift-detection
  - evidently
  - alerting
prerequisites:
  - mlops-13-deployment-strategies
knowledge_refs:
  - slug: mlops-13-deployment-strategies
    title: "Model Deployment Strategies"
  - slug: mlops-15-production-evaluation
    title: "Evaluation in Production"
  - slug: mlops-16-cicd-for-ml
    title: "CI/CD for Machine Learning"
references:
  - title: "Evidently AI — What Is Data Drift?"
    url: "https://www.evidentlyai.com/ml-in-production/data-drift"
  - title: "Evidently AI — What Is Concept Drift?"
    url: "https://www.evidentlyai.com/ml-in-production/concept-drift"
  - title: "Evidently AI — Data and Concept Drift"
    url: "https://www.evidentlyai.com/blog/machine-learning-monitoring-data-and-concept-drift"
  - title: "Evidently AI — ML Monitoring Dashboard Tutorial"
    url: "https://www.evidentlyai.com/blog/ml-model-monitoring-dashboard-tutorial"
  - title: "Evidently AI — ML Monitoring with Email Alerts"
    url: "https://www.evidentlyai.com/blog/ml-monitoring-with-email-alerts-tutorial"
---
## Monitoring & Drift Detection

Models decay silently. Unlike software bugs that cause crashes, ML model degradation is gradual and invisible without monitoring. Data drift, concept drift, and data quality issues slowly erode performance until someone notices — often too late.

### Data Drift

Data drift occurs when the statistical distribution of input features changes between training and production. The model encounters feature values it never saw during training.

**Example:** A fraud detection model trained on pre-pandemic transaction patterns fails when spending behavior shifts during lockdowns.

**Detection:** Statistical tests (Kolmogorov-Smirnov, Chi-Square, Population Stability Index) compare training and production distributions.

### Concept Drift

Concept drift occurs when the relationship between inputs and outputs changes. The features might look the same, but what they mean has shifted.

**Example:** A sentiment model trained to associate "unpredictable" with negative sentiment finds that in tech reviews, "unpredictable" becomes positive over time.

**Detection:** Monitor model accuracy over time as labels become available. Use prediction drift as a proxy when labels are delayed.

### Other Drift Types

**Prediction drift:** The distribution of model outputs shifts. Useful as an early warning when ground truth is delayed.

**Training-serving skew:** Structural mismatch between how features are computed in training vs. serving. Usually a pipeline bug, not environmental drift.

### Monitoring with Evidently AI

Evidently is an open-source Python framework for ML monitoring:

- **Reports:** Generate rich HTML/JSON visual summaries with statistical charts and metrics
- **Test Suites:** Automated pass/fail assertions against predefined thresholds
- **Integration:** Works with Streamlit dashboards, Airflow pipelines, and email alerting

### Alerting

Monitoring without alerting is just logging. Set up alerts for:
- Drift metrics exceeding thresholds
- Error rate spikes
- Latency anomalies
- Data quality issues (nulls, schema violations)

Connect alerts to Slack, email, or PagerDuty for immediate response.

### Common Mistakes

- **No monitoring:** Deploying without monitoring is flying blind.
- **Only monitoring accuracy:** Accuracy degrades slowly. Monitor data distributions and predictions too.
- **No alerting thresholds:** Alerts without thresholds produce noise, not signal.
- **Ignoring feedback delay:** In many domains (fraud, lending), labels arrive weeks later. Use proxy metrics.

---

*Continue to learn about evaluation in production — measuring model performance with live traffic.*
