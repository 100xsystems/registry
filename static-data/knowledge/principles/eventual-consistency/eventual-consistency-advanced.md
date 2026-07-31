---
title: "Advanced Eventual Consistency: Divergence and Reconciliation"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Detect and classify divergent states"
  - "Design reconciliation for divergent writes"
  - "Apply CRDTs where conflict resolution must be automatic"
  - "Avoid LWW data loss with hybrid clocks"
prerequisites:
  []
knowledge_refs:
  - "principles/eventual-consistency"
---

# Advanced Eventual Consistency: Divergence and Reconciliation

## Convergence vs Reconciliation

CRDTs converge automatically: any merge order gives the same result. Non-CRDT replicas need reconciliation: detect the divergence, apply a policy (LWW, merge, conflict UI), and converge. The distinction decides whether users ever see a conflict.

```python
# LWW with hybrid logical clock: causal-ish timestamps
import time
class HLC:
    def __init__(self):
        self.pt = 0            # physical
        self.l = 0             # logical

    def now(self):
        now = time.time_ns() // 1_000_000
        self.pt = max(self.pt, now)
        if now <= self.pt:     # same ms -> logical tick
            self.l += 1
        else:
            self.l = 0
        return self.pt, self.l

def lww_merge(a, b):  # (clock, value) pairs
    return a if a[0] >= b[0] else b   # concurrent ties -> arbitrary
```

## When LWW Loses Data

Last-writer-wins overwrites the whole value, so concurrent edits to different fields destroy one side's work. Field-level LWW (merge per field) and CRDTs (merge per element) recover most of the loss. The rule: the more concurrent editing, the finer the merge granularity must be.

## Practice: Choose a Convergence Strategy

A notes app: two devices edit the same note offline; both sync later.

**Task 1:** Classify the edits: different fields (mergeable), same field (conflict), delete vs edit (tombstone needed).

**Task 2:** Design field-level merge with an HLC and tombstones for deletes.

**Task 3:** Decide where CRDTs are worth it vs a "conflict found — keep both" UI.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why wall-clock LWW is unsafe across nodes without synchronized clocks, and what HLC adds.

**Prompt 2 — Implementation Design:**
> Design a distributed todo list where a completed item on one device and edited item on another must both survive the merge.

**Prompt 3 — Boundary Testing:**
> A delete on replica A races an edit on replica B. Without tombstones the item resurrects. Design the tombstone lifecycle and its cleanup.

## Key Takeaways

- CRDTs converge; non-CRDTs need reconciliation
- LWW at value granularity loses concurrent work
- Field-level and element-level merges preserve more
- Tombstones prevent resurrection; HLCs prevent clock lies

## Further Reading

- [Conflict-Free Replicated Data Types](https://hal.inria.fr/inria-00555588/document)
- [Hybrid Logical Clocks](https://cse.buffalo.edu/tech-reports/2014-04.pdf)
