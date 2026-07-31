---
title: "Load Shedding in Production: Queues and Priorities"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design bounded queues with shed-on-full"
  - "Implement priority admission control"
  - "Shed at multiple layers (edge, app, worker)"
  - "Monitor shedding as a signal"
prerequisites:
  []
knowledge_refs:
  - "principles/load-shedding"
---

# Load Shedding in Production: Queues and Priorities

## Bounded Queues and Admission

An unbounded queue is a latency bomb: work waits so long that it times out, and the queue becomes the outage. A bounded queue with shed-on-full converts overload into fast rejection. Admission control checks the queue depth and the in-flight count before accepting work.

```go
// Admission control: shed when the system is saturated
var sem = make(chan struct{}, 100)     // 100 concurrent jobs
var queueDepth atomic.Int64

func Enqueue(job Job) error {
    if queueDepth.Load() > 50 {
        return errShedding                   // shed fast, before queueing
    }
    if len(sem) >= 100 {
        return errShedding                   // all workers busy
    }
    queueDepth.Add(1)
    sem <- struct{}{}
    go func() { defer func() { <-sem; queueDepth.Add(-1) }(); run(job) }()
    return nil
}
```

## Shedding Layers

Shed at the edge (CDN/load balancer rejects early), at the app (admission control), and at workers (drop lowest-priority jobs). Each layer sheds earlier and cheaper than the one below, protecting the expensive resources closest to the source of truth.

## Practice: Design the Shed Ladder

A search service: query API, index-refresh jobs, analytics export, and autocomplete suggestions.

**Task 1:** Define capacity budgets per layer and per work type.

**Task 2:** Design the shed order and the responses clients see.

**Task 3:** Define the shedding metric dashboard (shed rate, shed by type) and its alerts.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why shedding early (edge) is cheaper than shedding late (worker). Ask me to trace the cost of each.

**Prompt 2 — Implementation Design:**
> Design admission control for a chat system where message delivery must never be shed but analytics may be. What budgets?

**Prompt 3 — Boundary Testing:**
> The shed signal itself gets noisy and clients over-backoff. Design the jitter and the recovery ramp.

## Key Takeaways

- Bounded queues + shed-on-full beat unbounded latency bombs
- Priority admission protects critical work
- Shed at every layer, cheapest first
- Shed rate is a first-class metric with alerts

## Further Reading

- [Admission Control — Google SRE](https://sre.google/sre-book/handling-overload/)
- [Netflix Overload Controls](https://netflixtechblog.com/performance-under-load-9a8a1f4f1e9b)
