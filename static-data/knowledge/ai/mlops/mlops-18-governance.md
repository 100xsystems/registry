---
slug: mlops-18-governance
title: "Data & Model Governance"
description: "Ensuring compliance and accountability — governance frameworks, data lineage, audit trails, and access control for ML."
order: 18
tags:
  - mlops
  - governance
  - compliance
  - audit-trails
  - access-control
prerequisites:
  - mlops-04-data-pipelines
knowledge_refs:
  - mlops-04-data-pipelines
    title: "Data Pipelines"
  - mlops-07-model-registry
    title: "Model Registry"
  - safety-08-governance
    title: "AI Governance & Policy"
references:
  - title: "ISO/IEC 42001:2023 — AI Management System"
    url: "https://www.iso.org/standard/42001"
  - title: "NIST AI Risk Management Framework"
    url: "https://www.nist.gov/itl/ai-risk-management-framework"
  - title: "CSA — AICM Auditing Guidelines for Model Providers"
    url: "https://cloudsecurityalliance.org/artifacts/aicmv1-1-auditing-guidelines-for-model-providers-mp"
  - title: "AWS — AI Lifecycle Risk Management with ISO 42001"
    url: "https://aws.amazon.com/blogs/security/ai-lifecycle-risk-management-iso-iec-420012023-for-ai-governance/"
  - title: "SureCloud — NIST AI RMF vs ISO 42001"
    url: "https://www.surecloud.com/blog-hub/nist-ai-rmf-vs-iso-42001"
---

## Data & Model Governance

Governance ensures ML systems are accountable, compliant, and trustworthy. It defines who can build, approve, and deploy models — and proves they did so responsibly.

### Why Governance Matters

**Regulatory compliance:** The EU AI Act, GDPR, and sector-specific regulations require documentation and audit trails for AI systems.

**Accountability:** When AI causes harm, governance frameworks establish who is responsible.

**Trust:** Customers, regulators, and partners need evidence that AI systems are well-managed.

### Governance Frameworks

**ISO/IEC 42001:2023:** The first certifiable AI management system standard. Plan-Do-Check-Act cycle with 38 controls. Requires formal leadership commitments, named owners, and documented risk assessments.

**NIST AI RMF:** Voluntary framework with four functions — Govern, Map, Measure, Manage. Focuses on risk identification, assessment, and mitigation.

### Data Lineage

ML systems depend on data quality and provenance. Lineage tracking records:
- Where data came from (source systems)
- How it was transformed (feature engineering code)
- Which models used it (training data versions)
- How it was validated (quality checks)

Tools like MLflow, Delta Lake, and data catalogs provide lineage tracking.

### Audit Trails

Regulated environments require tamper-proof logs of:
- Every model version registered and deployed
- Every training run and its inputs/outputs
- Every prediction served and its context
- Every access to model artifacts and data

Use append-only logs and cloud audit services (AWS CloudTrail, GCP Audit Logs).

### Access Control

**Role-based access control (RBAC):** Restrict who can:
- Train models (data scientists)
- Register models (ML engineers)
- Deploy to production (MLOps engineers)
- Access sensitive data (data engineers)

**Least privilege:** Give each role only the permissions it needs.

### Common Mistakes

- **No governance:** Without governance, you can't demonstrate compliance.
- **Paper governance:** Documents that exist but aren't followed are worthless.
- **Ignoring lineage:** Without data lineage, you can't audit model behavior.
- **Overly restrictive access:** Governance shouldn't block legitimate work.

---

*Continue to learn about cost and performance optimization — making ML systems efficient.*
