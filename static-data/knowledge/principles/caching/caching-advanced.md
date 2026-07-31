---
title: "Advanced Caching: Distributed Caches and Multi-Tier"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Explain consistent hashing and hotspot avoidance"
  - "Implement cache-aside with lock to avoid duplicate fills"
  - "Design an L1/L2 cache hierarchy"
  - "Handle cache node failure without a stampede"
prerequisites:
  []
knowledge_refs:
  - "principles/caching"
---

# Advanced Caching: Distributed Caches and Multi-Tier

## Consistent Hashing

Distributed caches place keys on nodes with consistent hashing: adding or removing a node only remaps a small fraction of keys, avoiding a full-cache stampede on resharding. Virtual nodes spread load evenly when keys cluster.

```python
# Consistent hashing with virtual nodes (simplified)
import hashlib, bisect

class ConsistentHash:
    def __init__(self, nodes, vnodes=100):
        self.ring = []
        self.nodes = {}
        for n in nodes:
            for v in range(vnodes):
                h = int(hashlib.md5(f"{n}:{v}".encode()).hexdigest()[:8], 16)
                self.ring.append(h); self.nodes[h] = n
        self.ring.sort()

    def get_node(self, key):
        h = int(hashlib.md5(key.encode()).hexdigest()[:8], 16)
        i = bisect.bisect_right(self.ring, h) % len(self.ring)
        return self.nodes[self.ring[i]]
```

## Cache-Aside with Lock

Cache-aside reads: try cache, on miss load from source and populate. Without a lock, concurrent misses duplicate work (mini-stampede). A per-key lock serializes the fill while reads outside the lock still work.

L1 (in-process) + L2 (distributed) caches give single-digit microsecond hits for hot keys while keeping the L2 as a safety net when a node restarts.

## Practice: Design a Multi-Tier Cache

A video-metadata service: 10k videos, metadata changes rarely, read QPS 100k. Six cache nodes, each with 1GB.

**Task 1:** Design L1 (in-process, 10k entries) + L2 (Redis cluster) with invalidation flow across tiers.

**Task 2:** Handle a cache node failure: what happens to the keys it owned? Is there a stampede? How do you prevent it?

**Task 3:** Design the write path: how does a metadata edit invalidate L1 on all servers plus L2 without missing updates?

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can derive why consistent hashing needs virtual nodes for skewed keys, and what happens without them.

**Prompt 2 — Implementation Design:**
> Design a distributed cache where a single node failure must not cause a stampede. Consider backup-key routing and degraded reads.

**Prompt 3 — Boundary Testing:**
> A cache stores a computed recommendation per user, but recommendations change every hour. Design a TTL + async recompute that never serves stale-for-more-than-10-min.

## Key Takeaways

- Consistent hashing makes resharding cheap and non-destructive
- Virtual nodes fix hot-key clustering
- Per-key fill locks prevent duplicate work on miss
- Multi-tier caches trade complexity for microsecond hits

## Further Reading

- [Consistent Hashing — Paper](https://dl.acm.org/doi/10.1145/258533.258642)
- [Cache-Aside Pattern — Microsoft Docs](https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside)
