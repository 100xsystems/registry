---
title: "CQRS: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate CQRS concepts"
  - "Design projections"
  - "Choose complexity deliberately"
prerequisites:
  []
knowledge_refs:
  - "patterns/cqrs"
---

# CQRS: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: CQRS gives commands and queries? (A: separate models / B: one model / C: no models)
- Q2: Consistency between write and read models is? (A: eventual / B: immediate / C: absent)
- Q3: Projections must be? (A: idempotent / B: random / C: fast only)
- Q4: True or false: CQS is the method-level version of CQRS.
- Q5: Event sourcing stores? (A: events as truth / B: only state / C: only queries)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A social feed: writes are simple, reads are complex joins. Design the CQRS split, the projection, and the lag budget.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why CQRS is a trade-off, not a default.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- CQRS buys read/write independence at consistency cost
- Projections and lag management are the operational core
