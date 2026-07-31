---
title: "Advanced Builder: Immutability and Validation Pipelines"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Guarantee immutability of built products"
  - "Design staged builders (type-safe steps)"
  - "Chain validations through the builder"
  - "Measure builder overhead"
prerequisites:
  []
knowledge_refs:
  - "patterns/builder"
---

# Advanced Builder: Immutability and Validation Pipelines

## Staged Builders

A staged builder makes illegal states unrepresentable: the first stage returns a type that only exposes the next legal step. A request builder can enforce "url first, then method, then optional headers, then build" in the type system — the compiler rejects invalid orders.

```typescript
// Staged builder: type system enforces the order of steps
interface HasUrl { withMethod(m: string): HasMethod; }
interface HasMethod { withHeader(k: string, v: string): HasMethod; build(): Request; }

class RequestBuilder implements HasUrl, HasMethod {
    private url = "";
    private method = "GET";
    constructor() {}

    withUrl(u: string): HasMethod { this.url = u; return this; }
    withMethod(m: string): HasMethod { this.method = m; return this; }
    withHeader(k: string, v: string): HasMethod { return this; }
    build(): Request { return new Request(this.url, this.method); }
}

// new RequestBuilder().withMethod("POST").withUrl(u) // compile error: url first
```

## Validation Pipelines

The builder can carry a validation pipeline: each withX registers a check, and build() runs them all in order, collecting errors instead of failing on the first. This turns the builder into a form-validation engine with a single error-reporting surface.

## Practice: Design the Staged Builder

A payment request builder must enforce: amount first, currency second, then optional fields, then build.

**Task 1:** Design the staged types so the compiler enforces the order.

**Task 2:** Add a validation pipeline that collects all errors at build().

**Task 3:** Verify the built object is deeply immutable (no setters, defensive copies).

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain how staged builders make illegal states unrepresentable.

**Prompt 2 — Implementation Design:**
> Design a request-validator builder for an API gateway: stages for auth, body, params, with error aggregation.

**Prompt 3 — Boundary Testing:**
> A builder with 20 stages becomes unusable. Design the line between staged safety and pragmatic flexibility.

## Key Takeaways

- Staged builders encode legal orders in types
- Validation pipelines aggregate errors at build()
- Immutability is the contract of a built product
- Stages should not multiply past usefulness

## Further Reading

- [Typestate Pattern (staged builders)](https://en.wikipedia.org/wiki/Typestate)
- [Immutability in Java — Effective Java Item 17](https://www.oreilly.com/library/view/effective-java-3rd/9780134686097/)
