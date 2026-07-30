---
title: "Higher-Order Functions, Iterators, and Generators"
description: "Functional programming patterns, custom iterables, generator functions, and async generators."
type: lesson
order: 12
duration: "60 min"
difficulty: intermediate
level: Advanced
learning_objectives:
  - "Implement function composition, currying, and partial application"
  - "Build custom iterables using the Symbol.iterator protocol"
  - "Create generator functions for lazy evaluation and infinite sequences"
  - "Use async generators and for-await-of for streaming data"
knowledge_refs:
  - languages/javascript/js-advanced-05-higher-order-generators
prerequisites:
  - "JS-03: Functions"
  - "JS-04: Objects and Arrays"
references:
    - title: "Eloquent JavaScript (4th Edition)"
      url: "https://eloquentjavascript.net/"
      chapters: "Chapter 5: Higher-Order Functions | Chapter 22 (async generators section)"
      description: "Classic introduction to functional programming in JS"
    - title: "The Modern JavaScript Tutorial"
      url: "https://javascript.info/"
      sections: "Iterables | Generators | Async iterators and generators | Currying"
      description: "Practical coverage of iterables and generators"
    - title: "You Don't Know JS Yet"
      url: "https://github.com/getify/you-dont-know-js"
      chapters: "Sync & Async — Ch. 4: Generators"
      description: "Deep dive into generators for async control flow"
    - title: "MDN JavaScript Guide"
      url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"
      sections: "Iterators and generators"
      description: "Authoritative reference for iteration protocols"
---

# JS-12: Higher-Order Functions, Iterators, and Generators

## Introduction

Higher-order functions accept or return other functions, enabling powerful
abstraction patterns. Iterators and generators provide a protocol for consuming
data one item at a time — essential for lazy evaluation and infinite sequences.

## Subtopics

### 1. Higher-Order Functions

- **Functions as values**: Assign to variables, pass as arguments, return from functions
- **Array methods as HOFs**: `map`, `filter`, `reduce`, `forEach`, `flatMap`
- **Function composition**: Combine small functions: `compose(f, g)(x) = f(g(x))`
- **Currying**: Transform multi-argument function into sequence of single-argument functions
- **Partial application**: Pre-fill some arguments, return a function for the rest
- **Throttling and debouncing**: Time-based function control
- *Reference:* Eloquent JS Ch. 5 | javascript.info — Currying | Exploring JS Ch. 16

### 2. Iterables and Iterators

- **Iterable protocol**: Object has `[Symbol.iterator]()` method that returns an iterator
- **Iterator protocol**: Object has `next()` method returning `{value, done}`
- Built-in iterables: Array, String, Map, Set, NodeList, arguments
- **Consumer protocol**: `for...of`, spread `...`, destructuring, `Array.from()`
- Build custom iterables by implementing `[Symbol.iterator]`
- *Reference:* javascript.info — Iterables | MDN — Iterators and generators | Exploring JS Ch. 22

### 3. Generator Functions

- `function* gen() { yield 1; yield 2; }` — returns a Generator object (both iterable and iterator)
- `yield` pauses execution, `next()` resumes it — enables two-way communication
- `yield*` delegates to another iterable or generator
- **Lazy evaluation**: Values are computed on-demand, not all at once
- **Infinite sequences**: `function* naturals() { let n=0; while(true) yield n++; }`
- *Reference:* javascript.info — Generators | Eloquent JS Ch. 22 | MDN — function*
  | YDKJSY Sync & Async Ch. 4

### 4. Async Generators

- `async function* gen() { while(true) { yield await fetch(url); } }`
- Consumed with `for await...of`
- Perfect for streaming data: paginated APIs, real-time feeds, large files
- *Reference:* javascript.info — Async iterators and generators | MDN — for await...of

## Practice Questions

1. Implement `compose(f, g)` where `compose(f, g)(x) === f(g(x))`.
2. Create a range iterable: `for (const n of range(1, 10, 2))` yields 1, 3, 5, 7, 9.
3. Write a generator `fibonacci()` that yields Fibonacci numbers infinitely.
4. Convert a paginated API into an async generator.

## Key Takeaways

- Higher-order functions enable composition, abstraction, and code reuse
- Iterables provide a standard protocol for consuming data sequences
- Generators are both iterable and iterator — they pause/resume execution
- Lazy evaluation with generators avoids computing values that are never consumed
- Async generators stream async data with `for await...of`

## Further Reading

- Eloquent JS, Chapter 5: Higher-Order Functions
- javascript.info: Generators, Async iterators and generators
- MDN: Iterators and generators, function*
