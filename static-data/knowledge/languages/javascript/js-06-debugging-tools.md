---
title: "Debugging, Errors, and Developer Tools"
description: "Browser DevTools, error types, try/catch/finally, stack traces, and debugging strategies."
type: lesson
order: 6
duration: "45 min"
difficulty: beginner
learning_objectives:
  - "Use Chrome/Firefox DevTools effectively: breakpoints, watch, call stack"
  - "Distinguish between SyntaxError, ReferenceError, TypeError, and RangeError"
  - "Implement robust error handling with try/catch/finally"
  - "Read and interpret stack traces to locate bugs"
knowledge_refs:
  - languages/javascript/js-06-debugging-tools
prerequisites:
  - "JS-01 through JS-05"
references:
    - title: "Eloquent JavaScript (4th Edition)"
      url: "https://eloquentjavascript.net/08_error.html"
      chapters: "Chapter 8: Bugs and Errors"
      description: "Debugging techniques, strict mode, and error handling patterns"
    - title: "The Modern JavaScript Tutorial"
      url: "https://javascript.info/try-catch"
      sections: "Debugging in Chrome | Error handling, "try...catch" | Custom errors"
      description: "Practical debugging walkthroughs and error handling guide"
    - title: "MDN JavaScript Guide"
      url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling"
      sections: "Control flow and error handling — Error types"
      description: "Complete reference for Error objects and handling patterns"
---

# JS-06: Debugging, Errors, and Developer Tools

## Introduction

Even experienced developers spend more time debugging than writing new code.
Mastering DevTools, understanding error types, and writing defensive code
is essential for productive JavaScript development.

## Subtopics

### 1. Error Types in JavaScript

- **SyntaxError**: Invalid language syntax — caught at parse time
- **ReferenceError**: Accessing an undeclared variable or TDZ violation
- **TypeError**: Operation on incompatible type (e.g., `null.foo`, calling a non-function)
- **RangeError**: Value out of allowed range (e.g., `Array(-1)`)
- **URIError**: Invalid URI handling
- **Custom errors**: Extend `Error` class for domain-specific errors
- *Reference:* [MDN — Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export/Statements/export/Global_Objects/Error) | javascript.info — Custom errors | Eloquent JS Ch. 8

### 2. try/catch/finally

- **`try { riskyCode }`** — wrap potentially failing code
- **`catch (err) { handle }`** — catch and handle errors gracefully
- **`finally { cleanup }`** — always executes, great for release resources
- **Optional catch binding** (ES10): `catch { /* no error variable needed */ }`
- *Reference:* javascript.info — Error handling | [MDN — try...catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export/Statements/export/Statements/try...catch)

### 3. Browser DevTools

- **Elements tab**: Inspect and modify DOM/CSS in real time
- **Console tab**: REPL, `console.log/table/time/group`, error messages
- **Sources tab**: Set breakpoints, step through code, watch variables, examine call stack
- **Network tab**: Monitor HTTP requests, inspect responses, simulate offline
- **Performance tab**: Record and analyze runtime performance, frame rate
- *Reference:* javascript.info — Debugging in Chrome | Eloquent JS Ch. 8

### 4. Debugging Strategies

- **Rubber duck debugging**: Explain the problem to someone/something
- **Divide and conquer**: Isolate the failing code section with binary search
- **Console.debugging**: Strategic `console.log` with labels
- **Breakpoints**: Conditional breakpoints, logpoints (console without pausing)
- **Stack trace analysis**: Read the call stack from bottom (initiator) to top (error)
- *Reference:* Eloquent JS Ch. 8 — strict mode, debugging tips

## Key Takeaways

- Four main error types: Syntax, Reference, TypeError, Range — learn to identify each
- `try/catch/finally` for graceful error handling; `finally` always runs
- DevTools Sources tab is more powerful than `console.log` for complex bugs
- A stack trace tells you exactly which functions were called — read it bottom-up
- Strict mode (`"use strict"`) catches common errors and prevents silent failures

## Further Reading

- Eloquent JS, Chapter 8: Bugs and Errors
- javascript.info: Error handling, Debugging in Chrome
- MDN: Error, try...catch, console
