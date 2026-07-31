---
title: "Load Shedding: Drop Work Before the System Drops"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Define load shedding and its goal"
  - "Distinguish shedding from failing"
  - "Pick what to shed (queues, non-essential work)"
  - "Signal shedding to clients"
prerequisites:
  - "principles/circuit-breaker"
  - "principles/graceful-degradation"
knowledge_refs:
  - "principles/load-shedding"
---

# Load Shedding: Drop Work Before the System Drops

## The Idea

When demand exceeds capacity, a system has three options: queue (and build latency until timeout), fail all (and take the whole service down), or shed (reject the least-valuable work and serve the rest well). Load shedding is the third: deliberate, prioritized rejection.

The goal is to protect the work already in flight and the core function — a video platform under load sheds low-priority transcoding before it drops playback.

```python
# Priority-based shedding at the edge
import time
IN_FLIGHT = 0
MAX_IN_FLIGHT = 200

def handle(request):
    global IN_FLIGHT
    if IN_FLIGHT >= MAX_IN_FLIGHT:
        if request.priority == 'critical':
            pass                    # only critical traffic gets in
        else:
            return 503_retry_after(2)   # shed: fast, explicit, retryable
    IN_FLIGHT += 1
    try:
        return process(request)
    finally:
        IN_FLIGHT -= 1
```

## Shedding vs Failing

Shedding is honest and explicit: reject with 429/503, a Retry-After header, and a clear reason. It tells the client "try later", so the client backs off instead of retrying harder. Shedding well is a coordination signal, not just a rejection.

## Practice: Pick What to Shed

A ticket site is overloaded during a flash sale. Requests: browsing, seat holds, checkout, analytics events, admin dashboard.

**Task 1:** Rank the traffic by value and decide the shed order.

**Task 2:** Design the response for shed traffic (status, Retry-After, message).

**Task 3:** Decide what MUST never be shed and why (seat holds mid-checkout).

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why queueing everything is worse than shedding the least-valuable work. Start with latency cliffs.

**Prompt 2 — Compare & Contrast:**
> Compare load shedding, rate limiting, and circuit breakers. When is each the right response to overload?

**Prompt 3 — Boundary Testing:**
> A client ignores 503s and retries immediately. Design the backoff contract and the server-side guard.

## Key Takeaways

- Shed the least-valuable work to protect the rest
- Explicit 429/503 with Retry-After is honest shedding
- Never shed in-flight critical work
- Shedding signals coordination to well-behaved clients

## Further Reading

- [Handling Overload — Google SRE Book](https://sre.google/sre-book/handling-overload/)
- [Load Shedding in Envoy](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/load_balancing/overload_manager)
