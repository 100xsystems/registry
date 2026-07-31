---
title: "Advanced Throttling: Adaptive and Fair Throttles"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Design adaptive throttle rates from feedback"
  - "Throttle fairly across consumers"
  - "Combine throttling with backpressure"
  - "Avoid throttle oscillation"
prerequisites:
  []
knowledge_refs:
  - "principles/throttling"
---

# Advanced Throttling: Adaptive and Fair Throttles

## Adaptive Rates

A fixed throttle rate is a guess; an adaptive one learns from feedback: measure downstream latency or queue depth, and raise or lower the rate smoothly (with hysteresis) to track the system's real capacity.

```go
// Adaptive: track downstream p99, adjust rate with AIMD-like logic
var p99 latencyPercentile
var rate = 100.0   // requests/sec

func tick() {
    if p99.value() > 500*time.Millisecond {
        rate *= 0.8            // multiplicative decrease (smooth)
    } else if p99.value() < 200*time.Millisecond {
        rate *= 1.05           // additive increase (cautious)
    }
    rate = clamp(rate, 10, 5000)
}
// Hysteresis: thresholds far apart prevent oscillation
```

## Fair Throttling

When multiple consumers share a downstream, fair throttling gives each a proportional slice of the rate — a chatty consumer cannot starve the quiet ones. Per-consumer budgets with a global cap implement fairness.

## Practice: Design the Adaptive Fair Throttle

Ten workers consume from one API; two workers are noisy; downstream capacity fluctuates.

**Task 1:** Design per-worker budgets with a fair-share rule.

**Task 2:** Add the adaptive rate driven by downstream p99 with hysteresis.

**Task 3:** Design the oscillation guard and the convergence test.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why AIMD (additive increase, multiplicative decrease) is the classic safe adaptive scheme.

**Prompt 2 — Implementation Design:**
> Design a throttling library clients embed: it reads server signals, shapes local rate, and reports. What is the wire protocol?

**Prompt 3 — Boundary Testing:**
> Downstream p99 spikes from an unrelated tenant and your adaptive throttle overreacts. Design the signal separation.

## Key Takeaways

- Adaptive rates track real capacity from feedback
- AIMD with hysteresis is the safe adaptive scheme
- Fair throttling protects quiet consumers
- Separate your signal from the noise of other tenants

## Further Reading

- [AIMD Congestion Control](https://en.wikipedia.org/wiki/Additive_increase/multiplicative_decrease)
- [gRPC Adaptive Throttling](https://github.com/grpc/proposal/blob/master/A62-google-default-credentials.md)
