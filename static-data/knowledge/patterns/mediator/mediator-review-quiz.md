---
title: "Mediator: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate mediator concepts"
  - "Design buses and orchestrators"
  - "Choose coordination"
prerequisites:
  []
knowledge_refs:
  - "patterns/mediator"
---

# Mediator: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: A mediator turns many-to-many into? (A: hub-and-spoke / B: one-to-one / C: a tree)
- Q2: Observer is? (A: one-to-many / B: many-to-many / C: zero-to-zero)
- Q3: An orchestrator is a mediator? (A: for services / B: for users / C: for browsers)
- Q4: True or false: choreography has no central hub.
- Q5: The main choreography risk is? (A: implicit flow / B: too fast / C: too many hubs)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A checkout flow spans 5 services with refund paths. Choose orchestration or choreography and justify the retry design.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why decoupling collaborators can still create a god object.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Hubs centralize coordination; use them deliberately
- Choreography trades control for independence
