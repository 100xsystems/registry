---
title: "Consistency in Production: Quorums and Transactions"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Apply quorum-based consistency to reads and writes"
  - "Explain serializable transactions and their cost"
  - "Design optimistic concurrency for consistency"
  - "Handle cross-key consistency needs"
prerequisites:
  []
knowledge_refs:
  - "principles/consistency-pattern"
---

# Consistency in Production: Quorums and Transactions

## Quorum Consistency in Practice

With N replicas, W writes and R reads with W + R > N guarantee a read sees the latest write. This is how Dynamo-style systems provide configurable consistency: tune W and R per operation.

```text
Quorum rules (N replicas, W writes, R reads):
  W + R > N  -> read sees latest write (quorum consistency)
  W > N/2    -> writes conflict only if concurrent (common)
  R = 1, W = N -> strong for reads, slow for writes
```

## Serializable Transactions

Serializable isolation makes concurrent transactions behave as if run one after another — the strongest database guarantee. It is expensive: conflict detection (locking or validation) on every transaction.

Use it where money, inventory, and uniqueness rules live. Everywhere else, weaker isolation with optimistic locking is cheaper.

## Practice: Tune the Quorum

A 5-node cart service. Reads must never show a lost item; writes must survive a node loss.

**Task 1:** Choose W and R with W+R>5 and W>2. Compute availability under 1-node and 2-node failure.

**Task 2:** Explain the latency cost of W=3 writes in a 3-region deployment.

**Task 3:** Design the read path so carts read-your-writes without global strong consistency.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why W+R>N is sufficient for a read to see the latest write, and what happens with W+R=N. Ask me to verify with small examples.

**Prompt 2 — Implementation Design:**
> Design a reservation system where two users cannot book the same seat, using optimistic concurrency. Where is the conflict detected?

**Prompt 3 — Boundary Testing:**
> Quorum says the latest write is visible, but the read replica is behind. Is that a contradiction? Explain with W=3, R=3, N=5.

## Key Takeaways

- W+R>N is the quorum consistency condition
- Serializable isolation is the strongest, most expensive guarantee
- Optimistic concurrency trades retries for availability
- Tune consistency per operation, not per system

## Further Reading

- [DynamoDB Read Consistency Options](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html)
- [Isolation Levels — PostgreSQL Docs](https://www.postgresql.org/docs/current/transaction-iso.html)
