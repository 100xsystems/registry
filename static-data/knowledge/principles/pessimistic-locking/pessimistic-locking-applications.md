---
title: "Pessimistic Locking in Production: Distributed Locks"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design distributed locks with leases"
  - "Use advisory locks and Redis locks"
  - "Handle lock expiry and fencing"
  - "Avoid the lock-across-network-call trap"
prerequisites:
  []
knowledge_refs:
  - "principles/pessimistic-locking"
---

# Pessimistic Locking in Production: Distributed Locks

## Distributed Locks

When the guarded resource spans processes, the lock lives in a shared store: a database row, a Redis SETNX with TTL, or a coordination service. The lock must expire (lease) so a crashed holder releases it — and holders must be fenced so an expired-but-still-running holder cannot write.

```python
# Redis lock with lease (simplified, fencing omitted for brevity)
import redis, time, uuid

def acquire(client, name, ttl_ms=10_000):
    token = uuid.uuid4().hex
    ok = client.set(f'lock:{name}', token, nx=True, px=ttl_ms)
    return token if ok else None

def release(client, name, token):
    # only release if we still own it (Lua for atomicity)
    script = "if redis.call('get', KEYS[1]) == ARGV[1] " \
             "then return redis.call('del', KEYS[1]) else return 0 end"
    client.eval(script, 1, f'lock:{name}', token)
```

## The Trap: Network Calls Under Lock

Holding a distributed lock across a slow external call makes the lease expire while the holder still works — then a second holder acquires the lock and both act. The fix: keep the locked section short and local, or carry a fencing token that storage validates.

## Practice: Design the Distributed Lock

A job scheduler must ensure only one node runs the nightly cleanup.

**Task 1:** Design the lock: store, lease duration, renewal loop, and release path.

**Task 2:** Handle the crash case: lease expires, another node acquires. What fences the old node?

**Task 3:** Explain why the cleanup must NOT call a slow external service while holding the lock.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why a lock without a lease is a time bomb and why a lease without fencing still allows double action.

**Prompt 2 — Implementation Design:**
> Design a payment double-charge guard using a distributed lock plus idempotency key. Where does the lock end and the key take over?

**Prompt 3 — Boundary Testing:**
> The lock store (Redis) is down. Design the degraded mode: fail open (risky) or fail closed (safe but unavailable)?

## Key Takeaways

- Distributed locks need leases and fencing
- Redis SETNX with TTL is a lock; the Lua release is atomic
- Never hold locks across slow network calls
- Fencing tokens make expired holders harmless

## Further Reading

- [How to Do Distributed Locking — Kleppmann](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html)
- [Redlock Controversy — Redis Docs](https://redis.io/docs/latest/develop/use/patterns/distributed-locks/)
