---
title: "Consistent Hashing: Stable Distribution Across Changing Nodes"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the rehash problem"
  - "Describe the hash ring"
  - "Understand why only neighbors move"
  - "Identify cache and shard uses"
prerequisites:
  - "patterns/hash-index"
  - "patterns/sharding"
knowledge_refs:
  - "patterns/consistent-hashing"
---

# Consistent Hashing: Stable Distribution Across Changing Nodes

## The Problem

Naive sharding uses hash(key) % N. When N changes (a node joins or dies), nearly every key remaps — a full cache flush or a migration storm. Consistent hashing maps keys onto a ring and nodes onto the same ring, so a node change only affects its neighbors.

```text
Hash ring (0..2^32):
  keys:   k1 at 100, k2 at 300, k3 at 900
  nodes:  n1 at 200, n2 at 800

  k1 (100) -> n1 (next clockwise: 200)
  k2 (300) -> n2 (800)
  k3 (900) -> n1 (wraps to 200)

Add n3 at 700: only k2 (300) moves from n2 to n3.
k1 and k3 stay put. 1/N of keys move, not all.
```

## Virtual Nodes

With few real nodes, hashing can be skewed (one node owns most of the ring). Virtual nodes place many pseudo-node positions per real node, smoothing the distribution — a standard fix in production systems.

## Practice: Simulate the Ring

A 3-node cache with 1000 keys; one node dies.

**Task 1:** Compute how many keys remap under naive mod vs consistent hashing.

**Task 2:** Explain why only the dead node's keys are lost, and where they go.

**Task 3:** Add virtual nodes (say 100/node) and show the load skew before and after.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why consistent hashing limits remapping to neighbors. Start with the ring walk.

**Prompt 2 — Compare & Contrast:**
> Compare consistent hashing with rendezvous hashing (HRW). When is each preferred?

**Prompt 3 — Boundary Testing:**
> Nodes cluster on the ring and load skews despite hashing. Design virtual-node placement that fixes it.

## Key Takeaways

- The ring maps keys and nodes to one space
- Node changes move only neighbor keys
- Virtual nodes smooth distribution
- It powers caches, shards, and DHTs

## Further Reading

- [Consistent Hashing — Wikipedia](https://en.wikipedia.org/wiki/Consistent_hashing)
- [Consistent Hashing Paper (Karger et al.)](https://dl.acm.org/doi/10.1145/258533.258642)
