---
title: "Advanced Strategy: Functional Strategies and Dynamic Selection"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Use functional strategies"
  - "Capture state in closures"
  - "Select strategies dynamically"
  - "Avoid strategy explosion"
prerequisites:
  []
knowledge_refs:
  - "patterns/strategy"
---

# Advanced Strategy: Functional Strategies and Dynamic Selection

## Functional Strategies

Where the strategy has no state of its own, a function is the strategy — the interface is a signature, the implementations are lambdas. Closures capture per-request state (a user tier, a region) without a class per combination. This collapses dozens of classes into a handful of functions and keeps the registry tiny.

```python
# Functional strategies: the interface is a signature
from typing import Callable

Pricing = Callable[[float, float], float]   # (base, factor) -> price

def make_tier_price(tier: str) -> Pricing:   # closure captures state
    rates = {'standard': 1.0, 'member': 0.85, 'premium': 0.7}
    return lambda base, factor: base * rates[tier] * factor

prices: dict[str, Pricing] = {
    'standard': make_tier_price('standard'),
    'member':   make_tier_price('member'),
    'premium':  make_tier_price('premium'),
}
total = prices['premium'](100, 1.2)          # 84.0
# Dynamic selection: the tier comes from the user, ML scoring,
# or A/B flags at call time — the call site never changes.
```

## Dynamic Selection and Limits

Selection can be dynamic — a scorer picks the strategy per request (A/B, ML, load). The discipline: the strategy family must stay small and the selection point explicit. Strategy explosion (a class per combination) is the smell; composition and functions compress it.

## Practice: Functionalize the Family

Twelve pricing strategy classes for region x tier combinations. Collapse them.

**Task 1:** Identify the orthogonal axes (tier, region, promotion).

**Task 2:** Rebuild as closures composing the axes.

**Task 3:** Add a dynamic selector (A/B flag) without new classes.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain when a function beats a class as a strategy.

**Prompt 2 — Implementation Design:**
> Design a routing family with an ML scorer selecting the strategy per request. How do you keep it testable?

**Prompt 3 — Boundary Testing:**
> The dynamic selector oscillates between strategies. Design the hysteresis and the logging that catches it.

## Key Takeaways

- Functions are stateless strategies
- Closures capture state without class explosion
- Dynamic selection keeps call sites stable
- Small families and explicit selection avoid the smell

## Further Reading

- [Strategy — Refactoring Guru](https://refactoring.guru/design-patterns/strategy)
- [Partial application and closures — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
