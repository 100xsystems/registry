---
title: "Singleton: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate singleton concepts"
  - "Scope instances"
  - "Manage lifecycles"
prerequisites:
  []
knowledge_refs:
  - "patterns/singleton"
---

# Singleton: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: A singleton ensures? (A: one instance / B: two instances / C: no instances)
- Q2: The common criticism is? (A: global access / B: speed / C: size)
- Q3: A multiton keeps? (A: one instance per key / B: one global / C: a queue)
- Q4: True or false: injection keeps the single instance without the global.
- Q5: Instance lifecycles belong to? (A: a manager / B: the static field / C: the client)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A multi-tenant app needs per-tenant caches with lifecycle management. Design the registry and the injection.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer when a singleton is legitimate and when it is a smell.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Single instance yes; global access no
- Scope and manage lifetimes explicitly
