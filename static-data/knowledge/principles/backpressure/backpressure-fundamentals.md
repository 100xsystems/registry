---
title: "Backpressure: Flow Control Fundamentals"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain why unbounded queues cause memory exhaustion"
  - "Define backpressure and its role in resilient systems"
  - "Identify the three flow-control strategies"
  - "Trace a slow-consumer scenario through a pipeline"
prerequisites:
  - "principles/fail-fast"
  - "principles/rate-limiting"
knowledge_refs:
  - "principles/backpressure"
---

# Backpressure: Flow Control Fundamentals

## The Problem: Unbounded Buffers

When a producer emits faster than a consumer can process, messages pile up. Without limits, that queue grows until memory is exhausted and the process dies — taking the whole service down with it.

Backpressure is the mechanism by which a consumer signals the producer to slow down. It converts a resource-exhaustion failure into a graceful, explicit slowdown that the system can survive.

## How Backpressure Works

There are three fundamental strategies: (1) bounded queues with blocking, (2) pull-based (reactive) demand where the consumer requests N items at a time, and (3) dropping or erroring when the buffer overflows.

The pull model is the strongest: the consumer declares exactly how much it can handle, so the producer never over-produces. This is the basis of Reactive Streams and Java Flow.

```java
// Reactive Streams: consumer declares demand
public final class SimpleSubscriber implements Flow.Subscriber<Integer> {
    private Flow.Subscription subscription;
    public void onSubscribe(Flow.Subscription s) {
        this.subscription = s;
        s.request(3);            // demand: 3 items at a time
    }
    public void onNext(Integer item) {
        System.out.println("got " + item);
        subscription.request(1); // one more after each
    }
    public void onError(Throwable t) { t.printStackTrace(); }
    public void onComplete() { System.out.println("done"); }
}
```

## Practice: Slow Consumer Simulation

Model a producer/consumer pair where the consumer sleeps 100ms per item and the producer bursts 10,000 items instantly.

**Task 1:** With an unbounded queue, record the memory growth and the time when the process dies.

**Task 2:** Switch to a bounded queue (capacity 100) with blocking. What happens to the producer? Is the system stable?

**Task 3:** Implement pull-based demand. Verify memory stays flat regardless of burst size.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time to help me reason about why a bounded queue with a blocking put can still deadlock a pipeline. Start with the producer thread.

**Prompt 2 — Compare & Contrast:**
> Compare backpressure in Kafka (no native backpressure), Reactive Streams, and TCP flow control. Give concrete scenarios where each fails.

**Prompt 3 — Boundary Testing:**
> What happens when a consumer requests a negative demand in a Reactive Streams implementation? What should the spec-compliant publisher do?

**Prompt 4 — Implementation Design:**
> Design a bounded async queue for a microservice that must never drop messages and never exhaust memory. Show the data structures and blocking semantics.

## Key Takeaways

- Unbounded queues convert slow consumers into OOM crashes
- Pull-based demand is the strongest backpressure model
- Blocking on a bounded queue is simple but can deadlock pipelines
- Dropping with error signals is a valid strategy for time-sensitive data

## Further Reading

- [Reactive Streams Specification](https://www.reactive-streams.org/)
- [Flow (Java) — API docs](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Flow.html)
- [Backpressure in Reactive Systems](https://www.reactivemanifesto.org/glossary#Back-Pressure)
