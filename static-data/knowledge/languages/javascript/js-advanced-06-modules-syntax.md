---
title: "ES6+ Modules and Modern Syntax"
description: "ES modules, modern syntax features (optional chaining, nullish coalescing, logical assignment), and the evolution of JavaScript."
type: lesson
order: 13
duration: "60 min"
difficulty: intermediate
level: Advanced
learning_objectives:
  - "Export and import using all ESM patterns (named, default, dynamic)"
  - "Use modern syntax: optional chaining, nullish coalescing, logical assignment"
  - "Understand module resolution, circular dependencies, and tree-shaking"
  - "Distinguish ESM from CommonJS and other module systems"
knowledge_refs:
  - languages/javascript/js-advanced-06-modules-syntax
prerequisites:
  - "JS-01 through JS-08"
  - "JS-10: Async"
references:
    - title: "The Modern JavaScript Tutorial"
      url: "https://javascript.info/"
      sections: "Modules — full section | Optional chaining | Nullish coalescing operator | Rest parameters and spread"
      description: "Practical guide to ES modules and modern syntax"
    - title: "MDN JavaScript Guide"
      url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"
      sections: "JavaScript modules | Expressions and operators — Optional chaining, Nullish coalescing"
      description: "Authoritative reference for all module patterns and syntax"
    - title: "Exploring JS: JavaScript for Programmers"
      url: "https://exploringjs.com/js/"
      chapters: "Ch. 12: Destructuring | Ch. 15: Modules"
      description: "Comprehensive coverage of ES6+ syntax features"
    - title: "You Don't Know JS Yet"
      url: "https://github.com/getify/you-dont-know-js"
      chapters: "ES.Next & Beyond — Ch. 2: Syntax, Ch. 3: Organization (ES Modules)"
      description: "Deep dive into ES module mechanics and syntax evolution"
---

# JS-13: ES6+ Modules and Modern Syntax

## Introduction

ECMAScript 2015 (ES6) introduced a module system, modern syntax features, and
new APIs that fundamentally changed JavaScript development. Understanding these
features is essential for writing idiomatic modern JavaScript.

## Subtopics

### 1. ES Modules (ESM)

- **Named exports**: `export const foo = 42; export function bar() {}`
- **Default export**: `export default class {}` — one per module
- **Named imports**: `import { foo, bar } from "./module.js"`
- **Default import**: `import Default from "./module.js"`
- **Namespace import**: `import * as Utils from "./module.js"`
- **Dynamic import**: `const module = await import("./dynamic.js")`
- **Import assertions**: `import data from "./data.json" assert { type: "json" }`
- **Re-exporting**: `export { foo } from "./module.js"` — barrel pattern
- *Reference:* javascript.info — Modules | MDN — JavaScript modules | Exploring JS Ch. 15

### 2. ESM vs CommonJS

| Feature | ESM | CommonJS (require) |
|---------|-----|-------------------|
| Syntax | import/export | require()/module.exports |
| Loading | Static (parse-time) | Dynamic (runtime) |
| Async | Static is sync, dynamic import() is async | Synchronous |
| Tree-shaking | Native support | Not supported |
| `this` at top-level | `undefined` | `module.exports` |
| File extension | `.mjs` or `"type": "module"` in package.json | `.cjs` by default |

- *Reference:* MDN — JavaScript modules guide | Node.js — ESM documentation

### 3. Modern Syntax Features

- **Optional chaining** `?.` (ES2020): `obj?.prop?.nested` — short-circuits on null/undefined
- **Nullish coalescing** `??` (ES2020): `val ?? "default"` — only null/undefined trigger default
- **Logical assignment** (ES2021): `x ||= y`, `x &&= y`, `x ??= y`
- **Numeric separators** (ES2021): `1_000_000` for readability
- **Top-level await** (ES2022): `await` at module top level
- **Array.at()** (ES2022): `arr.at(-1)` — negative indexing
- **Error cause** (ES2022): `throw new Error("msg", { cause: originalError })`
- **Records and Tuples** (proposal): Immutable data structures
- *Reference:* javascript.info — Optional chaining, ?., ?? | MDN — ES2020-2023 features

### 4. Module Resolution and Bundling

- **Node.js module resolution**: looks in `node_modules`, respects `exports` field in package.json
- **Barrel files**: `index.js` that re-exports from multiple modules
- **Circular dependencies**: Works in ESM if exports are initialized before the cycle
- **Tree-shaking**: Bundlers remove unused exports — requires ESM syntax

## Practice Questions

1. What's the difference between `export default` and `export { default }`?
2. Why does `import { readFile } from "fs"` work, but dynamic `import("fs")` returns a module namespace object?
3. When would you use `x ??= y` vs `x ||= y`?
4. How does `obj?.method?.()` differ from `obj.method && obj.method()`?

## Key Takeaways

- ESM is statically analyzable — enables tree-shaking and better optimizations
- `?.` short-circuits on null/undefined; `??` defaults only for null/undefined
- Dynamic `import()` enables code splitting and lazy loading
- Use `.mjs` or `"type": "module"` for ESM in Node.js

## Further Reading

- javascript.info: Modules (full section)
- MDN: JavaScript modules guide
- Exploring JS: Chapter 15: Modules
- Node.js: ESM documentation
