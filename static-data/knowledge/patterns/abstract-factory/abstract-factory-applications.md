---
title: "Abstract Factory in Production: Pluggable Backends"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Design a pluggable backend factory"
  - "Wire the factory at the composition root"
  - "Test with an in-memory product family"
  - "Avoid factory sprawl"
prerequisites:
  []
knowledge_refs:
  - "patterns/abstract-factory"
---

# Abstract Factory in Production: Pluggable Backends

## The Provider Pattern

Cloud SDKs and database drivers use abstract factories so application code is provider-agnostic: an S3Factory and a GCSFactory both produce Bucket and Blob products. Swapping the provider is a one-line wiring change.

```typescript
// Pluggable storage: the app depends only on the factory interface
interface StorageFactory {
    createBucket(name: string): Bucket;
    createBlob(key: string): Blob;
}
const factory: StorageFactory = process.env.PROVIDER === 'gcs'
    ? new GcsFactory()      // one wiring change swaps the cloud
    : new S3Factory();

const bucket = factory.createBucket('uploads');  // consistent pair
const blob = factory.createBlob('a/b.jpg');      // same provider
```

## Testing with a Family

A MemoryFactory that produces in-memory Buckets and Blobs lets integration tests run without a cloud. Because the app depends on the factory interface, the fake family is a drop-in — the same contract tests validate both families.

## Practice: Design the Provider Factory

A media service must support S3 and GCS with matching upload and stream products.

**Task 1:** Define the factory and product interfaces (Uploader, Streamer).

**Task 2:** Implement S3Factory, GcsFactory, and MemoryFactory.

**Task 3:** Run the same contract tests against all three families and wire the choice at startup.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why the composition root is the only place the concrete factory should appear.

**Prompt 2 — Implementation Design:**
> Design a notification system with email/push/sms families. Where does the factory fit, and what product types does each family produce?

**Prompt 3 — Boundary Testing:**
> Two providers have incompatible capabilities (GCS supports X, S3 does not). Design the capability negotiation that keeps the family abstraction honest.

## Key Takeaways

- Provider abstractions are abstract factories at scale
- The composition root is the single wiring point
- Fake families enable contract-tested integration tests
- Capability negotiation keeps the abstraction honest

## Further Reading

- [AWS SDK — Provider Interfaces](https://docs.aws.amazon.com/sdk-for-javascript/)
- [The Provider Pattern — Martin Fowler](https://martinfowler.com/eaaCatalog/serviceLocator.html)
