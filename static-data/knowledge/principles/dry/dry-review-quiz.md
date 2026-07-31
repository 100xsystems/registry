---
title: "DRY: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate DRY concepts"
  - "Identify knowledge vs code duplication"
  - "Right-size abstraction boundaries"
prerequisites:
  []
knowledge_refs:
  - "principles/dry"
---

# DRY: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: DRY prohibits duplicating? (A: code / B: knowledge / C: comments)
- Q2: Two same-shaped functions with different rules are? (A: duplicates / B: not duplicates / C: always DRY)
- Q3: The "rule of three" suggests extracting after? (A: 1 use / B: 3 similar uses / C: 10 uses)
- Q4: True or false: generated clients eliminate contract drift.
- Q5: A shared utils module used by everyone is a symptom of? (A: good DRY / B: over-abstraction / C: strong typing)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A tax rule exists in the backend, a reporting job, and a frontend form. Redesign with one source of truth and describe the deployment order.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "we DRYed it too early" is a real cost, with a concrete refactor story.

## Key Takeaways

- Q1: B; Q2: B; Q3: B; Q4: true; Q5: B
- Knowledge with one source of truth never drifts
- Abstractions earn their keep by reducing coupling, not lines
