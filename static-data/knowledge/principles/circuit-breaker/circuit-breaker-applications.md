---
title: "Circuit Breakers in Production"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Configure resilience4j/resilience4j-style breakers"
  - "Design meaningful fallbacks per dependency"
  - "Use breaker events for alerting"
  - "Avoid breaker anti-patterns (too sensitive, too slow)"
prerequisites:
  []
knowledge_refs:
  - "principles/circuit-breaker"
---

# Circuit Breakers in Production

## Configuring a Real Breaker

Resilience4j (Java) and similar libraries let you configure sliding-window failure rate, minimum calls, wait duration, and call-timeout. Key tuning: minimum calls prevents a breaker opening on a single transient blip.

```java
// resilience4j: sliding window breaker with fallback
CircuitBreakerConfig config = CircuitBreakerConfig.custom()
    .failureRateThreshold(50)                    // open at 50% failures
    .slidingWindowSize(10)                       // last 10 calls
    .minimumNumberOfCalls(5)                     // require 5 calls first
    .waitDurationInOpenState(Duration.ofSeconds(20))
    .build();
CircuitBreaker cb = CircuitBreaker.of("payments", config);

Supplier<String> safe = CircuitBreaker.decorateSupplier(cb, () ->
    paymentClient.charge(order));
String result = Try.ofSupplier(safe)
    .recover(t -> queueForRetry(order))          // fallback
    .get();
```

## Fallbacks That Matter

A fallback is what users actually experience: serve cached data, show degraded UI, queue the work, or return a default. A fallback that hides the failure entirely (silently dropping money) is worse than a visible error.

## Practice: Wire Breakers Across a Platform

Your platform calls search, recommendations, payments, and email. Each has different failure costs.

**Task 1:** Design thresholds + fallbacks per dependency (payments=queue, search=stale index, email=skip+log, recs=default).

**Task 2:** Define alerting: which breaker openings page on-call, which just log?

**Task 3:** Sketch a dashboard showing breaker state per dependency over time.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why minimumNumberOfCalls prevents flapping breakers and what "flapping" means.

**Prompt 2 — Implementation Design:**
> Design a breaker for a batch job that retries forever. Should the job use a breaker? What does failure fast mean there?

**Prompt 3 — Boundary Testing:**
> A breaker opens but the fallback itself calls the same dependency. Design the guard that prevents fallback recursion.

## Key Takeaways

- Tune with failure rate + minimum calls to avoid flapping
- Fallbacks are the user-visible contract of a breaker
- Breaker events are first-class alerting signals
- Fallbacks must not call the broken dependency

## Further Reading

- [Resilience4j Docs](https://resilience4j.readme.io/docs/circuitbreaker)
- [Fault Tolerance in a High Volume System (Google SRE)](https://sre.google/sre-book/service-level-objectives/)
