---
title: "Graceful Degradation in Production: Fallback Hierarchies"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design multi-tier fallback hierarchies"
  - "Use degraded modes with explicit status"
  - "Protect fallbacks from becoming the bottleneck"
  - "Operate degradation with runbooks"
prerequisites:
  []
knowledge_refs:
  - "principles/graceful-degradation"
---

# Graceful Degradation in Production: Fallback Hierarchies

## Fallback Hierarchies

A fallback chain: live data → cached (fresh TTL) → cached (stale allowed) → static defaults → error. Each tier is slightly worse but still useful, and each has its own staleness and cost profile.

```python
# Fallback hierarchy for a recommendation feed
def recommendations(user_id):
    try:
        return live_recs(user_id)              # tier 1: live
    except Timeout:
        pass
    fresh = cache.get(f'recs:{user_id}')      # tier 2: fresh cache
    if fresh is not None:
        return fresh
    stale = cache.get(f'recs:{user_id}', allow_stale=True)
    if stale is not None:
        return stale, {'degraded': 'stale'}   # tier 3: stale
    return default_recs(), {'degraded': 'default'}  # tier 4: static
```

## Protecting the Fallback

If a million requests all hit the same fallback at once, the fallback becomes the new outage. Cap fallback throughput (rate limits, cached responses served at the edge) so the degraded path itself cannot collapse.

## Practice: Design the Fallback Chain

A maps service loses its live traffic layer. Users still need directions.

**Task 1:** Design the chain: live traffic → cached traffic (10 min) → traffic-free map → static "directions unavailable".

**Task 2:** Cap the fallback tier so it does not become the bottleneck.

**Task 3:** Write the runbook: what the on-call does when the live layer recovers (flush stale cache, verify).

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why fallbacks need their own capacity planning. Ask me to compute the fallback QPS in a degradation scenario.

**Prompt 2 — Implementation Design:**
> Design a degraded checkout that queues payments and reconciles later. What does the user see, and how does recovery work?

**Prompt 3 — Boundary Testing:**
> Stale data in a fallback causes a user-visible contradiction (e.g., "in stock" for a sold-out item). Design the staleness guard and the UI hint.

## Key Takeaways

- Fallback hierarchies trade quality for availability
- Each tier needs its own staleness and cost profile
- Fallbacks need capacity caps or they become the outage
- Runbooks define recovery, not just degradation

## Further Reading

- [Resilience Patterns — Microsoft Docs](https://learn.microsoft.com/en-us/azure/architecture/patterns/category/resiliency)
- [Chaos Engineering — Principles](https://principlesofchaos.org/)
