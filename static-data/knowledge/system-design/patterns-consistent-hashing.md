---
slug: patterns-consistent-hashing
title: "Consistent Hashing & Sharding"
description: "Distributing data across nodes without rehashing everything when nodes are added or removed."
order: 10
tags:
  - system-design
  - patterns
  - consistent-hashing
  - sharding
  - distributed-systems
prerequisites:
  - building-blocks-databases
  - fundamentals-scalability
references:
  - title: "Consistent Hashing"
    author: "ByteByteGo"
    url: "https://blog.bytebytego.com/p/consistent-hashing"
    type: "article"
    description: "Visual explanation of consistent hashing with real examples."
  - title: "Introduction to Consistent Hashing"
    author: "Nivedita Gopalakrishna (Amazon)"
    url: "https://www.amazon.science/publications/consistent-hashing"
    type: "article"
    description: "Consistent hashing in distributed systems."
  - title: "System Design: Consistent Hashing"
    author: "Hello Interview"
    url: "https://www.hellointerview.com/learn/system-design/in-a-hurry/consistent-hashing"
    type: "article"
    description: "Practical explanation with examples."
  - title: "How DynamoDB Uses Consistent Hashing"
    author: "AWS"
    url: "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.partitions.html"
    type: "docs"
    description: "Real-world consistent hashing implementation."
  - title: "Consistent Hashing Paper"
    author: "David Karger et al. (MIT)"
    url: "https://dl.acm.org/doi/10.1145/258533.258537"
    type: "paper"
    description: "Original paper on consistent hashing."
related_knowledge:
  - slug: building-blocks-databases
    title: "Databases"
    lesson_number: 8
  - slug: patterns-cqrs
    title: "CQRS & Event Sourcing"
    lesson_number: 11
  - slug: building-blocks-caching
    title: "Caching"
    lesson_number: 6
knowledge_refs:
  - slug: "databases-redis"
    title: "Redis"
  - slug: "databases-cassandra"
    title: "Cassandra"
  - slug: "patterns-load-balancing"
    title: "Load Balancing"
---

# Consistent Hashing & Sharding

When distributing data across multiple nodes, consistent hashing ensures that adding or removing nodes only affects a small fraction of data — not everything.

## The Problem with Simple Hashing

Naive approach:
```
node = hash(key) % num_nodes
```

**Problem:** When `num_nodes` changes (e.g., from 3 to 4), almost every key maps to a different node. This causes massive data movement.

## The Consistent Hashing Solution

### The Hash Ring
Nodes and keys are both mapped to positions on a ring:
```
        Node A
       /      \
Node D          Node B
       \      /
        Node C

Key "user:123" → position on ring → walk clockwise to first node
```

### Adding/Removing Nodes
Only the keys between the new node and its predecessor need to move:
```
Before: Node A serves keys 0-90°, Node B serves 90-180°...
After adding Node E at 45°: Only keys from 45-90° move from A to E
```

**~1/n of data moves** when a node is added (where n = total nodes).

### Virtual Nodes
To handle uneven distribution, each physical node gets multiple positions on the ring:
```
Node A → positions at 0°, 120°, 240°
Node B → positions at 30°, 150°, 270°
Node C → positions at 60°, 180°, 300°
```

More virtual nodes = more even distribution.

## Use Cases

### Distributed Caches
- Redis Cluster uses consistent hashing for slot distribution
- Memcached clients use it for key routing

### Database Sharding
- Cassandra uses consistent hashing for partition placement
- DynamoDB uses it internally for data distribution

### Load Balancing
- Route users to servers based on consistent hash of user ID
- Same user always hits the same server (session affinity)

## Implementation Example

```python
import hashlib
import bisect

class ConsistentHash:
    def __init__(self, nodes, virtual_nodes=150):
        self.ring = {}
        self.sorted_keys = []
        for node in nodes:
            for i in range(virtual_nodes):
                key = self._hash(f"{node}:{i}")
                self.ring[key] = node
                bisect.insort(self.sorted_keys, key)
    
    def _hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16)
    
    def get_node(self, key):
        if not self.ring:
            return None
        h = self._hash(key)
        idx = bisect.bisect_right(self.sorted_keys, h) % len(self.sorted_keys)
        return self.ring[self.sorted_keys[idx]]
```

## Key Considerations

- **Virtual nodes:** Use 100-200 per physical node for good distribution
- **Hash function:** MD5 or MurmurHash are common choices
- **Node health:** Skip unhealthy nodes during lookup
- **Replication:** Store each key on N successive nodes on the ring

---

*References:*
1. ByteByteGo, "Consistent Hashing." [Link](https://blog.bytebytego.com/p/consistent-hashing)
2. Amazon Science, "Introduction to Consistent Hashing." [Link](https://www.amazon.science/publications/consistent-hashing)
3. Hello Interview, "Consistent Hashing." [Link](https://www.hellointerview.com/learn/system-design/in-a-hurry/consistent-hashing)
4. AWS, "How DynamoDB Uses Consistent Hashing." [Link](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.partitions.html)
5. David Karger et al., "Consistent Hashing," MIT. [Link](https://dl.acm.org/doi/10.1145/258533.258537)
