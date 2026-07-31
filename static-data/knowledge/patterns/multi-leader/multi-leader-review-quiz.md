---
title: "Multi-Leader: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate multi-leader concepts"
  - "Resolve conflicts"
  - "Order concurrent writes"
prerequisites:
  []
knowledge_refs:
  - "patterns/multi-leader"
---

# Multi-Leader: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Multi-leader trades consistency for? (A: write locality / B: read speed / C: storage)
- Q2: Two leaders accepting the same key causes? (A: a conflict / B: nothing / C: a lock)
- Q3: LWW resolution is vulnerable to? (A: clock skew / B: disk full / C: caching)
- Q4: True or false: CRDTs converge deterministically without a coordinator.
- Q5: Hybrid logical clocks combine? (A: physical time + logical counter / B: two clocks / C: GPS + NTP)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A note app syncs between laptop and phone with concurrent edits. Design the CRDT ops, the HLC ordering, and the merge.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "last writer wins" is a data-loss policy in disguise.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Many writers need explicit conflict semantics
- CRDTs + causal ordering make convergence real
