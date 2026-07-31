---
title: "Command: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate command concepts"
  - "Design command queues"
  - "Apply command sourcing"
prerequisites:
  []
knowledge_refs:
  - "patterns/command"
---

# Command: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: A command wraps? (A: an action and its parameters / B: a database / C: a thread)
- Q2: Undo requires commands to expose? (A: undo() / B: caching / C: logging)
- Q3: A job queue is a queue of? (A: commands / B: threads / C: databases)
- Q4: True or false: commands should be idempotent for safe replays.
- Q5: Command sourcing stores? (A: commands / B: only state / C: only logs)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A payment flow needs retry, audit, and undo. Model it as commands with idempotency and a compensating undo.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "just call the method" loses the ability to queue, log, and undo.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Commands make actions first-class values
- Sourcing turns them into the complete audit trail
