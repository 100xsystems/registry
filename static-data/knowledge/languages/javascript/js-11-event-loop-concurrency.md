---
title: "The Event Loop, Microtasks, and Concurrency"
description: "How the JavaScript event loop works: call stack, task queues, microtasks, requestAnimationFrame, and concurrent execution models."
type: lesson
order: 11
duration: "60 min"
difficulty: intermediate
learning_objectives:
  - "Understand the event loop: call stack, microtask queue, and macrotask queue"
  - "Explain the difference between microtasks (Promise callbacks) and macrotasks (setTimeout, I/O)"
  - "Predict execution order in complex async scenarios"
  - "Use requestAnimationFrame, requestIdleCallback, and Web Workers for concurrency"
knowledge_refs:
  - languages/javascript/js-11-event-loop-concurrency
prerequisites:
  - "JS-10: Async Promises"
references:
    - title: "You Don't Know JS Yet"
      url: "https://github.com/getify/you-dont-know-js/blob/2nd-ed/sync-async/ch1.md"
      chapters: "Sync & Async — Ch. 1: Asynchrony: Now & Later (event loop section)"
      description: "Deep dive into the event loop architecture"
    - title: "The Modern JavaScript Tutorial"
      url: "https://javascript.info/event-loop"
      sections: "Event loop: microtasks and macrotasks | Promise handling — Microtasks"
      description: "Practical event loop examples with timing diagrams"
    - title: "MDN Web Docs"
      url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript"
      sections: "Event loop | Concurrency and Event Loop"
      description: "Authoritative reference on the concurrency model"
    - title: "Eloquent JavaScript (4th Edition)"
      url: "https://eloquentjavascript.net/"
      chapters: "Chapter 11 (event loop section)"
      description: "Practical async programming with event loop understanding"
---

# JS-11: The Event Loop, Microtasks, and Concurrency

## Introduction

JavaScript has a concurrency model based on an event loop. Despite being
single-threaded, it can handle many operations concurrently through a queue
system. Understanding the event loop is essential for debugging async timing
issues and writing performant applications.

## Subtopics

### 1. The Event Loop Architecture

- **Call stack**: LIFO — tracks currently executing functions
- **Microtask queue** (Job queue): Promise `.then()`, `.catch()`, `.finally()`, queueMicrotask(), MutationObserver
- **Macrotask queue** (Task queue): setTimeout, setInterval, I/O, UI rendering events
- **Event loop iteration**: 1. Execute all synchronous code → 2. Drain microtask queue → 3. Render (if needed) → 4. Take one macrotask → repeat
- *Reference:* javascript.info — Event loop | [YDKJSY — Sync & Async Ch. 1](https://github.com/getify/you-dont-know-js/blob/2nd-ed/types-grammar/ch1.md/blob/2nd-ed/types-grammar/ch1.md/blob/2nd-ed/sync-async/ch1.md) | [MDN — Event loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Event_loop)

### 2. Microtasks vs Macrotasks

| Feature | Microtasks | Macrotasks |
|---------|-----------|-----------|
| Examples | Promise.then, queueMicrotask | setTimeout, setInterval, I/O |
| Priority | Higher — drained before next macrotask | Lower — one per event loop tick |
| Order | Entire queue emptied before rendering | One task, then check microtasks again |

- *Deep dive:* `Promise.resolve().then(() => console.log("micro"))` runs BEFORE
  `setTimeout(() => console.log("macro"), 0)` — even though the timeout is 0ms.
  The microtask queue is checked after every macrotask completes.

### 3. requestAnimationFrame and requestIdleCallback

- `requestAnimationFrame(callback)` — runs before the next repaint, ideal for animations
- `requestIdleCallback(callback)` — runs when browser is idle, for non-critical work
- Both run AFTER microtasks are drained but BEFORE the next macrotask
- *Reference:* MDN — requestAnimationFrame, requestIdleCallback

### 4. Web Workers for True Parallelism

- Web Workers run in a separate OS thread with their own event loop
- Communication: `postMessage()` and `onmessage` events
- No DOM access, no shared memory (except SharedArrayBuffer)
- `transferable` objects for zero-copy data transfer
- `worker.terminate()` to kill immediately
- *Reference:* [MDN — Web Workers API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Canvas_API/Web_Workers_API) | javascript.info — Web Workers

## Practice Questions

1. Predict the output: `console.log(1); setTimeout(() => console.log(2), 0); Promise.resolve().then(() => console.log(3)); console.log(4);`
2. What is the minimum delay of `setTimeout(fn, 0)`? (Hint: it's not 0ms in browsers)
3. Why does `for (var i=0; i<5; i++) { setTimeout(() => console.log(i), 0); }` log five 5s?
4. When would you use a Web Worker instead of async/await?

## Key Takeaways

- Microtasks (Promise callbacks) run before macrotasks (setTimeout, I/O)
- The event loop: call stack → microtask queue → render → macrotask
- `setTimeout(fn, 0)` is NOT immediate — it's deferred to the next macrotask
- Web Workers enable true parallelism but with communication overhead
- Understanding the event loop is crucial for debugging async timing

## Further Reading

- YDKJSY: Sync & Async, Chapter 1 (event loop section)
- javascript.info: Event loop, Microtasks and macrotasks
- MDN: Concurrency model and Event Loop
- Jake Archibald: "In The Loop" (JSConf talk)
