---
title: "Leader Election in Production: Consensus and Coordination"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Explain how Raft elects a leader"
  - "Use etcd/ZooKeeper for leader election"
  - "Handle leader handoff gracefully"
  - "Design failover with bounded downtime"
prerequisites:
  []
knowledge_refs:
  - "principles/leader-election"
---

# Leader Election in Production: Consensus and Coordination

## Raft Election

Raft nodes are followers, candidates, or leader. Followers elect a leader by majority vote with randomized timeouts; the leader replicates log entries to a majority before committing. If the leader dies, followers start a new election. Safety comes from requiring a majority — two leaders cannot both have majorities.

```text
Raft election in brief:
  1. Followers expect heartbeats; timeout triggers candidacy
  2. Candidate requests votes; majority wins
  3. Leader sends heartbeats; commits after majority ack
  4. Leader crash -> new election within one timeout window
Split-brain is impossible: two leaders would each need a majority,
and majorities always intersect.
```

## Election on etcd/ZooKeeper

Practical systems build election on a coordination service: contenders create an ephemeral key; the one whose create succeeds is leader. Ephemeral nodes vanish when the owner dies, triggering immediate re-election. The coordination service provides the consensus and the failure detection.

## Practice: Build an Election Client

Three replicas of a scheduler need a leader.

**Task 1:** Design the election flow on etcd: ephemeral leader key, election loop, and lease renewal.

**Task 2:** Handle the leader's graceful shutdown (release the key) vs crash (lease expiry).

**Task 3:** Define what the new leader does on takeover: state to reload, work to resume, alerts to fire.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why randomized election timeouts prevent split-vote deadlocks in Raft. Ask me to reason through two candidates.

**Prompt 2 — Implementation Design:**
> Design leader election for a single-writer database shard. What fencing token does the leader carry, and how is it checked on every write?

**Prompt 3 — Boundary Testing:**
> The coordination service itself partitions. What happens to the election? Design the fail-safe behavior of the data plane.

## Key Takeaways

- Raft requires a majority — split-brain becomes impossible
- Ephemeral keys + leases give practical election
- Failover downtime equals the election window
- Leaders need fencing tokens to be safe after failover

## Further Reading

- [The Raft Consensus Algorithm](https://raft.github.io/)
- [ZooKeeper Leader Election Recipes](https://zookeeper.apache.org/doc/current/recipes.html)
