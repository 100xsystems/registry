---
title: "Advanced Pub-Sub: Exactly-Once and Stream Processing"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Achieve exactly-once pipelines"
  - "Make consumers idempotent"
  - "Join streams correctly"
  - "Handle reprocessing"
prerequisites:
  []
knowledge_refs:
  - "patterns/publish-subscribe"
---

# Advanced Pub-Sub: Exactly-Once and Stream Processing

## Exactly-Once

Exactly-once in messaging means the consumer's side effects and the offset commit are atomic. Kafka's transactions write both to the log in one transaction; otherwise the consumer must be idempotent — the same message applied twice changes nothing. Idempotency keys and upserts make at-least-once behave like exactly-once.

```go
// Idempotent consumer: the effect, not the delivery, is exactly-once
func handle(msg Event) error {
    if processed, err := store.Exists(msg.ID); err != nil {
        return err
    } else if processed {
        return nil                      // already applied: skip
    }
    if err := applyEffect(msg); err != nil {   // the real work
        return err                      // don't commit; retry later
    }
    return store.MarkProcessed(msg.ID)  // record, then commit offset
}
// A crash between applyEffect and MarkProcessed re-delivers;
// the idempotency check makes the second apply a no-op.
// Exactly-once = at-least-once delivery + idempotent effect.
```

## Stream Processing

Stream processors (Kafka Streams, Flink) consume topics, transform, and produce topics — pub-sub as computation. Stateful joins and aggregations use local state backed by changelog topics. Reprocessing a topic (replay from an earlier offset) is the superpower and the hazard: downstream systems must tolerate the replay.

## Practice: Design the Idempotent Pipeline

A payment event topic is replayed during a recovery; the ledger must not double-post.

**Task 1:** Design the idempotency key and the dedupe store.

**Task 2:** Design the streaming join: orders topic + users topic -> enriched events.

**Task 3:** Design the replay policy: what re-runs, what is skipped, and the markers that make it safe.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why idempotent effects beat transactional magic in practice.

**Prompt 2 — Implementation Design:**
> Design a streaming aggregation with changelog state: how does a consumer recover its state after a crash?

**Prompt 3 — Boundary Testing:**
> A replay delivers an old event that should have been superseded. Design the version guard that drops stale application.

## Key Takeaways

- Exactly-once = idempotent effects + atomic commits
- Kafka transactions atomicize produce and consume
- Stream joins need recoverable local state
- Replay is powerful and demands idempotency

## Further Reading

- [Kafka — exactly-once semantics](https://kafka.apache.org/documentation/#semantics)
- [Flink — stateful stream processing](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/stateful-stream-processing/)
