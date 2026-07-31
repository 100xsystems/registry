---
title: "Adapter: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate adapter concepts"
  - "Isolate vendor dependencies"
  - "Translate models safely"
prerequisites:
  []
knowledge_refs:
  - "patterns/adapter"
---

# Adapter: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: An adapter changes? (A: the interface / B: the algorithm / C: the database)
- Q2: A facade differs from an adapter by? (A: simplifying vs translating / B: being slower / C: being faster)
- Q3: Vendor SDK usage should be? (A: scattered / B: isolated behind one adapter / C: copied)
- Q4: True or false: model translation should live at the boundary.
- Q5: A proxy controls? (A: access / B: translation / C: rendering)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A legacy SOAP billing API must serve the new JSON order service. Design the adapter, the model translation, and the error mapping.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why calling the vendor SDK in 30 places is a time bomb.

## Key Takeaways

- Q1: A; Q2: A; Q3: B; Q4: true; Q5: A
- Adapters make boundaries clean and upgrades cheap
- Isolate, translate, and test at the edge
