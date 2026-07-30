---
title: "Control Flow, Operators, and Expressions"
description: "Conditionals, loops, operators, and expression evaluation — the building blocks of program logic."
type: lesson
order: 2
duration: "60 min"
difficulty: beginner
learning_objectives:
  - "Write conditional logic with if/else and switch statements"
  - "Master all loop types: for, while, do-while, for-in, for-of"
  - "Understand operator precedence and associativity"
  - "Apply short-circuit evaluation and the ternary operator"
knowledge_refs:
  - languages/javascript/js-02-control-flow-operators
prerequisites:
  - "JS-01: Values, Types, and Variables"
references:
    - title: "Eloquent JavaScript (4th Edition)"
      url: "https://eloquentjavascript.net/02_program_structure.html"
      chapters: "Chapter 2: Program Structure — Control Flow"
      description: "Introduction to conditionals, loops, and program flow"
    - title: "The Modern JavaScript Tutorial"
      url: "https://javascript.info/while-for"
      sections: "Conditional operators: if, ? | Logical operators | Loops: while and for | switch statement"
      description: "Step-by-step guide through all control flow constructs"
    - title: "MDN JavaScript Guide"
      url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling"
      sections: "Control flow and error handling | Loops and iteration | Expressions and operators"
      description: "Authoritative reference for all control structures"
    - title: "You Don't Know JS Yet"
      url: "https://github.com/getify/you-dont-know-js"
      chapters: "Get Started Ch. 2 — Surveying JS (Control Flow section)"
      description: "Deep look at how JS handles conditional and loop evaluation"
    - title: "Exploring JS: JavaScript for Programmers"
      url: "https://exploringjs.com/js/ch_control-flow.html"
      chapters: "[Ch. 7: Control Flow](https://exploringjs.com/js/ch_control-flow.html) | [Ch. 6: Operators](https://exploringjs.com/js/ch_operators.html)"
      description: "Comprehensive treatment of operators and control structures"
---

# JS-02: Control Flow, Operators, and Expressions

## Introduction

Control flow determines the order in which statements execute. JavaScript provides
conditionals (if, switch), loops (for, while), and structured error handling
(try/catch). Combined with operators and expression evaluation, these form the
backbone of every JS program.

## Subtopics

### 1. Conditional Statements

- **if/else if/else**: The workhorse of conditional logic
- **switch/case**: For multi-way branching — note `break` fallthrough!
- **Ternary operator**: `condition ? expr1 : expr2` — expression, not statement
- *Reference:* javascript.info — Conditional operators | [MDN — if...else](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export/Statements/export/Statements/if...else) | Eloquent JS Ch. 2

### 2. Logical Operators and Short-Circuit

- **`&&` (AND)**: Returns first falsy operand or last truthy
- **`||` (OR)**: Returns first truthy operand or last falsy
- **`??` (Nullish coalescing, ES2020)**: Returns right side only if left is `null` or `undefined`
- **Short-circuit evaluation**: `expr1 && expr2` — if expr1 is falsy, expr2 never evaluates
- *Reference:* [javascript.info — Logical operators](https://javascript.info/service-workersservice-workerslogical-operators) | MDN — Logical operators | YDKJSY Get Started
- *Deep dive:* `??` vs `||` — `??` only treats `null`/`undefined` as absent, while `||`
  treats all falsy values as absent. Use `??` for default values, `||` for fallbacks.

### 3. Loop Constructs

- **`for`**: Initialize; condition; increment — classic C-style loop
- **`while`**: Runs while condition is true
- **`do...while`**: Always runs at least once
- **`for...in`**: Iterates enumerable string properties (avoid on arrays!)
- **`for...of`** (ES6): Iterates iterables (arrays, strings, Maps, Sets)
- **`break`/`continue`**: Exit early or skip iteration
- *Reference:* javascript.info — Loops | MDN — Loops and iteration | Eloquent JS Ch. 2
- *Deep dive:* `for...in` iterates prototype properties! Always use `hasOwnProperty` check
  or prefer `for...of`/`Object.keys()` for arrays.

### 4. Operator Precedence and Associativity

- **Precedence**: Determines which operator runs first in `a + b * c`
- **Associativity**: Left-to-right (most) or right-to-left (assignment, `**`)
- **The operator precedence table**: MDN has the complete reference
- *Reference:* MDN — Operator Precedence | Exploring JS Ch. 6

### 5. Error Handling with try/catch

- **`try { riskyCode() } catch (err) { handle() } finally { cleanup() }`**
- The `finally` block always executes, even after `return` in `try`
- *Reference:* javascript.info — Error handling, "try..catch" | [MDN — try...catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export/Statements/export/Statements/try...catch)

## Practice Questions

1. What does `console.log(0 && "hello")` output? Why?
2. What is the difference between `null ?? "default"` and `null || "default"`?
3. Why should you avoid `for...in` for iterating arrays?
4. Trace the output: `for (let i = 0; i < 3; i++) { if (i === 1) continue; console.log(i); }`
5. Does `finally` run if `try` has a `return` statement? Demonstrate.

## LLM Prompts

1. **Socratic Tutor**: "I keep getting confused about when to use `==` vs `===`. Can you explain the Abstract Equality Comparison algorithm step by step?"
2. **Practice Generator**: "Give me 5 exercises to practice nested loops, starting with a multiplication table and getting progressively harder."
3. **Debugging Coach**: "My `for...in` loop over an array is returning extra indices that I didn't define. What's happening and how do I fix it?"

## Key Takeaways

- Use `===` for strict equality, avoid `==` unless you explicitly want coercion
- `for...of` is the safe way to iterate arrays; `for...in` is for object properties
- `??` is for null/undefined defaults; `||` is for any falsy fallback
- Operator precedence follows the table — use parentheses for clarity
- `finally` always runs, even after `return` in try/catch

## Further Reading

- Eloquent JS, Chapter 2: Program Structure
- javascript.info: Conditional operators, Logical operators, Loops
- MDN: Operator Precedence table
- YDKJSY: Get Started Ch. 2
