---
title: "Deep Scope, Hoisting, and Closures"
description: "Lexical scope, hoisting mechanics, closure patterns, IIFEs, and the module pattern."
type: lesson
order: 8
duration: "75 min"
difficulty: intermediate
learning_objectives:
  - "Understand compilation-phase scope binding vs execution-phase"
  - "Master closure: definition, lifecycle, and common use cases"
  - "Implement the module pattern using closures and IIFEs"
  - "Explain Temporal Dead Zone and its relationship to hoisting"
knowledge_refs:
  - languages/javascript/js-08-scope-closures
prerequisites:
  - "JS-03: Functions"
  - "JS-04: Objects and Arrays"
references:
    - title: "You Don't Know JS Yet"
      url: "https://github.com/getify/you-dont-know-js/blob/2nd-ed/scope-closures/ch1.md"
      chapters: "Scope & Closures — ALL chapters (the definitive reference)"
      description: "The most comprehensive treatment of scope and closures in any JS book"
    - title: "Eloquent JavaScript (4th Edition)"
      url: "https://eloquentjavascript.net/03_functions.html"
      chapters: "Chapter 3: Functions (closure section) | Chapter 10: Modules"
      description: "Practical closure examples and the module pattern"
    - title: "The Modern JavaScript Tutorial"
      url: "https://javascript.info/closure"
      sections: "Closure | Variable scope, closure | Module patterns"
      description: "Interactive examples of closure in action"
    - title: "MDN JavaScript Guide"
      url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures"
      sections: "Functions — Closures | Advanced topics — Closures"
      description: "Authoritative guide on closure mechanics"
---

# JS-08: Deep Scope, Hoisting, and Closures

## Introduction

Scope determines where variables are visible. JavaScript uses lexical scoping:
scope is determined by where code is written, not where it's called. Closures
are functions that retain access to variables from their lexical scope even
when executed outside that scope.

## Subtopics

### 1. Compilation and Scope

- JavaScript is **compiled** before execution — scope is determined at compile time
- Three players: **Engine** (compiles/executes), **Compiler** (parses, generates scope), **Scope Manager** (tracks identifiers)
- LHS vs RHS references: LHS (assignment target: `a = 2`) vs RHS (source: `console.log(a)`)
- *Reference:* [YDKJSY — Scope & Closures Ch. 1](https://github.com/getify/you-dont-know-js/blob/2nd-ed/types-grammar/ch1.md/blob/2nd-ed/types-grammar/ch1.md/blob/2nd-ed/scope-closures/ch1.md)-2 | The definitive treatment

### 2. Lexical Scope

- Scope is a series of **nested bubbles**
- Inner bubbles can access outer bubbles, but not vice versa
- The global scope is the outermost bubble
- `eval()` and `with` can "cheat" lexical scope — avoid them
- *Reference:* [YDKJSY — Scope & Closures Ch. 2](https://github.com/getify/you-dont-know-js/blob/2nd-ed/types-grammar/ch1.md/blob/2nd-ed/types-grammar/ch1.md/blob/2nd-ed/scope-closures/ch2.md) | [javascript.info — Closure](https://javascript.info/service-workersservice-workersclosure)

### 3. Function vs Block Scope

- `var` is function-scoped — visible throughout the entire enclosing function
- `let`/`const` are block-scoped — visible only within the enclosing `{ }`
- IIFE (Immediately Invoked Function Expression): Create a scope boundary on the fly
- `try/catch` creates block scope for the catch variable
- *Reference:* [YDKJSY — Scope & Closures Ch. 3](https://github.com/getify/you-dont-know-js/blob/2nd-ed/types-grammar/ch1.md/blob/2nd-ed/types-grammar/ch1.md/blob/2nd-ed/scope-closures/ch3.md)-4

### 4. Hoisting and the Temporal Dead Zone

- **Variable hoisting**: `var` declarations are "moved" to the top of their scope (but not initialization)
- **Function hoisting**: Function declarations are fully hoisted (name AND body)
- **TDZ**: `let`/`const` exist in the scope from the start but cannot be accessed until the declaration
- *Reference:* [YDKJSY — Scope & Closures Ch. 6](https://github.com/getify/you-dont-know-js/blob/2nd-ed/types-grammar/ch1.md/blob/2nd-ed/types-grammar/ch1.md/blob/2nd-ed/scope-closures/ch6.md) | [javascript.info — Variables](https://javascript.info/service-workersservice-workersvariables) — Hoisting

### 5. Closures

- **Definition**: A closure is created when a function "remembers" its lexical scope
  even when the function is executed outside that scope
- **Lifecycle**: Variables referenced by closures persist as long as any closure references them
  (prevents garbage collection)
- **Common patterns**: Callbacks, event handlers, module pattern, partial application, memoization
- *Reference:* [YDKJSY — Scope & Closures Ch. 5](https://github.com/getify/you-dont-know-js/blob/2nd-ed/types-grammar/ch1.md/blob/2nd-ed/types-grammar/ch1.md/blob/2nd-ed/scope-closures/ch5.md) | Eloquent JS Ch. 3 | [javascript.info — Closure](https://javascript.info/service-workersservice-workersclosure)

### 6. The Module Pattern

- **Classic module**: IIFE that returns an object with methods —
  the methods close over private variables
- **ES Modules**: Native module system with `export`/`import`
- **Revealing module pattern**: Return an object with method names mapped to
  internal function references
- *Reference:* [YDKJSY — Scope & Closures Ch. 8](https://github.com/getify/you-dont-know-js/blob/2nd-ed/types-grammar/ch1.md/blob/2nd-ed/types-grammar/ch1.md/blob/2nd-ed/scope-closures/ch8.md) | Eloquent JS Ch. 10 | [javascript.info — Modules](https://javascript.info/service-workersservice-workersmodules-intro)

## Practice Questions

1. What will `console.log(x)` output if `var x = 5`? If `let x = 5`? Before or after the declaration?
2. Write a function `counter()` that returns an object with `increment()`, `decrement()`, and `getCount()` methods — all sharing private state via closure.
3. Explain why `for (var i = 0; i < 5; i++) { setTimeout(() => console.log(i), 100); }` logs 5 five times. How do you fix it with `let`? With a closure?
4. Does `let` hoist? If so, how is it different from `var` hoisting?

## Key Takeaways

- JavaScript scope is determined at compile time (lexical), not at runtime
- Closures "remember" their lexical scope — they keep variables alive
- The module pattern uses closures to create private state
- `let`/`const` are block-scoped with TDZ; `var` is function-scoped with hoisting

## Further Reading

- YDKJSY: Scope & Closures (entire book — the definitive reference)
- Eloquent JS, Chapter 3: Functions
- javascript.info: Closure, Variable scope
- MDN: Closures
