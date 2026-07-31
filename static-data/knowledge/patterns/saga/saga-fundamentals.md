---
title: "Saga: Long-Running Transactions Without Distributed Locks"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the saga model"
  - "Describe compensating transactions"
  - "Compare with 2PC"
  - "Design a saga flow"
prerequisites:
  - "patterns/two-phase-commit"
  - "patterns/mediator"
knowledge_refs:
  - "patterns/saga"
---

# Saga: Long-Running Transactions Without Distributed Locks

## The Problem

A checkout spans inventory, payment, and shipping — three databases. A distributed transaction (2PC) needs a coordinator and holds locks across services; sagas instead break the flow into local transactions with compensating actions. If a step fails, the saga runs the compensations of the completed steps — an eventual rollback, no global locks.

```python
# Saga: local steps + compensating actions
class OrderSaga:
    def __init__(self, inv, pay, ship):
        self.inv, self.pay, self.ship = inv, pay, ship

    def run(self, order):
        done = []
        try:
            self.inv.reserve(order)        # step 1
            done.append(lambda: self.inv.release(order))   # compensate
            self.pay.charge(order)         # step 2
            done.append(lambda: self.pay.refund(order))
            self.ship.dispatch(order)      # step 3
            done.append(lambda: self.ship.cancel(order))
            return 'success'
        except Exception as e:
            for compensate in reversed(done):   # undo, last first
                try: compensate()
                except Exception: log('compensation failed', e)
            raise e
```

## Compensations

A compensating action reverses the business effect of a completed step (release a reservation, refund a charge, cancel a shipment). It is not an undo of the transaction — it is a new transaction that makes the world whole again. Compensations must be idempotent and themselves reliable.

## Practice: Design the Checkout Saga

Checkout: reserve inventory, charge card, book shipment. A payment failure must unwind the reservation.

**Task 1:** List the steps and each compensating action.

**Task 2:** Trace the failure at each step and the compensation order.

**Task 3:** Make each compensation idempotent and design its retry.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why a saga needs compensations instead of a rollback. Start with two databases.

**Prompt 2 — Compare & Contrast:**
> Compare saga with two-phase commit: availability, locks, and consistency.

**Prompt 3 — Boundary Testing:**
> A compensation fails (the refund API is down). Design the retry and the manual-repair path.

## Key Takeaways

- Sagas split long transactions into compensatable steps
- Compensations are new transactions, not undos
- No global locks — availability stays high
- Compensations must be idempotent and reliable

## Further Reading

- [Saga pattern — microservices.io](https://microservices.io/patterns/data/saga.html)
- [Sagas — the original paper](https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf)
