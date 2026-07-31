---
title: "Publish-Subscribe: Review & Mastery Quiz"
order: 4
difficulty: "Intermediate"
duration: "30 min"
learning_objectives:
  - "Consolidate pub-sub concepts"
  - "Choose brokers and semantics"
  - "Design idempotent pipelines"
prerequisites:
  []
knowledge_refs:
  - "patterns/publish-subscribe"
---

# Publish-Subscribe: Review & Mastery Quiz

## Quiz

Answer these, then check against the key takeaways.

- Q1: Pub-sub decouples via? (A: a broker and topics / B: direct references / C: shared memory)
- Q2: Kafka orders messages? (A: within a partition / B: globally / C: never)
- Q3: A consumer group splits? (A: partitions / B: messages one by one / C: the broker)
- Q4: True or false: at-least-once delivery can duplicate messages.
- Q5: Exactly-once effects come from? (A: idempotency / B: luck / C: caching)

## Guided LLM Prompts

**Prompt 1 — Scenarios:**
> An order system must notify 6 services and never double-charge on replay. Design the topics, semantics, and idempotency.

**Prompt 2 — Open-Ended:**
> Explain to a junior engineer why "once" in distributed messaging is a choice, not a default.

## Key Takeaways

- Q1: A; Q2: A; Q3: A; Q4: true; Q5: A
- Brokers decouple; semantics are yours to choose
- Idempotency makes at-least-once feel exactly-once
