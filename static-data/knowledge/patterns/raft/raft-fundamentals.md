---
title: "Raft: Consensus Made Understandable"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the Raft roles"
  - "Describe leader election"
  - "Understand log replication"
  - "Know the safety guarantees"
prerequisites:
  - "patterns/paxos"
  - "principles/quorum"
knowledge_refs:
  - "patterns/raft"
---

# Raft: Consensus Made Understandable

## The Model

Raft splits consensus into three subproblems: leader election (nodes pick one leader), log replication (the leader appends entries and replicates to a majority), and safety (elections only produce leaders with all committed entries). Every node is a leader, follower, or candidate — the roles are explicit.

```text
Raft fundamentals:
  Terms: time is divided into terms; each term has at most one leader.
  Election: followers with no heartbeat become candidates, request
    votes, win with a majority, and start a new term.
  Log: the leader appends client commands to its log and replicates
    entries to followers; an entry is committed once a majority
    has it on disk.
  Safety (Election Restriction): a candidate only wins if its log
    is at least as up-to-date as a majority's — so a committed
    entry can never be overwritten by a new leader.
  Fencing: a higher term from any node demotes the current leader —
    a partitioned old leader cannot keep writing.
```

## Why Raft Exists

Paxos was famously hard to implement correctly. Raft restructures the same guarantees into understandable pieces — explicit roles, terms, and a single leader — and it is the consensus engine behind etcd, Consul, and CockroachDB.

## Practice: Trace an Election

A 5-node cluster loses its leader mid-term.

**Task 1:** Trace: heartbeat timeout -> candidate -> vote request -> majority.

**Task 2:** Show why a candidate with an older log cannot win.

**Task 3:** Design the split-vote tie: no majority -> timeout -> new term.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why a higher term fences the old leader. Start with the partition.

**Prompt 2 — Compare & Contrast:**
> Compare Raft with Paxos: same guarantees, different structure. Where are the practical wins?

**Prompt 3 — Boundary Testing:**
> Two candidates split the vote repeatedly. Design the randomized election timeout that breaks the tie.

## Key Takeaways

- Raft: explicit roles, terms, and one leader
- Commit requires a majority on disk
- Election restriction protects committed entries
- Terms fence stale leaders

## Further Reading

- [The Raft Paper (with animations)](https://raft.github.io/raft.pdf)
- [Raft — secret life of data](https://thesecretlivesofdata.com/raft/)
