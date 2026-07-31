---
title: "Multi-Leader Replication: Many Writers, One Log Each"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the multi-leader model"
  - "Describe topologies"
  - "Understand write conflicts"
  - "Know the use cases"
prerequisites:
  - "patterns/leader-follower"
  - "patterns/replication"
knowledge_refs:
  - "patterns/multi-leader"
---

# Multi-Leader Replication: Many Writers, One Log Each

## The Model

Multi-leader has several nodes that each accept writes; each leader replicates to the others. Use cases: multi-datacenter (write near users, async cross-DC sync), offline-first apps (device is a leader), and collaborative editing. The price is that two leaders can accept the same key concurrently — write conflicts.

```text
Multi-leader topology: every leader replicates to every other
  [DC1 leader] <----> [DC2 leader]
        ^                  ^
     writes near        writes near
     users in 1         users in 2
  Conflict example:
    DC1: user edits profile name -> "Alice"
    DC2: user edits profile name -> "Alicia"
    Both accepted concurrently; replication delivers both.
    Resolution (LWW, merge, CRDT, or surface-to-user) is REQUIRED.
  Compare single-leader: one writer, no conflicts, one region.
```

## Topologies

All-to-all replicates everywhere (simple, ordered). Circular and star topologies reduce links but forward through intermediates — a failure can stop propagation, and ordering across the chain is hard to guarantee. All-to-all with conflict-free data models (per-key single-writer) is the safest.

## Practice: Trace the Conflict

A shopping cart syncs between phone and laptop, both leaders, both offline.

**Task 1:** Trace two concurrent edits to the same item count.

**Task 2:** Apply LWW and show the lost update.

**Task 3:** Design the CRDT merge that loses nothing.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why two leaders make conflicts inevitable. Start with the offline window.

**Prompt 2 — Compare & Contrast:**
> Compare multi-leader with single-leader and leaderless. Which fits an offline-first notes app and why?

**Prompt 3 — Boundary Testing:**
> A partition splits the leaders and both serve writes. Design the reconciliation that converges when they reconnect.

## Key Takeaways

- Multi-leader trades consistency for write locality
- Conflicts are inevitable with multiple writers
- Resolution must be explicit: LWW, merge, or CRDT
- Topologies trade links for ordering guarantees

## Further Reading

- [Multi-leader replication — DDIA Ch. 5](https://dataintensive.net/)
- [CRDTs — an introduction](https://crdt.tech/)
