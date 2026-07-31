---
title: "LRU in Production: Page Caches and Memcached"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Configure eviction policies in Redis"
  - "Understand OS page cache LRU approximation"
  - "Design CDN edge caching"
  - "Monitor hit and eviction rates"
prerequisites:
  []
knowledge_refs:
  - "patterns/lru-cache"
---

# LRU in Production: Page Caches and Memcached

## Redis Eviction

Redis maxmemory policies are LRU families: allkeys-lru evicts any key, volatile-lru only keys with TTL, and LFU variants exist for frequency-shaped workloads. The choice shapes the cache: allkeys-lru protects hot keys globally; volatile-lru lets you pin the important ones by omitting TTL.

```config
# Redis eviction configuration
maxmemory 512mb
maxmemory-policy allkeys-lru   # evict least-recently-used key
# Alternatives:
#   volatile-lru   only evict keys WITH a TTL (others are pinned)
#   allkeys-lfu    evict least-frequently-used (hot keys stay hot)
#   noeviction     return errors instead of evicting (for queues)
```

## Approximation at Scale

The OS page cache and huge caches cannot maintain a perfect LRU list — they approximate with CLOCK-style bit scans (Linux uses an aging approximation of LRU). CDNs combine LRU with popularity tiers: hot objects pinned, warm objects in LRU, cold objects evicted fast.

## Practice: Tune the Cache

A Redis cache serves 90% of reads; the workload has a 5% long tail of one-hit wonders.

**Task 1:** Choose the policy: allkeys-lru vs allkeys-lfu, and justify with the workload.

**Task 2:** Set the maxmemory budget as a fraction of dataset and traffic.

**Task 3:** Design the monitoring: hit rate, eviction rate, and the alert when evictions spike.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why real systems approximate LRU at scale. Ask me what breaks with a perfect LRU on millions of keys.

**Prompt 2 — Implementation Design:**
> Design a CDN cache: object size classes, pinning rules, and the LRU tier per class. How does a viral video behave?

**Prompt 3 — Boundary Testing:**
> Evictions suddenly spike after a deploy. Design the diagnosis: what metrics and what fix?

## Key Takeaways

- Redis offers LRU and LFU policy families
- Perfect LRU is approximated at scale (CLOCK aging)
- TTL pinning lets you protect important keys
- Eviction rate is an operational alarm

## Further Reading

- [Redis — eviction policy docs](https://redis.io/docs/reference/eviction/)
- [Linux page cache — LWN](https://lwn.net/Articles/380931/)
