---
title: "Multi-Leader in Production: Conflict Resolution"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Apply LWW correctly"
  - "Design CRDT merges"
  - "Build conflict-free schemas"
  - "Test conflict resolution"
prerequisites:
  []
knowledge_refs:
  - "patterns/multi-leader"
---

# Multi-Leader in Production: Conflict Resolution

## Resolution Strategies

Last-writer-wins uses timestamps — simple, but clock skew silently loses updates. CRDTs merge deterministically (counters, sets, registers) and converge without a coordinator. Custom merges understand the domain (merge concurrent list edits by position). The right strategy depends on the semantic cost of losing an update.

```typescript
// CRDT examples that merge without a coordinator:
//  G-Counter (grow-only): merge = elementwise max; value = sum
//  G-Set / OR-Set: merge = union (removes tracked via tombstones)
//  LWW-Register: merge = take the higher (value, timestamp) pair
//  Convergent by construction: same inputs in any order, same result

// A merge for concurrent set edits (OR-Set style):
function mergeSets(a: Set<string>, b: Set<string>): Set<string> {
    // union of adds minus union of removes (both tracked with IDs)
    const adds = union(a.adds, b.adds);
    const removes = union(a.removes, b.removes);
    return new Set([...adds].filter(x => !removes.has(x)));
}
```

## Schema Design

The best conflict handling is avoiding conflicts: assign each key a single writing leader (shard by user), or design data as CRDT-friendly operations (add/remove with IDs rather than whole-list overwrites). Conflict-free schemas beat clever resolution every time.

## Practice: Design the Conflict-Free Schema

A shared grocery list syncs across family phones; items are added and checked off concurrently.

**Task 1:** Design the item-level operations (add id, check id) instead of list overwrites.

**Task 2:** Implement the merge and prove convergence with concurrent edits.

**Task 3:** Test the LWW alternative and document which update it loses.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why operation-based CRDTs beat state-based ones for lists, and what tombstones are for.

**Prompt 2 — Implementation Design:**
> Design a multi-leader calendar where the same slot is booked from two devices. What merge policy serves both users?

**Prompt 3 — Boundary Testing:**
> Clocks skew 30s between two leaders. Design the hybrid logical clock that fixes LWW ordering.

## Key Takeaways

- LWW is simple but loses updates under skew
- CRDTs converge deterministically
- Conflict-free schemas beat clever resolution
- Concurrent operation design matters more than merge code

## Further Reading

- [CRDT — crdt.tech](https://crdt.tech/)
- [Yjs — CRDTs for collaborative editing](https://docs.yjs.dev/)
