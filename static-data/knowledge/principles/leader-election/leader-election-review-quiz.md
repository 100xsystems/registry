---
title: "Leader Election: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate election concepts"
  - "Design safe failover"
  - "Prevent split-brain"
prerequisites:
  []
knowledge_refs:
  - "principles/leader-election"
---

# Leader Election: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Split-brain means? (A: two leaders acting / B: no leader / C: slow leader)
- Q2: A lease bounds leadership by? (A: memory / B: time / C: network)
- Q3: Raft requires a ___ to elect a leader. (A: majority / B: quorum of 1 / C: supermajority of 2/3)
- Q4: True or false: fencing tokens are rejected by storage when stale.
- Q5: Failover time equals? (A: detection + election + handoff / B: reboot only / C: network latency)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A single-writer service loses its leader for 30 seconds during failover. Design the pipeline that reduces this to under a second and the fencing that makes it safe.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "the old leader will just stop" is not a safe assumption.

## Key Takeaways

- Q1: A; Q2: B; Q3: A; Q4: true; Q5: A
- Election must be safe, live, and fast
- Fencing is what actually protects the data
