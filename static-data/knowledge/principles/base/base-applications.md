---
title: "BASE in Production: Caches, Feeds, and Counters"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design a cache with bounded staleness"
  - "Build a fan-out feed that tolerates stale reads"
  - "Implement an eventually consistent counter"
  - "Choose reconciliation over locking where possible"
prerequisites:
  []
knowledge_refs:
  - "principles/base"
---

# BASE in Production: Caches, Feeds, and Counters

## Caches Are BASE

A read-through cache is the simplest BASE system: it is basically available, holds soft state, and converges when the TTL expires or invalidation fires. The art is bounding staleness so users never notice.

Use a monotonically increasing version per key; when the client sees an older version, it refreshes from the source. This converts a silent staleness bug into a visible, correctable one.

```python
# Versioned cache entry: staleness becomes observable
import time

cache = {}  # key -> (version, value)

def put(key, value, version):
    cache[key] = (version, value, time.time())

def get(key, max_age_s=30):
    version, value, ts = cache.get(key, (0, None, 0))
    stale = (time.time() - ts) > max_age_s
    return value, version, stale
```

## Fan-Out Feeds

When a celebrity posts, a push fan-out writes to millions of inboxes asynchronously. Inbox reads are BASE: a follower may see the post seconds late, but the system stays available under load.

Pull-based fallback (timeline assembled on read) keeps the system alive when the push pipeline lags.

## Practice: Stale Counters and Reconciliation

Your like counter shows slightly wrong totals because counters are updated on replicas without a central lock.

**Task 1:** Design a counter that increments locally and periodically sends deltas to a central reconciler.

**Task 2:** What happens to the displayed count when two replicas both increment? Prove the delta-merge is commutative.

**Task 3:** Add a nightly job that recomputes true counts from the source of truth and corrects drift.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why a TTL cache with a 60-second expiry is acceptable for a profile page but not for a payment status page. Ask me questions as you go.

**Prompt 2 — Implementation Design:**
> Design a news feed that is BASE for reads but guarantees the author always sees their own post immediately (read-your-writes). Where does the read route?

**Prompt 3 — Boundary Testing:**
> A caching layer serves a deleted item for 5 minutes after deletion. List every user-visible consequence and design a tombstone mechanism.

## Key Takeaways

- Caches, feeds, and counters are the canonical BASE systems
- Versioning makes staleness observable and fixable
- Delta-merging counters requires commutative operations
- Tombstones prevent resurrecting deleted data in caches

## Further Reading

- [Eventually Consistent — Revisited](https://www.allthingsdistributed.com/2008/12/eventually_consistent.html)
- [Designing Data-Intensive Applications](https://dataintensive.net/)
