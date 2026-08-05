---
slug: safety-13-auditing-models
title: "Auditing AI Systems"
description: "Formal frameworks for verifying AI safety and compliance — auditing methodologies, third-party audits, and continuous monitoring."
order: 13
tags:
  - ai-safety
  - auditing
  - compliance
  - monitoring
  - iso-42001
prerequisites:
  - safety-08-governance
knowledge_refs:
  - slug: safety-08-governance
    title: "AI Governance & Policy"
  - slug: safety-10-safety-evaluations
    title: "Safety Evaluations"
  - slug: safety-09-transparency
    title: "Transparency & Disclosure"
references:
  - title: "NIST AI Risk Management Framework"
    url: "https://www.nist.gov/itl/ai-risk-management-framework"
  - title: "EU AI Act — Regulation (EU) 2024/1689"
    url: "https://artificialintelligenceact.eu/the-act/"
  - title: "ISO/IEC 42001:2023 AI Management System"
    url: "https://learn.microsoft.com/en-us/compliance/regulatory/offering-iso-42001"
  - title: "NIST AI RMF Playbook"
    url: "https://airc.nist.gov/airmf-resources/playbook/"
  - title: "CSA — ISO 42001 Lessons Learned"
    url: "https://cloudsecurityalliance.org/blog/2025/05/08/iso-42001-lessons-learned-from-auditing-and-implementing-the-framework"
---
## Auditing AI Systems

AI auditing is the systematic evaluation of AI systems against safety, fairness, and compliance standards. It's not optional — regulations like the EU AI Act require it, and market trust demands it.

### Auditing Frameworks

**NIST AI RMF:** Four continuous functions — Govern, Map, Measure, Manage. Organizations use this framework to build internal risk management processes that satisfy regulatory requirements.

**ISO/IEC 42001:2023:** The first certifiable international standard for AI management systems. It follows the Plan-Do-Check-Act cycle with 38 controls across 9 objectives. Certification requires external audits by accredited bodies.

**EU AI Act conformity assessments:** For high-risk AI systems, providers must perform formal conformity assessments before deployment. Independent notified bodies verify compliance for high-stakes domains like biometrics, healthcare, and law enforcement.

### Third-Party Audits

Self-attestation isn't enough. Independent audits provide:
- **Objective verification:** External auditors have no stake in the system passing
- **Standardized methodology:** Audits follow established frameworks, enabling comparison
- **Legal protection:** Third-party certification demonstrates due diligence

**ISO 42001 certification process:**
1. Stage 1: Readiness and design review
2. Stage 2: Operational effectiveness audit
3. Annual surveillance audits
4. Recertification every 3 years

### Continuous Monitoring

AI systems change over time. Models drift, data distributions shift, and new vulnerabilities emerge. Continuous monitoring tracks:
- **Performance metrics:** Accuracy, latency, error rates
- **Safety metrics:** Toxicity rates, refusal rates, content filter triggers
- **Fairness metrics:** Demographic parity, equalized odds across groups
- **Drift detection:** Changes in input distribution or model behavior

### Audit Trails

Audit trails log every decision, input, output, and guardrail action. They're essential for:
- **Incident investigation:** When something goes wrong, you need to trace what happened
- **Regulatory reporting:** The EU AI Act requires reporting of serious incidents
- **Legal defense:** Demonstrating due diligence in court
- **Model improvement:** Understanding failure patterns

### Common Mistakes

- **Point-in-time audits:** A single audit isn't enough. AI systems need continuous monitoring.
- **Checking boxes without substance:** Compliance theater doesn't improve safety.
- **Ignoring organizational factors:** Most AI failures stem from organizational issues, not technical ones.

---

*Continue to learn about the societal impact of AI — how it affects jobs, inequality, and power structures.*
