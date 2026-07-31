---
title: "Advanced Gossip: Sloppy Quorums and Anti-Entropy"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Explain hinted handoff"
  - "Design read repair and anti-entropy"
  - "Combine quorums with gossip"
  - "Reconcile divergent replicas"
prerequisites:
  []
knowledge_refs:
  - "patterns/gossip"
---

# Advanced Gossip: Sloppy Quorums and Anti-Entropy

## Sloppy Quorums and Hinted Handoff

Dynamo-style systems accept writes on any healthy node when the home replicas are unreachable, then hand off the write later — hinted handoff. Gossip carries the hints. The trade: the system stays available under partition but trades strict consistency, relying on read repair and anti-entropy to converge afterward.

```go
// Hinted handoff: stash for a down replica, deliver via gossip
type Hint struct {
    Key       string
    Value     []byte
    TargetID  string     // the replica that was down
    SourceID  string
}
func (n *Node) onWrite(key string, val []byte, replicas []string) {
    written := 0
    for _, r := range replicas {
        if err := n.client.Put(r, key, val); err == nil {
            written++
        } else {
            n.hints[r] = append(n.hints[r], Hint{key, val, r, n.id})
        }
    }
    if written < quorum {
        n.gossipHints()      // deliver hints when targets return
    }
}
```

## Read Repair and Anti-Entropy

Read repair compares replicas on every read and repairs stale ones. Anti-entropy runs continuously in the background, exchanging Merkle trees so divergent nodes find and fix differences without shipping full data. Together they pull a gossip system back to convergence after partitions.

## Practice: Converge After the Partition

A 5-node Dynamo-style ring splits for 5 minutes; writes land on isolated nodes via hints.

**Task 1:** Design the hinted-handoff delivery and its retry policy.

**Task 2:** Design read repair with a version comparison at read time.

**Task 3:** Design the Merkle-tree anti-entropy that repairs the ring without a full sync.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain how hinted handoff keeps writes available during a partition and how anti-entropy heals afterward.

**Prompt 2 — Implementation Design:**
> Design the merge rule for a key written on both sides of a partition with concurrent versions. Show the conflict-free or surfaced-conflict choice.

**Prompt 3 — Boundary Testing:**
> A node returns from a week-long partition. Design the reconciliation that detects and repairs every divergent key.

## Key Takeaways

- Hinted handoff keeps writes available through partitions
- Read repair fixes staleness on access
- Merkle anti-entropy finds divergence without full syncs
- Gossip systems converge but need explicit conflict policy

## Further Reading

- [Dynamo Paper (sloppy quorums, hinted handoff)](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf)
- [Cassandra — Read Repair](https://cassandra.apache.org/doc/stable/cassandra/operating/read_repair.html)
