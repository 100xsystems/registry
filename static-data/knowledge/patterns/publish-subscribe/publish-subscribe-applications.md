---
title: "Pub-Sub in Production: Kafka, RabbitMQ, and Delivery Guarantees"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Describe Kafka topics and partitions"
  - "Choose delivery semantics"
  - "Manage consumer groups"
  - "Handle ordering"
prerequisites:
  []
knowledge_refs:
  - "patterns/publish-subscribe"
---

# Pub-Sub in Production: Kafka, RabbitMQ, and Delivery Guarantees

## Kafka: Durable Logs as Topics

Kafka stores a topic as a partitioned, replicated log. Each partition orders messages; consumers in a group divide partitions. Durability is the differentiator: messages persist and replay, so late subscribers read history. Ordering is per-partition, not global — a constraint every design must respect.

```yaml
# Kafka design decisions that shape guarantees:
#   partitions:        more = more parallelism, less global order
#   replication:       >1 keeps data through broker loss
#   acks: all         wait for all replicas before acknowledging
#   consumer group:   members split partitions (not messages)
#   offsets:          committed position per consumer; replay = reset
# Delivery semantics:
#   at-most-once   consumer commits before processing
#   at-least-once  consumer processes then commits (retries dupes)
#   exactly-once   transactional produce + commit (Kafka 0.11+)
# Choose per-topic: notifications tolerate dupes; payments do not.
```

## RabbitMQ and Fan-Out

RabbitMQ uses exchanges and queues: exchanges route to queues (direct, topic, fan-out), consumers pull from queues. The model fits request-reply and work distribution; Kafka fits log replay and stream processing. The choice: queue semantics (each message once per queue) vs log semantics (replayable history).

## Practice: Choose the Broker

A platform needs: (1) every service notified of user events, (2) a work queue for image resizing, (3) replayable audit history.

**Task 1:** Map each need to a shape: topic fan-out, queue, or log.

**Task 2:** Choose brokers and the delivery semantics per need.

**Task 3:** Design ordering: what is per-partition and what breaks if you need global order?

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why Kafka orders within a partition and what global order would cost.

**Prompt 2 — Implementation Design:**
> Design an event pipeline: user actions into Kafka, three consumers (email, analytics, search) in separate groups. What is the topic layout?

**Prompt 3 — Boundary Testing:**
> A consumer crashes after processing but before committing. Design the at-least-once retry and the idempotent consumer.

## Key Takeaways

- Kafka topics are partitioned, durable logs
- Ordering is per-partition, not global
- Delivery semantics are a per-topic choice
- Queues distribute work; logs enable replay

## Further Reading

- [Kafka — documentation](https://kafka.apache.org/documentation/)
- [RabbitMQ — tutorial](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)
