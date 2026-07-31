---
title: "Builder: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate builder concepts"
  - "Design fluent APIs"
  - "Enforce validity at build time"
prerequisites:
  []
knowledge_refs:
  - "patterns/builder"
---

# Builder: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: The builder solves? (A: complex construction / B: slow queries / C: caching)
- Q2: Validation should happen? (A: at build() / B: never / C: in the caller)
- Q3: A staged builder enforces? (A: legal step order / B: faster build / C: smaller memory)
- Q4: True or false: built objects should be immutable.
- Q5: Fixture builders keep tests compiling by? (A: safe defaults / B: removing fields / C: mocking)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> An HTTP client constructor takes 9 positional args and callers keep mixing them up. Design the builder and migrate three call sites.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why named builder steps beat positional constructors for readability.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Builders name construction and validate at the end
- Stages and immutability make them safe
