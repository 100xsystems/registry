---
title: "Advanced Leader-Follower: Multi-Leader and the Raft Connection"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Explain multi-leader topologies"
  - "Resolve concurrent writes"
  - "Compare with Raft consensus"
  - "Design conflict-free data models"
prerequisites:
  []
knowledge_refs:
  - "patterns/leader-follower"
---

# Advanced Leader-Follower: Multi-Leader and the Raft Connection

## Multi-Leader

Multi-leader has several leaders, each accepting writes and shipping to the others — used for multi-datacenter locality and offline-first apps. The cost is write conflicts: two leaders accept the same key concurrently. Conflict resolution (LWW, CRDTs, custom merge) must be deterministic or user-facing.

```typescript
// LWW (last-writer-wins) merge: simple, but loses updates
function merge(a: {v: string; ts: number}, b: {v: string; ts: number}) {
    return a.ts >= b.ts ? a : b;
}
// CRDT (G-Counter): merges by taking the max of every replica counter
//   - no lost updates, no coordinator, deterministic convergence
//   - counter = [replica0, replica1, ...]; value = sum; merge = elementwise max
// Choose: LWW for logs, CRDTs for counters/sets, custom for domain merges.
```

## Raft as Leader-Follower

Raft is leader-follower with consensus: the leader is elected, holds a term/epoch, and replicates through a log with quorum acks. Raft solves the failover problem leader-follower leaves open — a new leader can only be elected with a majority, and old leaders are fenced by term. Most databases borrow Raft for exactly this.

## Practice: Choose the Topology

A notes app must work offline and sync; a billing system must never double-charge.

**Task 1:** Design the offline-first multi-leader sync with a CRDT for the notes.

**Task 2:** Design the single-leader billing path and why it must not be multi-leader.

**Task 3:** Compare the two designs: where does conflict resolution live in each?

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why multi-leader needs conflict resolution and single-leader does not.

**Prompt 2 — Implementation Design:**
> Design a shopping cart that syncs across devices with a CRDT. What is the merge rule for add and remove?

**Prompt 3 — Boundary Testing:**
> LWW loses a critical update because clocks skew. Design the hybrid logical clock that fixes the ordering.

## Key Takeaways

- Multi-leader adds locality at the cost of conflicts
- Conflict resolution must be deterministic or surfaced
- Raft is leader-follower made consensus-safe
- Some workloads must never be multi-leader

## Further Reading

- [CRDTs — an introduction](https://crdt.tech/)
- [Raft Paper](https://raft.github.io/raft.pdf)
