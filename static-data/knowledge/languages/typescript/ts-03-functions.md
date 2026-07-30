---
title: "Functions and Function Types"
description: "Function type annotations, optional/default/rest parameters, overloads, this typing, and call signatures."
type: lesson
order: 3
duration: "60 min"
difficulty: beginner
learning_objectives:
  - "Annotate function parameters and return types with TypeScript"
  - "Use optional, default, rest parameters correctly"
  - "Write function overloads for polymorphic call patterns"
  - "Type the `this` keyword in callbacks and methods"
knowledge_refs:
  - typescript/ts-03-functions
prerequisites:
  - "TS-02"
references:
  - title: "TS Handbook — More on Functions"
    url: "https://www.typescriptlang.org/docs/handbook/2/functions.html"
  - title: "TS Handbook — Function Overloads"
    url: "https://www.typescriptlang.org/docs/handbook/2/functions.html#function-overloads"
  - title: "TypeScript Deep Dive — Functions"
    url: "https://basarat.gitbook.io/typescript/type-system/functions"
---

# TS-03: Functions and Function Types

## Introduction

Functions are the fundamental building block of TypeScript applications. TypeScript enhances JavaScript functions with type annotations for parameters and return values, overloads, and `this` parameter typing.

## Basic Function Types

Every function in TypeScript has a type based on its parameters and return value:

```typescript
// Named function with type annotations
function add(a: number, b: number): number {
  return a + b;
}

// Arrow function
const subtract = (a: number, b: number): number => a - b;

// Function type expression — describes the shape of a function
type MathOp = (a: number, b: number) => number;
const multiply: MathOp = (x, y) => x * y;  // Types inferred from MathOp
```

## Optional and Default Parameters

```typescript
// Optional parameter with ? → must come after required params
function greet(name: string, greeting?: string): string {
  return `${greeting ?? "Hello"}, ${name}!`;
}

// Default parameter — acts as optional automatically
function createUrl(path: string, base: string = "https://example.com"): string {
  return `${base}/${path}`;
}

// Rest parameters — collects remaining arguments into an array
function sum(...numbers: number[]): number {
  return numbers.reduce((a, b) => a + b, 0);
}
```

## Function Overloads

TypeScript allows multiple call signatures for a single function:

```typescript
// Overload signatures — describe all valid call patterns
function format(input: string): string;
function format(input: number): string;
function format(input: boolean): string;

// Implementation signature — must be compatible with all overloads
function format(input: string | number | boolean): string {
  if (typeof input === "string") return input.trim();
  if (typeof input === "number") return input.toFixed(2);
  return input ? "yes" : "no";
}
```

## Typing `this`

In callbacks and event handlers, `this` can be ambiguous. TypeScript lets you type it:

```typescript
interface Button {
  text: string;
  onClick: (this: HTMLElement, event: MouseEvent) => void;
}

const button: Button = {
  text: "Click me",
  onClick(this: HTMLElement, event: MouseEvent) {
    // this is guaranteed to be an HTMLElement
    console.log(this.textContent);
  }
};
```

## Call Signatures and Construct Signatures

For more complex scenarios, you can describe callable objects:

```typescript
// Call signature — describes something callable
interface Logger {
  (message: string, level?: "info" | "warn" | "error"): void;
  prefix: string;
}

const logger: Logger = Object.assign(
  (message: string, level = "info" as const) => {
    console.log(`[${level.toUpperCase()}] ${logger.prefix}: ${message}`);
  },
  { prefix: "App" }
);

// Construct signature — describes a constructor
interface PointConstructor {
  new (x: number, y: number): { x: number; y: number };
}
```

## Practice Questions

1. Write a function overload for a `parseInput` function that accepts either a JSON string or a number.
2. Create a function type that accepts a callback with a typed `this` context.
3. When would you use a call signature instead of a regular function type?

## Key Takeaways

- Function overloads improve DX by showing valid call patterns
- Default parameters are cleaner than optional + null check
- Type `this` explicitly in callbacks to prevent runtime errors
- Construct signatures describe constructable types (classes)
