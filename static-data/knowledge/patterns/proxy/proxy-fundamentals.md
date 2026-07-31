---
title: "Proxy: Control Access Through a Stand-In"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the proxy intent"
  - "Describe the proxy kinds"
  - "Build a lazy proxy"
  - "Distinguish proxy from adapter"
prerequisites:
  - "patterns/adapter"
  - "patterns/decorator"
knowledge_refs:
  - "patterns/proxy"
---

# Proxy: Control Access Through a Stand-In

## The Problem

Sometimes the real object is expensive to create, lives on another machine, or must be protected. The proxy implements the same interface as the real object and controls access to it — the caller cannot tell the difference. The real object stays untouched.

```java
// Proxy kinds:
//   lazy proxy   — defer creating the expensive real object
//   remote proxy — translate calls to a remote service
//   protection   — check permissions before delegating
//   cache proxy  — answer from cache when possible

interface Image { void render(); }

class HugeImage implements Image {         // expensive to load
    HugeImage(String path) { loadFromDisk(path); }
    public void render() { /* draw */ }
}

class LazyImageProxy implements Image {    // same interface
    private HugeImage real;
    private final String path;
    LazyImageProxy(String p) { this.path = p; }
    public void render() {
        if (real == null) real = new HugeImage(path);  // load on first use
        real.render();
    }
}
// The caller uses the proxy exactly like the real image.
```

## Proxy vs Adapter vs Decorator

A proxy has the same interface and controls access. An adapter changes the interface to fit a client. A decorator adds behavior to the same interface. Proxies and decorators look alike in structure — the intent differs: control vs enhance.

## Practice: Build the Lazy Proxy

A gallery loads 1,000 high-res images at startup; most are never viewed.

**Task 1:** Implement the proxy that defers loading to first render.

**Task 2:** Add the cache proxy on top for revisited images.

**Task 3:** Measure startup time and memory before and after.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why the proxy must keep the same interface. Start with the caller.

**Prompt 2 — Compare & Contrast:**
> Compare proxy with adapter and decorator using one example each. When do the structures differ?

**Prompt 3 — Boundary Testing:**
> The remote proxy retries a call while the real object mutates. Design the idempotency guard at the boundary.

## Key Takeaways

- Proxy controls access with the same interface
- Lazy, remote, protection, and cache kinds
- Intent differs from adapter (interface) and decorator (behavior)
- Callers never know they hold a proxy

## Further Reading

- [Proxy — Refactoring Guru](https://refactoring.guru/design-patterns/proxy)
- [Proxy Pattern — Wikipedia](https://en.wikipedia.org/wiki/Proxy_pattern)
