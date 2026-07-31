---
title: "Bloom Filters in Production: Caches and Dedupe"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Use bloom filters to thin cache lookups"
  - "Deduplicate seen URLs and events"
  - "Combine with a small exact cache"
  - "Handle filter saturation"
prerequisites:
  []
knowledge_refs:
  - "patterns/bloom-filter"
---

# Bloom Filters in Production: Caches and Dedupe

## Cache Thinning

A bloom filter in front of a cache answers "is this key even worth a cache lookup?" for a fraction of the memory of the cache itself. Databases like Cassandra and RocksDB use them to skip SSTable lookups that cannot hit.

```go
// Bloom filter guards the cache: skip lookups that cannot hit
var filter = bloom.New(1_000_000, 7)

func Get(key string) (Value, bool) {
    if !filter.TestString(key) {
        return Value{}, false     // definitely not in cache: skip
    }
    return cache.Get(key)          // only probable keys hit the cache
}

func Set(key string, v Value) {
    filter.AddString(key)
    cache.Set(key, v)
}
```

## Deduplication

Crawlers and event pipelines dedupe with bloom filters: "have I already seen this URL/event ID?" The no-false-negative property is exactly right — reprocessing an unseen event is safe, missing one is not.

## Practice: Dedupe the Event Stream

An event pipeline receives 50k events/s; ~10% are duplicates from retries.

**Task 1:** Design the filter (size, k) for a day of events and the false-positive policy (drop vs verify).

**Task 2:** Combine with a small exact LRU for recent IDs to cut false positives.

**Task 3:** Design the daily rebuild and the saturation alert.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why dedupe needs "no false negatives" and how the false-positive policy (drop vs verify) is a product choice.

**Prompt 2 — Implementation Design:**
> Design a spell-check membership filter: dictionary in a bloom filter, correction lookup only on probable matches. What is the UX of a false positive?

**Prompt 3 — Boundary Testing:**
> The filter saturates and everything looks present. Design the rebuild trigger and the exact-set fallback.

## Key Takeaways

- Bloom filters skip impossible lookups cheaply
- Dedupe loves the no-false-negative property
- Pair with a small exact cache to cut false positives
- Saturation needs rebuild triggers

## Further Reading

- [RocksDB — Bloom Filters](https://github.com/facebook/rocksdb/wiki/RocksDB-Bloom-Filter)
- [Bloom filter in Apache Cassandra](https://cassandra.apache.org/doc/stable/cassandra/operating/bloom_filters.html)
