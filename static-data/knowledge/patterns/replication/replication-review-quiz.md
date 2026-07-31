---
title: "Replication: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate replication concepts"
  - "Tune quorums"
  - "Resolve conflicts"
prerequisites:
  []
knowledge_refs:
  - "patterns/replication"
---

# Replication: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Replication buys? (A: availability and read scaling / B: stronger CPUs / C: smaller disks)
- Q2: The price of replication is? (A: lag and consistency work / B: nothing / C: speed)
- Q3: W + R > N guarantees? (A: a fresh read / B: no writes / C: compression)
- Q4: True or false: CAP forces a choice during partitions.
- Q5: CRDTs converge? (A: deterministically / B: randomly / C: never)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A global cart service must work during a region partition. Design the model, the quorums, and the merge.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "just add replicas" is where the real design work begins.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Replicas give availability; you pay in consistency
- Quorums and CRDTs manage the payment
