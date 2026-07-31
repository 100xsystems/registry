---
title: "Strategy in Production: Pricing, Routing, and Policy Engines"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Select strategies by config"
  - "Register strategies in a registry"
  - "Combine strategies"
  - "Test strategy swaps"
prerequisites:
  []
knowledge_refs:
  - "patterns/strategy"
---

# Strategy in Production: Pricing, Routing, and Policy Engines

## Config-Driven Selection

Production systems select the strategy from configuration: a pricing tier, a routing rule, a policy name. A registry maps names to strategy instances, so adding a strategy is data plus one class — no call-site edits. The selection point (config, header, user attribute) decides which strategy the context composes.

```typescript
// Strategy registry: select by name from config
type Routing = (req: Req) => string;

const strategies: Record<string, Routing> = {
  roundRobin: (r) => pick(pool),
  leastConn:   (r) => leastBusy(pool),
  ipHash:      (r) => pool[hash(r.ip) % pool.length],
};

export function route(req: Req, name: string): string {
  const fn = strategies[name] ?? strategies.roundRobin; // fallback
  return fn(req);
}
// New strategy = one entry in the map. Callers never change.
// Config: route_strategy: leastConn flips behavior without a
// deploy of the routing code — the definition of open/closed.
```

## Composed Strategies

Strategies compose: a checkout applies member discount, then loyalty points, then tax — a pipeline of strategies, or a composite strategy that runs a list. The composite is itself a strategy, so the pattern nests cleanly. Testing swaps a strategy for a fake and asserts the context behavior changed.

## Practice: Design the Policy Registry

A gateway routes by header, IP, or weight; operators change the policy via config with zero deploys.

**Task 1:** Define the strategy interface and three implementations.

**Task 2:** Build the registry and the config-driven selection.

**Task 3:** Add the fallback and the test that swaps strategies.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why a registry turns strategy selection into configuration.

**Prompt 2 — Implementation Design:**
> Design a pricing engine: tiers, coupons, and taxes as composable strategies. How do they combine?

**Prompt 3 — Boundary Testing:**
> A config names a strategy that does not exist. Design the validation and the fallback.

## Key Takeaways

- Registries make strategy selection configurable
- New strategies are data plus one class
- Strategies compose into pipelines
- Tests swap strategies to assert behavior change

## Further Reading

- [Strategy — Refactoring Guru](https://refactoring.guru/design-patterns/strategy)
- [Policy engines — OPA](https://www.openpolicyagent.org/docs/latest/)
