---
title: "MVVM: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate MVVM concepts"
  - "Scope and inject view models"
  - "Handle async safely"
prerequisites:
  []
knowledge_refs:
  - "patterns/mvvm"
---

# MVVM: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: The view model prepares? (A: data for display / B: the database / C: the network)
- Q2: Binding wires? (A: the view to the view model / B: models together / C: the router)
- Q3: Async updates must be? (A: lifecycle-cancelled / B: global / C: synchronous)
- Q4: True or false: view models are unit-testable without a UI.
- Q5: Dependencies should be? (A: injected / B: constructed inline / C: global)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A live sports scoreboard: scores stream in, views update live. Design the view model, binding, and lifecycle.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why a UI-free view model is the testability win.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Presentation-ready state, bound declaratively
- Lifecycle and injection make it production-safe
