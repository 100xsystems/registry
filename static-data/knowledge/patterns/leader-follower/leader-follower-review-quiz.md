---
title: "Leader-Follower: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate leader-follower concepts"
  - "Design failover"
  - "Resolve conflicts"
prerequisites:
  []
knowledge_refs:
  - "patterns/leader-follower"
---

# Leader-Follower: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: In leader-follower, writes go to? (A: the leader / B: any follower / C: all nodes)
- Q2: Reads from followers may be? (A: stale / B: faster than the leader / C: impossible)
- Q3: Split-brain is prevented by? (A: fencing / B: backups / C: caching)
- Q4: True or false: multi-leader replication needs conflict resolution.
- Q5: Raft elects a leader with? (A: a majority quorum / B: a coin flip / C: admin action)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A global e-commerce site needs writes near users and zero double-spends. Design the hybrid: multi-leader carts, single-leader payments.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why the replication lag is the price of read scaling.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Single writer, many readers, explicit lag policy
- Failover and conflicts are the two hard problems
