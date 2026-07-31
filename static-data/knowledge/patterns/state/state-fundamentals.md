---
title: "State: Behavior That Changes with State"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the state pattern"
  - "Model states as classes"
  - "Delegate behavior to state"
  - "Simplify conditionals"
prerequisites:
  - "patterns/strategy"
  - "principles/single-responsibility"
knowledge_refs:
  - "patterns/state"
---

# State: Behavior That Changes with State

## The Problem

A network connection, an order, a document — each has states with different behavior for the same call. With if-chains, every method repeats the state checks and grows with every state and transition. The state pattern turns each state into an object; the context delegates to the current state object, which also owns its transitions.

```python
# State pattern: each state is an object owning behavior + transitions
class Order:
    def __init__(self):
        self.state = Draft(self)          # context holds current state
    def submit(self): self.state.submit()
    def cancel(self): self.state.cancel()

class Draft:                              # state 1
    def __init__(self, order): self.order = order
    def submit(self):
        print('draft -> submitted')
        self.order.state = Submitted(self.order)   # transition here
    def cancel(self):
        print('draft cancelled')
        self.order.state = Cancelled(self.order)

class Submitted:
    def __init__(self, order): self.order = order
    def submit(self):
        raise ValueError('already submitted')     # state forbids it
    def cancel(self):
        print('submitted -> cancelled')
        self.order.state = Cancelled(self.order)

class Cancelled:
    def __init__(self, order): self.order = order
    def submit(self): raise ValueError('cancelled orders are final')
    def cancel(self): raise ValueError('already cancelled')
```

## State vs Strategy

Strategy swaps algorithms (a sort policy) — the context picks the strategy and keeps it. State swaps behavior because the state itself changed — the context's state object transitions itself. Same structure, different driver: strategy is chosen, state is entered.

## Practice: Model the Order Lifecycle

An order moves draft -> submitted -> paid -> shipped, with guards on every transition.

**Task 1:** List the states, the legal transitions, and the forbidden calls.

**Task 2:** Implement the state classes and the context delegate.

**Task 3:** Rewrite the old if-chain version and compare the growth curves.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why states should own their transitions. Start with a forbidden call.

**Prompt 2 — Compare & Contrast:**
> Compare state with strategy and with a state machine table. When does the table beat the classes?

**Prompt 3 — Boundary Testing:**
> A transition should be impossible but a buggy caller invokes it. Design the exception the state throws and the guard tests.

## Key Takeaways

- State objects own behavior and transitions
- The context delegates and holds the current state
- It replaces growing if-chains
- State is entered; strategy is chosen

## Further Reading

- [State — Refactoring Guru](https://refactoring.guru/design-patterns/state)
- [State Pattern — Wikipedia](https://en.wikipedia.org/wiki/State_pattern)
