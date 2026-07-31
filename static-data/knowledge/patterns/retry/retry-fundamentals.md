---
title: "Retry: Try Again, Smarter"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Identify transient failures"
  - "Apply exponential backoff"
  - "Add jitter"
  - "Bound retries"
prerequisites:
  - "principles/circuit-breaker"
  - "principles/idempotency"
knowledge_refs:
  - "patterns/retry"
---

# Retry: Try Again, Smarter

## The Problem

Networks drop, services restart, locks time out — transient failures. A retry recovers many of them, but naive retries make things worse: immediate retries hammer a recovering service, and retrying non-idempotent operations double-applies effects. Retry is a policy, not a loop.

```go
// Exponential backoff with jitter — the standard shape
func Retry(ctx context.Context, attempts int, fn func() error) error {
    for i := 0; i < attempts; i++ {
        err := fn()
        if err == nil { return nil }
        if !isTransient(err) { return err }   // permanent: stop now
        base := time.Duration(1<<i) * 100 * time.Millisecond  // 100,200,400..
        sleep := base + time.Duration(rand.Intn(100))*time.Millisecond // jitter
        select {
        case <-time.After(sleep):
        case <-ctx.Done():
            return ctx.Err()                  // honour cancellation
        }
    }
    return lastErr
}
```

## Backoff and Jitter

Exponential backoff doubles the wait per attempt (100ms, 200ms, 400ms...), giving a recovering service room. Jitter — a random offset — prevents thundering herd: without it, all clients retry in sync and amplify the outage. Bounded retries with a max attempt count and a deadline are mandatory.

## Practice: Design the Retry Policy

A checkout calls a payment API that fails transiently under load.

**Task 1:** Classify errors: transient vs permanent. Which should never be retried?

**Task 2:** Apply backoff with jitter and a max attempt count.

**Task 3:** Make the operation idempotent so a retry after a timeout cannot double-charge.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why jitter matters when 100 clients retry together. Start with the herd.

**Prompt 2 — Compare & Contrast:**
> Compare retry with circuit breaker and with timeouts. When does each stop the bleeding?

**Prompt 3 — Boundary Testing:**
> A retry succeeds but the response is lost, so the client retries the idempotent operation. Design the idempotency key flow.

## Key Takeaways

- Retry only transient failures
- Exponential backoff + jitter prevents herds
- Bound attempts and honor deadlines
- Idempotency makes retries safe

## Further Reading

- [Retry pattern — Microsoft Azure](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry)
- [Exponential backoff — AWS docs](https://docs.aws.amazon.com/general/latest/gr/api-retries.html)
