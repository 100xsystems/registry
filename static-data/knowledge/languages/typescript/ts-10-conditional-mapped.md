---
{
  "title": "Conditional and Mapped Types",
  "description": "Write conditional types with extends and infer",
  "type": "lesson",
  "order": 10,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write conditional types with extends and infer",
    "Create mapped types with key remapping (TS 4.1+)",
    "Use distributive conditional types for union filtering",
    "Build template literal types for string transformations"
  ],
  "knowledge_refs": [
    "typescript/ts-10-conditional-mapped"
  ],
  "prerequisites": [
    "TS-08",
    "TS-09"
  ],
  "references": [
    {
      "title": "TS Handbook — Conditional Types",
      "url": "https://www.typescriptlang.org/docs/handbook/2/conditional-types.html"
    },
    {
      "title": "TS Handbook — Mapped Types",
      "url": "https://www.typescriptlang.org/docs/handbook/2/mapped-types.html"
    },
    {
      "title": "TS Handbook — Template Literal Types",
      "url": "https://www.typescriptlang.org/docs/handbook/2/template-literal-types.html"
    },
    {
      "title": "TS Handbook — infer",
      "url": "https://www.typescriptlang.org/docs/handbook/2/conditional-types.html#inferring-within-conditional-types"
    }
  ]
}
---

# TS-10-CONDITIONAL-MAPPED: Conditional and Mapped Types

## Introduction

Conditional types (`T extends U ? X : Y`) and mapped types (`{ [K in T]: ... }`) are TypeScript's most powerful type-level programming tools. Conditional types let you express type relationships; mapped types let you transform every property of a type. Combined, they enable the full power of type-safe metaprogramming.

## Key Concepts

### 1. Conditional Types — Type-Level Ternaries

A conditional type selects between two types based on a condition: `T extends U ? A : B`. If `T` is assignable to `U`, the result is `A`; otherwise `B`. They form the basis of type-level functions.

```typescript
// Simple conditional
type IsString<T> = T extends string ? 'yes' : 'no';
type A = IsString<'hello'>;  // 'yes'
type B = IsString<42>;       // 'no'

// Filter null/undefined
type NonNullable<T> = T extends null | undefined ? never : T;
type C = NonNullable<string | null>;  // string

// Practical: get return type of a function
type ReturnOf<T> = T extends (...args: any[]) => infer R ? R : never;
type D = ReturnOf<() => string>;  // string
```

### 2. The infer Keyword — Extract from Within

`infer` lets you introduce a new type variable within the true branch of a conditional type. It's like pattern matching at the type level. Used in built-in types like `ReturnType`, `Parameters`, and `InstanceType`.

```typescript
// Extract the element type from a Promise
type Unwrap<T> = T extends Promise<infer U> ? U : T;
type E = Unwrap<Promise<string>>;  // string
type F = Unwrap<number>;            // number

// Extract parameters from function type
type Params<T> = T extends (...args: infer P) => any ? P : never;
type G = Params<(name: string, age: number) => void>;
// [string, number]

// Extract first element from array type
type First<T extends any[]> = T extends [infer F, ...any[]] ? F : never;
type H = First<[string, number, boolean]>;  // string

// Recursive type: deep unwrap promises
type DeepUnwrap<T> = T extends Promise<infer U> ? DeepUnwrap<U> : T;
type I = DeepUnwrap<Promise<Promise<string>>>;  // string
```

### 3. Distributive Conditional Types

When a conditional type acts on a **naked type parameter** that is a union, it **distributes** over each member. This is why `NonNullable<string | null | undefined>` works — it processes each union member independently.

```typescript
// Distribution in action
type ToArray<T> = T extends any ? T[] : never;
type J = ToArray<string | number>;
// string[] | number[]  (not (string | number)[])

// Filter union members using distribution
type ExtractType<T, U> = T extends U ? T : never;
type K = ExtractType<'a' | 'b' | 'c', 'a' | 'c'>;
// 'a' | 'c'

type ExcludeType<T, U> = T extends U ? never : T;
type L = ExcludeType<'a' | 'b' | 'c', 'a'>;
// 'b' | 'c'

// To prevent distribution, wrap in tuple:
type NonDistributive<T> = [T] extends [string] ? 'yes' : 'no';
type M = NonDistributive<string | number>;  // 'no' (not distributed)
```

### 4. Mapped Types — Transform Every Property

A mapped type iterates over keys and transforms each property. `{ [K in keyof T]: NewType }` reads each key of `T` and produces a new type. Add `readonly`, `?` modifiers, or remove them with `-readonly` / `-?`.

```typescript
// Make all properties readonly
type MyReadonly<T> = { readonly [K in keyof T]: T[K] };

// Make all properties optional
type MyPartial<T> = { [K in keyof T]?: T[K] };

// Make all properties required (remove ?)
type MyRequired<T> = { [K in keyof T]-?: T[K] };

// Map property types
type Stringify<T> = { [K in keyof T]: string };
type N = Stringify<{ a: number; b: boolean }>;
// { a: string; b: string }

// Filter keys by type
type PickByType<T, V> = {
  [K in keyof T as T[K] extends V ? K : never]: T[K];
};
type O = PickByType<{ a: string; b: number; c: boolean }, string>;
// { a: string }
```

### 5. Key Remapping (TS 4.1+) and Template Literals in Mapped Types

With `as` in mapped types, you can **rename** or **filter** keys. Combined with template literals, this enables prefixing, suffixing, or transforming key names — perfect for state management and API client generation.

```typescript
// Prefix all keys with 'on'
type Events<T> = {
  [K in keyof T as `on${Capitalize<string & K>}`]: T[K];
};
type P = Events<{ click: void; hover: void }>;
// { onClick: void; onHover: void }

// Filter out keys starting with '_'
type Public<T> = {
  [K in keyof T as K extends `_${string}` ? never : K]: T[K];
};
type Q = Public<{ name: string; _secret: string; _key: string; age: number }>;
// { name: string; age: number }

// Advanced: create a getter type from an interface
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};
type R = Getters<{ name: string; age: number }>;
// { getName: () => string; getAge: () => number }
```

## Practice Questions

1. What does `ReturnType<(x: number) => string>` evaluate to? Explain how `infer` works here.
1. Why does `string | null extends string ? true : false` evaluate to `false`? How does distribution affect this?
1. Write a conditional type that extracts the resolved value from a Promise, handling nested Promises recursively.
1. Create a mapped type that adds `| null` to every property of an interface.

## LLM Prompts for Deeper Understanding

1. "Explain TypeScript conditional types and the infer keyword with advanced examples"
1. "Show me distributive conditional types and how to prevent distribution in TypeScript"
1. "Teach me mapped types with key remapping and template literal types for API client generation"

## Key Takeaways

- Conditional types are type-level functions — `T extends U ? X : Y`
- `infer` introduces new type variables in conditional types for pattern matching
- Mapped types with `as` key remapping can rename, filter, or transform property keys
