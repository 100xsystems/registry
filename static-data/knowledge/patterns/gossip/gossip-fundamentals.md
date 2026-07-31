---
title: "Gossip Protocol: Epidemic Dissemination"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the gossip model"
  - "Describe push, pull, and push-pull"
  - "Analyze convergence and fan-out"
  - "Use gossip for membership and state"
prerequisites:
  - "patterns/paxos"
  - "patterns/raft"
knowledge_refs:
  - "patterns/gossip"
---

# Gossip Protocol: Epidemic Dissemination

## The Model

Each node periodically picks a random peer and exchanges summaries. Information spreads exponentially: with fan-out f per round, after t rounds roughly f^t nodes have heard it. There is no coordinator, no tree, and no single point of failure — the protocol is self-healing and eventually consistent.

```python
# Push gossip: every round, send your state to a random peer
import random

class Node:
    def __init__(self, node_id, peers):
        self.id = node_id
        self.peers = peers          # neighbor set
        self.state = {}             # key -> (value, version)

    def round(self):
        peer = random.choice(self.peers)
        # push: send my newer entries; pull: ask for theirs
        newer = {k: v for k, v in self.state.items()
                 if self.state.get(k, (None, -1))[1] > peer.state.get(k, (None, -1))[1]}
        peer.merge(newer)
        newer_from_peer = {k: v for k, v in peer.state.items()
                           if peer.state.get(k, (None, -1))[1] > self.state.get(k, (None, -1))[1]}
        self.merge(newer_from_peer)

    def merge(self, entries):
        for k, (v, ver) in entries.items():
            if ver > self.state.get(k, (None, -1))[1]:
                self.state[k] = (v, ver)
```

## Push, Pull, Push-Pull

Push sends updates out; pull requests updates in; push-pull does both and converges fastest. Pull-only works when nodes are unreliable, push-only when updates are frequent. The exchange unit is a digest — checksums or version maps — so only the deltas travel.

## Practice: Converge the Cluster

A 100-node cluster must spread one configuration update to every node.

**Task 1:** Simulate push gossip with fan-out 3; count rounds to full coverage.

**Task 2:** Add pull and compare convergence on a cluster with 10% packet loss.

**Task 3:** Design the version scheme that stops old updates from overwriting newer ones.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why gossip needs no coordinator. Start with a node failure.

**Prompt 2 — Compare & Contrast:**
> Compare gossip with leader-based replication. When is epidemic dissemination the right choice?

**Prompt 3 — Boundary Testing:**
> A node rejoins after a long partition with a stale state. Design the version and repair path that reconciles it.

## Key Takeaways

- Gossip spreads state exponentially, coordinator-free
- Push, pull, and push-pull trade bandwidth for convergence
- Digests ensure only deltas travel
- Versioning prevents stale overwrites

## Further Reading

- [Gossip Protocol — Wikipedia](https://en.wikipedia.org/wiki/Gossip_protocol)
- [SWIM: Scalable Weakly-consistent Infection-style Membership](https://www.cs.cornell.edu/~asdas/research/dsn02-SWIM.pdf)
