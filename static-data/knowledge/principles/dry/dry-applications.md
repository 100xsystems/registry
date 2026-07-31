---
title: "DRY in Production: Single Sources of Truth"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Apply DRY to configuration and schemas"
  - "Use generated clients to avoid duplicated contracts"
  - "Keep documentation close to the code it describes"
  - "Avoid over-abstraction that couples unrelated things"
prerequisites:
  []
knowledge_refs:
  - "principles/dry"
---

# DRY in Production: Single Sources of Truth

## Contracts and Generated Clients

An API contract written once (OpenAPI, protobuf, GraphQL schema) and generating clients for every language is DRY at the service boundary: the wire format has one authoritative definition, and consumers cannot drift.

```text
Single sources of truth in a platform:
  OpenAPI spec       -> generated clients (TS, Go, Java)
  protobuf .proto    -> typed messages + RPC stubs
  DB schema / migrations -> the only place the schema lives
  Feature flags      -> one registry, many consumers
Never: hand-written clients that mirror the spec.
```

## Config and Docs

Config duplicated across environments (dev/staging/prod values copy-pasted) drifts and causes "works on my machine" bugs. Keep one schema for config, with per-environment values in a single store.

Documentation that repeats the code (e.g., a README that restates function behavior) becomes wrong the moment the code changes. Keep docs at the level of why and how-to-use, generated from code where possible.

## Practice: Eliminate Contract Drift

Your frontend hand-writes API client types, and the backend hand-writes the OpenAPI spec. Field renames break builds only at runtime.

**Task 1:** Make the OpenAPI spec the single source and generate the TS client from it.

**Task 2:** Add a CI check that fails when the spec and the backend routes diverge.

**Task 3:** Document the workflow: how does a developer change a field end-to-end?

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why generated clients are DRY but generated code checked into repos can still drift. Ask me about regeneration workflows.

**Prompt 2 — Implementation Design:**
> Design a feature-flag pipeline where the flag schema, defaults, and rollout docs are one artifact. What generates what?

**Prompt 3 — Boundary Testing:**
> Two services legitimately need different shapes of the same data. Is that a DRY violation? Design the boundary between shared and owned models.

## Key Takeaways

- Contracts should have one authoritative definition
- Generated clients prevent consumer drift
- Config and docs drift the same way code does
- Owning different shapes of shared data is legitimate

## Further Reading

- [OpenAPI Specification](https://swagger.io/specification/)
- [Protobuf Language Guide](https://protobuf.dev/programming-guides/proto3/)
