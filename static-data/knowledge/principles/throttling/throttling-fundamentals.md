---
title: "Throttling: Slow the Flow, Don't Stop It"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Define throttling and distinguish it from rate limiting"
  - "Explain the throttling curve (slowdown, not cutoff)"
  - "Apply throttling to clients and workers"
  - "Return proper throttling signals"
prerequisites:
  - "principles/rate-limiting"
  - "principles/load-shedding"
knowledge_refs:
  - "principles/throttling"
---

# Throttling: Slow the Flow, Don't Stop It

## Throttling vs Rate Limiting

Rate limiting caps the number of requests (a hard budget). Throttling controls the speed at which work proceeds — it slows the flow rather than stopping it. A throttled client gets responses, just slower; a rate-limited one gets 429s.

Think of a valve versus a lock: throttling is the valve that eases pressure; rate limiting is the lock that admits a fixed number. Both protect capacity; they do it differently.

```python
# Throttle: add delay so the flow matches capacity
import time

def throttle(request, tokens_per_sec=50):
    # delay based on how far ahead of the sustained rate we are
    gap = (1 / tokens_per_sec)
    elapsed = time.monotonic() - request.slot_started
    if elapsed < gap:
        time.sleep(gap - elapsed)       # slow down, don't reject
    return process(request)
```

## Where Throttling Lives

Clients throttle their own outbound calls (back off when the server is slow), workers throttle their consumption of a queue (process at a sustainable rate), and servers throttle responses to protect downstream capacity. Each layer eases the flow instead of cutting it.

## Practice: Design the Throttle

A batch client pulls 10k records/min from an API that can safely serve 5k/min.

**Task 1:** Design the client throttle: a token bucket that shapes the pull rate.

**Task 2:** Design the server-side signal (Retry-After on 429, and a smooth slowdown when near capacity).

**Task 3:** Explain when throttling beats hard rate limiting for this workload.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about the difference between shaping traffic (throttle) and capping traffic (rate limit). Start with a burst.

**Prompt 2 — Compare & Contrast:**
> Compare throttling with rate limiting, load shedding, and backpressure. Which is the right tool for a slow consumer?

**Prompt 3 — Boundary Testing:**
> A throttled client slows down but the server is still saturated. Design the escalation from throttle to shed.

## Key Takeaways

- Throttling slows the flow; rate limiting caps it
- The valve metaphor: ease pressure, do not cut it
- Clients, workers, and servers all throttle
- Throttle escalates to shedding when slowing is not enough

## Further Reading

- [Traffic Shaping — Wikipedia](https://en.wikipedia.org/wiki/Traffic_shaping)
- [Retry-After header — MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After)
