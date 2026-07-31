---
title: "Advanced Prototype: Structural Sharing and Versioned Clones"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Explain structural sharing"
  - "Build persistent structures"
  - "Version documents by clone"
  - "Analyze clone complexity"
prerequisites:
  []
knowledge_refs:
  - "patterns/prototype"
---

# Advanced Prototype: Structural Sharing and Versioned Clones

## Structural Sharing

A persistent (immutable) data structure clones by sharing: an update copies only the path from root to the changed node and shares the rest. Cloning a document becomes O(log n) or O(1) instead of O(n). The clone is a new version; the old version remains — which is version history for free.

```clojure
; Clojure: persistent structures share structure across versions
(def v0 [1 2 3 4 5 6 7 8])
(def v1 (assoc v0 3 :changed))     ; O(log32 n) — shares v0's tail

; Both v0 and v1 exist simultaneously:
v0   ; => [1 2 3 4 5 6 7 8]
v1   ; => [1 2 3 :changed 5 6 7 8]

; A version stack is just a list of roots:
(def history (list v1 v0))         ; undo = pop, redo = push
; This is the prototype pattern's advanced form: cloning by
; sharing instead of copying. Git's object model is the same idea.
```

## Versioned Clones

With structural sharing, "clone then mutate" becomes "create a new version": each version is a prototype of the next, and history is the chain. Branch and merge operate on version graphs. The cost shifts to garbage collection of unreachable old versions.

## Practice: Design the Version Chain

A collaborative document needs per-edit versions with O(1) undo and cheap forks.

**Task 1:** Implement the persistent structure and measure per-edit cost.

**Task 2:** Design the version chain and the branch/merge operations.

**Task 3:** Design GC for abandoned versions and the retention policy.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why an update touches only the root path in a persistent structure.

**Prompt 2 — Implementation Design:**
> Design a Git-like config versioning: commit, branch, checkout. What are the clones and the shared history?

**Prompt 3 — Boundary Testing:**
> A version chain grows unbounded. Design the snapshot + compact policy that bounds history without losing undo depth.

## Key Takeaways

- Structural sharing makes clones O(log n)
- Versions are clones; history is the chain
- Old versions survive until GC
- Branch and merge are version-graph operations

## Further Reading

- [Persistent data structures — Wikipedia](https://en.wikipedia.org/wiki/Persistent_data_structure)
- [Git — object model](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)
