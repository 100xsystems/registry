---
title: "Advanced Bloom Filters: Counting and Scaling"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Implement a counting bloom filter"
  - "Design a scalable (multi-tier) filter"
  - "Shard filters across nodes"
  - "Merge filters in distributed systems"
prerequisites:
  []
knowledge_refs:
  - "patterns/bloom-filter"
---

# Advanced Bloom Filters: Counting and Scaling

## Counting Filters

A counting bloom filter replaces bits with small counters, supporting deletion. The cost: 4x memory. It is the standard when membership changes over time (caching proxies that evict).

```python
# Counting filter: counters instead of bits, deletion supported
class CountingBloom:
    def __init__(self, size, k):
        self.counters = [0] * size
        self.k = k

    def _hashes(self, key):  # returns k positions
        ...

    def add(self, key):
        for p in self._hashes(key):
            self.counters[p] += 1

    def remove(self, key):   # the operation plain filters lack
        for p in self._hashes(key):
            if self.counters[p] > 0:
                self.counters[p] -= 1

    def might_contain(self, key):
        return all(self.counters[p] > 0 for p in self._hashes(key))
```

## Scalable and Distributed

Scalable filters grow by adding tiers when the base saturates; lookups check all tiers. Distributed systems merge filters (bitwise OR) when memberships are unions — gossip protocols use this to spread "I have seen X" cheaply. Counting filters do not merge cleanly; plain ones do.

## Practice: Design the Scalable Filter

A cache membership filter grows past its design size every week.

**Task 1:** Design the tiered scalable filter: when to add a tier, and how lookups check tiers.

**Task 2:** Design cross-node merging for the gossip membership use case.

**Task 3:** Quantify the memory and false-positive trade-off per tier.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why counting filters cannot merge while plain filters can (bitwise OR).

**Prompt 2 — Implementation Design:**
> Design distributed dedupe across 10 nodes: shared filter vs merged per-node filters. What are the consistency requirements?

**Prompt 3 — Boundary Testing:**
> A counter overflows (a hot key set many times). Design the saturation handling that prevents a false-negative.

## Key Takeaways

- Counting filters add deletion at 4x memory
- Scalable filters grow by tiers on saturation
- Plain filters merge via bitwise OR
- Gossip membership loves mergeable filters

## Further Reading

- [Scalable Bloom Filters — Paper](https://gsd.di.uminho.pt/members/cbm/ps/dbloom.pdf)
- [Counting Bloom Filters — Paper](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=6f95bf72914165dc59dd8d07e1db7ab84a33c6f0)
