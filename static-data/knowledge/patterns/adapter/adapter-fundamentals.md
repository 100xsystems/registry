---
title: "Adapter: Make Incompatible Interfaces Talk"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the adapter intent"
  - "Build an object adapter"
  - "Distinguish adapter from facade and proxy"
  - "Apply adapters at boundaries"
prerequisites:
  - "patterns/facade"
  - "patterns/proxy"
knowledge_refs:
  - "patterns/adapter"
---

# Adapter: Make Incompatible Interfaces Talk

## The Problem

A third-party SDK exposes saveDocument(doc, opts) but your code calls store(doc). Without an adapter, either your code contorts to the SDK or you fork the SDK. The adapter wraps the SDK and exposes the interface your code expects.

```java
// Your interface (what the app wants):
interface DocumentStore {
    void store(Document doc);
}

// The third-party SDK (what exists):
class SdkClient {
    void saveDocument(Document doc, SaveOptions opts) { ... }
}

// Adapter: translate without touching either side
class SdkStoreAdapter implements DocumentStore {
    private final SdkClient client;
    SdkStoreAdapter(SdkClient c) { this.client = c; }
    public void store(Document doc) {
        client.saveDocument(doc, SaveOptions.defaults());
    }
}
```

## Adapters vs Facades vs Proxies

An adapter changes an interface (so A can call B). A facade simplifies a complex subsystem behind one simple interface. A proxy controls access to an object (lazy, remote, protected). They are often combined at real boundaries, but their intents differ.

## Practice: Adapt the Legacy System

Your new order service needs an interface the legacy billing system does not provide.

**Task 1:** Define the interface your code needs and the legacy API that exists.

**Task 2:** Write the adapter translating calls, including error and return translation.

**Task 3:** Unit-test the adapter with a fake legacy client.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about the difference between adapting an interface and simplifying a subsystem. Start with the intent.

**Prompt 2 — Compare & Contrast:**
> Compare adapter, facade, and proxy with concrete examples of each at a system boundary.

**Prompt 3 — Boundary Testing:**
> The SDK throws checked exceptions your interface does not declare. Design the adapter's error translation policy.

## Key Takeaways

- Adapters translate interfaces at boundaries
- Neither side changes — the adapter bridges
- Adapter changes shape; facade simplifies; proxy controls
- Error translation is part of the adapter contract

## Further Reading

- [Adapter — Refactoring Guru](https://refactoring.guru/design-patterns/adapter)
- [Adapter Pattern — Wikipedia](https://en.wikipedia.org/wiki/Adapter_pattern)
