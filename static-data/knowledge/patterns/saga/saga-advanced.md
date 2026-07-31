---
title: "Advanced Saga: Exactly-Once Compensation and Sagas Across Partitions"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Make compensations exactly-once"
  - "Handle saga isolation anomalies"
  - "Run sagas across partitions"
  - "Design saga timeouts"
prerequisites:
  []
knowledge_refs:
  - "patterns/saga"
---

# Advanced Saga: Exactly-Once Compensation and Sagas Across Partitions

## Compensation Reliability

A compensation is itself a transaction that can fail and must be idempotent: retrying release() must not double-release. Store compensation status (pending/done) with the saga state; only mark done after the compensating transaction commits. The compensation log doubles as the audit trail.

```text
Saga isolation problems (when steps are visible mid-saga):
  Lost update: two sagas interleave on the same resource
  Dirty read: another reader sees a step before the saga finishes
  Phantom: the saga's global effect is not atomic to others
Mitigations:
  - semantic locks: a "reserved" flag others must respect
  - reorder steps so the risky resource is touched last
  - per-saga visibility: mark in-flight sagas and treat their
    data as provisional
  - timeout: every step has a deadline; a timed-out step triggers
    compensation even without an explicit failure
These turn the saga from "best effort" into a design with
bounded, documented anomalies.
```

## Scaling

Sagas scale with their orchestrator: sharded state stores, per-tenant saga instances, and retry queues with backoff. Timeouts are the subtle dial — too short compensates healthy work, too long leaves stuck reservations. Saga engines provide the timeouts, retries, and resumption for free.

## Practice: Design for Isolation

Two users book the same hotel room concurrently; both sagas start, one must win.

**Task 1:** Design the semantic lock (reserved flag) and the conflict outcome.

**Task 2:** Design step timeouts and the compensation trigger on timeout.

**Task 3:** Design the compensation log with exactly-once markers.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why saga isolation needs semantic locks rather than global locks.

**Prompt 2 — Implementation Design:**
> Design a seat-booking saga where overselling is impossible. What order, locks, and timeouts achieve it?

**Prompt 3 — Boundary Testing:**
> A timeout fires while the step actually succeeded. Design the reconciliation that detects and resolves the false compensation.

## Key Takeaways

- Compensations need exactly-once markers
- Saga isolation uses semantic locks, not global ones
- Timeouts drive compensation even without failures
- Orchestrator state shards to scale sagas

## Further Reading

- [Sagas — the original paper (isolation)](https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf)
- [Temporal — activities and compensations](https://docs.temporal.io/)
