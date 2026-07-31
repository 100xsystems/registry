---
title: "Advanced Memento: Persistent Structures and Deltas"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Use persistent data structures for undo"
  - "Design delta snapshots"
  - "Implement time travel queries"
  - "Reason about snapshot cost"
prerequisites:
  []
knowledge_refs:
  - "patterns/memento"
---

# Advanced Memento: Persistent Structures and Deltas

## Persistent Structures

A persistent data structure shares structure between versions: modifying one element creates a new version that shares everything else. Undo becomes keeping the old root pointer — O(1) per snapshot instead of O(n) copies. Git is the canonical example: commits are mementos sharing unchanged trees.

```python
# Persistent list via structural sharing (concept)
# v0 = Node(1, Node(2, Node(3)))
# v1 = prepend(v0, 0) -> Node(0, v0)   # shares v0 entirely
#
# Undo = keep a stack of version roots:
history = [root_v0]
root_v1 = prepend(root_v0, 0)          # shares old tail
history.append(root_v1)
root_v2 = prepend(root_v1, -1)         # shares v1's tail (v0 again)
history.append(root_v2)
# Pop the stack to undo: O(1), no copying.
# This is how Git, Clojure's persistent vectors, and
# immutable.js keep history cheap.
```

## Deltas and Time Travel

Delta snapshots store only what changed against the base; restore applies deltas in order. Time travel — querying state as of an instant — is mementos at scale: a database's MVCC keeps version chains; systems with full history (Git, temporal stores) let you inspect any past version cheaply.

## Practice: Design Cheap History

A collaborative document keeps 10k snapshots per session; full copies blow memory.

**Task 1:** Design the persistent-structure undo and measure per-edit cost.

**Task 2:** Design the delta snapshot chain with periodic full bases.

**Task 3:** Implement a time-travel query: state as of edit #4820.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain how structural sharing makes version history nearly free.

**Prompt 2 — Implementation Design:**
> Design a Git-like store for configuration files with branch, merge, and revert. What are the mementos?

**Prompt 3 — Boundary Testing:**
> A delta chain grows 10,000 deep and restore is slow. Design the base-compaction trigger and the worst-case restore.

## Key Takeaways

- Persistent structures share state between versions
- Undo becomes O(1) root-pointer swaps
- Delta chains need periodic full bases
- Time travel is mementos kept forever

## Further Reading

- [Git internals — the object model](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)
- [Persistent data structures — Wikipedia](https://en.wikipedia.org/wiki/Persistent_data_structure)
