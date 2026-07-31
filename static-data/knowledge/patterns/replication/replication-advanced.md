---
title: "Advanced Replication: Conflict Resolution and Consistency Models"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Resolve replication conflicts"
  - "Apply consistency models"
  - "Design convergent systems"
  - "Reason about availability"
prerequisites:
  []
knowledge_refs:
  - "patterns/replication"
---

# Advanced Replication: Conflict Resolution and Consistency Models

## The CAP Trade

CAP says a partition forces a choice: consistency (refuse to serve) or availability (serve possibly stale). Most systems choose availability and manage the consequences with conflict resolution and consistency policies. The practical design question is: during a partition, what do reads and writes return?

```python
# Convergent replication: LWW vs CRDT under partition
# LWW: keep the (value, timestamp) with the highest timestamp
def lww_merge(a, b):
    return a if a[1] >= b[1] else b      # loses the older update

# CRDT G-Counter: elementwise max, value = sum — nothing is lost
def counter_merge(ca, cb):
    return [max(x, y) for x, y in zip(ca, cb)]

# Set with tombstones: adds union, removes tracked, apply both
def set_merge(sa, sb):
    adds = sa.adds | sb.adds
    removes = sa.removes | sb.removes
    return adds - removes
# Deterministic merges converge without a coordinator — the
# replication topology becomes irrelevant to correctness.
```

## The Consistency Menu

Beyond strong and eventual: read-your-writes, monotonic reads, bounded staleness, and causal consistency each solve a specific user-visible failure. The cheapest correct option wins — causal consistency (DynamoDB) covers most real app needs without global ordering.

## Practice: Design the Convergent Store

A wishlist syncs across devices; adds, removes, and reorders happen offline on every device.

**Task 1:** Design the operation-based CRDTs for each operation.

**Task 2:** Show the LWW alternative and which user-visible update it loses.

**Task 3:** State the consistency model your design actually delivers.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why CRDT merges make the topology irrelevant.

**Prompt 2 — Implementation Design:**
> Design a messaging system with causal ordering: messages within a conversation appear in cause-effect order across devices. What is the causality mechanism?

**Prompt 3 — Boundary Testing:**
> A device offline for a week merges a huge backlog. Design the merge, the conflict surface, and the user-visible reconciliation.

## Key Takeaways

- Partitions force consistency vs availability choices
- CRDTs converge deterministically under any topology
- The consistency menu offers cheaper correct options
- Causal consistency covers most app needs

## Further Reading

- [CAP Theorem — Brewer](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/)
- [CRDTs — crdt.tech](https://crdt.tech/)
