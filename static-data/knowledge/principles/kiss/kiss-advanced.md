---
title: "Advanced KISS: Simplicity as a Design Discipline"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Apply the \"one way to do it\" discipline"
  - "Design minimal APIs and narrow contracts"
  - "Manage simplicity pressure under growth"
  - "Use simplicity reviews as a gate"
prerequisites:
  []
knowledge_refs:
  - "principles/kiss"
---

# Advanced KISS: Simplicity as a Design Discipline

## One Way to Do It

The simplest codebases have one idiomatic way to do each thing: one way to fetch, one way to validate, one way to handle errors. Multiple parallel mechanisms (two HTTP clients, three logging styles, both sync and async paths where one suffices) multiply cognitive load and bug surface.

```text
Simplicity review questions per change:
  - Does this add a new mechanism? (or reuse an existing one)
  - Does this add a new concept? (or use a known one)
  - Could a reader explain this in 3 sentences?
  - What existing code becomes simpler because of this?
If a change simplifies nothing and complicates something, reject it.
```

## Saying No

Simplicity is defended by saying no: no to speculative parameters, no to premature abstractions, no to "while we are here" features. The discipline lives in review — a change that adds machinery without simplifying anything should go back.

Growth pressure is real; the answer is not "never generalize" but "generalize when the second concrete case appears, not before".

## Practice: Run a Simplicity Review

A PR adds a caching framework, a config DSL, and an abstraction layer to support a feature that works without them.

**Task 1:** Apply the review questions and list what the PR simplifies.

**Task 2:** Rewrite the feature with the existing mechanisms only.

**Task 3:** Write the review note that explains why the machinery was cut.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me how to say no to complexity without being obstructionist. Ask me to role-play the review conversation.

**Prompt 2 — Implementation Design:**
> Design the minimal API for a feature that will grow: which knobs are justified now, which are speculative?

**Prompt 3 — Boundary Testing:**
> The team wants "one way to do it" but a legitimate second way exists (sync and async paths). Design the rule for when a second way is allowed.

## Key Takeaways

- One idiomatic way per concern keeps codebases navigable
- Simplicity reviews gate complexity at the PR level
- Saying no protects future readers
- Generalize on the second concrete case, not before

## Further Reading

- [Minimalism in Software Design](https://www.infoq.com/presentations/simple-made-easy/)
- [The Art of Code — Yegor Bugayenko](https://www.yegor256.com/elegant-objects.html)
