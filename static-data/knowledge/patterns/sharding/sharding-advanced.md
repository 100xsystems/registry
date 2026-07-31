---
title: "Advanced Sharding: Resharding and Cross-Shard Queries"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Reshard without downtime"
  - "Design cross-shard joins"
  - "Maintain global uniqueness"
  - "Distribute transactions"
prerequisites:
  []
knowledge_refs:
  - "patterns/sharding"
---

# Advanced Sharding: Resharding and Cross-Shard Queries

## Live Resharding

Growing past the shard count demands resharding: add shards and move data. The dual-write pattern keeps it live — writes go to both old and new layouts while a backfill copies history; a cutover flips reads when the copy converges; a rollback window covers mistakes. Each phase is a state machine with checks.

```text
Live resharding phases:
  1. Prepare: add the new shards, install the new routing rule
     (e.g., hash(key) % 8 instead of % 4)
  2. Dual-write: every write goes to the old and new shards;
     a backfill job copies historical rows (idempotent)
  3. Verify: compare row counts, checksums, and lag between
     old and new layouts
  4. Cutover: reads move to the new layout; keep the old for
     a rollback window
  5. Drain: drop the old copies and the dual-write path
Global uniqueness across shards:
  - UUIDs, or a central sequence, or per-shard ranges (id = shard*N + n)
Cross-shard transactions:
  - avoid them (design for single-shard atomicity)
  - or accept 2PC / saga semantics when unavoidable
```

## Cross-Shard Queries

Scatter-gather (ask every shard, merge) is the fallback for queries without the shard key — slow at scale. Distributed joins route by the join key so joined rows co-locate, or broadcast small tables. The discipline: every hot query must carry the shard key; everything else is a known cost.

## Practice: Plan the Reshard

A 4-shard user table must move to 8 shards with zero downtime.

**Task 1:** Design the dual-write, backfill, and verify phases.

**Task 2:** Design the cutover with a rollback window.

**Task 3:** Audit the hot queries: which ones carry the shard key?

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why dual-write plus backfill reshares without downtime.

**Prompt 2 — Implementation Design:**
> Design a globally unique ID scheme for a 64-shard system and the per-shard ordering it preserves.

**Prompt 3 — Boundary Testing:**
> The backfill and dual-write diverge on one row. Design the checksum verify that catches it before cutover.

## Key Takeaways

- Dual-write + backfill + verify + cutover = live reshard
- Hot queries must carry the shard key
- Scatter-gather is a known, bounded cost
- Global IDs need a per-shard scheme

## Further Reading

- [Vitess — resharding](https://vitess.io/docs/user-guides/sharding-resharding/)
- [The Pathologies of Big Data (scatter-gather)](https://queue.acm.org/detail.cfm?id=1563874)
