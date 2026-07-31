---
title: "Two-Phase Commit: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate 2PC concepts"
  - "Design recovery"
  - "Choose the right protocol"
prerequisites:
  []
knowledge_refs:
  - "patterns/two-phase-commit"
---

# Two-Phase Commit: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: 2PC provides? (A: atomicity across participants / B: eventual consistency / C: caching)
- Q2: Phase one is? (A: prepare and vote / B: commit / C: cleanup)
- Q3: The coordinator must persist? (A: its decision / B: the data / C: the cache)
- Q4: True or false: after voting yes, a participant must follow the decision.
- Q5: Microservices usually prefer? (A: sagas / B: 2PC / C: no transactions)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> Two financial databases need atomicity. Design the 2PC setup and its coordinator recovery.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer when 2PC is worth its blocking cost and when it is not.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Prepare-then-decide with durable coordination
- Atomicity for few reliable participants; sagas for many
