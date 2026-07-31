---
title: "Advanced BASE: CRDTs and Anti-Entropy"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Explain why merge functions must be commutative and associative"
  - "Build a G-Counter and an OR-Set CRDT"
  - "Understand gossip-based anti-entropy"
  - "Apply CRDTs where locks are unacceptable"
prerequisites:
  []
knowledge_refs:
  - "principles/base"
---

# Advanced BASE: CRDTs and Anti-Entropy

## CRDTs: Convergence Without Coordination

A CRDT is a data type whose replicas can diverge and yet merge deterministically into the same state, provided the merge operation is commutative, associative, and idempotent.

The grow-only counter (G-Counter) is the simplest: each replica keeps its own per-replica count, and the total is the sum across replicas. Merging is just element-wise max.

```python
# G-Counter: each replica owns a slot, total = sum of slots
class GCounter:
    def __init__(self, replica_id, slots=None):
        self.replica_id = replica_id
        self.slots = slots or {}  # replica -> count

    def inc(self):
        self.slots[self.replica_id] = self.slots.get(self.replica_id, 0) + 1

    def value(self):
        return sum(self.slots.values())

    def merge(self, other):
        for r, c in other.slots.items():
            self.slots[r] = max(self.slots.get(r, 0), c)

a, b = GCounter('a'), GCounter('b')
a.inc(); a.inc(); b.inc()          # divergent replicas
a.merge(b); b.merge(a)             # exchange state
assert a.value() == b.value() == 3 # converged
```

## Anti-Entropy and Gossip

Anti-entropy is the background process that keeps replicas converging: each replica periodically exchanges state with a random peer, merging as it goes. Gossip protocols use this to spread updates with logarithmic convergence time.

CRDTs shine precisely because they make the gossip merge a pure function — no consensus, no leader, no locking.

## Practice: Build an OR-Set

An observed-remove set must never resurrect a removed element after a merge.

**Task 1:** Design the state: a set of (element, unique-token) pairs, with add adding a token and remove adding a tombstone token.

**Task 2:** Implement merge as the union of both states. Prove that an element removed on one replica stays removed after merge.

**Task 3:** Extend to an LWW (last-writer-wins) register and explain the clock requirements for correctness.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why a naive set CRDT (union-based) resurrects deleted items, and what tokens fix it.

**Prompt 2 — Compare & Contrast:**
> Compare CRDT convergence with Raft-based consensus. When does a system need Raft despite CRDTs existing? Give concrete systems (e.g., Redis vs Riak).

**Prompt 3 — Implementation Design:**
> Design a distributed collaborative editing system (like a shared notes app) using CRDTs. How do you handle the text model, offline edits, and merge of concurrent typing?

## Key Takeaways

- CRDT merges must be commutative, associative, and idempotent
- G-Counter converges by summing per-replica slots
- Tombstones prevent resurrection in observed-remove sets
- Gossip + CRDTs gives convergence without a leader

## Further Reading

- [CRDTs for Mortals](https://medium.com/@istanbul_techie/crdts-for-mortal-developers-6dcfb10c5a7d)
- [The Paper: Conflict-free Replicated Data Types](https://hal.inria.fr/inria-00555588/document)
