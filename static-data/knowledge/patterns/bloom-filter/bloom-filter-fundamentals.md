---
title: "Bloom Filters: Maybe Yes, Definitely No"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the bloom filter structure"
  - "Describe false positives and zero false negatives"
  - "Tune size and hash count"
  - "Use \"definitely not in set\" to skip work"
prerequisites:
  - "principles/caching"
  - "principles/eventual-consistency"
knowledge_refs:
  - "patterns/bloom-filter"
---

# Bloom Filters: Maybe Yes, Definitely No

## The Structure

A bloom filter is a bit array with k hash functions. Adding a key sets k bits. Membership checks the same k bits: if any is zero, the key is definitely absent; if all are set, the key is probably present (false positive possible).

The magic: no false negatives. "Definitely not in the set" is a reliable negative that lets systems skip expensive lookups.

```python
# Bloom filter: the classic probabilistic set
import hashlib, struct

class BloomFilter:
    def __init__(self, size, k):
        self.bits = bytearray(size // 8 + 1)
        self.size, self.k = size, k

    def _hashes(self, key):
        return [int.from_bytes(hashlib.md5(f'{key}:{i}'.encode()).digest()[:4], 'big')
                % self.size for i in range(self.k)]

    def add(self, key):
        for h in self._hashes(key):
            self.bits[h // 8] |= 1 << (h % 8)

    def might_contain(self, key):
        return all(self.bits[h // 8] & (1 << (h % 8)) for h in self._hashes(key))

bf = BloomFilter(10_000, 7)
bf.add('user-42')
print(bf.might_contain('user-42'))   # True
print(bf.might_contain('user-99'))   # False (definitely absent)
```

## Tuning

False-positive rate depends on bit size m, keys n, and hash count k: k = (m/n) * ln 2 minimizes it. A 1% false-positive filter needs ~10 bits per key. Fewer bits = smaller but noisier.

## Practice: Skip the Cache Miss

A cache of 1M keys receives 100M lookups; most keys do not exist in the cache.

**Task 1:** Estimate the false-positive rate for a 10M-bit filter over 1M keys with optimal k.

**Task 2:** Design the flow: bloom filter before the cache to skip unnecessary lookups.

**Task 3:** Quantify the savings when 90% of lookups hit "definitely absent".

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why a bloom filter never produces a false negative. Start with the bit-setting mechanics.

**Prompt 2 — Compare & Contrast:**
> Compare bloom filters with hash sets and with counting bloom filters (deletions). When does each fit?

**Prompt 3 — Boundary Testing:**
> The filter is 99% full and false positives skyrocket. Design the rebuild/rescale strategy without downtime.

## Key Takeaways

- No false negatives; false positives tunable
- Bit array + k hashes, k = (m/n) ln 2 optimal
- "Definitely absent" is the valuable answer
- Counting filters add deletions

## Further Reading

- [Bloom Filter — Wikipedia](https://en.wikipedia.org/wiki/Bloom_filter)
- [Bloom Filters Explained — Brilliant](https://brilliant.org/wiki/bloom-filter/)
