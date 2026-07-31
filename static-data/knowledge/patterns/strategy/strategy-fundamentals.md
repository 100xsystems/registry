---
title: "Strategy: Swap Algorithms at Runtime"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the strategy intent"
  - "Define a family of algorithms"
  - "Compose instead of inherit"
  - "Swap strategies at runtime"
prerequisites:
  - "patterns/factory"
  - "principles/open-closed"
knowledge_refs:
  - "patterns/strategy"
---

# Strategy: Swap Algorithms at Runtime

## The Problem

A class that computes in one way (a formatter, a pricing rule, a sort) hard-codes that algorithm. Every new algorithm means editing the class, growing an if-chain, and risking regressions. Strategy extracts each algorithm into its own object with a common interface; the context holds whichever strategy it needs and can swap it at runtime.

```python
# Strategy: algorithms as interchangeable objects
from abc import ABC, abstractmethod

class Pricing(ABC):                 # the strategy interface
    @abstractmethod
    def price(self, base: float) -> float: ...

class StandardPricing(Pricing):
    def price(self, base): return base

class MemberPricing(Pricing):
    def price(self, base): return base * 0.85

class PremiumPricing(Pricing):
    def price(self, base): return base * 0.7

class Cart:
    def __init__(self, strategy: Pricing):
        self.strategy = strategy    # context holds the strategy
    def set_strategy(self, s: Pricing):
        self.strategy = s           # swap at runtime
    def total(self, base): return self.strategy.price(base)

cart = Cart(MemberPricing())
print(cart.total(100))              # 85.0
cart.set_strategy(PremiumPricing()) # swap: no if-chains
print(cart.total(100))              # 70.0
```

## Composition over Inheritance

Strategy is composition: the context has a strategy rather than being one. New algorithms extend the family without touching the context — the open-closed principle in action. The cost is indirection: one more object per algorithm, and callers must know which strategy fits.

## Practice: Build the Formatter Family

An exporter formats orders as JSON, XML, or CSV; the format is chosen per request.

**Task 1:** Define the Formatter interface and three strategies.

**Task 2:** Wire the context to accept and swap strategies.

**Task 3:** Add a fourth format without touching the context.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why strategies beat if-chains. Start with adding a new format.

**Prompt 2 — Compare & Contrast:**
> Compare strategy with the template method: composition vs inheritance for algorithm families.

**Prompt 3 — Boundary Testing:**
> A strategy throws mid-use. Design the fallback strategy and the error path.

## Key Takeaways

- Strategy makes algorithms interchangeable objects
- The context composes, not inherits
- Runtime swapping removes if-chains
- New algorithms extend without editing the context

## Further Reading

- [Strategy — Refactoring Guru](https://refactoring.guru/design-patterns/strategy)
- [Strategy pattern — Wikipedia](https://en.wikipedia.org/wiki/Strategy_pattern)
