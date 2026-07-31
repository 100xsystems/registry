---
title: "Abstract Factory: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate abstract factory concepts"
  - "Design product families"
  - "Extend families safely"
prerequisites:
  []
knowledge_refs:
  - "patterns/abstract-factory"
---

# Abstract Factory: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Abstract factory creates? (A: one object / B: a family of related objects / C: a singleton)
- Q2: The core guarantee of the pattern is? (A: speed / B: family consistency / C: caching)
- Q3: Factory method differs from abstract factory by? (A: one product vs a family / B: being faster / C: using singletons)
- Q4: True or false: the composition root is where concrete factories are chosen.
- Q5: A registry keeps the family? (A: open for extension / B: fixed forever / C: un-testable)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A reporting tool must render PDF and HTML with matching headers, tables, and charts. Design the abstract factory and the registry.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "just new it up everywhere" breaks product families.

## Key Takeaways

- Q1: B; Q2: B; Q3: A; Q4: true; Q5: A
- Families stay consistent by construction
- Registries and decorators keep them extensible
