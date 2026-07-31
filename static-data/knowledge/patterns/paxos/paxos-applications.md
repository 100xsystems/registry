---
title: "Paxos in Production: Chubby and ZooKeeper"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Describe Chubby's use of Paxos"
  - "Use ZooKeeper coordination primitives"
  - "Understand linearizability"
  - "Handle leader failures"
prerequisites:
  []
knowledge_refs:
  - "patterns/paxos"
---

# Paxos in Production: Chubby and ZooKeeper

## Chubby

Google's Chubby wraps Paxos in a lock service: a Paxos-replicated log backs a file-system-like namespace used for leader election and configuration. Clients lease locks; the Paxos state machine guarantees one lock owner. The pattern — consensus behind a familiar API — is what ZooKeeper and etcd replicate.

```java
// ZooKeeper: ephemeral znode = lease-based lock via consensus
String path = "/locks/db-writer";
try {
    // create ephemeral: auto-deleted if this session dies
    zk.create(path, data, ZooDefs.Ids.OPEN_ACL_UNSAFE,
              CreateMode.EPHEMERAL);
    // We hold the lock — ZooKeeper consensus ensures only one
    // ephemeral node exists at this path.
} catch (KeeperException.NodeExistsException e) {
    // Someone else holds the lock; watch it for deletion
}
// Leader election = same pattern; the session is the lease,
// and the consensus log guarantees ordering.
```

## Linearizability

The replicated log makes every operation appear instantaneous and total-ordered — linearizable. That is the coordination guarantee: reads and writes to the consensus service act as if on one machine. Application leaders use this to fence (epoch the lock) and to publish config atomically.

## Practice: Build the Coordination Layer

Three app instances need a single leader, a shared config, and fencing.

**Task 1:** Design the leader election with ephemeral nodes and fencing tokens.

**Task 2:** Publish the config atomically as a versioned znode.

**Task 3:** Design the failure path: leader death, lease expiry, and re-election.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why coordination services wrap consensus in familiar primitives. Ask me what a fencing token is for.

**Prompt 2 — Implementation Design:**
> Design a distributed cron: one leader schedules, workers execute. How does the lease and fencing work?

**Prompt 3 — Boundary Testing:**
> A partitioned leader still thinks it holds the lock. Design the fencing that makes its writes rejected.

## Key Takeaways

- Coordination services wrap Paxos in familiar APIs
- Ephemeral nodes + leases = distributed locks
- The log gives linearizable ordering
- Fencing rejects stale leaders

## Further Reading

- [The Chubby Lock Service — Google](https://static.googleusercontent.com/media/research.google.com/en//archive/chubby-osdi06.pdf)
- [ZooKeeper — programmer guide](https://zookeeper.apache.org/doc/current/zookeeperProgrammers.html)
