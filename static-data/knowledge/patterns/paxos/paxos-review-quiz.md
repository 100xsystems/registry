---
title: "Paxos: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate Paxos concepts"
  - "Design coordination"
  - "Choose variants"
prerequisites:
  []
knowledge_refs:
  - "patterns/paxos"
---

# Paxos: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Paxos roles are? (A: proposers, acceptors, learners / B: leaders, workers, clients / C: masters, slaves, caches)
- Q2: Safety comes from? (A: majority intersection / B: majority votes / C: backups)
- Q3: Livelock is prevented by? (A: a distinguished proposer / B: more votes / C: caching)
- Q4: True or false: Multi-Paxos runs consensus per log entry.
- Q5: ZooKeeper locks use? (A: ephemeral znodes / B: file locks / C: DNS)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A 5-node config service must elect a leader and fence the old one. Design the consensus layer and the fencing token.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why two majorities must always intersect.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Consensus is majority agreement, proven once
- Every modern variant is a Paxos descendant
