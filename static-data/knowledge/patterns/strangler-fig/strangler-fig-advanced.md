---
title: "Advanced Strangler: Parallel Run and Shadow Traffic"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Run systems in parallel"
  - "Shadow traffic to compare"
  - "Automate cutover decisions"
  - "Manage feature toggles"
prerequisites:
  []
knowledge_refs:
  - "patterns/strangler-fig"
---

# Advanced Strangler: Parallel Run and Shadow Traffic

## Shadow Traffic

Before a cutover, duplicate production traffic to the new system (shadow mode) and compare outputs — responses, errors, side effects. The comparison is the evidence the migration is safe. Discrepancies are analyzed; when the discrepancy rate drops to zero, the cutover is a formality, not a gamble.

```go
// Shadow traffic: send a copy to the new system, compare
func (g *Gateway) Handle(w http.ResponseWriter, r *http.Request) {
    // primary: legacy (during migration) or new (after)
    res := g.primary.Handle(r)
    if g.shadowEnabled(r) {
        shadowRes := g.shadow.Handle(r)   // new system, ignored output
        go g.compare(r, res, shadowRes)   // diff in the background
    }
    write(w, res)                          // user sees the primary only
}
// compare() records: matched, mismatch, error-only-in-shadow.
// A week of zero mismatches = evidence the cutover is safe.
// Feature toggles flip routes per user/region without deploys.
```

## Automating the Cutover

With continuous comparison, cutover becomes a toggle flip gated by the discrepancy metric — the automation releases only when the shadow matches for the required window. Toggles give instant rollback. The discipline: every toggle has an owner, a review, and a deletion date.

## Practice: Gate the Cutover

A payment feature is 90% migrated; the last 10% must not regress on edge cases.

**Task 1:** Design the shadow pipeline and the comparison metric.

**Task 2:** Design the toggle and the gate: zero mismatches for 7 days.

**Task 3:** Design the rollback toggle and the discrepancy alert.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why shadow traffic turns cutover from a gamble into evidence.

**Prompt 2 — Implementation Design:**
> Design a shadow comparison for an idempotent payment API: what is compared, what is ignored, and how are mismatches triaged?

**Prompt 3 — Boundary Testing:**
> Shadow traffic itself causes side effects (double side effects from the shadow system). Design the dry-run mode that prevents them.

## Key Takeaways

- Shadow traffic duplicates production to compare
- Mismatch rates are the migration evidence
- Toggles make cutover and rollback instant
- Toggles need owners and deletion dates

## Further Reading

- [Parallel Change — Fowler](https://martinfowler.com/bliki/ParallelChange.html)
- [Dark launch / shadow traffic](https://martinfowler.com/articles/feature-toggles.html)
