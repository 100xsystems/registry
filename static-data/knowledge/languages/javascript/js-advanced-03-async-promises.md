---
title: "Asynchronous JavaScript: Promises and Async/Await"
description: "Promises, async/await, error handling in async code, and the evolution of asynchronous patterns in JavaScript."
type: lesson
order: 10
duration: "75 min"
difficulty: intermediate
level: Advanced
learning_objectives:
  - "Create and chain Promises for sequential and parallel async operations"
  - "Handle async errors with try/catch, .catch(), and Promise.allSettled()"
  - "Write clean async/await code that reads synchronously"
  - "Implement advanced patterns: promise racing, cancellation, and retry"
knowledge_refs:
  - languages/javascript/js-advanced-03-async-promises
prerequisites:
  - "JS-03: Functions"
  - "JS-08: Scope and Closures"
references:
    - title: "You Don't Know JS Yet"
      url: "https://github.com/getify/you-dont-know-js"
      chapters: "Sync & Async — Ch. 2: Callbacks, Ch. 3: Promises, Ch. 4: Generators"
      description: "Deep dive into async patterns and promise mechanics"
    - title: "Eloquent JavaScript (4th Edition)"
      url: "https://eloquentjavascript.net/"
      chapters: "Chapter 11: Asynchronous Programming"
      description: "Practical async programming with promises and async/await"
    - title: "The Modern JavaScript Tutorial"
      url: "https://javascript.info/"
      sections: "Promises, async/await — full section | Promise API | Microtasks and event loop"
      description: "The most comprehensive practical async tutorial"
    - title: "MDN JavaScript Guide"
      url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"
      sections: "Using promises | Promises — Guarantees, Chaining, Error handling, Composition"
      description: "Authoritative guide to promise patterns and best practices"
    - title: "Exploring JS: JavaScript for Programmers"
      url: "https://exploringjs.com/js/"
      chapters: "Ch. 25: Promises | Ch. 26: Async Functions"
      description: "Detailed coverage of async patterns and their evolution"
---

# JS-10: Asynchronous JavaScript: Promises and Async/Await

## Introduction

JavaScript is single-threaded. Asynchronous programming allows non-blocking
operations by deferring work to be executed later. Promises represent values
not yet available, and async/await provides synchronous-looking syntax for
asynchronous operations.

## Subtopics

### 1. Callbacks and Callback Hell

- **Callback**: A function passed as an argument to be called later
- **Inversion of Control (IOC)**: When you pass a callback, you're handing control
  to the receiving function
- **Callback hell**: Nested callbacks create unreadable "pyramid of doom"
- Error-first callbacks: Node.js convention `callback(err, result)`
- *Reference:* YDKJSY Sync & Async Ch. 2 | javascript.info — Callbacks

### 2. Promises

- **Three states**: pending, fulfilled, rejected
- **Promise constructor**: `new Promise((resolve, reject) => { ... })`
- **Chaining**: `.then()` returns a new promise — enables flat chains
- **Error propagation**: Errors in `.then()` automatically flow to nearest `.catch()`
- **Promise static methods**: `Promise.all()`, `Promise.allSettled()`, `Promise.race()`,
  `Promise.any()`, `Promise.resolve()`, `Promise.reject()`
- **Promise combinators**: `all` (fail-fast), `allSettled` (wait for all), `race` (first settled),
  `any` (first fulfilled)
- *Reference:* javascript.info — Promises | Eloquent JS Ch. 11 | YDKJSY Sync & Async Ch. 3
  | MDN — Using promises | Exploring JS Ch. 25

### 3. Async/Await

- `async function` always returns a Promise
- `await` pauses execution until a Promise settles
- Error handling: wrap in `try/catch` — cleaner than `.catch()` chains
- `await` can only be used inside `async` functions (top-level await in modules)
- `for await...of` — iterate over async iterables
- Parallel execution: `const [a, b] = await Promise.all([p1, p2])`
- *Reference:* javascript.info — Async/await | Eloquent JS Ch. 11 | MDN — async function
  | Exploring JS Ch. 26

### 4. Advanced Promise Patterns

- **Retry with exponential backoff**: Wrap in a retry loop
- **Timeout**: `Promise.race([operation, timeoutPromise])`
- **Cancelation**: Use `AbortController` and `AbortSignal`
- **Caching**: Memoize async functions
- **Rate limiting**: Concurrency control with a semaphore pattern
- *Reference:* javascript.info — Fetch: Abort | MDN — AbortController

## Practice Questions

1. Convert this callback to a promise chain, then to async/await:
   `fs.readFile("a.txt", (err, data) => { if (err) throw err; ... })`
2. What does `Promise.allSettled()` return that's different from `Promise.all()`?
3. Write an `asyncRetry(fn, maxRetries, delay)` function that retries on failure.
4. Why can't you use `await` at the top level of a non-module script?

## Key Takeaways

- Promises solve inversion of control — they're trustable and composable
- `async`/`await` is syntactic sugar over promises — understand the underlying promises
- `Promise.all()` fails fast; `Promise.allSettled()` waits for all to complete
- Always handle promise rejections — unhandled rejections crash Node.js
- Use `AbortController` for fetch/timeout cancelation

## Further Reading

- YDKJSY: Sync & Async, Chapters 3-4
- Eloquent JS, Chapter 11: Asynchronous Programming
- javascript.info: Promises, async/await (full section)
- MDN: Using Promises
