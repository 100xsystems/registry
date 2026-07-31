---
title: "Advanced Circuit Breakers: Health Signals and Probing"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Detect failures invisible to status codes"
  - "Implement adaptive HALF_OPEN probing"
  - "Use circuit breakers in multi-node callers"
  - "Combine breakers with load shedding"
prerequisites:
  []
knowledge_refs:
  - "principles/circuit-breaker"
---

# Advanced Circuit Breakers: Health Signals and Probing

## Beyond Status Codes

A dependency can return 200 with stale or corrupt data, or respond slowly without erroring. Track latency percentiles as a health signal: if p99 latency exceeds a threshold, treat the dependency as degraded and open a "latency breaker".

```go
// Latency-based breaker: slow = unhealthy
var p99 = &slidingPercentile{window: 60, p: 0.99}

func Call(ctx context.Context, fn func() (any, error)) (any, error) {
    if p99.value() > 2*time.Second && breaker.isClosed() {
        breaker.open("latency above budget")   // slow path opens too
    }
    start := time.Now()
    v, err := fn()
    p99.add(time.Since(start))
    return v, err
}
```

## Adaptive Probing

Fixed HALF_OPEN probes can flood a barely-recovering dependency. Adaptive probing starts with one probe and ramps the success threshold: after a successful probe, allow a small percentage of traffic, and scale up as the dependency proves healthy.

In multi-node callers, breaker state is per-node — each node independently observes and probes. Coordinate via shared state (e.g., a central health registry) only when nodes would otherwise stampede the probe.

## Practice: Design a Latency-Aware Breaker

A dependency degrades: p99 goes from 80ms to 4s without any error status codes.

**Task 1:** Define the latency threshold and the window over which you measure p99.

**Task 2:** Design the probe ramp: how much traffic is allowed after a successful probe?

**Task 3:** Add a load-shedding rule: when the breaker is open AND the queue is full, reject new work at the edge.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why percentile latency is a better health signal than average latency.

**Prompt 2 — Implementation Design:**
> Design a breaker that distinguishes "provider down" from "provider slow for one tenant" and opens only for the affected tenant.

**Prompt 3 — Boundary Testing:**
> Every caller node opens its breaker simultaneously and all fallbacks point at the same cold cache. Design a fallback hierarchy that avoids the new stampede.

## Key Takeaways

- Latency and data-quality signals catch what status codes miss
- Adaptive probing ramps traffic as recovery proves itself
- Per-node breakers avoid synchronized probe floods
- Breakers + load shedding give end-to-end protection

## Further Reading

- [Latency Percentiles — Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- [Finagle Resilience (Twitter)](https://twitter.github.io/finagle/guide/Clients.html)
