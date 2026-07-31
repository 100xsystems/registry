---
title: "Caching: Speed by Storing Computed Answers"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain cache hit rates and why they matter"
  - "Choose cache placement (client, CDN, in-memory, distributed)"
  - "Set TTLs and invalidation strategies"
  - "Identify cache-related consistency bugs"
prerequisites:
  - "principles/base"
  - "principles/eventual-consistency"
knowledge_refs:
  - "principles/caching"
---

# Caching: Speed by Storing Computed Answers

## The Cache Hierarchy

Caches live at every layer: browser, CDN, reverse proxy, application memory, and distributed stores like Redis. Each layer trades staleness for latency. The hottest data sits closest to the user; the source of truth sits farthest.

A hit ratio of 99% for a hot endpoint means 100x fewer expensive queries — caching is usually the first and cheapest scaling lever.

```text
latency pyramid (typical p50):
  CPU L1            ~1ns        (hardware)
  RAM               ~100ns      (in-process dict)
  Redis / Memcached ~1ms        (distributed cache)
  Database          ~5-20ms     (source of truth)
  Network + render  ~100ms+     (uncached path)
```

## Consistency vs Speed

Every cache introduces staleness. The engineering question is not "is it stale?" but "is the staleness bounded and acceptable?" TTLs bound staleness by time; invalidation bounds it by event; versioning bounds it by logic.

## Practice: Pick the Cache Layer

Profile page: 1M reads/day, read-heavy, changes rarely. Product page: changes on price updates. Checkout: must be current.

**Task 1:** Assign a cache layer and TTL to each page type and justify.

**Task 2:** For the product page, design cache invalidation on price change (event-based, not TTL-only).

**Task 3:** Explain why checkout must bypass cache entirely.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about the trade-off between TTL length and consistency for a news feed. Start with hit ratio.

**Prompt 2 — Compare & Contrast:**
> Compare write-through, write-around, and write-back caching for a chat application. When does each make sense?

**Prompt 3 — Boundary Testing:**
> A cache stores a session token that is revoked server-side. Users stay logged in for 10 minutes. Design a revocation mechanism that does not defeat the cache.

## Key Takeaways

- Caching is the cheapest way to cut latency and load
- Staleness is bounded by TTL, invalidation, or versioning
- Place caches closest to the user for hot data
- Never cache the write-critical path

## Further Reading

- [Everything You Wanted to Know About Caching](https://aws.amazon.com/caching/)
- [Caching Strategies — Redis Docs](https://redis.io/docs/latest/develop/use/patterns/caching/)
