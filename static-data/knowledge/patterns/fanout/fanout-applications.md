---
title: "Fanout in Production: Feeds and Event Buses"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design timeline fanout"
  - "Use Kafka-style partitioned fanout"
  - "Handle fanout failures partially"
  - "Monitor fanout lag"
prerequisites:
  []
knowledge_refs:
  - "patterns/fanout"
---

# Fanout in Production: Feeds and Event Buses

## Partitioned Fanout

Kafka fanout: a topic has partitions; each message goes to one partition, and each consumer group reads all partitions. Fan-out to N consumer groups is inherent — every group reads every message. Within a group, partitions split the work.

```text
Kafka fanout model:
  topic "user.events" (8 partitions)
  consumer group "analytics"  -> reads ALL events (fanout to group)
  consumer group "notify"     -> reads ALL events (independent fanout)
  consumer group "search"     -> reads ALL events
Each group is a fanout destination; partitions parallelize within.

Ordering guarantee: per partition, per key (e.g., per user).
```

## Partial Failure

A fanout to 100 destinations should not fail all when one is slow: per-destination queues, dead-letter paths, and independent retry budgets keep one bad consumer from blocking the broadcast. Fanout lag per destination is the monitoring unit.

## Practice: Design the Broadcast Pipeline

A config change must reach 500 services; three are slow.

**Task 1:** Design the broadcast: per-service queues, timeouts, and retries.

**Task 2:** Design the partial-failure policy: slow services lag, others proceed.

**Task 3:** Design the lag dashboard and the "which services have not applied" query.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why fanout destinations need independent failure budgets. Ask me to trace one slow consumer.

**Prompt 2 — Implementation Design:**
> Design a feature-flag broadcast to 500 nodes with per-node ack and timeout. What guarantees can you honestly make?

**Prompt 3 — Boundary Testing:**
> A destination is down for an hour and misses the broadcast. Design the catch-up (replay or version check).

## Key Takeaways

- Partitioned topics fan out per consumer group
- Per-destination budgets isolate slow consumers
- Fanout lag is the monitoring unit
- Down destinations need catch-up paths

## Further Reading

- [Kafka Documentation](https://kafka.apache.org/documentation/)
- [Google Pub/Sub Fanout](https://cloud.google.com/pubsub/docs/fanout)
