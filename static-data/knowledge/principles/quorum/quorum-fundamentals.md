---
title: "Quorum: Majorities and Consensus"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Define a quorum and why it needs a majority"
  - "Explain the quorum intersection property"
  - "Use read/write quorums (W + R > N)"
  - "Apply quorums to replica consistency"
prerequisites:
  - "principles/cap-theorem"
  - "principles/leader-election"
knowledge_refs:
  - "principles/quorum"
---

# Quorum: Majorities and Consensus

## The Core Idea

A quorum is the minimum number of nodes that must agree for a decision to hold. In a 5-node cluster, a quorum of 3 guarantees one crucial property: any two quorums intersect in at least one node. That intersection is how the system knows a later read can always see an earlier acknowledged write.

The math: with N replicas, require W writes and R reads such that W + R > N. Then a read quorum and a write quorum overlap, so every consistent read sees the latest acknowledged write.

```text
Quorum math (N = 5):
  W=3, R=3 : W+R=6 > 5 -> reads always see latest write
  W=3, R=2 : W+R=5 = 5 -> NOT guaranteed (may miss the write)
  W=2, R=2 : W+R=4 < 5 -> stale reads possible (AP-ish)

Two quorums of 3 always share at least 1 node:
  {1,2,3} and {3,4,5} intersect at 3.  That is the guarantee.
```

## Quorum vs Consensus

A quorum is the membership rule; consensus (Raft, Paxos) is a protocol that uses quorums to agree on a total order of operations. Quorum reads/writes give consistency; consensus gives ordering and leader election on top.

## Practice: Design the Quorum

A 5-node key-value store: reads must never return stale acknowledged data; writes must survive one node loss.

**Task 1:** Pick W and R satisfying W+R>5 and W>2. Justify.

**Task 2:** Compute availability: what happens with 2 nodes down? With 3 down?

**Task 3:** Show why W=1, R=5 "sounds strong" but breaks the read guarantee when the write node is the read node.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why W+R>N is sufficient for the read guarantee. Start with the intersection argument.

**Prompt 2 — Compare & Contrast:**
> Compare quorum reads with Raft log replication. Where does the majority do different jobs?

**Prompt 3 — Boundary Testing:**
> W=3, R=3, N=5 but the write nodes and read nodes are disjoint groups (write set {1,2,3}, read set {4,5,1}). Is the guarantee intact?

## Key Takeaways

- Quorums intersect — that is the consistency guarantee
- W+R>N is the read-your-write condition
- Quorums trade write latency for availability
- Consensus builds ordering on top of quorums

## Further Reading

- [Raft Paper (Quorum sections)](https://raft.github.io/raft.pdf)
- [Dynamo Paper (Quorum-based replication)](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf)
