---
title: "Sharding in Production: Vitess, Citus, and DynamoDB"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Describe Vitess-style sharding"
  - "Use range vs hash sharding"
  - "Design rebalancing"
  - "Route queries correctly"
prerequisites:
  []
knowledge_refs:
  - "patterns/sharding"
---

# Sharding in Production: Vitess, Citus, and DynamoDB

## Range vs Hash

Range sharding (Citus, time-series) splits by key ranges: time ranges enable easy retention and predictable hotspots by time. Hash sharding distributes evenly but scatters ranges. The choice follows the workload: time-ordered ingestion loves range; uniform access loves hash.

```text
Range vs hash sharding:
  Range (Citus, timeseries):
    shard = the range containing the key
    + range scans local, retention = drop whole shards
    - hot ranges (recent time) concentrate load
  Hash (Vitess, DynamoDB):
    shard = hash(key) % N
    + even distribution, no inherent hotspot
    - range queries scatter
  Rebalancing:
    - hash: consistent hashing moves a fraction on resize
    - range: split a hot range in two, migrate half
  Routing:
    - a mapping service maps key -> shard (Vitess VSchema)
    - or the client hashes locally (DynamoDB)
```

## Operations

Production sharding needs a routing layer (Vitess VSchema, a shard map service), rebalancing tooling, and scatter-gather for cross-shard queries. Schema changes and migrations run per shard. The hardest operational truth: resharding is a migration, not a knob — it must be planned, rehearsed, and reversible.

## Practice: Design the Sharded Store

A 10B-row events table, time-ordered, queried by tenant over time ranges, must grow without downtime.

**Task 1:** Choose range vs hash for the access pattern.

**Task 2:** Design the routing layer and the rebalance drill.

**Task 3:** Design the retention (drop old shards) and the hot-range mitigation.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why time-series loves range sharding and what its hotspot is.

**Prompt 2 — Implementation Design:**
> Design a Vitess-style setup: VSchema, shard map, and the reshard command sequence for a growing table.

**Prompt 3 — Boundary Testing:**
> A shard fills to 90%. Design the split, the dual-write window, and the rollback.

## Key Takeaways

- Range fits time-series; hash fits uniform access
- Routing layers and shard maps decouple clients
- Resharding is a rehearsed migration
- Retention drops whole shards cheaply

## Further Reading

- [Vitess — sharding](https://vitess.io/docs/concepts/sharding/)
- [Citus — distributed tables](https://docs.citusdata.com/en/stable/)
