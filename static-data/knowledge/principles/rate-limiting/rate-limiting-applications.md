---
title: "Rate Limiting in Production: Distributed Limits"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design distributed rate limiters"
  - "Use Redis-based counters"
  - "Enforce at the edge (CDN, gateway)"
  - "Handle limiter failure modes"
prerequisites:
  []
knowledge_refs:
  - "principles/rate-limiting"
---

# Rate Limiting in Production: Distributed Limits

## Distributed Counting

With many servers behind a load balancer, per-server limits let a client get N× the budget by spreading requests. Distributed counting uses a shared store (Redis INCR with expiry, or a token-bucket service) so the limit is global.

```python
# Redis sliding-window-ish counter (per key, per window)
import redis, time
r = redis.Redis()

def allow(key, limit, window_s):
    now = int(time.time())
    bucket = f'rl:{key}:{now // window_s}'     # fixed window in Redis
    count = r.incr(bucket)
    if count == 1:
        r.expire(bucket, window_s + 1)         # auto-cleanup
    return count <= limit, max(0, window_s - (now % window_s))
```

## Edge Enforcement

The cheapest place to rate-limit is the edge: CDN and gateway rules reject early, before requests consume application capacity. Layered limits — edge (coarse, per IP), gateway (per key), app (per user logic) — catch abuse at the cheapest layer.

## Practice: Layer the Limits

An API with 40 backend servers: clients hit 40 different IPs, so per-server limits are meaningless.

**Task 1:** Design the Redis counter shared across servers with a per-key window.

**Task 2:** Layer edge vs app limits and decide what each enforces.

**Task 3:** Design the failure mode: Redis down. Do you fail open or closed, and what does each cost?

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why per-server limits are useless behind a load balancer and what distributed counting changes.

**Prompt 2 — Implementation Design:**
> Design a token-bucket limiter as a service: the API, the state, and how clients request permits without a round trip.

**Prompt 3 — Boundary Testing:**
> The limiter itself becomes the bottleneck under a flood. Design the degradation (approximate limits at the edge, exact in the app).

## Key Takeaways

- Distributed counting makes limits global
- Redis INCR + expiry is the workhorse counter
- Edge enforcement is the cheapest layer
- Limiter failure modes need explicit fail-open/closed policy

## Further Reading

- [Rate Limiting with Redis](https://redis.io/docs/latest/develop/use/patterns/rate-limiting/)
- [Envoy Rate Limiting Service](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/other_features/global_rate_limiting)
