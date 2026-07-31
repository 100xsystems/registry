---
title: "Advanced Leader Election: Fencing and Fast Failover"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Design fencing tokens to stop zombie leaders"
  - "Use epochs for safe failover"
  - "Minimize failover downtime"
  - "Handle cascading elections"
prerequisites:
  []
knowledge_refs:
  - "principles/leader-election"
---

# Advanced Leader Election: Fencing and Fast Failover

## Fencing Tokens

When leadership changes, the old leader may still run for a while. Fencing: every leadership term gets a monotonically increasing token; storage only accepts writes from the current token. A zombie leader with an old token is rejected — split-brain is converted into safe rejection.

```text
Fencing token flow:
  term 5: leader L5 writes with token 5  -> accepted
  L5 crashes; term 6: leader L6 elected, token 6
  L5 wakes and writes with token 5       -> REJECTED (stale token)

This is what makes "at most one leader" enforced by the storage,
not just by the election protocol.
```

## Fast Failover

Failover time = detection + election + handoff. Reduce each: tight heartbeat intervals, ready standbys with warm state, and idempotent handoff so the new leader resumes without double-processing. Balance tight detection against flapping (false failover) under network jitter.

## Practice: Design the Fenced Failover

A single-writer partition service: 3 nodes, storage enforces tokens.

**Task 1:** Design the token generation and storage-side validation.

**Task 2:** Trace the full failover: leader crash, election, token bump, resume. Where is downtime spent?

**Task 3:** Design the standby warm-up so handoff is near-instant without double-processing.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why election safety alone is not enough and fencing is what protects the data.

**Prompt 2 — Implementation Design:**
> Design a scheduler with 5 nodes and a 200ms failover target. What are the heartbeat, election, and handoff budgets?

**Prompt 3 — Boundary Testing:**
> Network jitter causes flapping elections. Design the hysteresis that prevents thrashing leadership.

## Key Takeaways

- Fencing tokens make zombie leaders harmless
- Epochs give every term a unique identity
- Failover time = detection + election + handoff
- Warm standbys and idempotent handoff cut downtime

## Further Reading

- [Fencing Tokens — Martin Kleppmann](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html)
- [Raft Leader Election Section](https://raft.github.io/raft.pdf)
