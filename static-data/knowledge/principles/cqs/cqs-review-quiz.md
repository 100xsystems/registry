---
title: "CQS: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate CQS concepts"
  - "Classify APIs and methods correctly"
  - "Apply CQRS where appropriate"
prerequisites:
  []
knowledge_refs:
  - "principles/cqs"
---

# CQS: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: A query should? (A: mutate / B: return a value without mutation / C: do both)
- Q2: GET /orders that deletes an order violates? (A: CQS / B: DRY / C: YAGNI)
- Q3: CQRS separates? (A: read and write models / B: teams / C: databases only)
- Q4: True or false: event sourcing stores only the latest state.
- Q5: A cache get() that fills the cache is? (A: always a violation / B: a defensible internal optimization / C: a command)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A reporting service runs heavy queries that slow the transactional path. Design the read-model split and its consistency story.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why hiding a mutation inside a getter is a "quiet bug factory".

## Key Takeaways

- Q1: B; Q2: A; Q3: A; Q4: false; Q5: B
- Separation enables caching, parallelism, and independent scaling
- Heavy tools like CQRS+ES earn their cost only on divergent shapes
