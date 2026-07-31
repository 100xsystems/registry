---
title: "Builder: Construct Complex Objects Step by Step"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the builder intent"
  - "Use fluent builders for many-parameter objects"
  - "Enforce valid intermediate states"
  - "Compare with constructors and factories"
prerequisites:
  - "patterns/factory"
  - "patterns/abstract-factory"
knowledge_refs:
  - "patterns/builder"
---

# Builder: Construct Complex Objects Step by Step

## The Problem: Telescoping Constructors

An object with 10 optional parameters needs either a constructor with 10 arguments (unreadable, easy to mix up) or a constellation of overloads. The builder constructs the object step by step, naming each setting, and produces the finished product at build() time.

```java
// Builder: fluent, named, validated construction
public class Request {
    public static class Builder {
        private String method = "GET";
        private String url;
        private Map<String, String> headers = new HashMap<>();
        private byte[] body;

        public Builder url(String u) { this.url = u; return this; }
        public Builder method(String m) { this.method = m; return this; }
        public Builder header(String k, String v) { headers.put(k, v); return this; }
        public Builder body(byte[] b) { this.body = b; return this; }

        public Request build() {
            if (url == null) throw new IllegalStateException("url required");
            return new Request(method, url, headers, body);
        }
    }
}

Request r = new Request.Builder()
    .url("https://api.example.com/orders")
    .method("POST")
    .header("Authorization", token)
    .body(json)
    .build();
```

## Validation at Build Time

The builder enforces invariants at build(): required fields present, combinations valid. Intermediate states (half-configured) cannot escape because the object is immutable once built.

## Practice: Build the Query Object

A search query has 8 optional filters; call sites currently pass 8-positional-argument constructors.

**Task 1:** Design the builder with fluent setters and build-time validation.

**Task 2:** Enforce one invalid combination at build() (e.g., limit without sort).

**Task 3:** Make the built object immutable and show two call sites.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about when a builder beats a well-named constructor. Start with parameter count.

**Prompt 2 — Compare & Contrast:**
> Compare builder with factory and with named parameters (Python kwargs). When is each simpler?

**Prompt 3 — Boundary Testing:**
> A builder method can be called twice with conflicting values. Design the "last wins" or "reject" policy.

## Key Takeaways

- Builders name each step of complex construction
- Build-time validation catches bad combos early
- Built objects stay immutable
- Use them when constructors get unreadable

## Further Reading

- [Builder — Refactoring Guru](https://refactoring.guru/design-patterns/builder)
- [Builder Pattern — Wikipedia](https://en.wikipedia.org/wiki/Builder_pattern)
