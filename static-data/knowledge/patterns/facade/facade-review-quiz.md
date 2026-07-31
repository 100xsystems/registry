---
title: "Facade: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate facade concepts"
  - "Design thin facades"
  - "Keep doors honest"
prerequisites:
  []
knowledge_refs:
  - "patterns/facade"
---

# Facade: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: A facade provides? (A: a simple interface over a complex subsystem / B: a translation layer / C: a cache)
- Q2: The subsystem behind a facade? (A: stays intact / B: is rewritten / C: disappears)
- Q3: A facade differs from an adapter by? (A: simplifying vs translating / B: being faster / C: using threads)
- Q4: True or false: facades should swallow errors silently.
- Q5: Per-audience facades are? (A: role-shaped doors / B: copies / C: singletons)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A checkout subsystem has 6 classes and error-prone orchestration. Design the facade, its result types, and the caller's new simplicity.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why a facade that hides failures is a fragile foundation.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: false; Q5: A
- Facades simplify and decouple
- Thin, honest facades are the sustainable ones
