---
title: "Advanced Raft: Membership Changes and Snapshots"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Change membership safely"
  - "Compact logs with snapshots"
  - "Use read leases"
  - "Diagnose Raft issues"
prerequisites:
  []
knowledge_refs:
  - "patterns/raft"
---

# Advanced Raft: Membership Changes and Snapshots

## Membership Changes

Changing the node set mid-flight is the classic Raft hazard: the old and new configurations can each form a majority that never overlaps. Raft solves this with joint consensus — the new config commits only when both old and new majorities agree — applied as a special log entry.

```text
Safe membership change (joint consensus):
  1. Leader appends ConfChange(NewConfig) entry.
  2. The entry commits only when BOTH the old and new
     configurations have a majority — a joint quorum.
  3. Once committed, the cluster switches to the new config
     and the old config is retired.
This prevents the split-brain window where an old-majority and
a new-majority disagree.

Log compaction:
  - The log grows forever; snapshot the state machine at an index.
  - New members receive a snapshot + tail instead of the full log.
  - InstallSnapshot replaces the follower's state and log prefix.
Read leases:
  - A leader can serve reads without a quorum round-trip within
    its election lease (it cannot be deposed during the lease).
```

## Diagnosis

Common Raft failures: election flapping (too short timeouts or a slow node), quorum loss (even node count or a partitioned majority), and split-brain appearance (a fenced leader still serving reads). Logs and metrics — term changes, commit index lag, leader transitions — diagnose each.

## Practice: Grow the Cluster

A 3-node Raft cluster must grow to 5 nodes during traffic without downtime.

**Task 1:** Design the joint-consensus membership change sequence.

**Task 2:** Design the snapshot strategy for a node added with a huge log.

**Task 3:** Set the observability: leader changes, commit lag, snapshot traffic.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why joint consensus prevents the membership split-brain window.

**Prompt 2 — Implementation Design:**
> Design a snapshot policy: when to snapshot, how install works, and how a brand-new node catches up.

**Prompt 3 — Boundary Testing:**
> A leader serves reads from a stale state after a partition. Design the lease check that detects and demotes it.

## Key Takeaways

- Joint consensus makes membership changes safe
- Snapshots bound the log and catch up new nodes
- Read leases avoid quorum round trips
- Term and lag metrics diagnose failures

## Further Reading

- [Raft — cluster membership changes](https://raft.github.io/raft.pdf)
- [etcd — Raft internals](https://etcd.io/docs/v3.5/learning/raft-internals/)
