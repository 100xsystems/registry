---
title: "Visitor: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate visitor concepts"
  - "Design visitors"
  - "Choose the right approach"
prerequisites:
  []
knowledge_refs:
  - "patterns/visitor"
---

# Visitor: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Visitor adds operations? (A: without editing elements / B: by editing elements / C: by copying)
- Q2: Double dispatch matches? (A: the concrete element type / B: the visitor count / C: the cache)
- Q3: Compilers use visitors over? (A: ASTs / B: databases / C: sockets)
- Q4: True or false: adding a new element type breaks every visitor.
- Q5: Pattern matching gives visitors without? (A: boilerplate / B: correctness / C: speed)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A config tree (scalar, list, map) needs validate, flatten, and render. Design the visitor set.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer the expression problem and where visitors fit.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Stable structures, growing operations
- Pattern matching is the visitor with exhaustiveness
