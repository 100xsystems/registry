---
title: "Error Handling and Defensive Programming"
description: "Robust error handling strategies, custom error types, defensive programming, and fault-tolerant design patterns."
type: lesson
order: 18
duration: "45 min"
difficulty: expert
learning_objectives:
  - "Design a custom error hierarchy extending the Error class"
  - "Implement the Result type pattern for functional error handling"
  - "Build asynchronous error boundaries and circuit breakers"
  - "Apply defensive programming: assertions, contracts, and input validation"
knowledge_refs:
  - languages/javascript/js-18-error-patterns
prerequisites:
  - "JS-06: Debugging"
  - "JS-10: Async"
references:
    - title: "The Modern JavaScript Tutorial"
      url: "https://javascript.info/custom-errors"
      sections: "Error handling, try..catch | Custom errors, extending Error"
      description: "Practical error handling patterns and custom error types"
    - title: "MDN JavaScript Guide"
      url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling"
      sections: "Control flow and error handling — Error types, try/catch/throw"
      description: "Authoritative reference for all JavaScript error handling"
    - title: "Eloquent JavaScript (4th Edition)"
      url: "https://eloquentjavascript.net/"
      chapters: "Chapter 8: Bugs and Errors"
      description: "Debugging strategies and error handling philosophy"
---

# JS-18: Error Handling Patterns and Defensive Programming

## Introduction

Robust software anticipates failures. JavaScript provides try/catch/finally
for handling exceptions, but production-grade error handling requires patterns
for error classification, recovery, and fault tolerance.

## Subtopics

### 1. Custom Error Hierarchy

- Extend `Error` for domain-specific errors: `class ValidationError extends Error { ... }`
- Add properties: `statusCode`, `code`, `details`, `timestamp`, `cause`
- `Error.cause` (ES2022): Chain errors: `throw new Error("Failed", { cause: originalError })`
- *Reference:* javascript.info — Custom errors | [MDN — Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export/Statements/export/Global_Objects/Error), Error.cause

### 2. The Result Type Pattern

- Instead of throwing, return `{ success: true, data }` or `{ success: false, error }`
- Enables type-safe error handling with discriminated unions in TypeScript
- Avoids unexpected thrown exceptions — errors are data
- *Reference:* Rust's Result type pattern adapted to JS/TS

### 3. Async Error Boundaries

- `try/catch` in async functions — wraps entire function body
- `window.onerror` and `window.onunhandledrejection` — global error handlers
- `process.on("uncaughtException")` and `process.on("unhandledRejection")` — Node.js
- **Circuit breaker pattern**: After N failures, stop trying for a cooldown period
- **Retry with exponential backoff**: `retry(fn, { retries: 3, backoff: "exponential" })`
- *Reference:* MDN — GlobalEventHandlers.onerror | Node.js — process events

### 4. Defensive Programming

- **Assertions**: `console.assert(condition, message)` — log if condition fails
- **Input validation**: Check function arguments at entry points
- **Guard clauses**: Return early for invalid inputs instead of deep nesting
- **Fail-fast vs fail-soft**: When to crash vs when to continue with degraded behavior
- *Reference:* Eloquent JS Ch. 8 — defensive programming strategies

## Practice Questions

1. Design an `HttpError` hierarchy: `NetworkError`, `AuthError`, `RateLimitError`, `ServerError`.
2. Implement a `Result` class with `ok(value)` and `err(error)` static constructors.
3. Write a `retry` wrapper with exponential backoff and max retries.

## Key Takeaways

- Use custom Error subclasses for different failure modes
- The Result type pattern makes errors explicit in the type signature
- Circuit breakers and retries with backoff are essential for production systems
- Defensive programming: validate early, fail close to the source
- `Error.cause` chains errors without losing context
