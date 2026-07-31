---
title: "Information Hiding: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate information hiding concepts"
  - "Design module surfaces"
  - "Apply hiding to security"
prerequisites:
  []
knowledge_refs:
  - "principles/information-hiding"
---

# Information Hiding: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Callers should depend on? (A: internals / B: the interface / C: the representation)
- Q2: A module with everything public has? (A: a strong boundary / B: no boundary / C: fewer bugs)
- Q3: Capabilities are? (A: global permissions / B: unforgeable narrow handles / C: passwords)
- Q4: True or false: error messages should include full stack traces for users.
- Q5: Public API changes should follow? (A: semver / B: no rules / C: internal whims)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A service exposes its data model in the API response, and now the schema cannot evolve. Redesign the response DTO boundary and the migration.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "it's all public anyway" destroys the ability to change anything.

## Key Takeaways

- Q1: B; Q2: B; Q3: B; Q4: false; Q5: A
- Boundaries are what make evolution possible
- Hiding is both a design tool and a security tool
