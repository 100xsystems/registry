---
title: "Defensive Programming: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate defensive concepts"
  - "Design validation and error policies"
  - "Choose test oracles wisely"
prerequisites:
  []
knowledge_refs:
  - "principles/defensive-programming"
---

# Defensive Programming: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: The worst failure mode in defensive programming is? (A: loud error / B: silent wrong behavior / C: fast crash)
- Q2: Validation belongs at? (A: everywhere / B: trust boundaries / C: the UI only)
- Q3: Property-based testing is stronger than example tests because it? (A: runs faster / B: covers generated inputs / C: needs no code)
- Q4: True or false: catch-all exception handlers are good defensive practice.
- Q5: An invariant that must never change is best enforced by? (A: assertion / B: documentation / C: a comment)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A config parser accepts a version field; a future version adds a field you ignore. Design the defensive check that fails loudly on unknown major versions.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "the input will always be valid because we control the caller" is a dangerous assumption.

## Key Takeaways

- Q1: B; Q2: B; Q3: B; Q4: false; Q5: A
- Defense belongs at boundaries; assertions guard internals
- Automated oracles make defense permanent
