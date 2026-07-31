---
title: "Bridge: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate bridge concepts"
  - "Detect inheritance explosions"
  - "Design honest seams"
prerequisites:
  []
knowledge_refs:
  - "patterns/bridge"
---

# Bridge: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Bridge separates? (A: two axes of variation / B: two teams / C: two databases)
- Q2: The naive cross-product of 3 x 4 classes is? (A: 7 / B: 12 / C: 3)
- Q3: In bridge, the abstraction? (A: holds the implementation / B: extends it / C: copies it)
- Q4: True or false: bridge lets each axis vary independently.
- Q5: Bridging a single-axis variation is usually? (A: necessary / B: needless indirection / C: faster)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A notification system supports 3 channels and 4 format policies. Redesign the naive 12-class hierarchy as a bridge and count the real classes.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "an interface and two implementations" is not automatically a bridge.

## Key Takeaways

- Q1: A; Q2: B; Q3: A; Q4: true; Q5: B
- Bridge kills cross-product class explosions
- The seam is the abstraction holding the implementation
