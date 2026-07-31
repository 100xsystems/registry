---
title: "Advanced Fail Fast: Timeouts, Deadlines, and Cancellation"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Design timeout hierarchies with bounded totals"
  - "Use deadlines and context cancellation end-to-end"
  - "Fail fast on budget exhaustion (load shedding)"
  - "Distinguish fast-fail from silent-drop"
prerequisites:
  []
knowledge_refs:
  - "principles/fail-fast"
---

# Advanced Fail Fast: Timeouts, Deadlines, and Cancellation

## Deadlines That Propagate

A single request may fan out to dozens of services. Per-call timeouts that are independent let the total budget balloon (10 calls × 500ms = 5s). Propagate a deadline: the context carries the remaining budget, and each hop checks and shrinks it.

```go
// Deadline propagation: fail fast when the budget is spent
func HandleOrder(ctx context.Context, id string) error {
    ctx, cancel := context.WithTimeout(ctx, 2*time.Second)
    defer cancel()

    price, err := priceService.Price(ctx, id)   // inherits deadline
    if err != nil { return err }                // deadline exceeded -> fast
    inv, err := inventoryService.Check(ctx, id)
    if err != nil { return err }
    return nil
}
```

## Budget Exhaustion Is a Fast Failure

When the system is saturated, failing fast on new work (429/503 at the edge, queue caps, load shedding) is the correct fast failure — it protects the workers already in flight. The art is signaling it loudly (with a clear status) instead of silently dropping or queueing forever.

## Practice: Design the Deadline Tree

A checkout spans gateway → auth, price, inventory, payments (4 parallel calls) and has a 3s total budget.

**Task 1:** Allocate sub-budgets so the total never exceeds 3s, including retries.

**Task 2:** Design the cancellation flow: one slow service must not delay the others.

**Task 3:** Define the fast-fail response when the budget is exhausted and how it differs from a silent drop.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why per-call timeouts without a shared deadline fail to bound end-to-end latency.

**Prompt 2 — Implementation Design:**
> Design a retry policy that respects the deadline: how many retries fit inside the remaining budget, and when is failing fast better than retrying?

**Prompt 3 — Boundary Testing:**
> A dependency returns a 503 that means "try later" versus "permanently down". Design the fast-fail distinction without two round trips.

## Key Takeaways

- Propagate deadlines, not independent timeouts
- Budget exhaustion should fail fast and loudly
- Cancellation must propagate to stop wasted work
- Retries must fit inside the remaining budget

## Further Reading

- [Google SRE — Handling Overload](https://sre.google/sre-book/handling-overload/)
- [gRPC Deadlines](https://grpc.io/docs/guides/deadlines/)
