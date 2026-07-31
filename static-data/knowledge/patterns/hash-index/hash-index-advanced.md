---
title: "Advanced Hash Index: DynamoDB-Style and Hash-Range Keys"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Design hash-range composite keys"
  - "Mitigate hot partitions"
  - "Understand adaptive hashing"
  - "Analyze hash index memory"
prerequisites:
  []
knowledge_refs:
  - "patterns/hash-index"
---

# Advanced Hash Index: DynamoDB-Style and Hash-Range Keys

## Hash-Range Keys

DynamoDB-style tables use a hash key for partitioning and a sort key for ordering within the partition. This gives both the O(1) partition routing AND ordered access within a partition: WHERE hash = tenant AND sort BETWEEN. It is the workhorse for multi-tenant systems.

```python
# Hash-range key design: partition by tenant, order by timestamp
#
#   partition key: tenant_id      (hash -> shard)
#   sort key:      created_at     (ordered within the shard)
#
# Query: all orders of tenant 42 in the last hour
#   WHERE tenant_id = 42 AND created_at > now() - 3600
#
# This is O(1) routing + a range scan inside one shard.
# Hot shard risk: a single huge tenant gets one shard's worth of
# throughput — hence key salting: tenant:shard, then query fan-out.
```

## Hot Keys and Adaptive Hashing

A single popular key (a viral post, a celebrity) concentrates traffic on one partition. Mitigations: cache the hot key in front of storage, salt the key across shards and query all, or let the system detect hot partitions and split them — adaptive hashing is the on-disk cousin that splits buckets under load.

## Practice: Design the Multi-Tenant Schema

A SaaS with 10,000 tenants, one with 40% of the events; queries are per-tenant time ranges.

**Task 1:** Design the hash-range schema and the query shapes it serves.

**Task 2:** Design hot-key mitigation for the 40% tenant without slowing the others.

**Task 3:** Measure the fan-out cost of salted hot keys and tune the salt width.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why a hot key defeats a hash index and what salting does about it.

**Prompt 2 — Implementation Design:**
> Design a feed system: hash key = user, sort key = timestamp, with read fan-out from followees. Where do hot users break the design?

**Prompt 3 — Boundary Testing:**
> A shard fills to 90% capacity. Design the split, the routing-table update, and the dual-read window.

## Key Takeaways

- Hash-range keys route by hash, order by sort key
- Hot keys need caching, salting, or adaptive splitting
- Multi-tenant schemas live or die by partition design
- Adaptive hashing grows buckets under load

## Further Reading

- [DynamoDB — Partition Keys and Sort Keys](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.PartitionKey.html)
- [Adaptive Hashing](https://en.wikipedia.org/wiki/Adaptive_hashing)
