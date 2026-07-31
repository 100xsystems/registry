---
title: "Facade: One Simple Door to a Complex System"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the facade intent"
  - "Simplify a complex subsystem"
  - "Keep the subsystem untouched"
  - "Distinguish from adapter"
prerequisites:
  - "patterns/adapter"
  - "patterns/singleton"
knowledge_refs:
  - "patterns/facade"
---

# Facade: One Simple Door to a Complex System

## The Idea

A subsystem has many moving parts: an order flow touches inventory, billing, shipping, and notifications. A facade offers one simple method — placeOrder() — that coordinates them. Callers see one door; the subsystem stays intact behind it.

```java
// Facade: one simple API over a complex subsystem
class OrderFacade {
    private final Inventory inv;
    private final Billing billing;
    private final Shipping ship;

    OrderFacade(Inventory i, Billing b, Shipping s) { ... }

    public OrderResult placeOrder(Cart cart, Payment pmt) {
        if (!inv.reserve(cart)) return OrderResult.outOfStock();
        ChargeResult ch = billing.charge(pmt, cart.total());
        if (!ch.ok) { inv.release(cart); return OrderResult.chargeFailed(); }
        String tracking = ship.schedule(cart);
        return OrderResult.ok(tracking);
    }
}
// Callers never touch inventory, billing, or shipping.
```

## Facade vs Adapter

An adapter translates an interface so two things can talk. A facade simplifies a subsystem for its callers — the intent is convenience and decoupling, not interface compatibility.

## Practice: Facade the Checkout

Checkout currently calls 5 subsystems in sequence with error handling at the call site.

**Task 1:** Identify the 5 subsystems and their interactions.

**Task 2:** Design the facade method with its result type and error paths.

**Task 3:** Move the orchestration into the facade and show callers simplify.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why a facade reduces caller coupling without hiding capability. Start with the result type.

**Prompt 2 — Compare & Contrast:**
> Compare facade with adapter and with the mediator pattern. When is each the right simplification?

**Prompt 3 — Boundary Testing:**
> A caller legitimately needs a subsystem detail the facade hides. Design the escape hatch that does not defeat the facade.

## Key Takeaways

- Facades simplify complex subsystems
- The subsystem stays intact behind the door
- Callers decouple from subsystem internals
- Facade simplifies; adapter translates; mediator coordinates peers

## Further Reading

- [Facade — Refactoring Guru](https://refactoring.guru/design-patterns/facade)
- [Facade Pattern — Wikipedia](https://en.wikipedia.org/wiki/Facade_pattern)
