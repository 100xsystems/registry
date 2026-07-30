---
{
  "title": "Generics: Basics and Constraints",
  "description": "Write generic functions with type parameters",
  "type": "lesson",
  "order": 8,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write generic functions with type parameters",
    "Constrain generics with extends clauses",
    "Create generic interfaces and classes",
    "Understand variance: covariance, contravariance, invariance"
  ],
  "knowledge_refs": [
    "typescript/ts-08-generics"
  ],
  "prerequisites": [
    "TS-04",
    "TS-06"
  ],
  "references": [
    {
      "title": "TS Handbook — Generics",
      "url": "https://www.typescriptlang.org/docs/handbook/2/generics.html"
    },
    {
      "title": "TS Handbook — Generic Constraints",
      "url": "https://www.typescriptlang.org/docs/handbook/2/generics.html#generic-constraints"
    },
    {
      "title": "TypeScript Deep Dive — Generics",
      "url": "https://basarat.gitbook.io/typescript/type-system/generics"
    }
  ]
}
---

# TS-08-GENERICS: Generics: Basics and Constraints

## Introduction

Generics are the backbone of reusable, type-safe code in TypeScript. They allow functions, classes, and types to operate with a variety of types while preserving type information. Without generics, you'd have to use `any` — losing all type safety.

## Key Concepts

### 1. Generic Functions — Type Parameters in Action

Type parameters are placeholders for actual types, inferred from usage. The classic example is `identity<T>`. Multiple type parameters are allowed, and you can provide explicit types if inference fails.

```typescript
// Basic generic function
function identity<T>(arg: T): T {
  return arg;
}
const num = identity(42);        // T inferred as number
const str = identity('hello');   // T inferred as string

// Multiple type parameters
function pair<A, B>(a: A, b: B): [A, B] {
  return [a, b];
}
const p = pair('key', 123);  // type: [string, number]

// Generic arrow functions (note the trailing comma for JSX)
const wrap = <T,>(value: T): { value: T } => ({ value });
```

### 2. Generic Constraints with extends

Without constraints, a generic function cannot access any properties on `T` (since `T` could be anything). The `extends` clause constrains `T` to types that have certain properties, unlocking property access.

```typescript
interface HasLength {
  length: number;
}

function logLength<T extends HasLength>(arg: T): T {
  console.log(arg.length);  // OK — constrained to HasLength
  return arg;
}

logLength('hello');       // string has length
logLength([1, 2, 3]);     // array has length
// logLength(42);         // Error: number has no length

// Constraint with keyof — ensure a property exists
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
const user = { name: 'Alice', age: 30 };
getProperty(user, 'name');  // string
// getProperty(user, 'email'); // Error
```

### 3. Generic Interfaces and Classes

Both interfaces and classes can accept type parameters. This enables reusable abstractions like `ApiResponse<T>`, `Repository<T>`, and `Stack<T>`.

```typescript
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

type UserResponse = ApiResponse<{ id: number; name: string }>;

// Generic class
class Stack<T> {
  private items: T[] = [];

  push(item: T): void {
    this.items.push(item);
  }

  pop(): T | undefined {
    return this.items.pop();
  }

  peek(): T | undefined {
    return this.items[this.items.length - 1];
  }

  get length(): number {
    return this.items.length;
  }
}

const numStack = new Stack<number>();
numStack.push(1);
numStack.push(2);
console.log(numStack.pop());  // 2
```

### 4. Default Type Parameters

Type parameters can have **defaults**, just like function parameters. This is useful when most callers use a common type but advanced users can override it.

```typescript
interface EventEmitter<T = string> {
  on(event: T, handler: (data: unknown) => void): void;
  emit(event: T, data: unknown): void;
}

// Uses default (string)
const emitter1: EventEmitter = {
  on(event: string, handler) { /* ... */ },
  emit(event: string, data) { /* ... */ },
};

// Override with union
type MyEvents = 'click' | 'hover' | 'focus';
const emitter2: EventEmitter<MyEvents> = {
  on(event: 'click' | 'hover' | 'focus', handler) { },
  emit(event: 'click' | 'hover' | 'focus', data) { },
};
```

### 5. Variance: Covariance, Contravariance, Invariance

Variance describes how generic types relate when their type parameters change. This matters for function arguments (contravariant) and return types (covariant). TypeScript structurally checks variance for methods.

```typescript
// Covariant — return type (producer)
interface Producer<T> {
  produce(): T;
}
// Producer<Cat> is assignable to Producer<Animal>

// Contravariant — argument type (consumer)
interface Consumer<T> {
  consume(value: T): void;
}
// Consumer<Animal> is assignable to Consumer<Cat>

// Invariant — both
interface Box<T> {
  get(): T;
  set(value: T): void;
}

// Practical example: function parameters are contravariant
type Logger = (msg: string) => void;
const log: Logger = (msg: string | number) => {  // wider param OK
  console.log(msg);
};
```

## Practice Questions

1. Why can't you access `.length` on a generic `T` without a constraint?
1. Write a generic function that extracts a value by key from an object, ensuring the key exists on the object type.
1. What is the difference between a generic class and a non-generic class that uses `any`?
1. Explain why `Producer<Cat>` is assignable to `Producer<Animal>` (covariance) but `Consumer<Animal>` is assignable to `Consumer<Cat>` (contravariance).

## LLM Prompts for Deeper Understanding

1. "Explain TypeScript generic constraints with keyof and extends patterns"
1. "Show me variance in TypeScript — covariance, contravariance, and invariance with examples"
1. "Teach me advanced generic patterns: conditional returns, mapped generics, and variadic tuples"

## Key Takeaways

- Generics preserve type information across reusable functions and classes
- The `extends` clause constrains type parameters to enforce property access
- Variance determines assignability of generic types — functions are contravariant in parameters
