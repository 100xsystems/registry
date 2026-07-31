---
title: "Liskov Substitution: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate LSP concepts"
  - "Detect contract violations"
  - "Design substitutable hierarchies"
prerequisites:
  []
knowledge_refs:
  - "principles/liskov-substitution"
---

# Liskov Substitution: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: A subtype must honor? (A: the base contract / B: only new methods / C: nothing)
- Q2: Square extends Rectangle is a classic LSP violation because? (A: it changes width too / B: it is too fast / C: it is abstract)
- Q3: Strengthening a precondition in a subtype? (A: is safe / B: violates LSP / C: is required)
- Q4: True or false: contract tests should run against every implementation.
- Q5: A mutable List<Square> is a List<Rectangle>? (A: yes / B: no / C: maybe)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A payment provider interface has two implementations that behave differently on declined payments. Design the contract test suite that catches the difference.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "it compiles, so it is substitutable" is false.

## Key Takeaways

- Q1: A; Q2: A; Q3: B; Q4: true; Q5: B
- Substitution is a behavioral promise, not a type label
- Contract tests make the promise executable
