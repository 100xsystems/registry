---
title: "Observer: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate observer concepts"
  - "Design streams"
  - "Model events"
prerequisites:
  []
knowledge_refs:
  - "patterns/observer"
---

# Observer: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: An observer pattern is? (A: one-to-many / B: one-to-one / C: many-to-one)
- Q2: The subject knows observers by? (A: interface / B: concrete type / C: memory address)
- Q3: Backpressure lets a slow observer? (A: slow the producer / B: skip events / C: restart)
- Q4: True or false: event sourcing stores state changes as facts.
- Q5: A projection is rebuilt by? (A: replaying events / B: restarting / C: patching)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A notification system must email, push, and log every order event. Design the observer set and the error isolation.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why knowing an interface beats knowing an implementation.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Decoupled notification is the superpower
- Streams and event sourcing scale the pattern
