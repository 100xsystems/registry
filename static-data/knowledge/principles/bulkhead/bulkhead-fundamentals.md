---
title: "Bulkheads: Isolating Failure Domains"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the bulkhead pattern as failure isolation"
  - "Partition thread pools, connections, and memory"
  - "Design per-dependency resource budgets"
  - "Recognize shared-resource coupling in a system diagram"
prerequisites:
  - "principles/circuit-breaker"
  - "principles/graceful-degradation"
knowledge_refs:
  - "principles/bulkhead"
---

# Bulkheads: Isolating Failure Domains

## The Shared-Pool Trap

A single shared thread pool looks efficient: one pool for all HTTP calls, database calls, and cache calls. But when the database slows down, its queued tasks occupy every thread, and HTTP requests begin to time out — a cascade across all services.

Bulkheads partition resources per dependency (or per tenant) so that one failing or slow dependency can only exhaust its own budget. The term comes from ship design: a hull is divided into compartments so a breach floods only one.

```java
// Per-dependency thread pools instead of one shared pool
ExecutorService dbPool   = Executors.newFixedThreadPool(10);  // DB calls
ExecutorService cachePool = Executors.newFixedThreadPool(5);  // cache calls
ExecutorService httpPool  = Executors.newFixedThreadPool(20); // outbound HTTP

// A slow DB now blocks only its own 10 threads; HTTP still works
Future<Row> row = dbPool.submit(() -> db.query(sql));
```

## Resource Budgets Per Tenant

In multi-tenant systems, one noisy tenant can exhaust shared queues. Per-tenant semaphores, rate limits, and connection limits keep a single tenant from degrading the platform for everyone.

Bulkheads do not prevent the failure; they contain it. Pair them with timeouts and circuit breakers so contained failures heal quickly.

## Practice: Redesign a Monolithic Pool

A service handles payments, search, and image uploads through one 100-thread pool. Search backend starts failing with 2s latency.

**Task 1:** Split into three pools sized by expected load and SLA. Justify sizes.

**Task 2:** Add per-pool queue bounds and rejection policy (what happens when payments pool is full?).

**Task 3:** Add a circuit breaker around the search pool so it stops wasting threads on a dead backend.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time to help me reason about when a shared pool is acceptable and when it must be partitioned. Start with the failure cascade mechanics.

**Prompt 2 — Compare & Contrast:**
> Contrast bulkheads with circuit breakers and rate limiting. Which prevents the flood, which contains the flood, and which heals the source?

**Prompt 3 — Boundary Testing:**
> A bulkhead isolates per tenant but the largest tenant is 40% of traffic. Design a sizing rule that still protects small tenants during the large one's failure.

## Key Takeaways

- Shared pools turn one slow dependency into a full outage
- Bulkheads partition resources so failures stay contained
- Pair bulkheads with timeouts and circuit breakers
- Per-tenant budgets protect the platform from noisy neighbors

## Further Reading

- [Bulkhead Pattern — Microsoft Docs](https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead)
- [Release It! (Michael Nygard)](https://pragprog.com/titles/mnee2/release-it-second-edition/)
