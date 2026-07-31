---
title: "YAGNI: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate YAGNI concepts"
  - "Defer speculation with triggers"
  - "Price design options"
prerequisites:
  []
knowledge_refs:
  - "principles/yagni"
---

# YAGNI: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: YAGNI says build? (A: everything predicted / B: what is needed now / C: the biggest design)
- Q2: Speculative code costs? (A: nothing / B: a permanent maintenance tax / C: only disk)
- Q3: A cheap seam that keeps a future open is? (A: an option / B: speculation / C: a bug)
- Q4: True or false: frameworks should be adopted when the problem they solve appears.
- Q5: A carried option with a trigger that keeps failing should? (A: stay forever / B: be cut / C: get more code)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A team wants to build a generic template engine for one page. Design the deferral: the seam, the trigger, and the review date.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "we might need it" is the most expensive phrase in software.

## Key Takeaways

- Q1: B; Q2: B; Q3: A; Q4: true; Q5: B
- YAGNI is options discipline: seams today, futures at the trigger
- Unbuilt code is the cheapest code of all
