---
title: "Throttling in Production: Workers and Backoff"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design worker consumption rates"
  - "Implement exponential backoff with jitter"
  - "Protect downstreams from bursty consumers"
  - "Monitor throttling as a health signal"
prerequisites:
  []
knowledge_refs:
  - "principles/throttling"
---

# Throttling in Production: Workers and Backoff

## Exponential Backoff

When a downstream signals "slow down" (429, timeout, slow response), the client backs off exponentially: 1s, 2s, 4s, 8s, capped — with jitter so synchronized clients do not retry in lockstep. This is throttling as a protocol.

```go
// Exponential backoff with jitter (AWS-style full jitter)
func backoff(attempt int) time.Duration {
    const base = time.Second
    const cap = 30 * time.Second
    exp := float64(1 << min(attempt, 30))   // 1s, 2s, 4s...
    return time.Duration(rand.Float64() * min(exp*float64(base), float64(cap)))
}
// Full jitter: random in [0, exp] prevents synchronized retry storms
```

## Worker Throttles

Workers that consume a queue too fast overwhelm the database or the API they call. A worker throttle — max messages per second, or adaptive to downstream latency — shapes the consumption rate to what the system can absorb.

## Practice: Shape the Consumer

A queue consumer calls a downstream API with a 100 QPS limit; messages arrive at 500/s.

**Task 1:** Design the consumer throttle to stay under the downstream limit.

**Task 2:** Add adaptive backoff when the downstream starts returning 429s.

**Task 3:** Design the alert: when is sustained throttling a downstream problem, not just load?

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why full-jitter backoff prevents retry storms. Ask me to simulate five synchronized clients.

**Prompt 2 — Implementation Design:**
> Design a self-protecting client: it throttles its own requests based on the server's latency signal. What signals does it read?

**Prompt 3 — Boundary Testing:**
> A client backs off forever because the server is permanently down. Design the escalation from backoff to alert to circuit-break.

## Key Takeaways

- Backoff with jitter is throttling as a protocol
- Workers must shape consumption to downstream capacity
- Sustained throttling is a downstream health signal
- Backoff escalates to circuit-breaking when permanent

## Further Reading

- [Exponential Backoff And Jitter — AWS](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/)
- [Google Cloud — Handling Throttling](https://cloud.google.com/storage/docs/retry-strategy)
