---
title: "Strategy: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate strategy concepts"
  - "Select and compose strategies"
  - "Recognize the explosion smell"
prerequisites:
  []
knowledge_refs:
  - "patterns/strategy"
---

# Strategy: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Strategy makes algorithms? (A: interchangeable / B: private / C: faster)
- Q2: The context holds a strategy via? (A: composition / B: inheritance / C: globals)
- Q3: Registries make selection? (A: configurable / B: random / C: slower)
- Q4: True or false: strategies compose into pipelines.
- Q5: Strategy explosion comes from? (A: a class per combination / B: too few strategies / C: caching)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A checkout applies tier, promotion, and tax. Design the strategy family and its composition order.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why composition beats inheritance for algorithm families.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Interchangeable algorithms, selected and composed
- Functions keep the family small
