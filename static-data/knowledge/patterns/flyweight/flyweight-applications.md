---
title: "Flyweight in Production: Caches and Runtimes"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Use string interning as a flyweight"
  - "Cache heavy shared assets"
  - "Design key composition for the factory"
  - "Avoid sharing mutable aggregates"
prerequisites:
  []
knowledge_refs:
  - "patterns/flyweight"
---

# Flyweight in Production: Caches and Runtimes

## Interning and Asset Caches

JVM string interning and Symbol tables are flyweights: one canonical instance per value, shared everywhere. UI frameworks cache icons and skins per theme; game engines cache meshes and textures per model. The factory key must capture every intrinsic dimension or distinct states collapse into one shared object.

```typescript
// Asset cache as flyweight factory
const assetCache = new Map<string, Texture>();

function getTexture(name: string, mipLevels: number): Texture {
    const key = `${name}#${mipLevels}`;   // key covers ALL intrinsic dims
    let t = assetCache.get(key);
    if (!t) {
        t = loadTexture(name, mipLevels);
        assetCache.set(key, t);
    }
    return t;  // one Texture shared by every sprite that uses it
}
```

## The Cache Is the Contract

The flyweight factory is a cache, and caches need eviction. When memory pressure rises, the factory must either pin hot flyweights or rebuild them — a shared object cannot simply be dropped while in use. Reference counting or weak references make eviction safe.

## Practice: Cache the Icon Set

A UI renders 5,000 icons from 40 themes; each icon+theme pair is a heavy raster.

**Task 1:** Design the factory key (icon id, theme, size, dpr).

**Task 2:** Add a least-recently-used eviction that is safe for in-flight renders.

**Task 3:** Measure hit rate and memory; tune the capacity.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why the factory key must cover every intrinsic dimension. Ask me what breaks when it does not.

**Prompt 2 — Implementation Design:**
> Design an interning table for user IDs and profile objects in a chat app. What is shared, what is per-user, and how is eviction handled?

**Prompt 3 — Boundary Testing:**
> Two threads request the same flyweight simultaneously. Design the factory concurrency (double-checked locking, or lock-free computeIfAbsent).

## Key Takeaways

- Interning and asset caches are flyweights in the wild
- The key must cover all intrinsic dimensions
- Flyweight factories are caches and need eviction policies
- Concurrency-safe factories need careful key handling

## Further Reading

- [String Interning — JVM](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html#intern--)
- [Flyweight — Refactoring Guru](https://refactoring.guru/design-patterns/flyweight)
