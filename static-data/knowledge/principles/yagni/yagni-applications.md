---
title: "YAGNI in Production: Features and Architectures"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Challenge speculative feature requests"
  - "Defer framework adoption with triggers"
  - "Apply YAGNI to architecture choices"
  - "Communicate YAGNI without being obstructive"
prerequisites:
  []
knowledge_refs:
  - "principles/yagni"
---

# YAGNI in Production: Features and Architectures

## Feature Requests

Product requests often arrive with future-proofing: "build it generically so we can add X later". The YAGNI response: build the current requirement cleanly, and design the seams that make X cheap to add later — without building X.

```text
YAGNI conversation script:
  "We should add X now because we will need it later."
  -> "What is the concrete trigger for X?"
  -> "What is the cheapest seam to add X when the trigger hits?"
  -> "Let us build the seam now and X at the trigger."
Seams = interfaces and structure that keep X cheap; X = deferred.
```

## Framework and Architecture Decisions

Frameworks are the biggest YAGNI temptation: adopting an orchestration platform "because we will need it" adds operational weight today for a problem that may never arrive. Defer with a trigger: adopt the framework when the problem it solves actually appears.

## Practice: Deflect with a Trigger

A team proposes an event-sourcing framework for a service that stores a list of settings.

**Task 1:** State the concrete trigger that would justify event sourcing.

**Task 2:** Design the cheapest seam now (audit log, plain storage) that keeps the future option open.

**Task 3:** Write the deferral decision in one paragraph, including the trigger and the review date.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me how to say "not yet" to a framework without being dismissed as lazy. Ask me to role-play the discussion.

**Prompt 2 — Implementation Design:**
> Design the seams for a feature that will likely grow: which structure today makes growth cheap without building the growth?

**Prompt 3 — Boundary Testing:**
> The trigger fires: a real second variant appears. Design the transition from the simple version to the generalized one without a rewrite.

## Key Takeaways

- Build the seam, defer the speculation
- Frameworks are adopted on triggers, not predictions
- The trigger must be concrete and reviewable
- YAGNI conversations need a deferral script, not a veto

## Further Reading

- [The YAGNI Trap in Architecture — ThoughtWorks](https://www.thoughtworks.com/insights/blog)
- [Deferring Decisions — ADR pattern](https://adr.github.io/)
