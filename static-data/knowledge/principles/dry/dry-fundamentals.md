---
title: "DRY: Every Piece of Knowledge, Once"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Define DRY as knowledge duplication, not code duplication"
  - "Identify duplicated knowledge (rules, logic, formats)"
  - "Distinguish DRY from premature abstraction"
  - "Refactor a repeated rule into one source of truth"
prerequisites:
  - "principles/kiss"
  - "principles/single-responsibility"
knowledge_refs:
  - "principles/dry"
---

# DRY: Every Piece of Knowledge, Once

## Code vs Knowledge

DRY is not "never copy-paste". It is: every piece of knowledge must have a single, unambiguous, authoritative representation. The same validation rule written in four places is four copies of knowledge — fixing it means fixing four files, and one will be forgotten.

Two blocks that merely look similar but encode different rules are not duplicates. Forcing them together creates a coupling that is worse than the repetition.

```python
# Duplicated knowledge: the discount rule exists twice
def cart_total(items):
    return sum(i.price * (0.9 if i.kind == 'bulk' else 1.0) for i in items)

def cart_total_for_report(items):
    # copy of the same rule, already diverging (0.85 here!)
    return sum(i.price * (0.85 if i.kind == 'bulk' else 1.0) for i in items)

# DRY: one authoritative rule
def bulk_discount(kind): return 0.9 if kind == 'bulk' else 1.0
def cart_total(items):   return sum(i.price * bulk_discount(i.kind) for i in items)
def report_total(items): return cart_total(items)  # reuses the rule
```

## When to Extract

Extract when a rule has multiple call sites and one source of truth matters (business rules, formats, identifiers). Do not extract two random similar snippets — that creates the "Shotgun Surgery" anti-pattern in reverse: change the abstraction, update everything.

The classic heuristic: wait for the third occurrence before generalizing; the first two reveal whether the shapes actually converge.

## Practice: Find the Duplicated Rule

In your codebase, an email-address validation regex appears in signup, invite, and billing.

**Task 1:** Locate every occurrence and check whether they have already drifted apart.

**Task 2:** Extract a single validateEmail() used everywhere, with tests.

**Task 3:** Find one "similar but different" pair and explain why merging them would be wrong.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about the difference between duplicated code and duplicated knowledge. Start with two same-shaped functions with different rules.

**Prompt 2 — Compare & Contrast:**
> Compare DRY with the "rule of three" and with premature abstraction. Where does each guide you differently?

**Prompt 3 — Boundary Testing:**
> A shared function is now used by 12 call sites, but two of them need slightly different behavior. Design the escape hatch that does not fork the knowledge.

## Key Takeaways

- DRY targets knowledge, not code
- Duplicated rules drift apart silently
- Similar shapes with different rules are not duplicates
- Rule of three: extract when shapes prove they converge

## Further Reading

- [The Pragmatic Programmer (DRY chapter)](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/)
- [DRY vs WET — Martin Fowler](https://martinfowler.com/bliki/DryPrinciple.html)
