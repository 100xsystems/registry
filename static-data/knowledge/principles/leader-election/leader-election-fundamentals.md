---
title: "Leader Election: One Coordinator at a Time"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain why a single leader is needed"
  - "Describe the leader election problem"
  - "Use leases to bound leader validity"
  - "Recognize split-brain risks"
prerequisites:
  - "principles/quorum"
  - "principles/cap-theorem"
knowledge_refs:
  - "principles/leader-election"
---

# Leader Election: One Coordinator at a Time

## The Problem

Many coordination tasks need exactly one actor at a time: the node that processes a partition, the node that owns a lock, the node that assigns sequence numbers. Leader election is the mechanism that picks that node and ensures there is never more than one.

The danger is split-brain: two nodes both believing they are leader, both writing — divergent state that may never reconcile. Safe election must guarantee that at most one leader is active at any time, even during partitions.

```text
Leader election requirements:
  1. Safety: at most one leader at any time (no split-brain)
  2. Liveness: if a leader fails, a new one is elected
  3. Speed: failover within a bounded window

Mechanism options:
  - Consensus (Raft): majority-based, crash-safe
  - Lease on a lock (etcd/ZooKeeper): lease = time-bounded ownership
  - Bully algorithm: highest-ID node takes over
```

## Leases

A lease is leadership with a time bound: the leader holds it for T seconds and must renew. If the lease expires, another node may take over. The lease bounds how long a dead leader can keep "leading" — the core protection against split-brain.

## Practice: Design a Lease

Two nodes serve a queue partition; exactly one may process messages at a time.

**Task 1:** Design the lease: how it is acquired, its duration, and its renewal loop.

**Task 2:** Trace a failure: leader dies mid-lease. When can the other node take over? What is the failover window?

**Task 3:** Explain what happens if the old leader wakes up after the lease expires but still thinks it is leader.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why a lease without a clock bound is unsafe. Start with the split-brain scenario.

**Prompt 2 — Compare & Contrast:**
> Compare lease-based election (etcd) with Raft consensus. When is each the right tool?

**Prompt 3 — Boundary Testing:**
> A slow leader renews its lease just after the standby took over. Design the fencing that prevents both from acting.

## Key Takeaways

- Exactly one leader must be active at any time
- Leases bound leadership by time
- Split-brain is the failure mode election must prevent
- Fencing tokens guard against zombie leaders

## Further Reading

- [Raft Paper](https://raft.github.io/raft.pdf)
- [etcd — Lease Documentation](https://etcd.io/docs/v3.5/learning/why/)
