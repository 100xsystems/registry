---
title: "Objects, Arrays, and Collections"
description: "JavaScript objects, arrays, Maps, Sets — creating, accessing, iterating, and manipulating data structures."
type: lesson
order: 4
duration: "75 min"
difficulty: beginner
level: Beginner
learning_objectives:
  - "Create and manipulate objects with bracket and dot notation"
  - "Master array methods: push, pop, map, filter, reduce, find"
  - "Understand Map, Set, WeakMap, and WeakSet"
  - "Destructure objects and arrays for cleaner code"
knowledge_refs:
  - languages/javascript/js-beginner-04-objects-arrays
prerequisites:
  - "JS-01: Values, Types, and Variables"
references:
    - title: "Eloquent JavaScript (4th Edition)"
      url: "https://eloquentjavascript.net/"
      chapters: "Chapter 4: Data Structures — Objects and Arrays"
      description: "The classic introduction to JS data structures"
    - title: "The Modern JavaScript Tutorial"
      url: "https://javascript.info/"
      sections: "Objects | Object references and copying | Arrays | Array methods | Map and Set | WeakMap and WeakSet | Destructuring assignment"
      description: "Comprehensive coverage of all collection types"
    - title: "MDN JavaScript Guide"
      url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"
      sections: "Indexed collections | Keyed collections | Working with objects"
      description: "Authoritative reference for all collection APIs"
    - title: "You Don't Know JS Yet"
      url: "https://github.com/getify/you-dont-know-js"
      chapters: "Objects & Classes — Ch. 3: Object Foundations | ES.Next & Beyond — Ch. 5: Collections"
      description: "Deep dive into how objects work at the engine level"
    - title: "Exploring JS: JavaScript for Programmers"
      url: "https://exploringjs.com/js/"
      chapters: "Ch. 10: Objects | Ch. 22: Arrays | Ch. 23: Maps and Sets"
      description: "Comprehensive treatment of all data structures"
---

# JS-04: Objects, Arrays, and Collections

## Introduction

Objects and arrays are the two most important compound data structures in JavaScript.
Objects store key-value pairs; arrays store ordered lists. ES6 added Map, Set, and
their weak counterparts for specialized use cases.

## Subtopics

### 1. Object Basics

- Creating objects: literal `{}`, `new Object()`, `Object.create()`
- Accessing properties: dot notation (`obj.key`) vs bracket notation (`obj["key with spaces"]`)
- Computed property keys (ES6): `const obj = { [dynamicKey]: value }`
- Shorthand properties (ES6): `const obj = { name, age }` instead of `{ name: name, age: age }`
- Property existence: `"key" in obj`, `obj.hasOwnProperty("key")`, `obj !== undefined`
- *Reference:* javascript.info — Objects | Eloquent JS Ch. 4 | MDN — Working with Objects

### 2. Object Methods and `this`

- Method shorthand (ES6): `const obj = { greet() { return "Hello"; } }`
- The `this` keyword inside methods refers to the object the method was called on
- `Object.keys()`, `Object.values()`, `Object.entries()` — iterate over own properties
- `Object.assign()` — shallow copy and merge objects
- *Reference:* javascript.info — Object methods, "this" | MDN — Object

### 3. Array Fundamentals

- Creating arrays: literal `[]`, `new Array()`, `Array.from()`, `Array.of()`
- Indexing and length: `arr[0]`, `arr[arr.length - 1]`
- Adding/removing: `push()`/`pop()` — end; `unshift()`/`shift()` — beginning (avoid: O(n))
- Iterating: `for`, `for...of`, `forEach()`
- *Reference:* javascript.info — Arrays | Eloquent JS Ch. 4

### 4. Powerful Array Methods

- **Transformation**: `map()`, `filter()`, `reduce()`, `flatMap()`
- **Search**: `find()`, `findIndex()`, `includes()`, `indexOf()`, `some()`, `every()`
- **Sort/Slice**: `sort()`, `slice()`, `splice()`, `concat()`
- **Reduce is the universal array method**: `reduce((acc, item) => newAcc, initial)`
  can implement map, filter, find, and more
- *Reference:* javascript.info — Array methods | Eloquent JS Ch. 5 (Higher-Order Functions)
- *Deep dive:* `reduce()` is the functional programming Swiss Army knife. Master it.

### 5. Destructuring (ES6)

- **Array destructuring**: `const [first, second] = [1, 2, 3]`
- **Object destructuring**: `const { name, age } = person`
- **Nested destructuring**: `const { address: { city } } = person`
- **Default values**: `const [x = 10] = []`
- **Rest in destructuring**: `const [head, ...tail] = [1, 2, 3, 4]`
- *Reference:* javascript.info — Destructuring assignment | Exploring JS Ch. 12

### 6. Map, Set, WeakMap, WeakSet

- **Map**: Key-value store where keys can be ANY value (not just strings)
- **Set**: Unique values collection
- **WeakMap/WeakSet**: GC-friendly versions — keys must be objects, no iteration
- When to use Map instead of Object: frequent additions/deletions, non-string keys,
  need for `.size`, preserving insertion order
- *Reference:* javascript.info — Map and Set, WeakMap and WeakSet | YDKJSY ES.Next Ch. 5

## Practice Questions

1. Given `const obj = { a: 1, b: 2 }`, why does `obj["a"]` work but `obj["c"]` returns `undefined`?
2. What's the difference between `arr.map(fn)` and `arr.forEach(fn)`?
3. Implement `map` using `reduce`.
4. When would you use a `Map` instead of a regular object? Give three examples.
5. Destructure `{ user: { name, age }, posts: [first] }` from a nested API response.

## LLM Prompts

1. **Socratic Tutor**: "I'm confused about reference vs value with objects. I did `const a = { x: 1 }; const b = a; b.x = 2;` and now `a.x` is also 2. Why?"
2. **Practice Generator**: "Create 5 progressively harder exercises for practicing `map`, `filter`, and `reduce`."
3. **Debugging Coach**: "My `sort()` on an array of numbers is returning `[1, 10, 2, 20]`. Why isn't it sorted numerically?"

## Key Takeaways

- Objects are the fundamental key-value store — use bracket notation for dynamic keys
- Array methods (`map`, `filter`, `reduce`) are preferred over imperative loops
- Destructuring makes code cleaner — destructure at the point of use
- Map when keys are dynamic/non-string; Object when structure is known and fixed
- All collections are iterable with `for...of` (except WeakMap/WeakSet)

## Further Reading

- Eloquent JS, Chapter 4: Data Structures
- javascript.info: Objects, Arrays, Array methods, Map and Set, Destructuring
- YDKJSY: Objects & Classes Ch. 3, ES.Next Ch. 5
- MDN: Array, Map, Set, Object
