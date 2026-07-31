---
title: "Quorum: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate quorum concepts"
  - "Design quorums for requirements"
  - "Handle membership and loss"
prerequisites:
  []
knowledge_refs:
  - "principles/quorum"
---

# Quorum: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: The quorum consistency condition is? (A: W+R>N / B: W+R=N / C: W>N)
- Q2: Two quorums always? (A: overlap / B: diverge / C: conflict)
- Q3: A 3-AZ, N=3, W=2,R=2 setup tolerates? (A: any single AZ loss / B: two AZ losses / C: nothing)
- Q4: True or false: on write-quorum loss, the system should fail closed.
- Q5: Epoch fencing rejects writes from? (A: old membership epochs / B: new nodes / C: reads)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A stock-trading ledger needs strong reads and low write latency. Design the quorum (N, W, R, AZ layout) and justify every number.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why quorum math is the difference between "mostly consistent" and "provably consistent".

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- The intersection property is the invariant
- Quorum choices are per-workload design decisions
