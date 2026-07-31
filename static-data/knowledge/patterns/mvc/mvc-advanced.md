---
title: "Advanced MVC: Unidirectional Flow and State Management"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Explain the observer tangle"
  - "Design unidirectional data flow"
  - "Manage global state"
  - "Handle side effects"
prerequisites:
  []
knowledge_refs:
  - "patterns/mvc"
---

# Advanced MVC: Unidirectional Flow and State Management

## Why Classic MVC Tangles

As apps grow, views mutate models, models notify views, and views call other views — the observer graph becomes untraceable. Unidirectional data flow (Redux, Flux) fixes this: one store holds state, actions describe intent, reducers produce new state, and views re-render from the store. One way, always.

```typescript
// Unidirectional flow: action -> reducer -> store -> view
type State = { count: number };
type Action = { type: 'INCREMENT' } | { type: 'SET'; value: number };

function reducer(state: State, action: Action): State {
    switch (action.type) {
        case 'INCREMENT': return { ...state, count: state.count + 1 };
        case 'SET': return { ...state, count: action.value };
    }
}
// The view dispatches actions and reads the store.
// It never mutates state directly; time travel = replay actions.
```

## Side Effects and Testing

Reducers must be pure, so side effects (API calls, timers) live in middleware or effects — outside the state transition. That purity is the payoff: every state change is a pure function of the previous state and an action, which makes the app testable and the history replayable.

## Practice: Convert to Unidirectional

A settings screen with 12 widgets mutates models directly and bugs are untraceable.

**Task 1:** Define the state shape and the action set.

**Task 2:** Convert widgets to dispatch actions and read the store.

**Task 3:** Move the API call to an effect and test the reducer in isolation.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why unidirectional flow kills the observer tangle.

**Prompt 2 — Implementation Design:**
> Design a global store for a shopping app: state shape, action set, and the effect layer for payments.

**Prompt 3 — Boundary Testing:**
> A reducer is called twice (React StrictMode) and must be pure. Find the impure pattern in a sample reducer and fix it.

## Key Takeaways

- Classic MVC tangles as views mutate models
- Unidirectional flow makes state transitions pure
- Side effects move to middleware
- Pure reducers enable time travel and tests

## Further Reading

- [Redux — core concepts](https://redux.js.org/introduction/core-concepts)
- [The Evolution of Flux Frameworks — M. Fowler](https://martinfowler.com/articles/evolving-flux.html)
