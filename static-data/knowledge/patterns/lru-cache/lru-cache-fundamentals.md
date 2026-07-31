---
title: "LRU Cache: Evict What You Use Least Recently"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the LRU eviction policy"
  - "Implement O(1) get and put"
  - "Understand why hash + list"
  - "Know when LRU fits"
prerequisites:
  - "principles/caching"
  - "patterns/flyweight"
knowledge_refs:
  - "patterns/lru-cache"
---

# LRU Cache: Evict What You Use Least Recently

## The Policy

An LRU cache has a capacity. Every get or put marks its key most-recently-used; when the cache is full, the least-recently-used entry is evicted. The assumption: if you have not used it recently, you probably will not use it soon — temporal locality.

```python
# LRU: dict (O(1) lookup) + doubly linked list (O(1) reorder/evict)
class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}          # key -> [value, prev, next]
        self.head = self.tail = None     # most-recent .. least-recent

    def _remove(self, key):
        _, p, n = self.cache[key]
        if p is not None: self.cache[p][2] = n
        else: self.head = n
        if n is not None: self.cache[n][1] = p
        else: self.tail = p

    def _push_front(self, key):
        self.cache[key][1] = None
        self.cache[key][2] = self.head
        if self.head is not None: self.cache[self.head][1] = key
        self.head = key
        if self.tail is None: self.tail = key

    def get(self, key):
        if key not in self.cache: return -1
        self._remove(key); self._push_front(key)
        return self.cache[key][0]

    def put(self, key, value):
        if key in self.cache:
            self.cache[key][0] = value
            self._remove(key); self._push_front(key); return
        if len(self.cache) >= self.cap:
            del self.cache[self.tail]      # evict least-recent
            if self.tail is not None:      # fix tail pointer
                self._remove(self.tail)
        self.cache[key] = [value, None, None]
        self._push_front(key)
```

## Why LRU Wins

LRU adapts to the workload: hot keys stay hot by being touched. FIFO evicts regardless of use; random is unpredictable; LFU tracks frequency but can keep a once-hot key forever. LRU needs one touch per access — O(1) with the right structures — and is the default for most page caches.

## Practice: Build and Test the LRU

A cache of 3 entries receives a workload that repeats some keys and scans others.

**Task 1:** Implement the O(1) LRU with the hash + list structure.

**Task 2:** Trace a workload: put a,b,c then get a then put d — what is evicted?

**Task 3:** Compare hit rates: LRU vs FIFO vs random on the same workload.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why LRU needs both a hash and a list. Start with the O(1) requirements.

**Prompt 2 — Compare & Contrast:**
> Compare LRU with LFU and with TTL-based expiry. When does a once-hot key poison LFU?

**Prompt 3 — Boundary Testing:**
> The workload is a full sequential scan — LRU thrashes. Design the scan-resistant variant (like CLOCK or ARC).

## Key Takeaways

- LRU evicts the least-recently-used entry
- Hash + doubly linked list gives O(1) operations
- LRU assumes temporal locality
- Scan workloads need resistant variants

## Further Reading

- [Cache replacement policies — Wikipedia](https://en.wikipedia.org/wiki/Cache_replacement_policies)
- [Redis — eviction policies](https://redis.io/docs/reference/eviction/)
