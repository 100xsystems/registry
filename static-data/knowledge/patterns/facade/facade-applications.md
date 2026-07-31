---
title: "Facade in Production: SDKs and Libraries"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design SDK public facades"
  - "Keep internals replaceable"
  - "Version the facade surface"
  - "Test through the facade"
prerequisites:
  []
knowledge_refs:
  - "patterns/facade"
---

# Facade in Production: SDKs and Libraries

## SDK Facades

A good SDK exposes a small facade and hides the engine: the client calls client.send(message) and never sees connection pools, retries, and serialization. The facade is the versioned public surface; internals can change freely beneath it.

```typescript
// SDK facade: the only public surface
export class Client {
    private readonly conn: ConnectionManager;
    private readonly serializer: Serializer;

    constructor(opts: ClientOptions) {   // options are the DSL
        this.conn = new ConnectionManager(opts);
        this.serializer = new Serializer(opts.format);
    }

    async send(msg: Message): Promise<MessageId> {
        const wire = this.serializer.serialize(msg);
        const id = await this.conn.send(wire);   // retries inside
        return id;
    }
}
// Internal modules are never exported. The facade IS the API.
```

## Testing Through the Facade

Integration tests drive the SDK through the facade — the same path users take. The facade also gives a natural seam for contract tests: the public surface is the contract, and internals are free to change.

## Practice: Design the SDK Surface

A metrics SDK: users need sendMetric, flush, and shutdown — nothing else.

**Task 1:** Design the facade class and its options type.

**Task 2:** Hide the batching, retry, and serialization internals behind it.

**Task 3:** Write the facade contract test and the internal refactor that proves internals are replaceable.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why the facade is the versioned contract of an SDK and internals are free to evolve.

**Prompt 2 — Implementation Design:**
> Design a library that hides a web socket layer behind a chat.send() facade. What does the facade promise?

**Prompt 3 — Boundary Testing:**
> A power user needs a knob the facade hides. Design the advanced-options surface that does not break the facade.

## Key Takeaways

- The facade is the SDK's versioned public surface
- Internals evolve freely beneath it
- Options types are the configuration DSL
- Contract tests pin the public surface

## Further Reading

- [API Design — Google API Design Guide](https://cloud.google.com/apis/design)
- [Semantic Versioning for SDKs](https://semver.org/)
