---
title: "Type Coercion, Equality, and Grammar Deep Dive"
description: "The ECMAScript specification algorithms for type coercion, abstract equality, and the syntactic grammar of JavaScript."
type: lesson
order: 15
duration: "60 min"
difficulty: expert
level: Expert
learning_objectives:
  - "Read and understand ECMAScript specification algorithms for coercion"
  - "Predict coercion outcomes in complex expressions"
  - "Master the Abstract Equality Comparison algorithm"
  - "Understand the syntactic grammar rules: ASI, operator precedence, and context-dependent syntax"
knowledge_refs:
  - languages/javascript/js-expert-01-coercion-equality
prerequisites:
  - "JS-01 through JS-14"
references:
    - title: "You Don't Know JS Yet"
      url: "https://github.com/getify/you-dont-know-js"
      chapters: "Types & Grammar — ALL chapters (the definitive reference)"
      description: "The most comprehensive treatment of JS types, coercion, and grammar"
    - title: "The Modern JavaScript Tutorial"
      url: "https://javascript.info/"
      sections: "Type Conversions | Object to primitive conversion | Comparison operators"
      description: "Practical coverage of type conversion behavior"
    - title: "Exploring JS: JavaScript for Programmers"
      url: "https://exploringjs.com/js/"
      chapters: "Ch. 6: Operators | Ch. 7: Control Flow"
      description: "Detailed analysis of operator semantics"
    - title: "MDN JavaScript Reference"
      url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference"
      sections: "Expressions and operators — full section | Equality comparisons and sameness"
      description: "Complete reference for all operators and equality comparisons"
    - title: "TC39 ECMAScript Spec"
      url: "https://tc39.es/ecma262/"
      sections: "Section 7.1 — Type Conversion | Section 13 — Expressions (Abstract Equality, Relational Comparison)"
      description: "The official specification — ultimate authority on coercion and grammar"
---

# JS-15: Type Coercion, Equality, and Grammar Deep Dive

## Introduction

JavaScript's type coercion is often misunderstood as "magic" or "broken."
In reality, coercion follows precise, well-defined algorithms in the
ECMAScript specification. Understanding these algorithms separates
advanced developers from beginners.

## Subtopics

### 1. The ECMAScript Coercion Algorithms

- **ToPrimitive**: Object → primitive hint (default, number, string)
- **ToString**: `null → "null"`, `undefined → "undefined"`, `true → "true"`,
  `-0 → "0"`, `[] → ""`, `[1] → "1"`, `[1,2] → "1,2"`, `{} → "[object Object]"`
- **ToNumber**: `"42" → 42`, `"42px" → NaN`, `null → 0`, `undefined → NaN`,
  `true → 1`, `false → 0`, `"" → 0`, `" " → 0`, `[] → 0`, `[1] → 1`
- **ToBoolean**: Falsy: `false, 0, -0, 0n, "", null, undefined, NaN`. Everything else truthy.
- *Reference:* YDKJSY Types & Grammar Ch. 1-4 | TC39 Spec Sec. 7.1 | Exploring JS Ch. 5-6

### 2. Abstract Equality Comparison (`==`)

The `==` algorithm:
1. Same type? Use `===`
2. `null == undefined` → `true`
3. Number vs String: ToNumber(string)
4. Boolean vs anything: ToBoolean(boolean) → then recurse
5. Object vs String/Number: ToPrimitive(object) → then recurse

- `==` allows coercion; `===` does not
- `Object.is()`: Same-value-zero equality (distinguishes `-0` and `NaN` behavior)
- *Reference:* YDKJSY Types & Grammar Ch. 4 | TC39 Spec Sec. 13.11 | MDN — Equality comparisons

### 3. Syntactic Grammar

- **Automatic Semicolon Insertion (ASI)**: Rules for when semicolons are automatically inserted
  — at line terminators, before `}`, after `continue/break/return/throw`
- **TDZ for `let`/`const`**: Cannot access before declaration
- **Operator precedence**: The exact order operators evaluate
- **Associativity**: Left-to-right vs right-to-left
- *Reference:* YDKJSY Types & Grammar Ch. 5 | TC39 Spec Sec. 13 (all expressions)

### 4. Common Coercion Patterns

- `+value` — unary plus coerces to number
- `"" + value` — quick string coercion
- `!!value` — double negation for boolean coercion
- `value || default` — falsy default (use `??` for null/undefined only)
- `value == null` — check for null OR undefined (not falsy check!)

## Practice Questions

1. Trace the coercions in: `[] == ![]` (hint: it evaluates to true)
2. Why does `Object.is(-0, 0)` return `false` but `-0 === 0` returns `true`?
3. What happens when `"1" + 2 + 3` evaluates? What about `1 + 2 + "3"`?
4. Use the spec algorithm to explain `3 == "03"` and `3 == "3.0"`.

## Key Takeaways

- `==` has a well-defined coercion algorithm — it's not "broken" but you must learn it
- `===` is for no-coercion equality; `Object.is()` for absolute identity
- ASI inserts semicolons at line breaks when the grammar requires them
- `+value` coerces to number; `"" + value` coerces to string
- `value == null` is the safe way to check for null OR undefined

## Further Reading

- YDKJSY: Types & Grammar (entire book — the definitive reference)
- TC39 ECMAScript Spec: Sections 7.1 (Type Conversion) and 13 (Expressions)
- MDN: Equality comparisons and sameness
- Exploring JS: Chapters 5-7
