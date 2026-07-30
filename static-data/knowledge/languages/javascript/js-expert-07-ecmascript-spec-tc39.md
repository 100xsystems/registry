---
title: "ECMAScript Specification, TC39, and Future Proposals"
description: "Navigating the ECMAScript specification, the TC39 standardization process, reading spec algorithms, and exploring future proposals."
type: lesson
order: 21
duration: "60 min"
difficulty: expert
level: Expert
learning_objectives:
  - "Navigate the ECMAScript specification to find and read algorithm definitions"
  - "Understand the TC39 proposal process from Stage 0 to Stage 4"
  - "Read and implement spec algorithms in JavaScript"
  - "Evaluate current Stage 3 proposals for future-readiness"
knowledge_refs:
  - languages/javascript/js-expert-07-ecmascript-spec-tc39
prerequisites:
  - "All previous lessons (JS-01 through JS-20)"
references:
    - title: "TC39 ECMAScript Spec"
      url: "https://tc39.es/ecma262/"
      sections: "Full specification — all sections"
      description: "The official JavaScript specification — ultimate authority"
    - title: "TC39 Proposals Repository"
      url: "https://github.com/tc39/proposals"
      sections: "Active proposals by stage | Finished proposals | ECMA-262 and ECMA-402"
      description: "Track all proposals through the standardization pipeline"
    - title: "MDN JavaScript Reference"
      url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference"
      sections: "All built-in objects, statements, operators"
      description: "Spec-backed reference for all JavaScript features"
    - title: "You Don't Know JS Yet"
      url: "https://github.com/getify/you-dont-know-js"
      chapters: "ES.Next & Beyond — Ch. 1: ES? Now & Future"
      description: "Overview of the TC39 process and what to expect in future JS"
---

# JS-21: ECMAScript Specification, TC39, and Future Proposals

## Introduction

The ECMAScript Language Specification (ECMA-262) is the definitive reference for
JavaScript. Understanding how to read it, how proposals become standard, and what
features are coming next separates expert developers from the rest.

## Subtopics

### 1. ECMA-262 Specification Structure

- **Clauses 1-4**: Scope, conformance, references, definitions
- **Clause 5**: Notational conventions — how algorithms are written
- **Clauses 6-7**: Language types, type conversion (ToPrimitive, ToString, ToNumber, etc.)
- **Clauses 8-12**: Execution contexts, lexical environments, JS source code, grammar
- **Clause 13**: Expressions (Primary, Left-Hand-Side, Unary, Binary, Conditional, Assignment)
- **Clauses 14-16**: Statements, declarations, function definitions, class definitions
- **Clauses 17-19**: Scripts, modules, the runtime execution model
- **Clauses 20-28**: Built-in objects (Object, Array, Function, Promise, Proxy, etc.)

- *Reference:* [tc39.es/ecma262/](https://tc39.es/ecma262/) — The living specification

### 2. Reading Spec Algorithms

The spec uses a custom notation for algorithms:

```javascript
// Example: Array.prototype.map spec algorithm
1. Let O = ? ToObject(this value)
2. Let len = ? LengthOfArrayLike(O)
3. If IsCallable(callbackfn) is false, throw a TypeError
4. Let A = ? ArrayCreate(len)
5. Let k = 0
6. Repeat while k < len
  a. Let Pk = ! ToString(k)
  b. Let kPresent = ? HasProperty(O, Pk)
  c. If kPresent is true
    i. Let kValue = ? Get(O, Pk)
    ii. Let mappedValue = ? Call(callbackfn, thisArg, kValue, k, O)
    iii. Perform ? CreateDataPropertyOrThrow(A, Pk, mappedValue)
  d. Set k = k + 1
7. Return A
```

- `?` denotes operation may return abrupt completion (throw)
- `!` denotes operation always returns normal completion
- `[[Notation]]` denotes internal slots/methods
- *Reference:* ECMA-262 Clause 5 — Notational conventions

### 3. TC39 Proposal Process

- **Stage 0 (Strawperson)**: Any idea — no champion required
- **Stage 1 (Proposal)**: Champion identified, problems described, high-level API sketched
- **Stage 2 (Draft)**: Formal spec language written, semantics fully described
- **Stage 3 (Candidate)**: Spec complete, implementation feedback collected, refinements made
- **Stage 4 (Finished)**: Two independent implementations, merged into spec, ready in next ES release
- **Stage 0 → 4 typically takes 2-4 years**
- *Reference:* [TC39 Proposals](https://github.com/tc39/proposals) — GitHub repository
  | YDKJSY ES.Next Ch. 1 — Overview of the process

### 4. Notable Current Proposals (2026)

- **Records & Tuples**: Immutable data structures `#{ x: 1 }` and `#[1, 2, 3]`
- **Decorators**: Annotations for classes, methods, and fields
- **Pattern Matching**: `match (value) { when (pattern) => ... }`
- **RegExp Escaping**: `RegExp.escape(str)` for safe regex creation
- **Import Attributes**: `import json from "./data.json" with { type: "json" }`
- *Reference:* TC39 proposals repository — Stage 2/3 proposals

## Practice Questions

1. Find and read the `Object.is` algorithm in the spec (Clause 20). What makes it different from `===`?
2. Trace the `Array.prototype.reduce` spec algorithm — identify where the initial value check happens.
3. Pick a Stage 3 proposal from the TC39 repository. Summarize the problem it solves and its proposed API.

## Key Takeaways

- The ECMAScript spec is the ultimate authority — learn to navigate it
- TC39 proposals go through 5 stages before becoming standard
- Spec algorithms use `?` for throwable operations and `!` for guaranteed operations
- Follow TC39 proposals to stay ahead of JavaScript evolution
- Understanding the spec enables confident reasoning about edge cases

## Further Reading

- [tc39.es/ecma262/](https://tc39.es/ecma262/) — The living specification
- [TC39 Proposals on GitHub](https://github.com/tc39/proposals)
- YDKJSY: ES.Next & Beyond, Chapter 1
- MDN: JavaScript Reference (spec-backed)
- Exploring JS: appendices on ES6+ specification details
