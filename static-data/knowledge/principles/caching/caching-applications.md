---
title: "Caching in Production: Thundering Herds and Stampedes"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Prevent cache stampedes with single-flight requests"
  - "Implement stale-while-revalidate"
  - "Use cache-aside correctly with locking"
  - "Design multi-tier cache invalidation"
prerequisites:
  []
knowledge_refs:
  - "principles/caching"
---

# Caching in Production: Thundering Herds and Stampedes

## The Stampede Problem

When a hot key expires, thousands of concurrent requests all miss and hit the database at once — the "thundering herd." Single-flight (only one request recomputes; the rest wait for its result) turns a stampede into a single refresh.

```go
// Single-flight: only one goroutine recomputes per key
var group singleflight.Group

func GetUser(id string) (*User, error) {
    if u, ok := cache.Get(id); ok {
        return u, nil
    }
    v, err, _ := group.Do(id, func() (any, error) {
        u, err := db.GetUser(id)   // only ONE caller hits DB
        cache.Set(id, u, ttl)
        return u, err
    })
    return v.(*User), err
}
```

## Stale-While-Revalidate

Serve the stale copy immediately while a background job refreshes it. Users never see a miss-latency spike, and the database sees one refresh instead of a stampede. CDNs and HTTP caches implement this with the stale-while-revalidate directive.

## Practice: Kill a Stampede

A leaderboard key expires every 5 minutes and its recompute takes 800ms. Under 5k QPS, the recompute phase pegs the database.

**Task 1:** Apply single-flight and measure the DB query count before/after.

**Task 2:** Add stale-while-revalidate with a background recompute every 60s.

**Task 3:** Add jitter to TTLs so keys do not expire in lockstep.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why random TTL jitter alone does not fully solve a stampede and what single-flight adds.

**Prompt 2 — Implementation Design:**
> Design a cache for a payment balance that must be strongly consistent with the ledger but fast. Where do you cache, and how do you invalidate?

**Prompt 3 — Boundary Testing:**
> A background revalidator crashes. Design a fail-safe so stale data still gets served but the system eventually refreshes.

## Key Takeaways

- Stampedes multiply one expired key into a DB outage
- Single-flight collapses concurrent misses into one recompute
- Stale-while-revalidate hides refresh latency entirely
- TTL jitter prevents lockstep expiry

## Further Reading

- [Stale-While-Revalidate — MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control)
- [singleflight — Go Docs](https://pkg.go.dev/golang.org/x/sync/singleflight)
