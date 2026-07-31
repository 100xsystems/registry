---
title: "Rate Limiting: Control the Flow"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Define rate limiting and its goals"
  - "Use fixed-window and sliding-window algorithms"
  - "Return proper rate-limit responses"
  - "Apply limits per user, IP, and key"
prerequisites:
  - "principles/throttling"
  - "principles/load-shedding"
knowledge_refs:
  - "principles/rate-limiting"
---

# Rate Limiting: Control the Flow

## The Idea

Rate limiting caps how many requests a client (user, IP, API key) can send in a window. It protects shared capacity from a single bursty consumer and from abusive traffic — a runaway loop, a scraper, or a DDoS-ish spike must not starve everyone else.

The simplest forms: fixed window (X requests per minute, reset on the minute) and sliding window (X requests per rolling window, smoother). Token bucket generalizes both with burst control.

```python
# Fixed window limiter (per key)
import time
WINDOW = 60
LIMIT = 30
hits = {}  # key -> (window_start, count)

def allow(key):
    now = time.time()
    start, count = hits.get(key, (now, 0))
    if now - start >= WINDOW:
        start, count = now, 0
    if count >= LIMIT:
        return False, retry_after(WINDOW - (now - start))
    hits[key] = (start, count + 1)
    return True, None
```

## Responses That Teach

A rate-limited request should return 429 with a Retry-After header — the client learns when to try again. Clients that honor it back off; the limit coordinates instead of just blocking. Include X-RateLimit-Limit/Remaining/Reset so clients can self-throttle.

## Practice: Design the Limits

A public API: anonymous users, free tier, paid tier, and an internal service.

**Task 1:** Set rate limits per tier with justification (burst vs sustained).

**Task 2:** Design the 429 response with Retry-After and rate-limit headers.

**Task 3:** Decide the limit granularity: per key, per user, per IP — and why IP alone is insufficient.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about the difference between fixed-window and sliding-window limits at the window boundary.

**Prompt 2 — Compare & Contrast:**
> Compare rate limiting with throttling, load shedding, and circuit breaking. Which problem does each solve?

**Prompt 3 — Boundary Testing:**
> A legitimate user bursts 100 requests in one second at a limit of 60/min. Design the burst allowance (token bucket) that admits them without opening the floodgates.

## Key Takeaways

- Rate limits protect shared capacity from bursts and abuse
- 429 + Retry-After coordinates well-behaved clients
- Sliding windows are smoother than fixed windows
- Token buckets allow controlled bursts

## Further Reading

- [Rate Limiting — MDN/Web standards](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429)
- [An Alternative Approach to Rate Limiting (Figma)](https://www.figma.com/blog/an-alternative-approach-to-rate-limiting/)
