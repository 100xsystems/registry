---
title: "Replication in Production: Streams and Quorums"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Replicate via logs"
  - "Tune quorums"
  - "Monitor replication lag"
  - "Handle replica failures"
prerequisites:
  []
knowledge_refs:
  - "patterns/replication"
---

# Replication in Production: Streams and Quorums

## Log-Based Replication

Modern systems replicate through logs: the leader's write-ahead log or a dedicated change stream (binlog, CDC) ships to replicas, which replay it. Log-based replication is decoupled from application code — triggers and dual-writes are unnecessary — and enables stream consumers (analytics, search) too.

```yaml
Replication architecture (Postgres example):
  primary -> WAL streaming -> standby 1, standby 2
  - synchronous standby: the primary waits for one standby to
    ack before answering (zero-loss failover window)
  - asynchronous: faster writes, possible small loss on failover
  Replication slots: ensure the primary retains WAL the standby
    has not consumed yet (prevents silent divergence)
  Lag monitoring: replay_lag per standby; alert when it grows
  CDC: logical replication publishes changes as events for
    downstream systems (search index, analytics, warehouses)
```

## Quorums

Leaderless systems tune consistency with quorums: write to W nodes, read from R nodes, and require W + R > N to guarantee a reader sees the latest write. W=3, R=1 favors reads; W=1, R=3 favors writes. Failures below the quorum reject the operation — availability is tunable, not absolute.

## Practice: Operate the Replicas

A primary + 2 standbys serve 95% reads from replicas; a replica lags during nightly loads.

**Task 1:** Design the lag alert and the read-routing guard.

**Task 2:** Choose sync vs async for the loss budget.

**Task 3:** Design the failover drill and the promotion checklist.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why W + R > N guarantees a fresh read in leaderless systems.

**Prompt 2 — Implementation Design:**
> Design a CDC pipeline: database changes to a search index with lag bounds. What breaks if the index lags?

**Prompt 3 — Boundary Testing:**
> A replica diverges silently (a missed WAL segment). Design the checksum/consistency check that detects and repairs it.

## Key Takeaways

- Logs replicate without application coupling
- W + R > N is the quorum freshness rule
- Lag is monitored and routed around
- Sync vs async sets the failover loss budget

## Further Reading

- [Dynamo — quorum replication](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf)
- [PostgreSQL — replication](https://www.postgresql.org/docs/current/runtime-config-replication.html)
