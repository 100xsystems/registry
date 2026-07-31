---
title: "Strangler Fig: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate strangler concepts"
  - "Plan migrations"
  - "Gate cutovers"
prerequisites:
  []
knowledge_refs:
  - "patterns/strangler-fig"
---

# Strangler Fig: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: The strangler pattern? (A: replaces systems incrementally / B: rewrites at once / C: restart)
- Q2: A stable facade makes routing? (A: reversible / B: permanent / C: fast)
- Q3: Database migrations use? (A: dual writes and backfill / B: downtime / C: backups only)
- Q4: True or false: read-only features migrate first.
- Q5: Shadow traffic provides? (A: comparison evidence / B: revenue / C: cache)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A 15-year-old CRM must move to microservices. Design the strangler plan: order of features, the gateway, and the cutover gates.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why replacing a system is a migration, not an event.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Incremental, reversible, evidence-gated
- The legacy is a safety net until the last feature moves
