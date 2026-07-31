---
title: "Defensive Programming in Production: Errors and Fallbacks"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design an error taxonomy for a service"
  - "Build safe fallbacks that never hide corruption"
  - "Protect persistent state with atomic writes"
  - "Log structured context for post-mortems"
prerequisites:
  []
knowledge_refs:
  - "principles/defensive-programming"
---

# Defensive Programming in Production: Errors and Fallbacks

## Error Taxonomy

Classify errors: expected (validation), transient (timeouts, 503), and unexpected (bugs). Each class gets a policy: expected → 4xx with message; transient → retry with backoff; unexpected → 500, alert, and detailed logs.

```go
// Error taxonomy drives policy
var (
    ErrInvalid = errors.New("invalid input")    // expected -> 4xx
    ErrTimeout = errors.New("upstream timeout") // transient -> retry
    ErrBroken  = errors.New("internal bug")     // unexpected -> alert
)

func handle(e error) {
    switch {
    case errors.Is(e, ErrInvalid): respond(400, e)
    case errors.Is(e, ErrTimeout): retryWithBackoff(e)
    default: alertAndLog(e)                     // never swallow
    }
}
```

## Atomic State Changes

When a step fails partway through a multi-step write, partial state corrupts the system. Write-then-commit (WAL, temp-file + rename, outbox pattern) ensures the visible state is always a complete state.

## Practice: Design the Error Policy

A sync service pulls from 3 sources and writes to a local store.

**Task 1:** Classify failures: source timeout, schema change, disk full, record too large.

**Task 2:** Design the atomic commit for a batch (all-or-nothing per batch, retry-able).

**Task 3:** Define what gets logged for each class so a post-mortem is possible.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why "try/catch everything" is as harmful as "catch nothing". Ask me to rank error-handling strategies.

**Prompt 2 — Implementation Design:**
> Design a fallback for a feature flag service: when it is unreachable, what do you serve — and how do you avoid serving a dangerous default?

**Prompt 3 — Boundary Testing:**
> A retry loop double-applies a side effect (payment). Design idempotency keys as the defensive guard.

## Key Takeaways

- Classify errors to drive policy automatically
- Fallbacks must never hide corruption
- Atomic writes prevent partial-state bugs
- Structured logs make unexpected errors debuggable

## Further Reading

- [Robust Error Handling — Google Style Guide](https://google.github.io/styleguide/)
- [Error Handling in Go — The Go Blog](https://go.dev/blog/error-handling-and-go)
