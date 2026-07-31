---
title: "Advanced LRU: Segmented and Adaptive Caches"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Design a two-tier LRU"
  - "Explain ARC adaptation"
  - "Handle cache poisoning"
  - "Co-design caches and data flow"
prerequisites:
  []
knowledge_refs:
  - "patterns/lru-cache"
---

# Advanced LRU: Segmented and Adaptive Caches

## Segmented LRU

Two-tier LRU splits the cache: a small probationary segment for new entries and a protected segment for entries that survive. On a hit in probation, the entry promotes. This resists scan poisoning — a one-time sweep cannot evict the protected hot set, because scans only churn probation.

```python
# Two-tier LRU: probation + protected segments
class SegLRU:
    def __init__(self, capacity):
        self.protected = LRUCache(int(capacity * 0.8))
        self.probation = LRUCache(capacity - int(capacity * 0.8))

    def get(self, key):
        if key in self.protected.cache:
            return self.protected.get(key)
        if key in self.probation.cache:
            self.probation.remove(key)
            self.protected.put(key, value)     # promote on second hit
        return None

# A full sequential scan only fills probation; the protected set
# survives untouched. Cold churn never reaches the hot segment.
```

## ARC and Cache-Aware Design

ARC (Adaptive Replacement Cache) maintains four lists — recent and frequent, ghost and real — and adapts the split between recency and frequency based on which direction the misses point. It often beats plain LRU on mixed workloads. The deeper lesson: cache design must be co-designed with the data access pattern.

## Practice: Resist the Scan

A nightly batch job scans 100x the cache capacity, thrashing the hot set for other tenants.

**Task 1:** Model the damage: what the scan evicts from plain LRU.

**Task 2:** Design the two-tier cache and measure hot-set survival.

**Task 3:** Optionally size an ARC variant and compare on the mixed workload.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why a probation segment absorbs scan churn.

**Prompt 2 — Implementation Design:**
> Design a cache for a database fronting: hot rows protected, range scans in probation. What is the promotion rule?

**Prompt 3 — Boundary Testing:**
> Two tenants share a cache; one scans constantly. Design the isolation (per-tenant segments) that stops the bleed.

## Key Takeaways

- Two-tier LRU resists scan poisoning
- ARC adapts between recency and frequency
- Cache design follows the access pattern
- Multi-tenant caches need isolation

## Further Reading

- [ARC — the paper](https://www.usenix.org/legacy/publications/library/proceedings/fast03/tech/full_papers/megiddo/megiddo.pdf)
- [Cache replacement policies — Wikipedia](https://en.wikipedia.org/wiki/Cache_replacement_policies)
