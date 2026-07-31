---
title: "Factory: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate factory concepts"
  - "Design creation boundaries"
  - "Keep creation open-closed"
prerequisites:
  []
knowledge_refs:
  - "patterns/factory"
---

# Factory: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: A factory method defers creation to? (A: subclasses / B: the caller / C: the database)
- Q2: The "does the choice vary?" test decides? (A: whether a factory is justified / B: the database / C: the UI)
- Q3: A registry keeps creation? (A: open for extension / B: fixed / C: hidden)
- Q4: True or false: direct new in business code couples callers to concretes.
- Q5: A factory that switches on every product type is a smell of? (A: god-factory / B: good design / C: DI)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> An exporter supports 5 formats with per-format options. Design the creation boundary: factory method, registry, or DI — and justify.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why creation belongs behind a boundary when the choice varies.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Factories localize the varying creation decision
- Registries make creation open for extension
