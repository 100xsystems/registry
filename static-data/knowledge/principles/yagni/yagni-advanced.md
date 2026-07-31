---
title: "Advanced YAGNI: Options Thinking and Seams"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Apply options thinking to design"
  - "Build cheap seams that keep options open"
  - "Distinguish seam from speculation"
  - "Measure the cost of carrying options"
prerequisites:
  []
knowledge_refs:
  - "principles/yagni"
---

# Advanced YAGNI: Options Thinking and Seams

## Options, Not Futures

Financial options cost a premium and expire. Design options are the same: a cheap seam (interface, boundary, config point) that keeps a future choice open costs a little today and is worth it only if the option is plausibly exercised and cheap to keep. Every seam is also maintenance — count its premium.

```text
Options thinking checklist for a seam:
  1. What future choice does this seam keep open?
  2. How much does the seam cost to maintain today?
  3. How plausible is the future? (evidence, not vibes)
  4. Can the seam be added later for about the same cost?
If the seam is cheap, plausible, and hard to add later -> keep it.
Otherwise -> it is speculation, not an option.
```

## The Cost of Carrying

Every carried option is reviewed, tested, and explained forever. The discipline is to price the premium honestly: a seam that costs more than the future it hedges is a liability. Revisit carried options on a schedule and cut the ones whose trigger keeps failing to fire.

## Practice: Price the Options

A service carries a plugin registry, a config DSL, and an abstraction layer — all for "future flexibility".

**Task 1:** Price each: maintenance cost today, plausibility, and cost-to-add-later.

**Task 2:** Cut the ones that fail the checklist; keep the cheap, plausible ones.

**Task 3:** Set the review date for the kept options and the trigger for each.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can articulate the difference between an option (priced, cheap, expiring) and speculation (free in imagination, expensive forever).

**Prompt 2 — Implementation Design:**
> Design the cheapest seam that keeps a future multi-region option open, without building any multi-region machinery.

**Prompt 3 — Boundary Testing:**
> A kept option is now used by one consumer and has drifted from the codebase. Design the decision: migrate it in, or cut it?

## Key Takeaways

- Options cost a premium; price it honestly
- A cheap seam is an option; an expensive one is speculation
- Carried options need triggers and review dates
- Cut options whose triggers keep failing to fire

## Further Reading

- [Options Thinking in Software — Martin Fowler](https://martinfowler.com/bliki/OptionThinking.html)
- [YAGNI and the Economics of Software](https://www.martinfowler.com/articles/is-quality-worth-cost.html)
