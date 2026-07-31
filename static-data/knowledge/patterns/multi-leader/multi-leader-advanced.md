---
title: "Advanced Multi-Leader: Hybrid Logical Clocks and Ordering"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Order writes with hybrid logical clocks"
  - "Design causal delivery"
  - "Resolve collaborative edits"
  - "Analyze convergence guarantees"
prerequisites:
  []
knowledge_refs:
  - "patterns/multi-leader"
---

# Advanced Multi-Leader: Hybrid Logical Clocks and Ordering

## Ordering Writes

Replica clocks drift, so timestamps cannot order concurrent writes. Hybrid logical clocks (HLC) combine a physical timestamp with a logical counter, capturing causality while staying close to wall time. Causal delivery — deliver operations in causal order — plus CRDT convergence gives collaborative systems their guarantees.

```go
// Hybrid logical clock: physical time + logical counter
type HLC struct {
    mu    sync.Mutex
    pt    int64   // physical ms
    ct    int64   // logical counter
}
func (h *HLC) Now() int64 {
    h.mu.Lock(); defer h.mu.Unlock()
    now := time.Now().UnixMilli()
    if now > h.pt { h.pt = now; h.ct = 0 } else { h.ct++ }
    return h.pt<<16 | h.ct    // sortable, causal
}
// When receiving an event with a higher pt, adopt it and bump ct.
// Events that are causally related get increasing HLCs; concurrent
// events tie-break deterministically (e.g. by origin id).
```

## Collaborative Editing

Real-time editors are multi-leader: every client is a leader, operations replicate, and CRDTs (Yjs, Automerge) or OT (Operational Transformation) merge concurrent edits into a consistent document. The difference: CRDTs converge by construction; OT transforms operations against each other — both are multi-leader conflict resolution refined to text.

## Practice: Build the Editor Merge

Two users edit the same paragraph concurrently on a shared doc.

**Task 1:** Implement the HLC and order the two edits causally.

**Task 2:** Design the CRDT merge and prove both edits survive.

**Task 3:** Compare with the LWW approach: which characters does it lose?

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain what a hybrid logical clock adds over a wall clock.

**Prompt 2 — Implementation Design:**
> Design a distributed todo list where two users reorder the same item list concurrently. What operation-based CRDT handles reordering?

**Prompt 3 — Boundary Testing:**
> A client replays an old operation after reconnecting. Design the idempotent apply that prevents double-effects.

## Key Takeaways

- HLCs give causality to timestamp ordering
- Causal delivery + CRDTs = collaborative guarantees
- CRDTs converge; OT transforms
- Idempotent apply protects against replays

## Further Reading

- [Hybrid Logical Clocks — the paper](https://cse.buffalo.edu/tech-reports/2014-04.pdf)
- [Automerge — CRDTs for apps](https://automerge.org/)
