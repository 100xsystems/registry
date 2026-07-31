---
title: "Advanced Quorum: Flexible and Epoch Quorums"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Design flexible (asymmetric) quorums"
  - "Use epochs to fence stale quorums"
  - "Tune quorums per workload skew"
  - "Handle quorum membership changes"
prerequisites:
  []
knowledge_refs:
  - "principles/quorum"
---

# Advanced Quorum: Flexible and Epoch Quorums

## Flexible Quorums

The read-write intersection can be split asymmetrically: reads need W nodes, writes need R nodes, with W+R>N but neither necessarily a majority. For read-heavy workloads, a flexible quorum (W=N, R=1) gives strong reads with a single-node read cost — at the price of slow writes.

```text
Flexible quorum variants (N=5):
  Classic  : W=3, R=3  (balanced)
  Read-opt : W=4, R=2  (cheaper reads, costlier writes)
  Write-opt: W=2, R=4  (cheaper writes, costlier reads)
All satisfy W+R>5. Choose by workload skew.

Epoch fencing: when membership changes (node join/leave), start a new
epoch; old-epoch quorum decisions are rejected by storage.
```

## Membership and Epochs

Quorum membership changes (a node joins or is evicted) invalidate the old quorum math. Epoch-based fencing: every configuration change bumps the epoch, storage stamps accepted writes with the epoch, and nodes from the old epoch are rejected — preventing a stale majority from writing after reconfiguration.

## Practice: Tune and Fence

A 5-node store: reads are 20x writes, and you must add a 6th node without downtime.

**Task 1:** Pick the flexible quorum for the read-heavy skew and justify W+R>5.

**Task 2:** Design the membership change: new config, new epoch, and the fencing that rejects old-epoch writers.

**Task 3:** Verify the intersection still holds with N=6 and your chosen W/R.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why flexible quorums keep the intersection property without both sides being majorities.

**Prompt 2 — Implementation Design:**
> Design a config-change protocol for a quorum system: how do nodes learn the new membership safely and fence the old one?

**Prompt 3 — Boundary Testing:**
> A write quorum meets but a member of it is running stale state (missed a prior write). Is that possible with W+R>N? Prove or refute.

## Key Takeaways

- Flexible quorums tune cost by workload skew
- Epochs fence stale membership decisions
- Membership changes must be atomic with the new quorum math
- The intersection property is the invariant to preserve

## Further Reading

- [Flexible Paxos — Quorum Flexibility](https://arxiv.org/abs/1608.06696)
- [Epoch-based Reconfiguration — Raft](https://raft.github.io/raft.pdf)
