---
title: "Fail Fast: Surface Errors Immediately"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Define fail-fast and fail-loud"
  - "Validate inputs at the boundary"
  - "Use assertions for programmer assumptions"
  - "Explain the cost of deferred failures"
prerequisites:
  - "principles/defensive-programming"
  - "principles/kiss"
knowledge_refs:
  - "principles/fail-fast"
---

# Fail Fast: Surface Errors Immediately

## The Principle

Fail fast means invalid states, bad inputs, and violated assumptions are detected at the earliest possible moment and surfaced loudly — not swallowed, logged, or deferred. A failure found now costs seconds; the same failure found in production costs an incident.

The opposite is fail-late-and-silently: an invalid order ID stored as 0, a null name defaulted to "unknown", a retry loop that hides a permanent error. Each one delays the signal until the damage compounds.

```python
# Fail fast: reject invalid input at the boundary
def create_order(user_id, items):
    if not user_id:                raise ValueError('user_id required')
    if not items:                  raise ValueError('order needs items')
    if any(i.qty <= 0 for i in items): raise ValueError('qty must be positive')
    return order_store.create(user_id, items)

# Anti-pattern: sanitize silently
def create_order(user_id, items):
    user_id = user_id or 'unknown'        # hides the bug
    items = [i for i in items if i.qty > 0]  # drops data silently
    return order_store.create(user_id, items)
```

## Fail Fast vs Defensive

Fail-fast and defensive programming overlap but differ in emphasis: defensive programming assumes inputs are hostile and guards broadly; fail-fast emphasizes the speed and loudness of the signal. Both agree that silent acceptance is the enemy.

## Practice: Audit a Silent-Failure Path

A report generator catches all exceptions, logs "error", and returns an empty report.

**Task 1:** List every place a failure is silently swallowed and what it hides.

**Task 2:** Redesign: which failures should propagate, which should surface to the user, and which legitimately degrade?

**Task 3:** Add monitoring that alerts on each loud failure with context.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why deferred failure is more expensive than immediate failure. Start with the debugging distance.

**Prompt 2 — Compare & Contrast:**
> Contrast fail-fast with graceful degradation. When is degradation the right choice, and how do you keep it from becoming silent failure?

**Prompt 3 — Boundary Testing:**
> A fail-fast assertion in a hot library crashes a production service over a benign input. Where is the right boundary between fail-fast and validate-with-fallback?

## Key Takeaways

- Surface failures at the earliest, loudest moment
- Silent sanitization hides the bug and delays the signal
- Fail-fast and graceful degradation must be explicitly distinguished
- Alerting makes loud failures actually visible

## Further Reading

- [Fail Fast — Martin Fowler](https://martinfowler.com/ieeeSoftware/failFast.pdf)
- [Fail Fast Principle — Wikipedia](https://en.wikipedia.org/wiki/Fail-fast)
