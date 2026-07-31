---
title: "Dependency Inversion: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate DIP concepts"
  - "Design inversion boundaries"
  - "Enforce arrows with tests"
prerequisites:
  []
knowledge_refs:
  - "principles/dependency-inversion"
---

# Dependency Inversion: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: DIP says high-level modules should depend on? (A: low-level modules / B: abstractions / C: nothing)
- Q2: The composition root is where you? (A: write domain logic / B: wire concrete adapters / C: define interfaces)
- Q3: Hexagonal architecture keeps the domain free of? (A: interfaces / B: infrastructure imports / C: tests)
- Q4: True or false: dependency injection frameworks are required for dependency inversion.
- Q5: Architecture tests are used to? (A: test UI / B: enforce import rules / C: measure performance)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A team adds a second database to a service that was written without ports. Map the refactor: which interfaces, which adapters, and what stays untouched?

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "we only ever use Postgres, so no interface needed" fails when the requirement changes.

## Key Takeaways

- Q1: B; Q2: B; Q3: B; Q4: false; Q5: B
- Inversion is about arrows, not frameworks
- Enforcement in CI keeps the architecture honest
