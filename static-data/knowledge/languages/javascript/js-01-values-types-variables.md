---
title: "Values, Types, and Variables"
description: "Core JavaScript values — primitives, objects, type system, and variable declarations (var, let, const). Set up your dev environment and write your first program."
type: lesson
order: 1
duration: "60 min"
difficulty: beginner
learning_objectives:
  - "Understand JavaScript's dynamic type system and the 7 primitive types"
  - "Master variable declarations: var, let, const, and block scoping rules"
  - "Distinguish between primitive values and object references"
  - "Set up Node.js and a code editor to run JavaScript programs"
knowledge_refs:
  - languages/javascript/js-01-values-types-variables
prerequisites:
  - "None — this is the entry point"
references:
    - title: "Eloquent JavaScript (4th Edition)"
      url: "https://eloquentjavascript.net/01_values.html"
      chapters: "Chapter 1: Values, Types, and Operators | Chapter 2: Program Structure"
      description: "Introduction to JS values and basic program structure with practical examples"
    - title: "You Don't Know JS Yet"
      url: "https://github.com/getify/you-dont-know-js/blob/2nd-ed/get-started/ch2.md"
      chapters: "Get Started, Chapter 2: Surveying JS — Values & Types"
      description: "Deep dive into JS types and how variables actually work at the engine level"
    - title: "The Modern JavaScript Tutorial"
      url: "https://javascript.info/variables"
      sections: "Variables | Data types | Type Conversions | Comparisons | Primitives vs Objects"
      description: "Practical step-by-step guide through variable declaration and type behavior"
    - title: "MDN JavaScript Guide"
      url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_Types"
      sections: "Grammar and Types | Expressions and Operators — Assignment | Numbers and Strings"
      description: "The authoritative reference for JS syntax, declarations, and type semantics"
    - title: "MDN JavaScript Reference"
      url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let"
      sections: "Statements: var, let, const | Global Objects: Number, String, Boolean | Operators: typeof, delete, void"
      description: "Complete specification-level reference for all built-in types and declarations"
    - title: "Exploring JS: JavaScript for Programmers"
      url: "https://exploringjs.com/js/ch_values.html"
      chapters: "[Ch. 5: Values](https://exploringjs.com/js/ch_values.html) | [Ch. 6: Operators](https://exploringjs.com/js/ch_operators.html) | [Ch. 8: Numbers](https://exploringjs.com/js/ch_numbers.html) | [Ch. 9: Strings](https://exploringjs.com/js/ch_strings.html)"
      description: "Detailed analysis of JS value semantics and type behavior by Dr. Axel Rauschmayer"
---

# JS-01: Values, Types, and Variables

## Introduction

JavaScript is a dynamically-typed language with a small set of primitive types and
objects. Understanding how values behave — when they're copied, when they're
referenced, and how type coercion works — is the foundation of all JS programming.

## Subtopics

### 1. The JavaScript Runtime

- **Node.js** for server-side execution: install via `nvm`, `fnm`, or official installer
- **Browser console** (DevTools) for quick experimentation
- **Online playgrounds**: CodePen, JSFiddle, StackBlitz
- *Reference:* javascript.info — DevTools | Eloquent JS — Introduction

### 2. Seven Primitive Types

