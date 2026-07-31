---
title: "SOLID: The Five Principles of Maintainable Design"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "List the five SOLID principles"
  - "Explain what each principle protects"
  - "Recognize violations in code"
  - "Apply the principles together coherently"
prerequisites:
  - "principles/single-responsibility"
  - "principles/open-closed"
  - "principles/liskov-substitution"
  - "principles/interface-segregation"
  - "principles/dependency-inversion"
knowledge_refs:
  - "principles/solid"
---

# SOLID: The Five Principles of Maintainable Design

## The Five

SOLID is five principles that together produce code that tolerates change: Single Responsibility (one reason to change), Open-Closed (extend without modifying), Liskov Substitution (subtypes honor contracts), Interface Segregation (small role interfaces), and Dependency Inversion (depend on abstractions).

They are not a checklist — they are one coherent stance: small surfaces, clear contracts, and dependency arrows that point at abstractions so the system can evolve without rippling.

```text
SOLID in one line each:
  S - One reason to change per class
  O - Extend via new code, not edits to tested code
  L - Subtypes keep their promises
  I - Clients depend only on interfaces they use
  D - Depend on abstractions, not details

Together: a design where change is local, cheap, and safe.
```

## The Payoff

Each principle removes a specific class of pain: SRP removes change-conflict, OCP removes regression risk, LSP removes surprise behavior, ISP removes coupling, DIP removes direction entanglement. A system that respects them changes in small, reviewable, low-risk steps.

## Practice: Assess a Class Against SOLID

A 300-line PaymentProcessor that parses, validates, charges, emails, and logs, with a fat interface and concrete dependencies.

**Task 1:** Score it against each of the five principles, with the violation named.

**Task 2:** Refactor the two worst violations (likely S and D).

**Task 3:** Explain how fixing one violation makes the others easier.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about how the five principles reinforce each other. Start with S and D.

**Prompt 2 — Compare & Contrast:**
> Compare SOLID with GRASP and with composition-over-inheritance. Where do they converge?

**Prompt 3 — Boundary Testing:**
> A codebase applies SOLID everywhere and ends up with hundreds of tiny classes. Design the judgment that keeps SOLID from over-fragmenting.

## Key Takeaways

- SOLID is one stance: small surfaces, clear contracts
- Each principle removes a specific class of pain
- The principles reinforce each other
- Balance SOLID against simplicity — do not fragment for its own sake

## Further Reading

- [The SOLID Principles — Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html)
- [SOLID — Wikipedia](https://en.wikipedia.org/wiki/SOLID)
