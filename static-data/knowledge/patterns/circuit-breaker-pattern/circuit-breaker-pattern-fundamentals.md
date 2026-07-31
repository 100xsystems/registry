---
title: "Circuit Breaker: Fail Fast, Recover Slow"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the three breaker states"
  - "Open on failure threshold, close on probe success"
  - "Define fallbacks"
  - "Distinguish from retry and timeout"
prerequisites:
  - "principles/circuit-breaker"
  - "patterns/retry"
knowledge_refs:
  - "patterns/circuit-breaker-pattern"
---

# Circuit Breaker: Fail Fast, Recover Slow

## The Pattern

Wrap a dependency call in a breaker with three states: CLOSED (calls flow), OPEN (calls fail fast for a window), HALF_OPEN (a probe tests recovery). Failure counting happens in CLOSED; a successful probe closes, a failed probe reopens.

```python
# Circuit breaker state machine (core)
class Breaker:
    def __init__(self, threshold=5, open_timeout=30):
        self.threshold = threshold
        self.open_timeout = open_timeout
        self.failures = 0
        self.state = 'CLOSED'
        self.opened_at = None

    def allow(self):
        if self.state == 'OPEN':
            if time.time() - self.opened_at > self.open_timeout:
                self.state = 'HALF_OPEN'   # allow one probe
            else:
                return False
        return True

    def record_success(self):
        self.failures = 0
        self.state = 'CLOSED'

    def record_failure(self):
        self.failures += 1
        if self.failures >= self.threshold:
            self.state = 'OPEN'
            self.opened_at = time.time()
```

## The Point

Failing fast in OPEN protects the caller's resources from a dead dependency and gives the dependency recovery room. Without it, every call waits on a timeout, threads exhaust, and the failure cascades.

## Practice: Instrument the Breaker

A search API starts returning 500s; your service times out at 5s per call.

**Task 1:** Choose threshold, open timeout, and the fallback (stale index).

**Task 2:** Trace the timeline: when does it open, what do users see, when does it probe?

**Task 3:** Design the HALF_OPEN probe so it does not flood a recovering API.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why the breaker must fail fast in OPEN rather than retry. Start with thread exhaustion.

**Prompt 2 — Compare & Contrast:**
> Compare circuit breaker with retry, timeout, and bulkhead. Which problem does each solve?

**Prompt 3 — Boundary Testing:**
> The dependency returns 200 with garbage. Design the health signal that opens the breaker anyway.

## Key Takeaways

- OPEN fails fast; HALF_OPEN probes recovery
- Breakers protect caller resources
- Fallbacks define the user-visible degraded state
- Health signals beyond status codes matter

## Further Reading

- [Circuit Breaker — Microsoft Docs](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker)
- [Netflix Hystrix](https://github.com/Netflix/Hystrix/wiki/How-it-Works)
