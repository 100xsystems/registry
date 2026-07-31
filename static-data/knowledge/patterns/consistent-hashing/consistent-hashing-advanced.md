---
title: "Advanced Consistent Hashing: Bounded Loads and DHTs"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Apply bounded-load consistent hashing"
  - "Understand DHT ring routing"
  - "Handle churn and replication"
  - "Design load-aware placement"
prerequisites:
  []
knowledge_refs:
  - "patterns/consistent-hashing"
---

# Advanced Consistent Hashing: Bounded Loads and DHTs

## Bounded Loads

Standard consistent hashing balances on average but can overload a hot node. Bounded-load hashing places each key on the closest node that is under a load cap — guaranteeing no node exceeds the cap while keeping placement stable and minimal-movement.

```python
# Bounded-load: place on the nearest under-cap node
def place(key, ring, load, cap):
    start = bisect.bisect_right(ring, h(key)) % len(ring)
    for i in range(len(ring)):
        node = ring[(start + i) % len(ring)]
        if load[node] < cap:
            return node
    raise OverloadedError()      # every node at cap: shed or scale
```

## DHT Routing

Distributed hash tables (Chord, Pastry) extend the ring with finger tables: each node knows a few distant nodes, so lookups jump logarithmically instead of walking the ring. Churn (nodes joining/leaving) is handled by stabilization protocols that fix finger tables continuously.

## Practice: Design Load-Aware Placement

A hot-key product gets 30% of traffic on one node under plain hashing.

**Task 1:** Apply bounded-load placement and show the hot node stays under cap.

**Task 2:** Model the movement cost when the cap forces keys off their natural node.

**Task 3:** Design the DHT-style finger table for log-time lookups under churn.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain the trade-off between load balance and placement stability.

**Prompt 2 — Implementation Design:**
> Design a replicated ring: each key replicated to the next k nodes. What happens when two adjacent nodes die?

**Prompt 3 — Boundary Testing:**
> A hot key exceeds every cap and nothing fits. Design the overflow path (replicate, shed, or scale).

## Key Takeaways

- Bounded-load hashing guarantees per-node caps
- DHT finger tables give log-time routing
- Stabilization handles churn continuously
- Replication across neighbors survives multi-node loss

## Further Reading

- [Bounded Loads — SNAP Paper](https://arxiv.org/abs/1608.01350)
- [Chord: A Scalable P2P Lookup](https://pdos.csail.mit.edu/papers/chord:sigcomm01/chord_sigcomm.pdf)