| Type | Examples | Notes |
|------|----------|-------|
| `undefined` | `let x;` | Default value of uninitialized variables |
| `null` | `let x = null;` | Explicit "no value" |
| `boolean` | `true`, `false` | Logical values |
| `number` | `42`, `3.14`, `Infinity`, `NaN` | IEEE-754 double precision |
| `bigint` | `42n` | Arbitrary precision integers (ES2020) |
| `string` | `"hello"`, `'world'`, \`template\` | UTF-16 encoded text |
| `symbol` | `Symbol("desc")` | Unique, immutable identifiers |

- *Reference:* [MDN — Grammar and Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules/Modules/Grammar_and_Types) | [YDKJSY — Get Started Ch. 2](https://github.com/getify/you-dont-know-js/blob/2nd-ed/types-grammar/ch1.md/blob/2nd-ed/types-grammar/ch1.md/blob/2nd-ed/get-started/ch2.md)
- *Deep dive:* All types are primitives EXCEPT `object`. Everything else is a value,
  copied by value. Objects are copied by reference.
- *Gotcha:* `typeof null === "object"` — a historical bug preserved for compatibility.
  See YDKJSY — Types & Grammar for the full story.

### 3. Variable Declarations: `var`, `let`, `const`

- **`var`**: Function-scoped, hoisted to the top of its function. Can be redeclared.
  Avoid in modern code except for legacy patterns.
- **`let`**: Block-scoped, not hoisted in the traditional sense. Temporal Dead Zone (TDZ)
  between the block start and the declaration.
- **`const`**: Block-scoped, must be initialized at declaration. The binding is constant,
  not the value — objects and arrays declared with `const` can still be mutated.

- *Reference:* [javascript.info — Variables](https://javascript.info/service-workersservice-workersvariables) | [MDN — let](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export/Statements/export/Statements/let), const | [YDKJSY — Scope & Closures Ch. 6](https://github.com/getify/you-dont-know-js/blob/2nd-ed/types-grammar/ch1.md/blob/2nd-ed/types-grammar/ch1.md/blob/2nd-ed/scope-closures/ch6.md)
- *Deep dive:* See [YDKJSY — Scope & Closures Ch. 6](https://github.com/getify/you-dont-know-js/blob/2nd-ed/types-grammar/ch1.md/blob/2nd-ed/types-grammar/ch1.md/blob/2nd-ed/scope-closures/ch6.md) "The (Not So) Secret Lifecycle of Variables"
  for a complete walkthrough of hoisting, TDZ, and redeclaration rules.

### 4. Type Coercion Basics

- **Explicit coercion**: `Number("42")`, `String(true)`, `Boolean(0)`
- **Implicit coercion**: `"5" - 2` → `3`, `"5" + 2` → `"52"`
- **Truthy vs Falsy**: `false`, `0`, `""`, `null`, `undefined`, `NaN` are falsy.
  Everything else is truthy.
- *Reference:* [javascript.info — Type Conversions](https://javascript.info/service-workersservice-workerstype-conversions) | [YDKJSY — Types & Grammar Ch. 4](https://github.com/getify/you-dont-know-js/blob/2nd-ed/types-grammar/ch1.md/blob/2nd-ed/types-grammar/ch1.md/blob/2nd-ed/types-grammar/ch4.md)
- *Deep dive:* `==` vs `===` — YDKJSY argues `==` is not "loose equality" but rather
  "coercive equality" with a well-defined algorithm. Study the Abstract Equality
  Comparison algorithm in the spec.

### 5. Objects vs Primitives

- Primitives are **immutable** and **compared by value**
- Objects are **mutable** and **compared by reference**
- Autoboxing: When you access a property on a primitive (e.g., `"hello".length`),
  JS temporarily wraps it in its corresponding object type (`String` object).

- *Reference:* Eloquent JS Ch. 4 | MDN — Working with Objects | [javascript.info — Objects](https://javascript.info/service-workersservice-workersobject)

## Practice Questions

1. What does `typeof null` return? Why is this the case historically?
2. Explain the Temporal Dead Zone with `let`. How does it differ from `var` hoisting?
3. Why is `"5" - 2` equal to `3` but `"5" + 2` equal to `"52"`?
4. What does `const arr = [1,2,3]; arr.push(4)` do? Is this valid? Why?
5. Trace the coercions in: `(![] + [])[+[]]` (the famous JS wtf moment).

## LLM Prompts for Deeper Exploration

1. **Socratic Tutor**: "I don't understand why `typeof null === 'object'`. Walk me through the history of how JavaScript was created at Netscape and why this bug was never fixed."
2. **Concept Explainer**: "Explain the difference between `undefined` and `null` as if I'm a beginner. Use analogies involving empty containers and missing labels."
3. **Debugging Coach**: "I wrote `let x = 5; let y = x; y = 10;` but `x` is still `5`. I thought variables were just containers. What's happening?"

## Key Takeaways

- JavaScript has 7 primitive types (plus Object) — all non-object values are primitives
- `let` and `const` are block-scoped with TDZ; `var` is function-scoped
- Primitives are immutable and compared by value; Objects are mutable and compared by reference
- Type coercion follows well-defined rules — understanding them prevents bugs

## Further Reading

- Eloquent JavaScript, Chapter 1: Values, Types, and Operators
- YDKJSY: Get Started, Chapter 2 — Surveying JS
- javascript.info: Variables, Data types, Type Conversions
- MDN: Grammar and Types — https://mzl.la/grammar-types
- Exploring JS: Chapters 5-9 on values, operators, numbers, strings
