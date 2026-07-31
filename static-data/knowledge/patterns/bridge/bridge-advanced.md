---
title: "Advanced Bridge: Engines and Platforms"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Design engine-agnostic abstractions"
  - "Apply bridge across platforms"
  - "Version the two axes independently"
  - "Avoid the \"bridge everything\" trap"
prerequisites:
  []
knowledge_refs:
  - "patterns/bridge"
---

# Advanced Bridge: Engines and Platforms

## Engine Abstractions

Scripting engines (V8, JSC, Hermes) are a classic bridge: the runtime abstraction (executing scripts, calling functions) is separate from the engine implementation. Products swap engines under the same abstraction to tune performance or memory.

```text
Engine bridge (React Native / Hermes / JSC):
  JSExecutor (abstraction): evaluate, call, createRuntime
  HermesExecutor, JSCExecutor (implementations)
  -> swap engines by configuration; app code untouched.

The bridge pattern at platform scale:
  - OS abstraction (POSIX) is the oldest bridge
  - Database drivers (JDBC/ODBC) bridge SQL dialects
  - Web APIs bridge browser engines
```

## Versioning and the Over-Bridge Trap

The two axes version independently: the abstraction bumps when contracts change, implementations bump on engine upgrades. But not everything needs a bridge — bridging a single-axis variation adds a pointless indirection layer. Bridge only the axes that actually vary.

## Practice: Design the Engine Seam

A product runs scripts on V8 today and must support Hermes for mobile.

**Task 1:** Define the JSExecutor abstraction the product uses.

**Task 2:** Implement V8 and Hermes adapters behind it.

**Task 3:** Design the capability/version matrix and the startup engine selection.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can articulate when an abstraction is a bridge (two axes) versus a needless indirection (one axis).

**Prompt 2 — Implementation Design:**
> Design a cross-platform storage layer (local disk, cloud, memory) as a bridge where the data-model axis is separate from the store axis.

**Prompt 3 — Boundary Testing:**
> An engine supports a language feature another lacks. Design the feature detection that degrades gracefully instead of crashing.

## Key Takeaways

- Engines and platforms are the bridge at product scale
- The two axes version independently
- Feature detection keeps implementations honest
- Bridge only axes that actually vary

## Further Reading

- [Hermes Engine — React Native](https://reactnative.dev/docs/hermes)
- [JDBC — the database bridge](https://docs.oracle.com/javase/tutorial/jdbc/overview/index.html)
