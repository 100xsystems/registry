---
title: "CAP Theorem: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate CAP reasoning"
  - "Apply quorum math to new systems"
  - "Choose consistency contracts per workload"
prerequisites:
  []
knowledge_refs:
  - "principles/cap-theorem"
---

# CAP Theorem: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: During a partition, a CP system on the minority side? (A: serves stale / B: stops serving / C: serves fresh)
- Q2: W=2, R=2, N=3 gives? (A: quorum consistency / B: no consistency / C: linearizability always)
- Q3: PACELC's "E" stands for? (A: eventually / B: else / C: errors)
- Q4: True or false: a single-node DB is always both consistent and available.
- Q5: Session guarantee that prevents "I posted but I can't see it" is? (A: read-your-writes / B: monotonic reads / C: linearizability)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A multi-region payment system must never double-charge and must survive a region loss. Design the quorum and the reconciliation, and identify where you accept availability loss.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "CAP means pick two" is misleading without "during a partition" and PACELC.

## Key Takeaways

- Q1: B; Q2: A; Q3: B; Q4: true (no partitions); Q5: A
- CAP choices are per data path and per failure mode
- Quorums and session guarantees are the practical tools
