---
title: "Information Hiding: Keep Secrets from Callers"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Define information hiding"
  - "Distinguish interface from implementation"
  - "Explain why exposed internals create coupling"
  - "Apply private/encapsulation in code"
prerequisites:
  - "principles/separation-of-concerns"
  - "principles/single-responsibility"
knowledge_refs:
  - "principles/information-hiding"
---

# Information Hiding: Keep Secrets from Callers

## The Principle

Information hiding (David Parnas): every module hides a design decision behind an interface. Callers depend on the interface, never on the internals — so the internals can change freely without breaking callers.

The cost of leaking internals: callers read fields, subclass internals, and depend on ordering and format details. Every change to those internals ripples into every caller. The interface is the only contract, and it should stay small and stable.

```java
// Leaked internals: callers depend on the backing list
class ShoppingCart {
    public List<Item> items = new ArrayList<>();  // public field!
    public double total() { ... }
}
// Caller: cart.items.add(...)  -> can corrupt invariants, tied to ArrayList

// Hidden: the representation is an implementation detail
class ShoppingCart {
    private final Map<String, Item> bySku = new HashMap<>();
    public void add(Item item) { bySku.merge(item.sku(), item, Item::combine); }
    public double total() { return bySku.values().stream().mapToDouble(Item::price).sum(); }
}
```

## Interfaces Are Promises

A public field, a public type, a public method is a promise. The more of the module you expose, the more promises you must keep forever. Hiding information is how you keep the surface area small and the freedom to evolve large.

## Practice: Tighten the Surface

A DateRange class exposes start, end, and a public List<LocalDate> of every day in the range.

**Task 1:** Identify which exposures are implementation details (the day list) versus essential (start/end).

**Task 2:** Make the day list private and expose days() as a computed, unmodifiable view.

**Task 3:** Change the internal representation (e.g., store as interval) and show callers did not break.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why exposing the representation (list, map, array) is worse than exposing behavior.

**Prompt 2 — Compare & Contrast:**
> Compare information hiding with encapsulation and abstraction. Where do they overlap and differ?

**Prompt 3 — Boundary Testing:**
> A performance tool needs deep internals. Design the deliberate, narrow escape hatch that keeps the rest hidden.

## Key Takeaways

- Hide design decisions behind interfaces
- Exposed internals become promises you must keep
- Small, stable surfaces enable large internal change
- Narrow escape hatches beat broad exposure

## Further Reading

- [On the Criteria for Decomposing Systems (Parnas)](https://www.cs.umd.edu/class/spring2003/cmsc838p/Design/criteria.pdf)
- [Information Hiding — Wikipedia](https://en.wikipedia.org/wiki/Information_hiding)
