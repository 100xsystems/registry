---
title: "Advanced Paxos: Multi-Paxos and Fast Paxos"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Explain Multi-Paxos"
  - "Describe Fast Paxos"
  - "Compare variants"
  - "Reason about liveness"
prerequisites:
  []
knowledge_refs:
  - "patterns/paxos"
---

# Advanced Paxos: Multi-Paxos and Fast Paxos

## Multi-Paxos

Consensus on one value is not enough — a replicated state machine needs consensus on every log entry. Multi-Paxos elects a stable leader once, then the leader drives accept rounds for each log slot without re-running prepare every time. The leader change is the expensive moment; steady state is one message round.

```text
Multi-Paxos: consensus on a log of values
  Phase 1 (once per leader term): the leader runs prepare with
    a new ballot and learns the highest chosen value per slot.
  Phase 2 (steady state): for each log slot i, the leader sends
    accept(i, v); a majority ack -> slot i is decided.
  Clients read by following the decided log; the state machine
  applies entries in order.
Leader failure -> a new leader runs phase 1 for all slots and
  continues. The cost of consensus is thus one round trip per
  log entry in the common case.
Variants: Fast Paxos (clients propose directly to acceptors,
  one phase in the happy path), Mencius (no leader, per-slot
  rotation), EPaxos (dependent commands ordered causally).
```

## Choosing a Variant

Raft made Paxos understandable and is the default choice today; ZooKeeper uses Zab; etcd and CockroachDB use Raft. Mencius and EPaxos optimize for wide-area deployments where a single leader is a bottleneck. The trade space: leader simplicity vs message rounds vs fault tolerance vs WAN latency.

## Practice: Compare the Family

A WAN-replicated database spanning 5 regions needs consistent replication.

**Task 1:** Trace Multi-Paxos steady state: message rounds per log entry.

**Task 2:** Compare Raft and EPaxos for the WAN topology.

**Task 3:** Design the leader-change protocol and its cost.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why Multi-Paxos pays the prepare cost once per leader term.

**Prompt 2 — Implementation Design:**
> Design a replicated state machine over Multi-Paxos: what is in the log, how do reads work, and how is a new leader caught up?

**Prompt 3 — Boundary Testing:**
> A leader partitions and a new one is elected with an older log. Design the quorum rule that prevents stale overwrites.

## Key Takeaways

- Multi-Paxos = consensus on every log slot
- Stable leaders make steady state one round
- Raft, Zab, Mencius, EPaxos trade the same guarantees
- Leader changes are the expensive moments

## Further Reading

- [Paxos Made Moderately Complex](https://paxos.systems/)
- [EPaxos — the paper](https://dl.acm.org/doi/10.1145/2517349.2522732)
