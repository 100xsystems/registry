---
title: "Caching: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate caching concepts"
  - "Apply caching reasoning to new workloads"
  - "Identify cache anti-patterns"
prerequisites:
  []
knowledge_refs:
  - "principles/caching"
---

# Caching: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: 99% hit ratio on a 100 QPS endpoint means how many DB queries/sec? (A: 1 / B: 99 / C: 100)
- Q2: A thundering herd is caused by? (A: TTL too long / B: hot key expiry with concurrent misses / C: small cache)
- Q3: Stale-while-revalidate serves? (A: only fresh / B: stale immediately + background refresh / C: errors)
- Q4: True or false: consistent hashing remaps all keys when a node joins.
- Q5: Which path should never be cached? (A: leaderboard / B: checkout balance / C: profile picture)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> Black Friday: a product page key expires and 50k concurrent requests stampede the database. Design the full fix (single-flight + SWR + jitter) and estimate the new DB load.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why invalidation is hard and TTL-only caching eventually bites, with a concrete example.

## Key Takeaways

- Q1: A; Q2: B; Q3: B; Q4: false; Q5: B
- Caching multiplies capacity but introduces staleness
- Stampedes, not TTLs, are the usual production killer
