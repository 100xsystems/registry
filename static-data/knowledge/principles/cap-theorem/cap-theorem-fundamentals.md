---
title: "The CAP Theorem: Pick Two"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "State the CAP theorem precisely"
  - "Define consistency, availability, and partition tolerance"
  - "Explain what \"during a partition\" means"
  - "Map real systems (CP/AP) onto the CAP space"
prerequisites:
  - "principles/base"
  - "principles/quorum"
knowledge_refs:
  - "principles/cap-theorem"
---

# The CAP Theorem: Pick Two

## The Three Properties

Consistency means every read returns the latest write (linearizability). Availability means every request receives a response (not necessarily the latest data). Partition tolerance means the system keeps operating when network messages are lost or delayed.

During a partition, a system cannot be both fully consistent and fully available: either the minority side refuses to serve (CP, choosing consistency) or serves with possibly stale data (AP, choosing availability).

```text
CAP during a partition (network split between A and B):
  CP choice: A serves, B returns errors/slow-down   -> consistent, not available
  AP choice: A and B both serve possibly stale data -> available, not consistent

After the partition heals, AP systems must reconcile divergent writes.
```

## CAP Is About Partitions

When there is no partition, a system can be both consistent and available. The theorem only forces the trade-off during a partition — so engineers design for the partition case and optimize the no-partition case.

PACELC extends this: even without partitions, you choose between latency and consistency (e.g., synchronous vs asynchronous replication).

## Practice: Classify Real Systems

Classify each as CP or AP and justify: a primary-replica SQL database, Cassandra with quorum, a DNS system, a shopping cart.

**Task 1:** For the SQL primary-replica system, describe exactly what happens to the replica's reads during a split.

**Task 2:** For Cassandra with quorum reads/writes, what does it do during a partition?

**Task 3:** Design a cart that is AP during a partition and reconciles merges after healing. What conflicts arise?

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why "pick two" is a simplification and what PACELC adds. Start with the definition of a partition.

**Prompt 2 — Compare & Contrast:**
> Compare how MongoDB (primary), Cassandra (tunable), and DynamoDB (configurable) sit on the CAP spectrum and what knobs you turn to move them.

**Prompt 3 — Boundary Testing:**
> A single-node database has no partitions, so is it both C and A? What happens with two replicas and a 200ms network delay between them?

## Key Takeaways

- CAP forces a choice only during a partition
- CP favors consistency, AP favors availability
- PACELC adds the latency/consistency trade-off without partitions
- Classify each data path, not the whole system

## Further Reading

- [CAP Theorem — MIT Gilbert & Lynch](https://groups.csail.mit.edu/tds/papers/Gilbert/Brewer2.pdf)
- [CAP Twelve Years Later](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/)
