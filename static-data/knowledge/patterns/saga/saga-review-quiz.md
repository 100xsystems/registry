---
title: "Saga: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate saga concepts"
  - "Choose orchestration"
  - "Design compensations"
prerequisites:
  []
knowledge_refs:
  - "patterns/saga"
---

# Saga: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: A saga replaces? (A: 2PC / B: caching / C: sharding)
- Q2: A compensation is? (A: a new transaction / B: an undo / C: a lock)
- Q3: Orchestrated sagas are? (A: resumable and visible / B: faster / C: smaller)
- Q4: True or false: compensations must be idempotent.
- Q5: Saga isolation uses? (A: semantic locks / B: global locks / C: no locks)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A travel booking saga spans hotel, flight, and car. Design the steps, compensations, and timeout policy.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why compensating is different from rolling back.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Local steps plus compensations beat global locks
- Isolation and idempotency are the hard parts
