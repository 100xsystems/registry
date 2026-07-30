---
title: "Metaprogramming: Proxy, Reflect, and Symbols"
description: "Metaprogramming with Proxy, Reflect API, well-known Symbols, and property descriptors — intercepting and customizing language-level operations."
type: lesson
order: 17
duration: "60 min"
difficulty: expert
level: Expert
learning_objectives:
  - "Use Proxy to intercept object operations: get, set, apply, construct, delete"
  - "Apply Reflect for safe default behavior and forwarding"
  - "Leverage well-known Symbols (Symbol.iterator, Symbol.hasInstance, Symbol.toPrimitive)"
  - "Define property semantics with property descriptors and Object.defineProperty"
knowledge_refs:
  - languages/javascript/js-expert-03-metaprogramming
prerequisites:
  - "JS-04: Objects"
  - "JS-12: Generators"
references:
    - title: "The Modern JavaScript Tutorial"
      url: "https://javascript.info/"
      sections: "Proxy and Reflect — full section | Symbols"
      description: "Practical guide to Proxy, Reflect, and Symbol usage"
    - title: "MDN JavaScript Guide"
      url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"
      sections: "Meta programming | Enumerability and ownership of properties"
      description: "Authoritative guide to metaprogramming concepts"
    - title: "Exploring JS: JavaScript for Programmers"
      url: "https://exploringjs.com/js/"
      chapters: "Ch. 27: Metaprogramming with Proxies | Ch. 11: Symbols"
      description: "Comprehensive coverage of JS metaprogramming features"
    - title: "You Don't Know JS Yet"
      url: "https://github.com/getify/you-dont-know-js"
      chapters: "ES.Next & Beyond — Ch. 7: Meta Programming"
      description: "Deep dive into Proxy, Reflect, and Symbol metaprogramming"
---

# JS-17: Metaprogramming: Proxy, Reflect, and Symbols

## Introduction

Metaprogramming is writing code that operates on other code. JavaScript provides
three powerful metaprogramming tools: Proxy for intercepting object operations,
Reflect for forwarding operations with correct semantics, and Symbols for
customizing language-level behavior.

## Subtopics

### 1. Well-Known Symbols

- `Symbol.iterator` — Make object iterable with `for...of`
- `Symbol.hasInstance` — Customize `instanceof` behavior
- `Symbol.toStringTag` — Customize `Object.prototype.toString.call(obj)`
- `Symbol.toPrimitive` — Customize object-to-primitive coercion
- `Symbol.isConcatSpreadable` — Control array concatenation behavior
- `Symbol.species` — Control derived object constructors
- `Symbol.match`/`Symbol.replace`/`Symbol.search`/`Symbol.split` — Customize regex behavior
- *Reference:* javascript.info — Symbols | MDN — Symbol | Exploring JS Ch. 11

### 2. Proxy

- `new Proxy(target, handler)` — wraps target with interceptor handlers
- **Handler traps**: `get`, `set`, `has`, `deleteProperty`, `apply`, `construct`,
  `getPrototypeOf`, `setPrototypeOf`, `defineProperty`, `getOwnPropertyDescriptor`,
  `ownKeys`, `preventExtensions`, `isExtensible`, `enumerate`
- **Use cases**: Validation, logging, default values, lazy initialization, reactivity (Vue 3)
- **Revocable Proxy**: `Proxy.revocable(target, handler)` — can be revoked for security
- *Reference:* javascript.info — Proxy | MDN — Proxy | Exploring JS Ch. 27

### 3. Reflect API

- `Reflect` methods mirror Proxy traps — use inside handlers for default behavior
- `Reflect.get(target, prop, receiver)` — safe property access
- `Reflect.set(target, prop, value, receiver)` — safe property assignment
- `Reflect.has(target, prop)` — equivalent to `prop in obj`
- `Reflect.ownKeys(target)` — returns all own property keys (string + symbol)
- **Why Reflect?** Instead of `target[prop]` in a Proxy get trap, use `Reflect.get(target, prop, receiver)`
  to correctly propagate the receiver (important for inheritance)
- *Reference:* javascript.info — Reflect | MDN — Reflect | Exploring JS Ch. 27

### 4. Property Descriptors

- **Data descriptor**: `value`, `writable`, `enumerable`, `configurable`
- **Accessor descriptor**: `get`, `set`, `enumerable`, `configurable`
- `Object.defineProperty(obj, prop, descriptor)` — define with precise semantics
- `Object.getOwnPropertyDescriptor(obj, prop)` — inspect descriptor
- `Object.freeze()` — sets all descriptors to non-writable, non-configurable
- `Object.seal()` — sets all to non-configurable (but still writable)

## Practice Questions

1. Implement a Proxy that logs all property access on an object.
2. Write a range validator Proxy: rejects numeric values outside [0, 100].
3. Use `Symbol.toPrimitive` to make a `Temperature` class work with arithmetic.
4. When would you use `Reflect.get()` over direct property access `obj.prop` in a Proxy?

## Key Takeaways

- Proxy intercepts fundamental object operations via handler traps
- Reflect provides default behavior for each trap — always use inside Proxy handlers
- Well-known Symbols customize language behavior (iteration, coercion, type checking)
- Property descriptors give fine-grained control over property semantics
- Together, Proxy + Reflect + Symbols enable powerful metaprogramming

## Further Reading

- javascript.info: Proxy and Reflect, Symbols
- MDN: Proxy, Reflect, Symbol
- Exploring JS: Chapter 27: Metaprogramming with Proxies
- YDKJSY: ES.Next & Beyond, Chapter 7
