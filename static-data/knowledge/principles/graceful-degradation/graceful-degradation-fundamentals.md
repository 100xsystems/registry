---
title: "Graceful Degradation: Fail Partially, Stay Useful"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Define graceful degradation and its goals"
  - "Identify degradable and non-degradable features"
  - "Design fallbacks per dependency"
  - "Communicate degraded state to users"
prerequisites:
  - "principles/circuit-breaker"
  - "principles/fail-fast"
knowledge_refs:
  - "principles/graceful-degradation"
---

# Graceful Degradation: Fail Partially, Stay Useful

## The Idea

Graceful degradation means when a dependency fails, the system serves the next-best experience instead of an error page. The search engine that falls back to cached results, the checkout that queues payments, the map that loads without live traffic — each is a degraded-but-useful state.

The alternative is the all-or-nothing failure: one dead dependency takes down the whole page, the whole app, the whole platform. Degradation converts a full outage into a partial, honest one.

```typescript
// Degrade: serve cached data when the live API fails
async function getFeed(): Promise<Feed> {
    try {
        const live = await fetchFeedApi();
        cache.set('feed', live, 5 * 60_000);
        return live;
    } catch {
        const cached = cache.get('feed');
        if (cached) return cached;              // degraded but useful
        return { posts: [], degraded: true };   // honest empty state
    }
}
```

## Degradable vs Essential

Decide per feature: what is essential (must work or fail loudly) and what is augmentative (nice-to-have, degradable)? Augmentative features get fallbacks; essential features get redundancy and alarms.

## Practice: Map the Degradation Plan

A news home page depends on: breaking-news API, weather widget, comments, live scores.

**Task 1:** Classify each dependency as essential or augmentative.

**Task 2:** Design the fallback for each augmentative one (cached copy, hide widget, show empty).

**Task 3:** Define how the UI communicates degraded state without alarming users.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about the difference between graceful degradation and hiding failures. Start with user communication.

**Prompt 2 — Compare & Contrast:**
> Compare graceful degradation with fail-fast. When is each the right primary behavior, and how do they coexist?

**Prompt 3 — Boundary Testing:**
> A fallback serves stale pricing for 10 minutes during a price-API outage. Is that graceful or dangerous? Design the guard.

## Key Takeaways

- Degradation converts outages into partial, honest states
- Classify features: essential vs augmentative
- Fallbacks need staleness guards to stay safe
- Users must see that the state is degraded

## Further Reading

- [Graceful Degradation — Nielsen Norman Group](https://www.nngroup.com/articles/graceful-degradation/)
- [Degradation Strategies — Azure Architecture](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig)
