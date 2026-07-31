---
title: "Fanout: One Write, Many Readers"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the fanout intent"
  - "Push vs pull fanout"
  - "Compare with publish-subscribe"
  - "Identify fanout in feeds and events"
prerequisites:
  - "patterns/publish-subscribe"
  - "patterns/sharding"
knowledge_refs:
  - "patterns/fanout"
---

# Fanout: One Write, Many Readers

## The Idea

Fanout delivers one write to many destinations: a celebrity post to a million inboxes, a config change to every node, an event to every subscriber. The two shapes are push (write to each destination) and pull (readers fetch and merge).

```text
Fanout shapes:
  Push:  author posts -> write to 1M inboxes (fast reads, heavy writes)
  Pull:  author posts -> one timeline; readers fetch + merge (light writes)
  Hybrid: push to active readers, pull for the long tail

Real systems:
  Kafka: topic partitions broadcast to consumer groups
  Redis: pub/sub broadcasts to live subscribers
  Social feeds: push fanout with pull fallback
```

## The Fanout Challenge

The difficulty is scale and latency: a million-inbox write is a million writes. Fanout design balances write amplification against read latency — push makes reads instant and writes heavy; pull makes writes light and reads slower.

## Practice: Design the Feed Fanout

A social app: 1M users, celebrities post hourly, followers read on demand.

**Task 1:** Design push fanout: the writer fan-out job, batching, and retries.

**Task 2:** Design the pull fallback for inactive users.

**Task 3:** Compare write amplification and read latency for push vs pull vs hybrid.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about the trade-off between push and pull fanout. Start with read latency.

**Prompt 2 — Compare & Contrast:**
> Compare fanout with publish-subscribe and with the observer pattern. When is each the right shape?

**Prompt 3 — Boundary Testing:**
> A celebrity with 10M followers posts at peak. Design the fanout that does not collapse the write path.

## Key Takeaways

- Fanout delivers one write to many readers
- Push = instant reads, heavy writes; pull = the reverse
- Hybrid fanout balances active and inactive readers
- Scale design is the whole game

## Further Reading

- [Fanout on Twitter — InfoQ](https://www.infoq.com/presentations/ebay-fanout/)
- [Designing a News Feed (System Design Primer)](https://github.com/donnemartin/system-design-primer)
