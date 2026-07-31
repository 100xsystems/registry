---
title: "Advanced Rate Limiting: Token Buckets and Fairness"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Implement a token bucket precisely"
  - "Apply per-tenant fair share"
  - "Design adaptive limits"
  - "Avoid limit-cascades (laddering)"
prerequisites:
  []
knowledge_refs:
  - "principles/rate-limiting"
---

# Advanced Rate Limiting: Token Buckets and Fairness

## Token Bucket

The token bucket allows bursts up to capacity B while sustaining a rate R: tokens refill at R/sec, each request spends one. It is the standard for APIs that must allow bursts but not floods.

```python
# Token bucket (per key)
import time
class TokenBucket:
    def __init__(self, rate, capacity):
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.updated = time.monotonic()

    def take(self):
        now = time.monotonic()
        self.tokens = min(self.capacity,
                          self.tokens + (now - self.updated) * self.rate)
        self.updated = now
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False
```

## Fairness and Ladders

Fair share: when demand exceeds capacity, give each tenant a proportional slice rather than letting the fastest client win. And watch for laddering — a client that crawls upward through tiers (IP limit, then key limit, then account limit) must hit a final cap.

## Practice: Design the Fair Bucket

A multi-tenant platform with 100 tenants; three tenants generate 80% of traffic.

**Task 1:** Design per-tenant token buckets with a global cap.

**Task 2:** Define the fair-share rule when total demand exceeds capacity.

**Task 3:** Design the anti-laddering final cap and the alert on sustained cap-hits.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why token buckets allow bursts while fixed windows cannot.

**Prompt 2 — Implementation Design:**
> Design an adaptive limiter that raises limits when capacity is available and lowers them under pressure, without thrashing.

**Prompt 3 — Boundary Testing:**
> A tenant bursts at exactly the bucket rate for an hour, starving others. Design the fairness override that protects the small tenants.

## Key Takeaways

- Token buckets = burst capacity + sustained rate
- Fair share protects small tenants from big bursts
- Anti-laddering caps close tier-crawl loopholes
- Adaptive limits need hysteresis

## Further Reading

- [Token Bucket — Wikipedia](https://en.wikipedia.org/wiki/Token_bucket)
- [Stripe Rate Limits](https://stripe.com/docs/rate-limits)
