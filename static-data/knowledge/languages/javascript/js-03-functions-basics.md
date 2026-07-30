---
title: "Functions: Declarations, Scope, and Arrow Functions"
description: "Function declarations, expressions, arrow functions, parameters, and arguments — the core of JS modularity."
type: lesson
order: 3
duration: "60 min"
difficulty: beginner
learning_objectives:
  - "Declare and invoke functions using declarations, expressions, and arrow syntax"
  - "Understand default parameters, rest parameters, and the arguments object"
  - "Master function scope and the difference between var, let, and const in functions"
  - "Use pure functions and understand side effects"
knowledge_refs:
  - languages/javascript/js-03-functions-basics
prerequisites:
  - "JS-01: Values, Types, and Variables"
  - "JS-02: Control Flow"
references:
    - title: "Eloquent JavaScript (4th Edition)"
      url: "https://eloquentjavascript.net/03_functions.html"
      chapters: "Chapter 3: Functions"
      description: "The definitive beginner introduction to JS functions"
    - title: "The Modern JavaScript Tutorial"
      url: "https://javascript.info/function-basics"
      sections: "Functions | Function expressions | Arrow functions basics | Rest parameters and spread syntax"
      description: "Practical guide with examples for every function pattern"
    - title: "MDN JavaScript Guide"
      url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions"
      sections: "Functions | Closures | Using arguments object"
      description: "Authoritative reference on function declaration and invocation"
    - title: "You Don't Know JS Yet"
      url: "https://github.com/getify/you-dont-know-js"
      chapters: "Get Started Ch. 2 — Surveying JS (Functions section) | Scope & Closures — Ch. 3-4"
      description: "Deep dive into how functions create scope and closure"
    - title: "Exploring JS: JavaScript for Programmers"
      url: "https://exploringjs.com/js/ch_functions.html"
      chapters: "[Ch. 16: Functions](https://exploringjs.com/js/ch_functions.html)"
      description: "Comprehensive coverage of all function types and patterns"
---

# JS-03: Functions: Declarations, Scope, and Arrow Functions

## Introduction

Functions are the primary unit of code organization in JavaScript. They create scope,
encapsulate logic, and enable higher-order patterns. JavaScript has multiple function
forms: declarations, expressions, arrow functions, methods, and generators.

## Subtopics

### 1. Three Ways to Define a Function

- **Function declaration**: `function foo() {}` — hoisted, named, creates a binding in the enclosing scope
- **Function expression**: `const foo = function() {};` — not hoisted, can be anonymous or named
- **Arrow function** (ES6): `const foo = () => {};` — concise, lexically binds `this`, no `arguments` object
- *Reference:* [javascript.info — Functions](https://javascript.info/service-workersservice-workersfunction-basics), Function expressions | Eloquent JS Ch. 3
- *Deep dive:* Arrow functions are NOT just syntactic sugar — they differ in:
  1. `this` binding (lexical, not dynamic)
  2. No `arguments` object (use rest parameters)
  3. Cannot be used as constructors (no `new`)
  4. No `super` or `new.target`

### 2. Parameters and Arguments

- **Default parameters** (ES6): `function greet(name = "World") {}`
- **Rest parameters** (ES6): `function sum(...nums) {}` — gathers remaining args into an array
- **The `arguments` object**: Array-like (but not Array) — available in regular functions, NOT arrows
- **Spread operator** in calls: `Math.max(...[1, 2, 3])` — expands iterables
- *Reference:* javascript.info — Rest parameters, Spread syntax | Eloquent JS Ch. 3

### 3. Return Values and Side Effects

- **Pure functions**: Given same input, always same output; no side effects
- **Impure functions**: Modify external state, rely on I/O, mutate arguments
- **Implicit return** in arrow functions: `const double = x => x * 2`
- *Reference:* Eloquent JS Ch. 3 — "Functions grow on trees" | Exploring JS Ch. 16

### 4. Call Stack and Execution

- Every function call creates a new **execution context**
- The **call stack** tracks which function is currently executing
- Stack overflow: when recursion is too deep (typically ~10k frames)
- *Reference:* [javascript.info — Recursion and stack](https://javascript.info/service-workersservice-workersrecursion) | Eloquent JS Ch. 3

### 5. Recursion

- A function calling itself to solve smaller sub-problems
- Requires a **base case** to terminate
- Example: factorial, Fibonacci, tree traversal
- *Reference:* Eloquent JS Ch. 3 — "Functions and Side Effects" | javascript.info — Recursion

## Practice Questions

1. What is the difference between a function declaration and a function expression regarding hoisting?
2. Convert this to an arrow function: `function add(a, b) { return a + b; }`. Now what if it needs `this` context?
3. Write a function that accepts any number of arguments and returns their sum.
4. What does `const foo = () => {}; new foo();` do? Why?
5. Trace the call stack for `factorial(3)`.

## LLM Prompts

1. **Socratic Tutor**: "I'm confused about hoisting. Walk me through what happens when the JavaScript engine encounters `console.log(x); var x = 5;` versus `console.log(x); let x = 5;`"
2. **Comparison**: "When should I use an arrow function vs a regular function? Give me concrete scenarios from real React code."
3. **Debugging Coach**: "My function is returning `undefined` even though I have a return statement. Here's my code: `const double = (x) => { x * 2 }`. What's wrong?"

## Key Takeaways

- Function declarations are hoisted; function expressions and arrow functions are not
- Arrow functions lexically bind `this` — use for callbacks, avoid for methods
- Default/rest parameters and spread operator are ES6+ — prefer over `arguments`
- Pure functions are easier to test, reason about, and debug
- Every function call adds a stack frame — too much recursion = stack overflow

## Further Reading

- Eloquent JS, Chapter 3: Functions
- YDKJSY: Scope & Closures, Chapters 3-4
- javascript.info: Functions, Arrow functions, Rest/Spread
