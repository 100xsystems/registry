---
title: "MVC: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate MVC concepts"
  - "Keep layers clean"
  - "Design state flow"
prerequisites:
  []
knowledge_refs:
  - "patterns/mvc"
---

# MVC: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: The model holds? (A: data and rules / B: input parsing / C: rendering)
- Q2: The view re-renders when the model? (A: notifies / B: crashes / C: loads)
- Q3: "Fat model, thin controller" means logic lives? (A: in the model / B: in the view / C: in CSS)
- Q4: True or false: unidirectional flow makes state changes pure.
- Q5: Side effects in Redux live in? (A: middleware / B: reducers / C: components)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A checkout form with validation, totals, and a pay button. Design the MVC layers and where the rules live.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why separating data, presentation, and input is worth the files.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Separation of concerns is the point of MVC
- Unidirectional flow fixes the tangle at scale
