---
title: "Advanced Load Shedding: Adaptive and Fair Shedding"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Estimate capacity from signals, not guesses"
  - "Implement adaptive shedding thresholds"
  - "Shed fairly across tenants"
  - "Prevent shed cascades"
prerequisites:
  []
knowledge_refs:
  - "principles/load-shedding"
---

# Advanced Load Shedding: Adaptive and Fair Shedding

## Signal-Based Capacity

Shedding thresholds are better derived from live signals than static guesses: CPU saturation, queue depth, request latency percentiles, and error rates. An adaptive controller raises the shed threshold as capacity proves itself and lowers it as latency climbs.

```go
// Adaptive: shed when p99 latency exceeds the budget
var p99 latencyPercentile

func shouldShed() bool {
    return p99.value() > 500*time.Millisecond   // latency budget
        || cpu > 0.85                            // resource budget
}
// The threshold is a target, not a constant: under load it responds
// before queues grow, because latency reflects saturation early.
```

## Fair Shedding and Cascades

Shedding must be fair across tenants: one flood should not shed everyone. Per-tenant budgets and per-tenant shed rates isolate the noisy tenant. And shedding must not cascade — if every node sheds simultaneously and the client retries everywhere, the retry storm is the new overload.

Coordination: shed responses carry Retry-After with jitter, and clients exponentially back off. Recovery ramps traffic gradually instead of reopening the floodgates.

## Practice: Design Fair Adaptive Shedding

A multi-tenant analytics platform: one tenant bursts 10x during their marketing campaign.

**Task 1:** Design per-tenant budgets and the fair-share shed rule.

**Task 2:** Design the adaptive threshold from latency signals with hysteresis.

**Task 3:** Design the recovery ramp and the client backoff contract that prevents a retry storm.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why latency percentiles signal saturation earlier than CPU or queue depth.

**Prompt 2 — Implementation Design:**
> Design admission control for a system with three SLA classes (gold/silver/bronze). How does shedding respect the classes?

**Prompt 3 — Boundary Testing:**
> All nodes shed at once and the fleet looks "fine" (low CPU) because work is being rejected. Design the alert that distinguishes healthy shedding from a real outage.

## Key Takeaways

- Derive shed thresholds from live signals
- Per-tenant budgets make shedding fair
- Retry-After with jitter prevents retry storms
- Shedding must be distinguishable from outages in monitoring

## Further Reading

- [Performance Under Load — Netflix](https://netflixtechblog.com/performance-under-load-9a8a1f4f1e9b)
- [AIMD Congestion Control (the classic adaptive scheme)](https://en.wikipedia.org/wiki/Additive_increase/multiplicative_decrease)
