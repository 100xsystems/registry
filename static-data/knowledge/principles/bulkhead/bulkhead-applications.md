---
title: "Bulkheads in Production Systems"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Apply bulkheads to database and HTTP connection pools"
  - "Use process/instance isolation for the strongest bulkhead"
  - "Size pools from real latency and throughput data"
  - "Combine bulkheads with backpressure correctly"
prerequisites:
  []
knowledge_refs:
  - "principles/bulkhead"
---

# Bulkheads in Production Systems

## Connection Pools as Bulkheads

Database connection pools are the most common bulkhead: a bounded pool per datasource. If one database dies, its pool drains (or errors fast) while other datasources keep serving.

Never share one connection pool across a hot path and a batch path — the batch job will starve the hot path of connections.

```go
// Separate pools per dependency in Go
var dbPool = make(chan struct{}, 20)      // DB: 20 concurrent
var cachePool = make(chan struct{}, 10)   // Cache: 10 concurrent

func queryDB(q string) (Row, error) {
    dbPool <- struct{}{}                  // acquire ticket
    defer func() { <-dbPool }()           // release ticket
    return db.QueryRow(q)
}
```

## Instance-Level Bulkheads

The strongest bulkhead is a separate process or deployment: an ML-scoring service that OOMs cannot take down the API that calls it. This trades cost for isolation.

Microservices are, in part, an exercise in bulkheading at the process level — each service is a compartment with its own memory, CPU, and lifecycle.

## Practice: Size the Pools

You have 4 core services: checkout (60 RPS), search (200 RPS), recommendations (50 RPS), image resize (10 RPS). Each downstream call takes ~80ms p95.

**Task 1:** Use Little's Law (concurrency = rate × latency) to size each pool.

**Task 2:** Add 30% headroom and explain the trade-off between isolation and cost.

**Task 3:** Decide which dependency deserves its own deployment and why.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why Little's Law dictates pool sizing and what happens when concurrency exceeds pool capacity. Ask me to compute examples.

**Prompt 2 — Implementation Design:**
> Design bulkheads for a lambda/serverless architecture where there are no long-lived pools. How do you isolate there?

**Prompt 3 — Boundary Testing:**
> A memory-cache failure now floods the database because the cache miss path has no pool. Where do you add the bulkhead?

## Key Takeaways

- Connection pools are cheap, effective bulkheads
- Never share a pool between hot and batch paths
- Separate deployments give the strongest isolation
- Pool sizes come from Little's Law, not guesses

## Further Reading

- [Little's Law and Pool Sizing](https://en.wikipedia.org/wiki/Little%27s_law)
- [Hystrix Thread Pools](https://github.com/Netflix/Hystrix/wiki/How-it-Works)
