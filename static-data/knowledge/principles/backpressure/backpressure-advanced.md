---
title: "Advanced Backpressure Patterns"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Combine rate limiting with backpressure correctly"
  - "Build adaptive batching that responds to consumer speed"
  - "Propagate backpressure across service boundaries"
  - "Handle multi-tenant backpressure without starving tenants"
prerequisites:
  - "principles/backpressure/backpressure-applications"
  - "principles/rate-limiting"
knowledge_refs:
  - "principles/backpressure"
---

# Advanced Backpressure Patterns

## Backpressure vs Rate Limiting

Rate limiting is producer-side: it caps how much work enters the system. Backpressure is consumer-side: it signals the producer to slow down based on actual capacity. The two are complementary — a rate limit is the safety ceiling, backpressure is the adaptive floor.

## Adaptive Batching

An adaptive consumer measures its own processing rate and adjusts the batch size it requests. When the rate drops (GC pause, cold cache), it shrinks demand; when it rises, it grows demand. This keeps latency low and memory flat.

```python
# Adaptive batch sizing from measured throughput
import time

def next_batch_size(current_bps: float, target_latency_ms: int) -> int:
    # aim: batch roughly equals target_latency_ms of work
    per_item_us = 1_000_000 / max(current_bps, 1e-6)
    desired = target_latency_ms * 1000 / per_item_us
    return int(max(1, min(desired, 1000)))  # clamp 1..1000
```

## Practice: End-to-End Backpressure Design

Design flow control for: client → API gateway → worker pool → PostgreSQL.

**Task 1:** Decide where each layer applies pressure: client-side retry backoff, gateway request queues, worker pool bounds.

**Task 2:** Model the failure mode when PostgreSQL connection pool is exhausted. Does the gateway queue grow unbounded?

**Task 3:** Add a circuit breaker between the gateway and the worker pool. Where does it sit relative to backpressure?

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why TCP-style sliding windows are the canonical backpressure mechanism and how they map to an HTTP API that returns 429.

**Prompt 2 — Boundary Testing:**
> A single tenant floods the system. Design backpressure that degrades only that tenant while protecting others (shard-local tokens, per-tenant queues).

**Prompt 3 — Implementation Design:**
> Implement an adaptive batch consumer in Go using channels where the worker reports its processing rate back to the fetcher. Sketch the goroutines and channels.

## Key Takeaways

- Rate limiting caps entry; backpressure adapts to real capacity
- Adaptive batching keeps latency bounded under load changes
- Backpressure must propagate end-to-end or buffers hide the problem
- Multi-tenant systems need per-tenant pressure isolation

## Further Reading

- [Backpressure in Reactive Manifesto](https://www.reactivemanifesto.org/glossary#Back-Pressure)
- [Designing Data-Intensive Applications, Ch. 11](https://dataintensive.net/)
