---
title: "Event Sourcing in Production: Streams and Snapshots"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Store events in streams"
  - "Use snapshots to bound replay cost"
  - "Version events for schema evolution"
  - "Concurrently append without conflicts"
prerequisites:
  []
knowledge_refs:
  - "patterns/event-sourcing"
---

# Event Sourcing in Production: Streams and Snapshots

## Streams and Snapshots

Events live in per-aggregate streams (Kafka, EventStore, or a table). Replaying a 10-year stream is slow, so snapshots store periodic state: rebuild loads the last snapshot, then replays only the events after it.

```sql
-- Events table with a version per aggregate
CREATE TABLE events (
    aggregate_id uuid,
    sequence    bigint,
    type        text,
    payload     jsonb,
    created_at  timestamptz,
    PRIMARY KEY (aggregate_id, sequence)
);
-- Snapshot table: state at a sequence, to bound replay
CREATE TABLE snapshots (
    aggregate_id uuid PRIMARY KEY,
    at_sequence bigint,
    state jsonb
);
-- Rebuild: load snapshot at seq N, replay events > N.
```

## Versioning and Appends

Events evolve: an old OrderCreated lacks a field new code expects. Version events (v1, v2) and let the fold handle each version. Concurrent appends are safe because appends are additive — no overwrite conflicts, only ordering.

## Practice: Design the Stream Store

A 10M-event order stream; reads must be fast and audits complete.

**Task 1:** Design the events + snapshots schema and the rebuild algorithm.

**Task 2:** Version the OrderCreated event and migrate the fold.

**Task 3:** Design the snapshot cadence: every N events, or on demand, and why.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why snapshots are the scalability lever for event sourcing. Ask me to compute the replay savings.

**Prompt 2 — Implementation Design:**
> Design a versioned event stream with upcaster functions for a payroll system. What happens to old payouts?

**Prompt 3 — Boundary Testing:**
> Two snapshots disagree with the event log. Design the verification (replay diff) that detects drift.

## Key Takeaways

- Streams hold per-aggregate event sequences
- Snapshots bound replay cost
- Versioning keeps old events replayable
- Append-only means concurrency is safe

## Further Reading

- [EventStoreDB](https://www.eventstore.com/)
- [Kafka as an Event Store](https://kafka.apache.org/documentation/)
