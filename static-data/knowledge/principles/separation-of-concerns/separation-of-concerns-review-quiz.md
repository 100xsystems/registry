---
title: "Separation of Concerns: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate SoC concepts"
  - "Separate tangled concerns"
  - "Design event boundaries"
prerequisites:
  []
knowledge_refs:
  - "principles/separation-of-concerns"
---

# Separation of Concerns: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Separation of concerns divides a system by? (A: team / B: concern / C: size)
- Q2: Logging and auth are? (A: core concerns / B: cross-cutting concerns / C: layers)
- Q3: Cross-cutting concerns are best applied? (A: everywhere inline / B: once via middleware / C: never)
- Q4: True or false: events decouple producers from consumers.
- Q5: A controller querying the DB directly is? (A: a layering violation / B: best practice / C: a cache)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A payment notification handler validates, charges, emails, and updates a dashboard. Separate the concerns and design the event boundary.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "it works in one function" is not the same as "it is well-separated".

## Key Takeaways

- Q1: B; Q2: B; Q3: B; Q4: true; Q5: A
- Separation makes each concern independently evolvable
- Events extend separation across services
