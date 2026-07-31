---
title: "Circuit Breaker in Production: Libraries and Config"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Configure a real breaker library"
  - "Tune thresholds with sliding windows"
  - "Design fallbacks per dependency"
  - "Alert on breaker events"
prerequisites:
  []
knowledge_refs:
  - "patterns/circuit-breaker-pattern"
---

# Circuit Breaker in Production: Libraries and Config

## Sliding-Window Breakers

Libraries like Resilience4j count failures in a sliding window: open at 50% failure over the last 10 calls, with a minimum call count to avoid opening on a blip. The knobs are failure-rate threshold, window size, minimum calls, and wait duration.

```java
// Resilience4j: sliding-window breaker
CircuitBreakerConfig config = CircuitBreakerConfig.custom()
    .failureRateThreshold(50)                  // open at 50% failures
    .slidingWindowSize(10)                     // last 10 calls
    .minimumNumberOfCalls(5)                   // require 5 calls first
    .waitDurationInOpenState(Duration.ofSeconds(20))
    .build();
CircuitBreaker cb = CircuitBreaker.of("search", config);

Supplier<String> safe = CircuitBreaker.decorateSupplier(cb,
    () -> searchClient.query(q));
String result = Try.ofSupplier(safe)
    .recover(t -> staleIndex())                // fallback
    .get();
```

## Fallback Design

The fallback is what users actually see: cached data, degraded UI, a queued retry, or a clear error. A fallback that silently returns wrong data is worse than an error — each dependency gets a fallback designed for its failure cost.

## Practice: Wire the Platform Breakers

Four dependencies: payments, search, recommendations, email. Each has different failure costs.

**Task 1:** Set thresholds + fallbacks per dependency (payments=queue, search=stale, recs=default, email=skip+log).

**Task 2:** Define which breaker events page on-call vs just log.

**Task 3:** Build the dashboard: breaker state per dependency over time.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why minimumNumberOfCalls prevents flapping breakers. Ask me to trace a transient blip.

**Prompt 2 — Implementation Design:**
> Design a breaker for a batch job that retries forever. Should a batch job use a breaker at all?

**Prompt 3 — Boundary Testing:**
> The fallback itself calls the same dependency. Design the guard that prevents fallback recursion.

## Key Takeaways

- Sliding windows + minimum calls prevent flapping
- Fallbacks are the user-visible contract
- Breaker events are alerting signals
- Fallbacks must never call the broken dependency

## Further Reading

- [Resilience4j Docs](https://resilience4j.readme.io/docs/circuitbreaker)
- [Polly (dotnet)](https://github.com/App-vNext/Polly)
