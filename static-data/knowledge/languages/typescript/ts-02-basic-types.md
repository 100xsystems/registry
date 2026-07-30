---
title: "Basic Types and Type Annotations"
description: "Primitive types, array/tuple/enum types, special types (any, unknown, never, void), and type inference."
type: lesson
order: 2
duration: "60 min"
difficulty: beginner
learning_objectives:
  - "Write type annotations for variables, parameters, and return types"
  - "Use primitive types: string, number, boolean, null, undefined, bigint, symbol"
  - "Understand special types: any, unknown, never, void"
  - "Leverage type inference to reduce unnecessary annotations"
knowledge_refs:
  - typescript/ts-02-basic-types
prerequisites:
  - "TS-01"
references:
  - title: "TS Handbook — Everyday Types"
    url: "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html"
  - title: "TS Handbook — Basic Types"
    url: "https://www.typescriptlang.org/docs/handbook/basic-types.html"
  - title: "TypeScript Deep Dive — Type System"
    url: "https://basarat.gitbook.io/typescript/type-system"
---

# TS-02: Basic Types and Type Annotations

## Introduction

TypeScript's type system is **structural** (not nominal) — compatibility is determined by shape, not by explicit declarations. Understanding the primitive types and how type inference works is the foundation of all TypeScript programming.

## Primitive Types

TypeScript's primitive types map directly to JavaScript's runtime values:

```typescript
// String — Unicode text
let name: string = "Alice";
let template: string = `Hello, ${name}!`;

// Number — all numbers are floating-point (IEEE 754)
let integer: number = 42;
let float: number = 3.14159;
let hex: number = 0xff;     // 255
let binary: number = 0b1010; // 10
let big: number = 1e6;      // 1,000,000

// Boolean
let isDone: boolean = false;

// BigInt — for arbitrarily large integers (ES2020+)
let large: bigint = 9007199254740991n;

// Symbol — unique, immutable identifier
let sym: symbol = Symbol("unique");
```

## Type Inference

You don't always need to write type annotations — TypeScript infers types from values:

```typescript
let name = "Alice";     // inferred as string
let age = 30;           // inferred as number
let isActive = true;    // inferred as boolean

// TypeScript catches mistakes based on inference
name = 42;  // ❌ Error: Type 'number' is not assignable to type 'string'
```

Use inference for simple cases, annotations for function signatures and complex types.

## Special Types

### any — opt-out of type checking

```typescript
let loose: any = 42;
loose = "hello";         // OK
loose = { anything: true }; // OK
loose.toUpperCase();     // OK at compile time, may crash at runtime
```

Avoid `any` in production code — it defeats TypeScript's purpose. Prefer `unknown` if you need flexibility.

### unknown — type-safe any

```typescript
let value: unknown = JSON.parse('{"name": "Alice"}');

// Can't use unknown without narrowing
value.toUpperCase();  // ❌ Error: Object is of type 'unknown'

// Must narrow first
if (typeof value === "object" && value !== null && "name" in value) {
  console.log((value as { name: string }).name);  // "Alice"
}
```

### void — absence of a value

```typescript
function log(message: string): void {
  console.log(message);
  // No return statement needed
}
```

### never — values that never occur

```typescript
function fail(message: string): never {
  throw new Error(message);
  // Never returns — always throws
}

function infiniteLoop(): never {
  while (true) {}
}
```

`never` is also useful for exhaustiveness checking in discriminated unions.

### null and undefined

With `strict: true`, `null` and `undefined` are their own types:

```typescript
let nothing: null = null;
let missing: undefined = undefined;

// They are NOT assignable to other types
let name: string = null;  // ❌ Error with strictNullChecks
```

## Type Annotations for Functions

```typescript
// Parameter types and return type
function add(a: number, b: number): number {
  return a + b;
}

// Arrow function with types
const multiply = (a: number, b: number): number => a * b;

// Void return — no return value
function logError(message: string): void {
  console.error(message);
}
```

## Arrays, Tuples, and Enums

### Arrays

```typescript
// Two equivalent syntaxes
let numbers: number[] = [1, 2, 3];
let strings: Array<string> = ["a", "b", "c"];

// Readonly arrays
let readonly: readonly number[] = [1, 2, 3];
// readonly.push(4);  // ❌ Error: Property 'push' does not exist on type 'readonly number[]'
```

### Tuples — arrays with fixed length and types per element

```typescript
let pair: [string, number] = ["Alice", 30];
console.log(pair[0]);  // string
console.log(pair[1]);  // number

// Tuple with optional element and rest
let variadic: [string, ...number[]] = ["scores", 85, 92, 78];
```

### Enums

```typescript
// Numeric enum (auto-increments from 0)
enum Direction {
  Up,      // 0
  Down,    // 1
  Left,    // 2
  Right,   // 3
}

// String enum
enum Color {
  Red = "#FF0000",
  Green = "#00FF00",
  Blue = "#0000FF",
}

// Const enum — completely inlined, no runtime cost
const enum LogLevel {
  Debug = 0,
  Info = 1,
  Warn = 2,
  Error = 3,
}
```

## Practice Questions

1. What's the difference between `any` and `unknown`? When would you use each?
2. Create a tuple type for a 2D coordinate `(x, y)` that also supports a `z` coordinate.
3. Why does `const enum` behave differently at runtime than a regular `enum`?

## Key Takeaways

- TypeScript infers types — annotate only where inference isn't enough
- `strict: true` changes how `null` and `undefined` behave
- Prefer `unknown` over `any` for values of uncertain type
- Use `readonly` for arrays that shouldn't be mutated
