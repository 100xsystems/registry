---
title: "Observer in Production: Events and Reactive Streams"
order: 2
difficulty: "Intermediate"
duration: "60 min"
learning_objectives:
  - "Use DOM and UI events"
  - "Design reactive streams"
  - "Apply backpressure"
  - "Bridge to distributed events"
prerequisites:
  []
knowledge_refs:
  - "patterns/observer"
---

# Observer in Production: Events and Reactive Streams

## From Callbacks to Streams

UI frameworks are observer engines: every click, scroll, and keystroke is a subject notifying listeners. Reactive streams (RxJS, Reactive Streams) formalize the observer into push-based pipelines with operators — map, filter, debounce — and add backpressure so a slow observer signals the producer to slow down.

```typescript
// RxJS: observer pipelines with backpressure semantics
import { fromEvent } from 'rxjs';
import { debounceTime, map, distinctUntilChanged } from 'rxjs/operators';

const input = document.querySelector('#search')!;
fromEvent(input, 'input')            // subject: every keystroke
  .pipe(
    debounceTime(300),               // throttle bursty events
    map((e: any) => e.target.value),
    distinctUntilChanged()           // skip repeats
  )
  .subscribe(q => search(q));        // observer reacts
// The pipeline is lazy; backpressure via debounce/drain policies.
```

## Distributed Observers

Cross-service, the observer becomes publish-subscribe with a broker: services subscribe to topics, producers publish, and the broker decouples them across machines. Durability is the new concern — a broker buffers for offline observers — and the ordering guarantees differ from in-process observers.

## Practice: Design the Reactive Form

A search box fires 20 keystrokes/s; each triggers an API call that must be debounced and deduped.

**Task 1:** Build the pipeline: debounce, map, distinct, switch to latest.

**Task 2:** Add cancellation: a stale response must not overwrite a newer one.

**Task 3:** Add the distributed variant: publish the query events to a topic for analytics.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Teach me why reactive streams add backpressure to the observer model. Ask me what a slow subscriber does without it.

**Prompt 2 — Implementation Design:**
> Design a real-time dashboard: sensor streams, windows, and the UI subscription. Where does backpressure live?

**Prompt 3 — Boundary Testing:**
> A subscriber throws on one event and the stream dies. Design the error handler that keeps the stream alive.

## Key Takeaways

- UI frameworks are observer engines
- Reactive streams add operators and backpressure
- Distributed observers need a durable broker
- Error handling must not kill the stream

## Further Reading

- [RxJS — docs](https://rxjs.dev/guide/overview)
- [Reactive Streams — the spec](https://www.reactive-streams.org/)
