---
title: "Advanced Retry: Circuit Breakers and Chaos"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Combine retry with circuit breaking"
  - "Set timeout hierarchies"
  - "Shed load under pressure"
  - "Test with chaos"
prerequisites:
  []
knowledge_refs:
  - "patterns/retry"
---

# Advanced Retry: Circuit Breakers and Chaos

## The Full Stack

Retry alone amplifies; the mature stack layers: timeout (bound the attempt), retry (recover transients), circuit breaker (stop trying when the dependency is down), and load shedding (drop work when the system is saturated). Each layer fails fast when the one below cannot recover.

```go
// Layered resilience: timeout -> retry -> breaker -> shed
func Call(ctx context.Context) (Resp, error) {
    if shedder.ShouldDrop() {           // overload: shed now
        return Resp{}, ErrOverloaded
    }
    if !breaker.Allow() {               // circuit open: fail fast
        return Resp{}, ErrCircuitOpen
    }
    ctx, cancel := context.WithTimeout(ctx, 2*time.Second) // bound
    defer cancel()
    err := Retry(ctx, 3, func() error { return client.Do(ctx) })
    if err != nil { breaker.Fail() } else { breaker.Success() }
    return resp, err
}
// A retry only runs when the breaker is closed; an open circuit
// returns immediately instead of amplifying with more attempts.
```

## Chaos Testing

Retry policies rot: they work until a dependency fails in a new way. Chaos testing (inject latency, packet loss, and failures into dependencies) proves the retry stack behaves — recovery time, no amplification, budgets respected. The failure injection is a first-class test suite.

## Practice: Build the Stack

A search service calls an LLM API that is slow, flaky, and expensive.

**Task 1:** Layer: timeout, retry with backoff, circuit breaker, shedder.

**Task 2:** Set the thresholds: timeout budget, error rate to open, retry cap.

**Task 3:** Run a chaos drill: inject 5s latency and verify the stack sheds without amplifying.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why retry without a breaker amplifies a real outage.

**Prompt 2 — Implementation Design:**
> Design the timeout hierarchy for a 3-hop call: client -> gateway -> LLM. What is each timeout, and what retries run at which hop?

**Prompt 3 — Boundary Testing:**
> The breaker opens during a sale and requests fail fast for minutes. Design the half-open recovery and the degraded-response fallback.

## Key Takeaways

- Timeout, retry, breaker, and shedder layer together
- Breakers stop amplification; shedders stop saturation
- Chaos drills prove the stack, not just the code
- Half-open states test recovery safely

## Further Reading

- [Resilience4j — the full toolkit](https://resilience4j.readme.io/)
- [Chaos Engineering — principles](https://principlesofchaos.org/)
