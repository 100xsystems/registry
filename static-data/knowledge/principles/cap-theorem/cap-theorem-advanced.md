---
title: "Advanced CAP: Linearizability, Sessions, and Reconciliation"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Define linearizability and serializability precisely"
  - "Apply session guarantees to AP systems"
  - "Design conflict resolution with version vectors"
  - "Explain the read-your-writes and monotonic reads guarantees"
prerequisites:
  []
knowledge_refs:
  - "principles/cap-theorem"
---

# Advanced CAP: Linearizability, Sessions, and Reconciliation

## Linearizability and Session Guarantees

Linearizability orders operations in real time: once a write completes, all subsequent reads see it. Fully linearizable AP systems are impossible during partitions, but session guarantees give users a weaker, useful contract: read-your-writes, monotonic reads, and monotonic writes.

A read-your-writes session routes a user's reads to a replica that has seen their writes — cheap, and it fixes the most common user-visible consistency bug.

```python
# Session affinity: stick a user to the replica that saw their writes
session = {}
def route_read(user_id, replica_versions):
    # pick the replica whose version >= user's last-seen write version
    want = session.get(user_id, 0)
    for replica, version in replica_versions.items():
        if version >= want:
            session[user_id] = replica   # sticky affinity
            return replica
    return min(replica_versions, key=replica_versions.get)
```

## Version Vectors

When two replicas diverge, version vectors tell you whether one state is newer (descendant), equal, or concurrent. Concurrent writes must be merged by application logic — that is where CRDTs and LWW registers come in.

## Practice: Design Conflict Resolution

An AP cart service has two replicas that each received an add-to-cart during a partition.

**Task 1:** Use version vectors to detect the concurrent writes.

**Task 2:** Merge the carts (union) and decide how to handle a concurrent remove of an item added on the other replica.

**Task 3:** Add a last-writer-wins register for the cart "coupon" field and explain the clock it needs.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can distinguish linearizability from serializability and explain why AP systems give up the former but keep transactions.

**Prompt 2 — Implementation Design:**
> Design session guarantees for a chat app that is otherwise AP. Which guarantees does each message need to preserve ordering of one conversation?

**Prompt 3 — Boundary Testing:**
> Two users concurrently rename the same file in a distributed filesystem. Design a resolution policy and describe the user-visible result for each case.

## Key Takeaways

- Linearizability is a real-time ordering; AP gives it up during partitions
- Session guarantees fix common user-visible bugs cheaply
- Version vectors distinguish causal from concurrent writes
- Concurrent writes need application-level merge rules

## Further Reading

- [Linearizability — Herlihy & Wing](https://cs.brown.edu/~mph/HerlihyW90/p463-herlihy.pdf)
- [Session Guarantees for Weakly Consistent Replicated Data](https://www.cs.utexas.edu/users/dahlin/papers/session83.pdf)
