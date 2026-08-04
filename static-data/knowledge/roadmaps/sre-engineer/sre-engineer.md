---
slug: sre-engineer
title: "SRE Roadmap"
description: "Complete learning path for site reliability engineers — monitoring, incident response, SLIs/SLOs, and chaos engineering."
order: 9
tags:
  - roadmap
  - sre
  - reliability
  - monitoring
  - incident-response
---

# SRE Roadmap

A structured learning path for applying software engineering principles to infrastructure and operations.

## Phase 1: Foundations (Weeks 1-6)

### Step 1: Linux Systems
- Kernel troubleshooting
- CPU/memory/disk analysis
- Network diagnostics (tcpdump, netstat)
- Performance profiling

### Step 2: Programming
- Python or Go for automation
- Scripting for toil reduction
- Building internal tools
- API interaction

**→ [Languages: Python](/knowledge/languages/python) | [Go](/knowledge/languages/go)**

### Step 3: Networking Deep Dive
- TCP/IP internals
- DNS resolution
- HTTP/HTTPS protocols
- Load balancing algorithms

**→ [System Design: Load Balancers](/knowledge/system-design/building-blocks-load-balancers)**

## Phase 2: SRE Core (Weeks 7-14)

### Step 4: SRE Fundamentals
- Google SRE principles
- SLIs, SLOs, SLAs
- Error budgets
- Toil reduction

### Step 5: Monitoring & Observability
- Metrics (Prometheus)
- Dashboards (Grafana)
- Log aggregation (ELK, Loki)
- Distributed tracing (Jaeger, OpenTelemetry)

**→ [System Design: Fundamentals](/knowledge/system-design/fundamentals-availability)**

### Step 6: Alerting
- Designing high-signal alerts
- Alert fatigue prevention
- PagerDuty / Opsgenie
- Runbooks and escalation

### Step 7: Incident Management
- Incident commander role
- Communication during incidents
- War room practices
- Blameless postmortems

## Phase 3: Reliability Engineering (Weeks 15-22)

### Step 8: Capacity Planning
- Load testing (k6, Locust)
- Performance benchmarking
- Growth forecasting
- Resource provisioning

### Step 9: Chaos Engineering
- Failure injection
- Game days
- Steady-state hypothesis
- Blast radius control

**→ [Case Studies: Netflix Chaos Engineering](/knowledge/case-studies/netflix-streaming)**

### Step 10: Disaster Recovery
- RTO and RPO definitions
- Backup strategies
- Failover mechanisms
- DR testing

**→ [System Design: Availability](/knowledge/system-design/fundamentals-availability)**

### Step 11: Performance Engineering
- Latency analysis
- Throughput optimization
- Resource utilization
- Bottleneck identification

## Phase 4: Advanced (Weeks 23-30)

### Step 12: Automation
- Toil elimination through code
- Self-healing systems
- Automated remediation
- ChatOps

### Step 13: Cost Management
- Resource rightsizing
- Cost attribution
- Budget alerts
- FinOps practices

### Step 14: Compliance & Governance
- Audit logging
- Security controls
- Compliance frameworks
- Policy enforcement

---

*Each step links to existing knowledge topics. Click through for deep dives.*
