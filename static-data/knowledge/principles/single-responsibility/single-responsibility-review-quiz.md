---
title: "Single Responsibility: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate SRP concepts"
  - "Detect multi-responsibility classes"
  - "Design honest boundaries"
prerequisites:
  []
knowledge_refs:
  - "principles/single-responsibility"
---

# Single Responsibility: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: SRP means one? (A: method / B: reason to change / C: file)
- Q2: A repository with find/create/delete has? (A: three responsibilities / B: one responsibility (persistence) / C: no responsibility)
- Q3: Two actors changing one service means? (A: good / B: split the boundary / C: merge teams)
- Q4: True or false: a shared database transaction across responsibilities is a coupling.
- Q5: The outbox pattern preserves? (A: one giant transaction / B: per-responsibility atomicity / C: nothing)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A "notification service" now owns templates, sends, retries, and unsubscribe. Redesign the responsibility split and the interface between them.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "it is one class, it is simpler" fails the moment two actors want different changes.

## Key Takeaways

- Q1: B; Q2: B; Q3: B; Q4: true; Q5: B
- The reason to change is the unit of responsibility
- Boundaries survive transactions via outbox and sagas
