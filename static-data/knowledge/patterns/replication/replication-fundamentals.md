---
title: "Replication: Copies for Availability"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain replication purposes"
  - "Describe replication models"
  - "Understand consistency trade-offs"
  - "Choose replication factors"
prerequisites:
  - "patterns/leader-follower"
  - "patterns/multi-leader"
knowledge_refs:
  - "patterns/replication"
---

# Replication: Copies for Availability

## Why Replicate

Replication serves three goals: high availability (a node dies, others serve), read scaling (more copies, more read throughput), and latency (a copy near every region). The cost is consistency: replicas can diverge, and the replication lag decides what readers see.

```text
Replication models:
  Single-leader: one writer, many readers (Postgres, MySQL)
    - strong write order; reads may lag
  Multi-leader: several writers, replicated between (offline-first)
    - write locality; needs conflict resolution
  Leaderless (quorum): writes go to N nodes, reads from N (Dynamo)
    - tunable consistency; needs read repair / anti-entropy
Consistency spectrum:
  Strong: reads always see the latest committed write
  Eventual: replicas converge, readers may see stale data
  Read-your-writes: your own writes are visible to you
  Monotonic: reads never go backward in time
Replication factor: the number of copies. Higher = more fault
tolerance and read capacity, but more write cost and lag risk.
```

## Choosing a Model

Pick single-leader when writes must be ordered and simple (most OLTP). Pick multi-leader for multi-region writes or offline apps. Pick leaderless when availability and partition tolerance beat strict ordering (carts, counters). The data's semantics — not fashion — choose the model.

## Practice: Choose the Replication

A global inventory app: writes happen in any region; double-selling must never happen.

**Task 1:** Evaluate the three models against the write-ordering requirement.

**Task 2:** Design the chosen model with its consistency policy.

**Task 3:** Show the failure mode of each rejected model for this workload.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why more copies mean more consistency work. Start with a read.

**Prompt 2 — Compare & Contrast:**
> Compare single-leader, multi-leader, and leaderless with one workload each. Where do the guarantees differ?

**Prompt 3 — Boundary Testing:**
> A replica lags 30 seconds and a user sees their order missing. Design the read-your-writes routing that fixes it.

## Key Takeaways

- Replication buys availability, reads, and locality
- Lag is the price; consistency policies manage it
- Model choice follows write semantics
- Replication factor tunes fault tolerance vs cost

## Further Reading

- [Replication — DDIA Ch. 5](https://dataintensive.net/)
- [PostgreSQL — streaming replication](https://www.postgresql.org/docs/current/warm-standby.html)
