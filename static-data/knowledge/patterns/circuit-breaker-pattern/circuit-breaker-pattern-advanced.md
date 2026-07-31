---
title: "Advanced Circuit Breaker: Health Signals and Probing"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Open on latency and data-quality signals"
  - "Design adaptive HALF_OPEN probing"
  - "Coordinate breakers across nodes"
  - "Avoid synchronized probe storms"
prerequisites:
  []
knowledge_refs:
  - "patterns/circuit-breaker-pattern"
---

# Advanced Circuit Breaker: Health Signals and Probing

## Signals Beyond Status

A dependency can return 200 while being slow or returning garbage. Track p99 latency and response validity as health signals: if p99 exceeds a budget or validation fails, treat the dependency as degraded and open the breaker.

```go
// Latency-based breaker signal
var p99 = percentile(0.99, window=60)

func Call(ctx context.Context, fn func() (any, error)) (any, error) {
    if p99.value() > 2*time.Second && breaker.isClosed() {
        breaker.open("p99 above budget")     // slow = degraded too
    }
    start := time.Now()
    v, err := fn()
    p99.add(time.Since(start))
    return v, err
}
```

## Adaptive Probing

Fixed HALF_OPEN probes can flood a barely-recovering dependency. Adaptive probing starts with one probe and ramps traffic as success proves out. In multi-node callers, per-node state means synchronized probes — coordinate via a shared health registry or stagger probes with jitter.

## Practice: Design the Adaptive Breaker

A dependency degrades: p99 goes 80ms -> 4s with no error codes.

**Task 1:** Define the latency threshold and measurement window.

**Task 2:** Design the probe ramp: 1 call, then 1% traffic, then scale as healthy.

**Task 3:** Add jitter so 20 caller nodes do not probe in lockstep.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why percentile latency beats average latency as a health signal.

**Prompt 2 — Implementation Design:**
> Design a per-tenant breaker: one tenant's flood opens only their breaker. What state and keys?

**Prompt 3 — Boundary Testing:**
> All callers open simultaneously and all fallbacks hit one cold cache. Design the fallback hierarchy that avoids the new stampede.

## Key Takeaways

- Latency and validity signals catch what codes miss
- Adaptive probes ramp traffic as recovery proves
- Per-node breakers need coordination or jitter
- Fallback hierarchies must not create a new stampede

## Further Reading

- [Google SRE — Handling Overload](https://sre.google/sre-book/handling-overload/)
- [Finagle Resilience (Twitter)](https://twitter.github.io/finagle/guide/Clients.html)
