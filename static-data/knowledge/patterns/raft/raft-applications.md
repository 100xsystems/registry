---
title: "Raft in Production: etcd, Consul, and CockroachDB"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Describe etcd's Raft use"
  - "Use Raft for service discovery"
  - "Replicate storage with Raft"
  - "Operate Raft clusters"
prerequisites:
  []
knowledge_refs:
  - "patterns/raft"
---

# Raft in Production: etcd, Consul, and CockroachDB

## etcd and Configuration

etcd is a Raft-replicated key-value store: Kubernetes stores cluster state in it, and the Raft log guarantees every node sees the same writes. Reads are linearizable (the leader answers) or slightly stale (any node with a consistent snapshot). The replicated log is the coordination backbone.

```bash
# etcd: a Raft-replicated configuration store
etcdctl put /config/feature-flags '{"checkout_v2": true}'
etcdctl get /config/feature-flags --prefix

# How Raft makes this safe:
#   put -> leader appends to its log -> replicates to a majority
#   -> committed -> applied to the state machine -> answered
# A minority of down nodes does not stop writes.
# The leader holds the write path; followers replicate and serve
# consistent reads via the commit index.
```

## Storage Replication

CockroachDB and TiKV replicate ranges with Raft: each range is a Raft group, and writes commit only after a majority of replicas durably store the log entry. Reads go through the same consensus (or a lease) so they see committed state. Raft turns a storage engine into a replicated state machine.

## Practice: Operate the Cluster

A 5-node etcd cluster must survive node failures, upgrades, and network partitions.

**Task 1:** Design the upgrade: one node at a time while keeping quorum.

**Task 2:** Design the failure response: what does quorum loss look like and how do you recover?

**Task 3:** Set the election timeouts and heartbeat for your network latency.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why Raft needs an odd number of nodes and what quorum loss means. Ask me about a 2-node cluster.

**Prompt 2 — Implementation Design:**
> Design a replicated lock service on Raft: how does the lease, the fencing token, and the quorum interact?

**Prompt 3 — Boundary Testing:**
> A node is slow and triggers frequent elections. Design the leader stability (pre-vote, lease) that prevents flapping.

## Key Takeaways

- etcd runs Raft for Kubernetes-grade config
- Each storage range is its own Raft group
- Quorum loss stops writes, not reads from peers
- Election tuning keeps leaders stable

## Further Reading

- [etcd — documentation](https://etcd.io/docs/)
- [CockroachDB — Raft](https://www.cockroachlabs.com/docs/stable/architecture/replication-layer.html)
