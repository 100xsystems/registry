---
title: "CAP in Practice: CP and AP Systems"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Explain quorum-based reads and writes"
  - "Describe how Raft implements CP"
  - "Describe how Dynamo-style systems implement AP"
  - "Choose CP or AP for a given workload"
prerequisites:
  []
knowledge_refs:
  - "principles/cap-theorem"
---

# CAP in Practice: CP and AP Systems

## Quorums: The Middle Ground

With N replicas, require W writes and R reads such that W + R > N. Then any read sees at least one node with the latest write — quorum consistency, without waiting for all replicas. Choosing W and R tunes where you sit on the CP/AP spectrum.

```text
Quorum math (N=3):
  W=2, R=2  -> W+R=4 > 3  : strong-ish, tolerates 1 node loss
  W=1, R=1  -> W+R=2 < 3  : AP-ish, may read stale
  W=3, R=1  -> W+R=4 > 3  : CP-ish, write needs all 3

Tune per workload: strong for payments, loose for feeds.
```

## Raft vs Dynamo

Raft-based systems (etcd, ZooKeeper, CockroachDB) are CP: a leader replicates writes to a majority, and the minority side of a partition refuses to elect a leader — it stops serving rather than diverge.

Dynamo-style systems (Cassandra, Riak, original DynamoDB) are AP: every replica accepts writes and serves reads; conflicts are resolved later with vector clocks, timestamps, or application logic.

## Practice: Design the Quorum

A multi-region order service with 5 replicas. Reads must never see a lost order; writes must succeed during a single-region outage.

**Task 1:** Choose W and R and prove W+R>5. Compute worst-case availability during a region outage.

**Task 2:** What happens to reads if the region with the latest write is down? Is that acceptable for orders?

**Task 3:** Redesign so writes still succeed during the outage (loosen W) and explain the new consistency risk.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why W+R>N gives quorum consistency and walk me through a W=2,R=2,N=3 read. Ask me to compute variants.

**Prompt 2 — Compare & Contrast:**
> Compare how etcd (Raft) and Cassandra handle a 3-node split 2v1. Which serves reads on the minority side and why?

**Prompt 3 — Boundary Testing:**
> Quorum is satisfied but a read lands on a node that missed the last write. Is that possible with W+R>N? Construct a counterexample or prove it impossible.

## Key Takeaways

- W+R>N yields quorum consistency
- Raft systems are CP; Dynamo systems are AP
- Quorums tune the CP/AP trade-off per workload
- Multi-region quorums trade write latency for availability

## Further Reading

- [Raft: Understandable Distributed Consensus](https://raft.github.io/raft.pdf)
- [DynamoDB Consistency Models](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html)
