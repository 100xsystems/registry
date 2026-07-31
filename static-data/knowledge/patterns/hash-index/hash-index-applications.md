---
title: "Hash Indexes in Production: Partitioned Tables and Hashing Schemes"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design hash partitioning"
  - "Explain open addressing vs chaining"
  - "Rehash without downtime"
  - "Use hash joins"
prerequisites:
  []
knowledge_refs:
  - "patterns/hash-index"
---

# Hash Indexes in Production: Partitioned Tables and Hashing Schemes

## Hash Partitioning

Distributed databases partition by hash of the key so each partition holds a uniform slice: hash(key) % N routes writes and reads to one partition. The catch: adding a node rehashes nearly every key — which is why consistent hashing maps keys to a ring and only a fraction move per node.

```python
# Consistent hashing: only a fraction of keys move on resize
import hashlib, bisect

class ConsistentHash:
    def __init__(self, vnodes=128):
        self.vnodes = vnodes
        self.ring = []       # sorted positions
        self.nodes = {}      # position -> node

    def _pos(self, key):
        return int.from_bytes(hashlib.md5(key.encode()).digest()[:8], 'big')

    def add_node(self, node):
        for i in range(self.vnodes):
            p = self._pos(f'{node}:{i}')
            bisect.insort(self.ring, p)
            self.nodes[p] = node

    def get(self, key):
        p = self._pos(key)
        i = bisect.bisect_left(self.ring, p) % len(self.ring)
        return self.nodes[self.ring[i]]

# Removing one node only remaps keys that hashed into its vnodes.
```

## On-Disk Hashing

Disk hash indexes use extendible or linear hashing to grow gracefully: buckets split instead of full rehash. Open addressing (probing) avoids chain pointers and is cache-friendlier in memory; chaining is simpler and resilient. Hash joins exploit exact-equality keys to pair buckets without sorting.

## Practice: Design the Shard Map

A 1B-row event table is sharded by event_id across 8 nodes and must grow to 12.

**Task 1:** Design the hash function and vnode count for balanced shards.

**Task 2:** Simulate the resize: how many keys move from 8 to 12 nodes with consistent hashing?

**Task 3:** Design the routing table lookup and the dual-write during migration.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why naive mod-N hashing makes resharding painful and consistent hashing does not.

**Prompt 2 — Implementation Design:**
> Design a hash-partitioned message queue: partition key, routing, and consumer assignment. What happens when a consumer dies?

**Prompt 3 — Boundary Testing:**
> One shard gets 40% of traffic because keys are skewed. Design the key-salting strategy that balances load.

## Key Takeaways

- Hash partitioning gives uniform data distribution
- Consistent hashing makes resize touch only a fraction
- Extendible/linear hashing grow on disk without full rehash
- Hash joins pair buckets without sorting

## Further Reading

- [Consistent Hashing — Wikipedia](https://en.wikipedia.org/wiki/Consistent_hashing)
- [Cassandra — Partitioning](https://cassandra.apache.org/doc/stable/cassandra/architecture/partitioning.html)
