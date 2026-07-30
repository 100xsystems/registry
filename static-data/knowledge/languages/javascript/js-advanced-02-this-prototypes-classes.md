---
title: "The `this` Keyword, Prototypes, and Classes"
description: "The `this` binding rules, prototype chain inheritance, and the ES6 class syntax — understanding JavaScript's unique object model."
type: lesson
order: 9
duration: "75 min"
difficulty: intermediate
level: Advanced
learning_objectives:
  - "Determine `this` binding using the four rules: default, implicit, explicit, and `new`"
  - "Traverse the prototype chain and understand property lookup delegation"
  - "Implement inheritance patterns: constructor functions, classes, and OLOO"
  - "Understand when to use `class` vs prototype delegation"
knowledge_refs:
  - languages/javascript/js-advanced-02-this-prototypes-classes
prerequisites:
  - "JS-08: Scope and Closures"
references:
    - title: "You Don't Know JS Yet"
      url: "https://github.com/getify/you-dont-know-js"
      chapters: "Objects & Classes — ALL chapters | Scope & Closures Ch. 7"
      description: "The definitive deep dive into JS object mechanics"
    - title: "Eloquent JavaScript (4th Edition)"
      url: "https://eloquentjavascript.net/"
      chapters: "Chapter 6: The Secret Life of Objects"
      description: "Classic introduction to prototypes and object-oriented JS"
    - title: "The Modern JavaScript Tutorial"
      url: "https://javascript.info/"
      sections: "Object methods, "this" | Prototypes, inheritance | Class basics | Class inheritance | Class checking: instanceof"
      description: "Comprehensive guide across all OOP topics"
    - title: "MDN JavaScript Guide"
      url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"
      sections: "Working with objects | Using classes | Inheritance and the prototype chain"
      description: "Authoritative guide to JS object orientation"
    - title: "Exploring JS: JavaScript for Programmers"
      url: "https://exploringjs.com/js/"
      chapters: "Ch. 10: Objects | Ch. 14: Classes"
      description: "Comprehensive treatment of OOP in JS"
---

# JS-09: The `this` Keyword, Prototypes, and Classes

## Introduction

JavaScript has a unique object model based on prototypes rather than classical
inheritance. The `this` keyword is dynamically bound based on how a function is
called. ES6 classes provide syntactic sugar over prototypes but behave differently
from classes in languages like Java or C++.

## Subtopics

### 1. The Four `this` Binding Rules

1. **Default binding**: Standalone function call — `this` points to global object
   (or `undefined` in strict mode)
2. **Implicit binding**: Called as method of object — `this` points to that object
3. **Explicit binding**: `call()`, `apply()`, `bind()` — `this` is whatever you pass
4. **`new` binding**: Constructor call — `this` points to the newly created object

- **Precedence**: `new` > explicit > implicit > default
- Arrow functions bypass all four rules — `this` is lexically scoped from enclosing context
- *Reference:* YDKJSY Objects & Classes Ch. 1-2 | javascript.info — Object methods, this
  | MDN — this | Eloquent JS Ch. 6

### 2. The Prototype Chain

- Every JS object has an internal `[[Prototype]]` link (accessible via `__proto__` or `Object.getPrototypeOf()`)
- Property access follows the chain: own property → prototype → prototype's prototype → ... → null
- `Object.create(proto)` creates an object with a specific prototype
- `new F()` creates an object whose prototype is `F.prototype`
- *Reference:* YDKJSY Objects & Classes Ch. 5 | javascript.info — Prototypal inheritance
  | Eloquent JS Ch. 6 | MDN — Inheritance and the prototype chain

### 3. ES6 Classes

- `class` syntax is syntactic sugar over constructor functions + prototypes
- `constructor()` method runs on instantiation with `new`
- `extends` for inheritance — sets up prototype chain AND `super()` call
- `super()` calls parent constructor — must be called before using `this` in subclass
- Public and private class fields, static methods, static initialization blocks
- *Reference:* javascript.info — Class basics, inheritance | Eloquent JS Ch. 6
  | YDKJSY Objects & Classes — Appendix A | MDN — Classes

### 4. OLOO (Objects Linked to Other Objects)

- YDKJSY's alternative to class-based design
- Create objects directly, link them with `Object.create()`, use delegation
- No `new`, no `class`, no `extends` — just objects linked to objects
- *Reference:* YDKJSY Objects & Classes Ch. 6 — Behavior Delegation

## Practice Questions

1. What does `this` refer to in `setTimeout(obj.method, 100)`? How would you fix it?
2. Write a function `newBind(fn, ctx)` that implements `Function.prototype.bind`.
3. Given `function A() {} A.prototype.x = 10; const a = new A();`, where does `a.x` resolve?
4. What's the difference between `Object.create(proto)` and `new Constructor()`?

## Key Takeaways

- `this` is bound by call-site (how the function is called), not where it's defined
- Prototype chain enables property delegation — objects inherit from objects
- `class` is syntactic sugar over prototypes — understand what it abstracts
- `bind()` returns a new function with permanent `this` — `call()` and `apply()` invoke immediately
- Arrow functions use lexical `this` — great for callbacks, wrong for methods

## Further Reading

- YDKJSY: Objects & Classes (entire book)
- Eloquent JS, Chapter 6: The Secret Life of Objects
- javascript.info: Prototypes, Class, this
- MDN: Inheritance and the prototype chain
