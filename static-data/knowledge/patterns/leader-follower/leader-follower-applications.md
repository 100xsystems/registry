---
title: "Leader-Follower in Production: Failover and Lag"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design leader failover"
  - "Monitor replication lag"
  - "Promote a follower safely"
  - "Handle split-brain"
prerequisites:
  []
knowledge_refs:
  - "patterns/leader-follower"
---

# Leader-Follower in Production: Failover and Lag

## Failover

When the leader dies, a follower promotes. The window between the last acked write on the old leader and the promoted follower position determines data loss — sync replication narrows it, async replication risks it. Failover must be triggered carefully: a delayed leader returning and still accepting writes splits the brain.

```yaml
# Failover decision inputs (high-level):
#   leader_heartbeat: last seen leader heartbeat
#   follower_lag:     position delta to the candidate
#   quorum:           majority of nodes agree the leader is gone
#
# Promote only if:
#   - leader heartbeat expired > threshold
#   - candidate lag is acceptable for the data-loss budget
#   - majority quorum confirms leadership is vacant
# Split-brain guard: the old leader must fence (lose quorum) before
# the new leader accepts writes — typically via a shared lock/epoch.
```

## Lag as a First-Class Signal

Replication lag is the top operational risk of leader-follower. Track it per replica; route reads away from replicas past a threshold; alert when lag grows. Sync replication trades write latency for zero-loss failover; semi-sync (one sync replica) is the common middle ground.

## Practice: Design the Failover Runbook

A 3-node Postgres cluster with async replication must fail over in under 60 seconds.

**Task 1:** Define the failure detection, the lag budget, and the promotion order.

**Task 2:** Design the fencing that prevents the old leader from accepting writes.

**Task 3:** Write the verification checklist for a safe promotion and the rollback path.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me the failover trade-off: async replication speed vs the loss window. Ask me to quantify it.

**Prompt 2 — Implementation Design:**
> Design semi-sync replication: the leader waits for one follower before acking. What is the write latency cost and the loss guarantee?

**Prompt 3 — Boundary Testing:**
> The old leader survives a partition and a new leader is promoted. Design the fencing that prevents two writers.

## Key Takeaways

- Failover trades the ack window for loss risk
- Fencing prevents the split-brain double leader
- Lag must be monitored and routed around
- Semi-sync balances latency and durability

## Further Reading

- [Patroni — Postgres HA](https://patroni.readthedocs.io/)
- [Replication — DDIA Ch. 5](https://dataintensive.net/)
