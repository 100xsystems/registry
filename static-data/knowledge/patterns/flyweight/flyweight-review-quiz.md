---
title: "Flyweight: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate flyweight concepts"
  - "Split state correctly"
  - "Design safe caches and pools"
prerequisites:
  []
knowledge_refs:
  - "patterns/flyweight"
---

# Flyweight: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Intrinsic state must be? (A: mutable / B: immutable / C: per-user)
- Q2: Extrinsic state is passed? (A: per use / B: once / C: never)
- Q3: The flyweight factory acts as a? (A: cache / B: database / C: compiler)
- Q4: True or false: a pool is a reusable flyweight with a reset contract.
- Q5: Weak-reference caches evict? (A: via GC / B: via LRU / C: never)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A chess game shows 32 pieces reused across 10,000 board cells. Design the flyweight and what the extrinsic state holds.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why sharing mutable state across objects is worse than not sharing at all.

## Key Takeaways

- Q1: B; Q2: A; Q3: A; Q4: true; Q5: A
- Share immutable intrinsic state; pass extrinsic per use
- Caches and pools operationalize the pattern safely
