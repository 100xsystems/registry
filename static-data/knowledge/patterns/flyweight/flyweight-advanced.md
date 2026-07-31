---
title: "Advanced Flyweight: Pools, Weak References, and Shared Mutable State"
order: 3
difficulty: "Advanced"
duration: "75 min"
learning_objectives:
  - "Combine flyweight with object pooling"
  - "Use weak references for safe eviction"
  - "Recognize shared-mutable-state hazards"
  - "Design flyweights for concurrent use"
prerequisites:
  []
knowledge_refs:
  - "patterns/flyweight"
---

# Advanced Flyweight: Pools, Weak References, and Shared Mutable State

## Flyweight + Pooling

A pool is a flyweight whose instances are reusable rather than immutable: database connections, buffers, worker objects. The pool hands out an instance, the borrower returns it, and the pool resets it. The reset must fully restore the intrinsic contract or the next borrower inherits corruption.

```go
// Pooled flyweight: reuse, reset, return
type ConnPool struct {
    idle chan *Conn
    newConn func() *Conn
}
func (p *ConnPool) Acquire() *Conn {
    select {
    case c := <-p.idle:
        c.Reset()          // full reset = intrinsic contract restored
        return c
    default:
        return p.newConn()
    }
}
func (p *ConnPool) Release(c *Conn) {
    c.Reset()
    select { case p.idle <- c: default: c.Close() }  // pool full: close
}
```

## Weak-Reference Caches and Concurrency

Weak-reference caches (WeakHashMap, weakref) let the GC reclaim unused flyweights — eviction without policy. The cost: a request may miss and rebuild. For concurrent use, flyweights must be safe to share: immutable fields, no internal mutable counters, or explicit synchronization.

## Practice: Design the Safe Pool

A request-scoped buffer pool is shared across 40 goroutines handling concurrent requests.

**Task 1:** Design the pool with acquire/release and a full-reset contract.

**Task 2:** Add the weak-reference variant and compare eviction behavior under GC.

**Task 3:** Write the race test that proves resets and borrows never overlap.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me questions until I can explain why a pool flyweight must fully reset before reuse.

**Prompt 2 — Implementation Design:**
> Design a thread-safe shared render state: immutable geometry shared, mutable transform per call. Where do the flyweight and the extrinsic state live?

**Prompt 3 — Boundary Testing:**
> A borrower forgets to return a pooled object. Design the leak detection (finalizers, metrics) that surfaces it.

## Key Takeaways

- Pools are reusable flyweights with a reset contract
- Weak references give eviction without policy
- Shared mutable state is the flyweight failure mode
- Concurrent flyweights must be immutable or synchronized

## Further Reading

- [Object Pool — Refactoring Guru](https://refactoring.guru/design-patterns/object-pool)
- [WeakHashMap — Javadoc](https://docs.oracle.com/javase/8/docs/api/java/util/WeakHashMap.html)
