---
title: "State: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate state concepts"
  - "Design machines"
  - "Model complexity"
prerequisites:
  []
knowledge_refs:
  - "patterns/state"
---

# State: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: In the state pattern, behavior lives? (A: in state objects / B: in if-chains / C: in the DB)
- Q2: Transitions are owned by? (A: the state objects / B: the callers / C: the cache)
- Q3: A state machine centralizes? (A: states, events, guards / B: money / C: logs)
- Q4: True or false: persisted state makes workflows resumable.
- Q5: Statecharts add? (A: hierarchy and parallelism / B: caching / C: sharding)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A payment flow: authorized -> captured -> settled, with a partial-refund substate. Design the machine and its guards.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why a state machine is documentation that runs.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- State as objects or as tables — explicit either way
- Machines audit, persist, and resume
