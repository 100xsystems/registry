---
slug: patterns-circuit-breaker
title: "Circuit Breaker & Resilience"
description: "Preventing cascade failures with circuit breakers, bulkheads, retry patterns, and graceful degradation."
order: 12
tags:
  - system-design
  - patterns
  - circuit-breaker
  - resilience
  - fault-tolerance
  - bulkhead
prerequisites:
  - fundamentals-availability
  - building-blocks-message-queues
references:
  - title: "Circuit Breaker Pattern"
    author: "Microsoft Azure"
    url: "https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker"
    type: "docs"
    description: "Official Microsoft guide to circuit breaker implementation."
  - title: "Release It! Design and Deploy Production-Ready Software"
    author: "Michael Nygard"
    url: "https://pragprog.com/titles/mnee2/release-it-second-edition/"
    type: "book"
    description: "Foundational text on resilience patterns."
  - title: "Hystrix: Latency and Fault Tolerance"
    author: "Netflix"
    url: "https://github.com/Netflix/Hystrix"
    type: "docs"
    description: "Netflix's circuit breaker library (now legacy but instructive)."  - title: "Resilience4j Documentation"
    author: "Resilience4j"
    url: "https://resilience4j.readme.io/"
    type: "docs"
    description: "Modern resilience library for Java."
  - title: "System Design: Circuit Breaker"
    author: "ByteByteGo"
    url: "https://blog.bytebytego.com/p/circuit-breaker"
    type: "article"
    description: "Visual breakdown of circuit breaker architecture."
related_knowledge:
  - slug: fundamentals-availability
    title: "Availability & Reliability"
    lesson_number: 3
  - slug: building-blocks-load-balancers
    title: "Load Balancers"
    lesson_number: 5
  - slug: patterns-api-gateway
    title: "API Gateway & Rate Limiting"
    lesson_number: 13
knowledge_refs:
  - slug: "patterns-retry"
    title: "Retry Pattern"
  - slug: "patterns-timeout"
    title: "Timeout Pattern"
  - slug: "patterns-bulkhead"
    title: "Bulkhead"
---

# Circuit Breaker & Resilience

When a service fails, retrying aggressively can make things worse — overwhelming the failing service and causing cascade failures. Circuit breakers, bulkheads, and retry patterns prevent this.

## The Circuit Breaker Pattern

Like an electrical circuit breaker, it stops requests when a service is failing:

### Three States

**Closed (Normal):**
- Requests pass through normally
- Failures are counted
- If failures exceed threshold → Open

**Open (Failing):**
- All requests fail immediately (no waiting)
- After timeout → Half-Open

**Half-Open (Testing):**
- Allow a few test requests through
- If they succeed → Closed
- If they fail → Open

### Implementation

```python
class CircuitBreaker:
    def __init__(self, failure_threshold=5, recovery_timeout=30):
        self.failure_count = 0
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.state = "CLOSED"
        self.last_failure_time = None
    
    def call(self, func, *args, **kwargs):
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF_OPEN"
            else:
                raise CircuitBreakerOpen()
        
        try:
            result = func(*args, **kwargs)
            if self.state == "HALF_OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()
            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
            raise
```

## The Bulkhead Pattern

Isolate components so failure in one doesn't bring down everything:

```
Service A → Thread Pool 1 (10 threads) → Payment Service
           → Thread Pool 2 (20 threads) → User Service
           → Thread Pool 3 (15 threads) → Notification Service
```

If Payment Service is slow, only Thread Pool 1 is exhausted. User and Notification services continue normally.

### Bulkhead Types

**Thread Pool Bulkhead:** Separate thread pools for each dependency
**Semaphore Bulkhead:** Limit concurrent calls with a semaphore
**Connection Pool Bulkhead:** Separate connection pools per service

## Retry Patterns

### Simple Retry
```
Attempt 1 → Fail → Attempt 2 → Fail → Attempt 3 → Fail → Give up
```

### Exponential Backoff
```
Attempt 1 → Fail → Wait 1s → Attempt 2 → Fail → Wait 2s → Attempt 3 → Fail → Wait 4s → ...
```

### Exponential Backoff with Jitter
```
Wait time = min(base * 2^attempt + random(0, 1), max_wait)
```
Jitter prevents thundering herd when many clients retry simultaneously.

## Graceful Degradation

When a dependency fails, provide a reduced but functional experience:

| Scenario | Degradation |
|---|---|
| Recommendation service down | Show popular items instead |
| Payment service slow | Queue payment, confirm later |
| Search service down | Show cached results |
| Analytics service down | Buffer events, process later |

## Timeout Strategies

**Connection timeout:** How long to wait for TCP connection (e.g., 5 seconds)
**Read timeout:** How long to wait for response (e.g., 30 seconds)
**Total timeout:** Maximum time for entire operation (e.g., 60 seconds)

**Always set timeouts.** Without them, a slow service can hang threads indefinitely.

---

*References:*
1. Microsoft Azure, "Circuit Breaker Pattern." [Link](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker)
2. Michael Nygard, *Release It!* [Link](https://pragprog.com/titles/mnee2/release-it-second-edition/)
3. Netflix, "Hystrix." [Link](https://github.com/Netflix/Hystrix)
4. Resilience4j, "Documentation." [Link](https://resilience4j.readme.io/)
5. ByteByteGo, "System Design: Circuit Breaker." [Link](https://blog.bytebytego.com/p/circuit-breaker)
