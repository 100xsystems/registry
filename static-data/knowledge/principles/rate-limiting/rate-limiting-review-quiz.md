---
title: "Rate Limiting: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate rate-limiting concepts"
  - "Design limiter algorithms"
  - "Apply fair distribution"
prerequisites:
  []
knowledge_refs:
  - "principles/rate-limiting"
---

# Rate Limiting: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: The rate-limit response status is? (A: 200 / B: 429 / C: 500)
- Q2: A token bucket allows? (A: controlled bursts / B: no bursts / C: unlimited)
- Q3: Behind a load balancer, limits must be? (A: distributed / B: per server / C: disabled)
- Q4: True or false: Retry-After tells the client when to retry.
- Q5: Fair share protects? (A: the loudest tenant / B: small tenants / C: the edge)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> A flash sale: 1M users hit a checkout API. Design the layered rate limits (edge, gateway, app), the token buckets, and the 429 contract.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why rate limiting is a coordination signal, not just a rejection.

## Key Takeaways

- Q1: B; Q2: A; Q3: A; Q4: true; Q5: B
- Limits protect capacity and coordinate clients
- Algorithms choose the burst/smoothness trade-off
