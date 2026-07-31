---
title: "Circuit Breakers: Stop Calling a Dead Dependency"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the three circuit breaker states"
  - "Describe why failing fast beats failing slowly"
  - "Implement a basic circuit breaker"
  - "Choose thresholds and timeouts"
prerequisites:
  - "principles/bulkhead"
  - "principles/graceful-degradation"
knowledge_refs:
  - "principles/circuit-breaker"
---

# Circuit Breakers: Stop Calling a Dead Dependency

## The Problem: Slow Failures Cascade

When a downstream service is down, callers that keep waiting occupy threads, connections, and queues. Their timeouts stack up, the caller's resources exhaust, and the failure cascades upstream — an outage that started in one service spreads to the whole platform.

A circuit breaker wraps the dependency: when failures cross a threshold, the breaker "opens" and subsequent calls fail immediately (or hit a fallback) without touching the broken dependency. It gives the dependency time to recover while the caller stays healthy.

```python
# A minimal circuit breaker (closed -> open -> half-open)
class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout_s=30):
        self.failure_threshold = failure_threshold
        self.timeout_s = timeout_s
        self.failures = 0
        self.state = 'CLOSED'
        self.opened_at = None

    def call(self, fn, fallback):
        if self.state == 'OPEN':
            if time_since(self.opened_at) > self.timeout_s:
                self.state = 'HALF_OPEN'   # try one probe call
            else:
                return fallback()          # fast fail
        try:
            result = fn()
            self.failures = 0
            self.state = 'CLOSED'
            return result
        except Exception:
            self.failures += 1
            if self.failures >= self.failure_threshold:
                self.state = 'OPEN'
                self.opened_at = now()
            return fallback()
```

## The Three States

CLOSED: calls go through normally, failures counted. OPEN: calls fail fast for the timeout window. HALF_OPEN: a single probe call tests recovery — success closes the breaker, failure reopens it.

This state machine is what makes the pattern self-healing: it probes the dependency periodically without flooding it.

## Practice: Instrument a Breaker

Your service calls a payment provider. It starts returning 503s. 40% of your requests start timing out at 5s.

**Task 1:** Set the failure threshold, timeout, and fallback (queue the payment for retry). Justify each number.

**Task 2:** Sketch the timeline: when does the breaker open, and what do users see during OPEN?

**Task 3:** Design the HALF_OPEN probe so it does not flood the recovering provider (one probe, then a ramp).

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time to reason about the difference between a timeout and a circuit breaker. Start with the resource cost of slow failures.

**Prompt 2 — Compare & Contrast:**
> Compare circuit breakers with retries, bulkheads, and rate limiting. Which one prevents the flood, contains it, and heals the source?

**Prompt 3 — Boundary Testing:**
> A breaker is closed, but the dependency returns 200s with garbage data. Your circuit is "healthy" while behavior is broken. How do you detect that failure mode?

## Key Takeaways

- Slow failures are more dangerous than fast ones
- OPEN fails fast, giving the dependency time to recover
- HALF_OPEN probes recovery without flooding
- Breakers need health signals beyond HTTP status codes

## Further Reading

- [Circuit Breaker Pattern — Microsoft Docs](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker)
- [Netflix Hystrix Circuit Breaker](https://github.com/Netflix/Hystrix/wiki/How-it-Works)
