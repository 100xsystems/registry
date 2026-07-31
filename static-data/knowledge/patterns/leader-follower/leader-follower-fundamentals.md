---
title: "Leader-Follower: One Node Writes, All Read"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the leader-follower model"
  - "Describe replication flow"
  - "Understand read scaling"
  - "Know the single-writer guarantee"
prerequisites:
  - "patterns/replication"
  - "patterns/paxos"
knowledge_refs:
  - "patterns/leader-follower"
---

# Leader-Follower: One Node Writes, All Read

## The Model

One leader accepts all writes and appends them to a log; followers stream the log and apply it, staying behind the leader by a replication lag. Reads can go anywhere — but reads from a follower may be stale by that lag. This is the workhorse of Postgres, MySQL, and most databases.

```python
# Leader-follower replication: log shipping with position tracking
class Leader:
    def __init__(self):
        self.log = []                 # every write appended here
        self.position = 0

    def write(self, op):
        self.log.append(op)
        self.position += 1
        return self.position

class Follower:
    def __init__(self, leader):
        self.leader = leader
        self.applied = 0

    def poll(self):
        while self.applied < self.leader.position:   # stream the log
            op = self.leader.log[self.applied]
            self.apply(op)
            self.applied += 1

    def apply(self, op):
        print(f'follower applied: {op}')
```

## Consistency Trade-Off

The leader guarantees a total write order; followers are eventually consistent with it. Read-after-write needs routing: read your own writes from the leader, everything else from any replica. Replication lag breaks monotonic reads if the same user reads two followers at different positions.

## Practice: Route the Reads

A forum app: 95% reads, 5% writes; users must always see their own posts.

**Task 1:** Design the routing rule: which reads go to the leader, which to followers?

**Task 2:** Model the replication lag and its effect on a user reading two replicas.

**Task 3:** Design the read-your-writes guarantee with a session pin.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about where reads go and what lag means for users. Start with read-your-writes.

**Prompt 2 — Compare & Contrast:**
> Compare leader-follower with multi-leader and leaderless (quorum) replication. When is single-writer the right call?

**Prompt 3 — Boundary Testing:**
> A follower lags 30 seconds and serves stale prices during a sale. Design the staleness guard (max lag routing) that protects users.

## Key Takeaways

- One leader serializes writes; followers scale reads
- Followers replicate via a streamed log
- Replication lag = read staleness
- Read-your-writes needs session-aware routing

## Further Reading

- [Replication — Designing Data-Intensive Applications, Ch. 5](https://dataintensive.net/)
- [PostgreSQL — Streaming Replication](https://www.postgresql.org/docs/current/warm-standby.html)
