---
slug: mlops-13-deployment-strategies
title: "Model Deployment Strategies"
description: "Safe ways to ship models to production — canary, blue-green, shadow deployment, A/B testing, and rollback strategies."
order: 13
tags:
  - mlops
  - deployment
  - canary
  - blue-green
  - shadow-deployment
  - ab-testing
prerequisites:
  - mlops-12-kubernetes-basics
knowledge_refs:
  - mlops-12-kubernetes-basics
    title: "Kubernetes Basics for ML"
  - mlops-10-model-serving
    title: "Model Serving APIs"
  - mlops-14-monitoring-and-drift
    title: "Monitoring & Drift Detection"
references:
  - title: "Shadow Mode, Canary Deployments, and A/B Testing for LLMs"
    url: "https://tianpan.co/blog/2026-04-09-llm-gradual-rollout-shadow-canary-ab-testing"
  - title: "Model Deployment: Strategies, Best Practices, and Use Cases"
    url: "https://www.qwak.com/post/model-deployment"
  - title: "Canary Model Deployment Guide"
    url: "https://oneuptime.com/blog/post/2026-01-30-mlops-canary-model-deployment/view"
  - title: "KServe — Model Serving on Kubernetes"
    url: "https://kserve.github.io/website/"
  - title: "Argo Rollouts — Progressive Delivery"
    url: "https://argo-rollouts.readthedocs.io/"
---

## Model Deployment Strategies

How you deploy a model determines how quickly you can detect failures and how much damage a bad model causes. The right strategy balances risk, cost, and velocity.

### Shadow Deployment (Dark Launch)

The candidate model runs alongside production but never serves users. Both models receive requests, but only the production model's predictions are returned. The candidate's predictions are logged for comparison.

**When to use:** First deployment of a new model, testing infrastructure changes, validating feature pipelines.

**Pros:** Zero risk to users. Verifies latency and behavior under real traffic.

**Cons:** Doubles infrastructure costs. Cannot measure user interaction metrics.

### Canary Deployment

A small fraction of traffic (0.1–5%) is routed to the new model. If metrics remain stable, traffic gradually increases.

**When to use:** Routine model updates with known-good behavior.

**Pros:** Limits blast radius. Automated rollback on metric degradation.

**Cons:** Requires sticky routing (consistent user assignment). More complex than simple replacement.

### Blue-Green Deployment

Two identical environments (blue and green). One serves production, the other receives the new model. Traffic switches atomically.

**When to use:** When you need instant rollback and zero-downtime deployment.

**Pros:** Instant rollback by switching traffic back. Clean separation of environments.

**Cons:** Requires double the infrastructure. Doesn't provide gradual exposure.

### A/B Testing

Users are split into randomized cohorts seeing different models. Statistical analysis determines which model performs better on business metrics.

**When to use:** When you need to measure user impact, not just technical metrics.

**Pros:** Measures real business impact (clicks, conversions, revenue).

**Cons:** Requires significant traffic for statistical significance. Longer experiment cycles.

### Automated Rollback

Connect monitoring to deployment orchestration. If error rates, latency, or drift metrics cross thresholds, automatically roll back to the previous version.

### Common Mistakes

- **Direct deployment:** Pushing to production without any safety mechanism is gambling.
- **No monitoring during deployment:** Canary deployments need real-time metric comparison.
- **Ignoring user consistency:** Users seeing different model versions in one session degrades experience.
- **Over-complicating:** Start with canary. Add complexity only when needed.

---

*Continue to learn about monitoring and drift detection — watching for model decay in production.*
