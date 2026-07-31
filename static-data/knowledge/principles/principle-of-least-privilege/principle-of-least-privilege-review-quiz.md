---
title: "Least Privilege: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate least-privilege concepts"
  - "Scope grants correctly"
  - "Design zero-trust access"
prerequisites:
  []
knowledge_refs:
  - "principles/principle-of-least-privilege"
---

# Least Privilege: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Least privilege grants? (A: everything / B: the minimum needed / C: admin by default)
- Q2: Blast radius scales with? (A: granted privilege / B: team size / C: latency)
- Q3: Zero trust assumes? (A: the network is trusted / B: nothing is implicitly trusted / C: VPN is enough)
- Q4: True or false: short-lived credentials reduce leaked-key risk.
- Q5: Temporary escalation should have? (A: approval and expiry / B: no limit / C: a wiki note)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A leaked read-only reports key exposes all customer data because the reports bucket contains PII. Redesign the bucket layout and policy so a report key cannot reach PII.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "admin for everyone is simpler" is how breaches become total.

## Key Takeaways

- Q1: B; Q2: A; Q3: B; Q4: true; Q5: A
- Scope by resource, row, column, and time
- Zero trust and capabilities operationalize it
