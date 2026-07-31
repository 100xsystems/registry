---
title: "Paxos: Consensus with a Majority"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the consensus problem"
  - "Describe proposers, acceptors, learners"
  - "Trace a two-phase round"
  - "Know the majority guarantee"
prerequisites:
  - "principles/quorum"
  - "patterns/raft"
knowledge_refs:
  - "patterns/paxos"
---

# Paxos: Consensus with a Majority

## The Problem

Consensus: several nodes must agree on one value even with failures and message loss. Paxos solves it with three roles: proposers suggest values, acceptors vote in phases, learners observe the outcome. The key invariant — once a value is chosen, every future round chooses the same value — comes from the majority intersection: any two majorities share a node.

```text
Paxos two phases (prepare/accept):
  Prepare phase:
    1. proposer -> acceptors: prepare(n)   (n = new higher ballot)
    2. acceptors reply: promise to ignore ballots < n,
       and return any value they already accepted
    3. proposer picks the value from the highest returned ballot,
       or its own value if none
  Accept phase:
    4. proposer -> acceptors: accept(n, v)
    5. acceptors accept if they have promised >= n; a majority
       acceptance means v is CHOSEN
  Learn phase:
    6. chosen value is learned by learners and all nodes
Why it works: a future proposer with a higher ballot must
intersect the previous majority in prepare, learn v, and propose
v again. Majorities always intersect -> one chosen value.
```

## Roles and Safety

Safety (only one value chosen) holds under any failure pattern; liveness (progress) needs a distinguished proposer (leader) to avoid livelock — competing proposers can starve each other by raising ballots forever. Multi-Paxos runs repeated instances over a log with a stable leader.

## Practice: Trace the Round

Three acceptors; two propose different values concurrently.

**Task 1:** Trace: prepare(1, X) then prepare(2, Y) — which promises win?

**Task 2:** Show why the higher ballot must adopt the earlier accepted value.

**Task 3:** Design the leader election that prevents ballot livelock.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why any two majorities intersect. Start with 3 nodes and 2-of-3 quorums.

**Prompt 2 — Compare & Contrast:**
> Compare Paxos with Raft. Raft reorders roles and phases for understandability — where are the practical differences?

**Prompt 3 — Boundary Testing:**
> An acceptor fails after prepare but before accept. Show why the round still completes and the value stays safe.

## Key Takeaways

- Paxos: proposers, acceptors, learners
- Majority intersection guarantees one chosen value
- Safety holds under any failure; liveness needs a leader
- Multi-Paxos logs repeated instances

## Further Reading

- [The Part-Time Parliament (original Paxos paper)](https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf)
- [Paxos Made Simple — Lamport](https://lamport.azurewebsites.net/pubs/paxos-simple.pdf)
