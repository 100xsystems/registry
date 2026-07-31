---
title: "Quorum in Production: Multi-AZ and Geo"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design quorums across AZs"
  - "Balance quorum size with failure tolerance"
  - "Handle quorum loss (degraded mode)"
  - "Measure quorum write latency"
prerequisites:
  []
knowledge_refs:
  - "principles/quorum"
---

# Quorum in Production: Multi-AZ and Geo

## AZ-Aware Quorums

A 3-replica quorum (W=2, R=2) across 3 AZs tolerates any single-AZ loss: the two remaining AZs still form a quorum. This is the standard strong-consistency deployment for managed databases.

```text
3 AZs x 1 replica each, N=3:
  W=2, R=2 : one AZ dies -> 2 nodes remain -> quorum works
  W=3, R=1 : one AZ dies -> writes fail (no quorum) -> reads may work
  W=1, R=1 : any split -> stale reads possible (AP)

Write latency = max of the slowest node in the write quorum.
Across regions, W=2 in one region then async to the other.
```

## Quorum Loss

When fewer than a quorum of nodes are reachable, the system cannot safely accept writes. The correct behavior is to refuse writes (fail closed) rather than accept them without quorum and risk divergence. Reads may continue from surviving nodes if the read quorum is met.

## Practice: Design the Multi-AZ Quorum

A payments store must survive one AZ loss and keep reads consistent.

**Task 1:** Pick the replica count and W/R for the requirements.

**Task 2:** Define the fail-closed behavior when the write quorum is lost.

**Task 3:** Estimate the write latency impact of W=2 across AZs and whether the payments SLA accepts it.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why a quorum spanning AZs is the standard strong-consistency design. Ask me to compute AZ-loss scenarios.

**Prompt 2 — Implementation Design:**
> Design a multi-region order store with quorum in the primary region and async replication to a standby. What does the standby guarantee?

**Prompt 3 — Boundary Testing:**
> Two of three AZs have a slow link (partition but not full loss). Quorum still meets — but latency spikes. Design the degradation signal.

## Key Takeaways

- 3 AZs with W=2,R=2 survive any single-AZ loss
- Quorum loss = fail closed, never diverge
- Write latency tracks the slowest quorum node
- Geo quorums use local quorum + async replication

## Further Reading

- [Cassandra Tunable Consistency](https://docs.datastax.com/en/cassandra-oss/3.x/cassandra/dml/dmlConfigConsistency.html)
- [Google Spanner TrueTime & Paxos](https://research.google/pubs/pub45855/)
