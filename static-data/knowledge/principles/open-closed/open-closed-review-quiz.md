---
title: "Open-Closed: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate OCP concepts"
  - "Design extension points"
  - "Evolve contracts additively"
prerequisites:
  []
knowledge_refs:
  - "principles/open-closed"
---

# Open-Closed: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: OCP means modules are open for? (A: modification / B: extension / C: deletion)
- Q2: The mechanism of openness is? (A: copying / B: abstraction / C: comments)
- Q3: Adding a payment method should ideally? (A: edit the switch / B: add a class / C: rewrite the core)
- Q4: True or false: removing an API field is always safe if you control the callers.
- Q5: Deprecation should follow? (A: a documented timeline / B: instant removal / C: silence)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A pricing engine edits a switch statement monthly. Redesign as an open-closed policy set and describe the first migration.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "I just changed the tested code, it's fine" is how bugs get shipped.

## Key Takeaways

- Q1: B; Q2: B; Q3: B; Q4: false; Q5: A
- Openness is earned by abstraction, kept by contract discipline
- Additive evolution keeps APIs closed forever
