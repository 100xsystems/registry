---
title: "Advanced Consistency: Causal Ordering and Conflict Resolution"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Explain causal consistency and why apps need it"
  - "Use vector clocks to detect concurrent writes"
  - "Design conflict resolution policies"
  - "Implement last-writer-wins with correct clocks"
prerequisites:
  []
knowledge_refs:
  - "principles/consistency-pattern"
---

# Advanced Consistency: Causal Ordering and Conflict Resolution

## Causal Consistency

Causal consistency guarantees that causally related operations are seen in the same order everywhere — the "I replied to your message, so my reply must be visible after your message" guarantee. It is stronger than eventual, cheaper than strong, and often exactly what chat and feeds need.

Tracking causality is done with vector clocks: each replica maintains a counter per replica, and the full vector establishes happens-before relationships between writes.

```python
# Vector clock: detect causality between writes
class VectorClock:
    def __init__(self, replica, counters=None):
        self.replica = replica
        self.counters = counters or {}     # replica -> logical time

    def tick(self):
        self.counters[self.replica] = self.counters.get(self.replica, 0) + 1

    def merge(self, other):
        for r, c in other.counters.items():
            self.counters[r] = max(self.counters.get(r, 0), c)

    def happens_before(self, other):
        # True if every counter <= other's and at least one <
        return all(self.counters.get(r, 0) <= other.counters.get(r, 0)
                   for r in self.counters) and \
               any(self.counters.get(r, 0) < other.counters.get(r, 0)
                   for r in self.counters)
```

## Resolving Concurrent Writes

When two writes are concurrent (neither happens-before the other), the system must pick: merge (CRDT), last-writer-wins (needs trustworthy clocks), or escalate to the application. The choice is a product decision, not a database one.

## Practice: Detect and Resolve Conflict

A note-taking app: the same note is edited offline on two devices, then both sync.

**Task 1:** Use vector clocks to classify the two edits: one-after-other or concurrent?

**Task 2:** Design a merge that keeps both edits (per-field merge) and identify which fields conflict.

**Task 3:** Add LWW for the title field with a hybrid logical clock. Explain what breaks if clocks are not synchronized.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why wall-clock timestamps alone cannot establish causality, and what a vector clock adds.

**Prompt 2 — Implementation Design:**
> Design causal delivery for a chat system: messages within a conversation must appear in causal order even across devices and offline periods.

**Prompt 3 — Boundary Testing:**
> Two replicas exchange states and their vector clocks both grow unboundedly. Design a pruning strategy that does not break causality.

## Key Takeaways

- Causal consistency orders causally related writes everywhere
- Vector clocks detect concurrency precisely
- Conflict resolution is a product decision
- LWW needs trustworthy clocks or hybrid logical clocks

## Further Reading

- [Vector Clocks — Wikipedia](https://en.wikipedia.org/wiki/Vector_clock)
- [Hybrid Logical Clocks](https://cse.buffalo.edu/tech-reports/2014-04.pdf)
