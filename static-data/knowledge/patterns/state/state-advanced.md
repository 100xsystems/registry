---
title: "Advanced State: Hierarchical and Concurrent States"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Model hierarchical states"
  - "Run parallel regions"
  - "Design statecharts"
  - "Handle complex workflows"
prerequisites:
  []
knowledge_refs:
  - "patterns/state"
---

# Advanced State: Hierarchical and Concurrent States

## Statecharts

Flat state machines explode with real workflows: nested substates (a connection's connecting/connected/retrying), parallel regions (an order being paid while being shipped), and history states. Statecharts add these — hierarchical states, orthogonal regions, and actions — which is why XState implements them.

```typescript
// Statechart: nested + parallel regions
const machine = createMachine({
  id: 'checkout',
  initial: 'cart',
  states: {
    cart: { on: { CHECKOUT: 'processing' } },
    processing: {
      initial: 'payment',
      states: {                    // sequential substates
        payment: { on: { PAID: 'fulfillment' } },
        fulfillment: { on: { DONE: '#checkout.complete' } },
      },
    },
    complete: { type: 'final' },
  },
});
// Parallel regions (orthogonal): payment and inventory checks run
// independently; the machine only completes when BOTH regions do.
// History: a retry returns to the substate it left, not to the
// top of the parent. Statecharts make these explicit.
```

## Complexity

Statecharts scale to real workflows — but the lesson is the same as always: states, transitions, and guards belong in one explicit model, not scattered conditionals. When a flow grows, formalize it; when it shrinks, delete the formalism.

## Practice: Formalize the Deployment

A deploy flow: build (with retry substates) while config is verified (parallel), then release.

**Task 1:** Model the nested states and the parallel regions.

**Task 2:** Implement the statechart and walk its transition graph.

**Task 3:** Add the history state and the retry substate.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why flat machines explode and statecharts compress them.

**Prompt 2 — Implementation Design:**
> Design a statechart for a CI pipeline: build, test (parallel jobs), deploy (with rollback states). What are the regions?

**Prompt 3 — Boundary Testing:**
> Two parallel regions must both finish before the parent proceeds. Design the completion guard and the timeout.

## Key Takeaways

- Statecharts add hierarchy, parallelism, and history
- Nested substates replace state explosion
- Orthogonal regions model independent work
- Explicit models beat scattered conditionals

## Further Reading

- [The World of Statecharts — Harel](https://statecharts.dev/)
- [XState — statechart concepts](https://stately.ai/docs/statecharts-overview)
