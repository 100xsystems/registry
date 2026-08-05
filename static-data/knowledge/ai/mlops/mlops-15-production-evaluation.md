---
slug: mlops-15-production-evaluation
title: "Evaluation in Production"
description: "Measuring real-world model performance — online evaluation, A/B testing, shadow mode, and production metrics."
order: 15
tags:
  - mlops
  - evaluation
  - online-evaluation
  - ab-testing
  - production-metrics
prerequisites:
  - mlops-14-monitoring-and-drift
knowledge_refs:
  - slug: mlops-14-monitoring-and-drift
    title: "Monitoring & Drift Detection"
  - slug: mlops-13-deployment-strategies
    title: "Model Deployment Strategies"
  - slug: mlops-16-cicd-for-ml
    title: "CI/CD for Machine Learning"
references:
  - title: "Deploying ML Models in Shadow Mode"
    url: "https://christophergs.com/machine%20learning/2019/03/30/deploying-machine-learning-applications-in-shadow-mode/"
  - title: "Shadow Mode, Canary Deployments, and A/B Testing for LLMs"
    url: "https://tianpan.co/blog/2026-04-09-llm-gradual-rollout-shadow-canary-ab-testing"
  - title: "Canary Model Deployment Guide"
    url: "https://oneuptime.com/blog/post/2026-01-30-mlops-canary-model-deployment/view"
  - title: "Model Deployment: Strategies and Use Cases"
    url: "https://www.qwak.com/post/model-deployment"
  - title: "ML System Design — Evaluation"
    url: "https://www.hellointerview.com/learn/ml-system-design/core-concepts/evaluation"
---
## Evaluation in Production

Offline evaluation on test sets provides a baseline, but production is where truth lives. Real-world dynamics — data drift, user behavior, infrastructure constraints — can't be captured in offline tests.

### Why Online Evaluation Matters

Offline test sets are static. Production is dynamic. A model that scores 95% offline might score 70% in production due to:
- Distribution shift between training data and real traffic
- Latency constraints affecting model choice
- User behavior that differs from test scenarios
- Feedback loops where model predictions influence future data

### Evaluation Strategies

**Shadow mode:** Run the candidate model alongside production without serving users. Compare predictions offline. Zero risk, but can't measure user impact.

**Canary evaluation:** Route 0.1–5% of traffic to the new model. Monitor error rates, latency, and proxy metrics. Gradually increase if stable.

**A/B testing:** Split users into cohorts. Measure business metrics (clicks, conversions, revenue). Requires statistical significance.

**Interleaving:** For ranking/recommendation systems, mix results from two models into one list. 10–20× more statistically efficient than A/B testing.

### Production Metrics Stack

**Infrastructure metrics:** CPU/GPU utilization, memory, request throughput, latency percentiles (p50, p95, p99).

**ML metrics:** Error rates, refusal rates, drift scores, online accuracy (when labels are available).

**Business metrics:** User retention, click-through rate, task completion, cost per request.

### The Feedback Delay Problem

In many domains, ground truth arrives days or weeks later (fraud detection, loan defaults, churn). During this delay, you need proxy metrics:
- Feature drift as an early warning
- Prediction drift as a signal
- Human review of edge cases

### Common Mistakes

- **Only offline evaluation:** Test sets don't capture production dynamics.
- **No statistical rigor:** A/B tests need proper sample sizes and significance testing.
- **Ignoring latency:** A more accurate model that's 10× slower may be worse for users.
- **No rollback plan:** When production evaluation reveals problems, you need to revert quickly.

---

*Continue to learn about CI/CD for ML — automating testing and deployment of ML pipelines.*
