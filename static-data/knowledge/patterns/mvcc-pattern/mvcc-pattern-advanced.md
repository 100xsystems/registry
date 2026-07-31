---
title: "Advanced MVCC: Distributed Snapshot Isolation"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Explain distributed snapshot isolation"
  - "Describe commit ordering"
  - "Design cross-shard consistent reads"
  - "Compare MVCC engines"
prerequisites:
  []
knowledge_refs:
  - "patterns/mvcc-pattern"
---

# Advanced MVCC: Distributed Snapshot Isolation

## Distributed Snapshots

In a sharded database, a snapshot spans shards: the read must see a consistent set of versions across all of them. True distributed snapshot isolation needs synchronized commit timestamps (Spanner uses TrueTime) or a global commit protocol that orders transactions and hands out timestamps from a coordinator.

```text
Distributed MVCC approaches:
  CockroachDB: hybrid logical clocks (HLC) order commits; a
    transaction's timestamp defines its snapshot across shards.
  Spanner: TrueTime (GPS + atomic clocks) gives a global commit
    timestamp with bounded uncertainty; reads at a timestamp see
    a consistent snapshot across the whole database.
  YugaByte/others: central timestamp authority for ordering.
The invariant every approach provides: if tx A commits before B
starts, B's snapshot must include A — no matter which shards
each touched. Clock sync is the entire problem.
```

## Reads Across Shards

A cross-shard read either takes a consistent snapshot (paying for global ordering) or reads at a possibly inconsistent point in time. Materialized aggregates and causal consistency (read-your-writes across shards) are the practical middle grounds most apps actually need.

## Practice: Design the Snapshot

A 16-shard ledger needs a cross-shard balance report that never double-counts in-flight transfers.

**Task 1:** Design the HLC ordering and the per-shard snapshot.

**Task 2:** Design the read protocol that assembles a consistent view.

**Task 3:** Compare the TrueTime vs coordinator approaches for a global financial table.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why cross-shard snapshots need globally ordered timestamps.

**Prompt 2 — Implementation Design:**
> Design causal read-your-writes across shards without full distributed snapshot isolation. What is the routing guarantee?

**Prompt 3 — Boundary Testing:**
> Two shards commit at clock-skewed times and a report sees a half-committed transfer. Design the guard (timestamp bounds) that prevents it.

## Key Takeaways

- Distributed snapshots need globally ordered timestamps
- HLCs and TrueTime are the two main answers
- Causal consistency is the practical middle ground
- Clock skew is the enemy of cross-shard reads

## Further Reading

- [Spanner — TrueTime](https://research.google/pubs/spanner-google-s-globally-distributed-database/)
- [CockroachDB — Serializable Transactions](https://www.cockroachlabs.com/docs/stable/serializable.html)
