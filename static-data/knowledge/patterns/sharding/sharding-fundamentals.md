---
title: "Sharding: Split Data to Scale"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the sharding model"
  - "Choose a shard key"
  - "Understand query routing"
  - "Know the hot-shard risk"
prerequisites:
  - "patterns/hash-index"
  - "patterns/replication"
knowledge_refs:
  - "patterns/sharding"
---

# Sharding: Split Data to Scale

## The Model

Sharding splits a dataset by a shard key: hash the key, route the row to its shard. No node holds everything, so capacity grows with nodes. The shard key decides everything — a good key distributes evenly and keeps related data together; a bad key concentrates traffic on one shard.

```text
Sharding by hash of the shard key:
  shard = hash(user_id) % N

  Good shard keys:
    - high cardinality (user_id, order_id, tenant_id)
    - even distribution (uniform values)
    - query affinity (all of a user's rows in one shard)
  Bad shard keys:
    - low cardinality (status, country)
    - skewed values (one giant tenant)
  Query routing:
    - point query on shard key: one shard, fast
    - query without the key: scan every shard (scatter-gather)
  Hot shard: one key with huge traffic overwhelms its shard —
    the ceiling of the whole system.
```

## Key Choice

Composite keys fix many routing problems: tenant_id as the shard key routes all of a tenant's data to one shard (query affinity), while a secondary key orders within the shard. The cardinality and the query shapes — not fashion — pick the key.

## Practice: Choose the Shard Key

A messaging app: conversations, messages, users — queries are per-user and per-conversation.

**Task 1:** List the query shapes and their hot paths.

**Task 2:** Choose the shard key with query affinity and justify.

**Task 3:** Identify the scatter-gather queries and their cost.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why the shard key choice is the whole design. Start with a bad key.

**Prompt 2 — Compare & Contrast:**
> Compare sharding with replication: one scales capacity, the other availability. When do you need both?

**Prompt 3 — Boundary Testing:**
> A tenant grows to 40% of the data. Design the re-shard or the tenant split that rebalances.

## Key Takeaways

- Sharding scales capacity by splitting data
- The shard key decides distribution and routing
- Query affinity keeps related data co-located
- Hot shards are the scaling ceiling

## Further Reading

- [Sharding — Martin Fowler](https://martinfowler.com/articles/database-sharding-ballerina.html)
- [PostgreSQL — partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html)
