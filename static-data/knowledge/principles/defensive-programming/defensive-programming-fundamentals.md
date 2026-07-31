---
title: "Defensive Programming: Code That Survives the Unexpected"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the defensive mindset"
  - "Validate inputs at trust boundaries"
  - "Use assertions to catch programmer errors"
  - "Fail loudly instead of corrupting state"
prerequisites:
  - "principles/fail-fast"
  - "principles/kiss"
knowledge_refs:
  - "principles/defensive-programming"
---

# Defensive Programming: Code That Survives the Unexpected

## Trust Nothing

Defensive programming assumes inputs are hostile or broken until proven otherwise. Every boundary — API, file, network, user input — validates before use. Garbage in must produce a clear error, not a corrupt state.

It is not paranoia: production bugs overwhelmingly come from unvalidated inputs meeting unwritten assumptions.

```python
# Validate at the boundary, then trust internally
def transfer(sender, recipient, amount):
    if not isinstance(sender, str) or not sender.strip():
        raise ValueError('sender must be a non-empty string')
    if amount is None or amount <= 0:
        raise ValueError('amount must be positive')
    if amount > balance(sender):
        raise InsufficientFunds(sender)
    return execute(sender, recipient, amount)
```

## Fail Loudly

A silent failure (log-and-continue with wrong data) is a time bomb. Fail loudly: raise, crash, or surface the error prominently. The worst outcome is a system that looks healthy while doing the wrong thing.

## Practice: Harden an Endpoint

POST /users accepts JSON. Malformed bodies, negative ages, and huge payloads currently flow through.

**Task 1:** List every validation the boundary needs (schema, ranges, sizes, types).

**Task 2:** Define the error responses (4xx with specific codes) for each violation.

**Task 3:** Decide where you fail fast versus sanitize (e.g., trim whitespace) and justify each.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about the difference between defensive checks and over-engineering. Start with the trust boundary concept.

**Prompt 2 — Compare & Contrast:**
> Contrast "fail fast" with "be liberal in what you accept". When is each correct, and how do they conflict in APIs?

**Prompt 3 — Boundary Testing:**
> A parser receives a 10MB JSON with 100k keys. Design the size/depth limits and their error paths.

## Key Takeaways

- Validate at every trust boundary
- Garbage in must produce clear errors, not corruption
- Silent failures are the most dangerous bugs
- Assert programmer assumptions; validate user input

## Further Reading

- [Defensive Programming — Wikipedia](https://en.wikipedia.org/wiki/Defensive_programming)
- [Robustness Principle — RFC](https://www.rfc-editor.org/rfc/rfc1122#page-18)
