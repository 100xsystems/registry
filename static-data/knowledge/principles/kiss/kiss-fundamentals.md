---
title: "KISS: Keep It Simple, Stupid"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Define the KISS principle"
  - "Recognize complexity that buys nothing"
  - "Simplify a convoluted solution"
  - "Explain the maintenance cost of complexity"
prerequisites:
  - "principles/yagni"
  - "principles/dry"
knowledge_refs:
  - "principles/kiss"
---

# KISS: Keep It Simple, Stupid

## The Principle

KISS says the simplest solution that meets the requirement is the best one. Simplicity means fewer moving parts, fewer branches, fewer abstractions, fewer failure modes. Every line of complexity is code that can break, must be tested, and will be read by someone else.

Complexity is a tax: it is paid at review time, test time, debugging time, onboarding time, and refactor time. The simplest design minimizes the total tax, not just today's code.

```python
# Convoluted: over-abstracted for a single use
class DiscountEngine:
    def __init__(self, strategy, config_loader, cache):
        ...
    def apply(self, order):
        return self.strategy(order, self.config_loader.load(), self.cache.get())

# Simple: a function
def total_with_discount(order):
    return order.total - (order.total * 0.1 if order.coupon else 0)
```

## Simple vs Simplistic

Simple is not the same as simplistic. KISS does not mean ignoring requirements — it means meeting them with the least machinery. A simple solution handles the real requirements directly; a simplistic one ignores them and fails in production.

## Practice: Simplify a Feature

A search filter feature was built with a rule engine, plugin registry, and caching layer — for three filter types.

**Task 1:** List the machinery and what each piece actually buys for three filter types.

**Task 2:** Rewrite it with the minimal structure that still supports the three filters.

**Task 3:** Decide at what point (how many filter types) the rule engine becomes justified.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about the difference between "simple for the author now" and "simple for every future reader". Start with an over-engineered example.

**Prompt 2 — Compare & Contrast:**
> Compare KISS with YAGNI and DRY. When do they agree, and when does DRY tempt you into complexity KISS would avoid?

**Prompt 3 — Boundary Testing:**
> A simple solution needs to grow. Design the decision rule for when to generalize and how to do it without a rewrite.

## Key Takeaways

- Complexity is a recurring tax, not a one-time cost
- The simplest solution that meets requirements wins
- Simple is not simplistic — requirements still count
- Generalize only when the pattern has proven itself

## Further Reading

- [KISS Principle — Wikipedia](https://en.wikipedia.org/wiki/KISS_principle)
- [Simple Made Easy — Rich Hickey](https://www.infoq.com/presentations/Simple-Made-Easy/)
