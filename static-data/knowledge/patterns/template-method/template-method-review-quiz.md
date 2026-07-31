---
title: "Template Method: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate template method concepts"
  - "Design hooks"
  - "Enforce contracts"
prerequisites:
  []
knowledge_refs:
  - "patterns/template-method"
---

# Template Method: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Template method fixes? (A: the algorithm skeleton / B: the data / C: the UI)
- Q2: Subclasses fill? (A: the variable steps / B: the main method / C: the cache)
- Q3: A hook is? (A: an optional extension point / B: a database / C: an error)
- Q4: True or false: frameworks are template methods at scale.
- Q5: Contracts in the skeleton belong? (A: in the base class / B: in each subclass / C: nowhere)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A payment provider integration: authorize, capture, settle — one skeleton, two providers. Design the template and the hooks.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why the flow should be written once and only the steps overridden.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- One skeleton, overridable steps, optional hooks
- Contracts make the skeleton verifiable
