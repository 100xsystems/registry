---
title: "Advanced Proxy: Virtual Proxies and Copy-on-Write"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Build virtual proxies"
  - "Use copy-on-write proxies"
  - "Generate dynamic proxies"
  - "Reason about proxy overhead"
prerequisites:
  []
knowledge_refs:
  - "patterns/proxy"
---

# Advanced Proxy: Virtual Proxies and Copy-on-Write

## Virtual and COW Proxies

A virtual proxy stands in for a heavy object (a full document when only metadata is needed). A copy-on-write proxy lazily copies: multiple clients share one object until one mutates — the proxy clones on first write. Both defer cost until it is actually needed.

```java
// Dynamic proxy: java.lang.reflect.Proxy generates the proxy class
import java.lang.reflect.*;

Service svc = (Service) Proxy.newProxyInstance(
    Service.class.getClassLoader(),
    new Class[]{Service.class},
    (proxy, method, args) -> {
        long start = System.nanoTime();
        Object result = method.invoke(realService, args);   // delegate
        long ms = (System.nanoTime() - start) / 1_000_000;
        metrics.record(method.getName(), ms);               // cross-cutting
        return result;
    });
// One handler instruments every method — no per-method wrapper code.
// Dynamic proxies power AOP, mocks, and retrofits of interfaces.
```

## Overhead

Every proxy adds a hop: a dispatch, a check, a round trip. In hot paths, proxy chains multiply latency and complicate debugging (stack traces show proxies). The discipline: proxy at boundaries where the control is worth the hop, and measure the added latency.

## Practice: Design the COW Cache

A 100-client shared config object must not be copied until a client edits it.

**Task 1:** Implement the COW proxy with copy-on-first-write.

**Task 2:** Add the dynamic proxy that instruments every access.

**Task 3:** Measure the proxy overhead in a hot loop and decide where to bypass it.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why a COW proxy shares until mutation and what the first writer pays.

**Prompt 2 — Implementation Design:**
> Design an AOP-style metrics proxy over a repository interface. What is recorded, and how do you keep it out of hot paths?

**Prompt 3 — Boundary Testing:**
> A COW proxy is written by two clients concurrently. Design the synchronization that gives each a consistent copy.

## Key Takeaways

- Virtual proxies defer heavy construction
- COW proxies share until first mutation
- Dynamic proxies instrument whole interfaces
- Proxy hops cost latency and debug clarity

## Further Reading

- [java.lang.reflect.Proxy — Javadoc](https://docs.oracle.com/javase/8/docs/api/java/lang/reflect/Proxy.html)
- [Lazy loading and proxies — Martin Fowler](https://martinfowler.com/eaaCatalog/lazyLoad.html)
