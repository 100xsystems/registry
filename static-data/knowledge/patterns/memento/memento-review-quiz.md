---
title: "Memento: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate memento concepts"
  - "Design recovery"
  - "Scale history"
prerequisites:
  []
knowledge_refs:
  - "patterns/memento"
---

# Memento: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: A memento preserves? (A: encapsulation / B: speed / C: coupling)
- Q2: Undo/redo uses? (A: two stacks / B: one list / C: a database)
- Q3: Checkpoint recovery replays? (A: only the tail / B: everything / C: nothing)
- Q4: True or false: persistent structures share unchanged state between versions.
- Q5: Git commits are? (A: mementos / B: commands / C: caches)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A stream processor with 20GB state must recover in under 30s. Design the checkpoint interval, format, and replay path.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why snapshotting must not break the encapsulation that made the object safe.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Snapshots + replay = recovery
- Structural sharing makes history cheap
