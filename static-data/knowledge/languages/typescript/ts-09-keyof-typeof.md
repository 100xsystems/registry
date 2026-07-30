---
{
  "title": "keyof, typeof, and Type Operators",
  "description": "Use keyof to extract property keys from a type",
  "type": "lesson",
  "order": 9,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use keyof to extract property keys from a type",
    "Use typeof to capture runtime value types",
    "Combine keyof and typeof for dynamic access patterns",
    "Master indexed access types (T[K]) for property value extraction"
  ],
  "knowledge_refs": [
    "typescript/ts-09-keyof-typeof"
  ],
  "prerequisites": [
    "TS-02",
    "TS-08"
  ],
  "references": [
    {
      "title": "TS Handbook — keyof",
      "url": "https://www.typescriptlang.org/docs/handbook/2/keyof-types.html"
    },
    {
      "title": "TS Handbook — typeof Type",
      "url": "https://www.typescriptlang.org/docs/handbook/2/typeof-types.html"
    },
    {
      "title": "TS Handbook — Indexed Access Types",
      "url": "https://www.typescriptlang.org/docs/handbook/2/indexed-access-types.html"
    }
  ]
}
---

# TS-09-KEYOF-TYPEOF: keyof, typeof, and Type Operators

## Introduction

TypeScript provides operators that let you derive new types from existing ones at the type level. `keyof` gets the union of property keys; `typeof` captures the type of a runtime value. Combined with indexed access (`T[K]`), these form the foundation of advanced type transformation.

## Key Concepts

### 1. keyof — Get Union of Property Keys

`keyof T` yields a union of all known property keys of `T`. For a type with keys `a`, `b`, `c`, `keyof T` is `'a' | 'b' | 'c'`. This is essential for type-safe dynamic property access.

```typescript
interface Person {
  name: string;
  age: number;
  email?: string;
}

type PersonKeys = keyof Person;  // 'name' | 'age' | 'email'

// Practical use: type-safe getter
function get<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const p: Person = { name: 'Alice', age: 30 };
const n = get(p, 'name');  // string
const a = get(p, 'age');   // number
// get(p, 'ssn');          // Error

// keyof with arrays
type ArrayKeys = keyof [string, number];  // '0' | '1' | keyof any[]
```

### 2. typeof — Capture Runtime Type

`typeof` in type position captures the static type of a runtime value. This is useful when you want to reuse a type inferred from an object literal, function, or class.

```typescript
const config = {
  host: 'localhost',
  port: 3000,
  ssl: false,
} as const;

type Config = typeof config;
// {
//   readonly host: "localhost";
//   readonly port: 3000;
//   readonly ssl: false;
// }

// typeof for functions
function createUser(name: string, age: number) {
  return { id: crypto.randomUUID(), name, age };
}
type CreateUserFn = typeof createUser;
// (name: string, age: number) => { id: string; name: string; age: number }

// typeof for classes
class Service { /* ... */ }
type ServiceType = typeof Service;  // the constructor type
```

### 3. keyof + typeof = Dynamic from Runtime

Combine `keyof typeof` to derive a union of keys from a runtime object. This is the most common pattern for creating types from const objects — replacing enums without the baggage.

```typescript
export const Colors = {
  Red: '#FF0000',
  Green: '#00FF00',
  Blue: '#0000FF',
} as const;

type ColorName = keyof typeof Colors;
// 'Red' | 'Green' | 'Blue'

type HexValue = (typeof Colors)[ColorName];
// '#FF0000' | '#00FF00' | '#0000FF'

function getColor(name: ColorName): HexValue {
  return Colors[name];  // fully type-safe
}
```

### 4. Indexed Access Types (Lookup Types)

`T[K]` gives you the type of property `K` on type `T`. When `K` is a union, the result is the union of property types. This is how you extract nested types from complex structures.

```typescript
interface ApiResponse {
  status: number;
  data: {
    users: { id: number; name: string }[];
    pagination: { page: number; total: number };
  };
}

type DataType = ApiResponse['data'];
// { users: { id: number; name: string }[]; pagination: { page: number; total: number } }

type UserType = ApiResponse['data']['users'][number];
// { id: number; name: string }

// Union index access
type Mixed = { a: string; b: number; c: boolean };
type AB = Mixed['a' | 'b'];  // string | number
type All = Mixed[keyof Mixed];  // string | number | boolean
```

### 5. Template Literal Types with keyof

TypeScript 4.1+ supports **template literal types**, which can be combined with `keyof` to create computed property name patterns — like event names derived from component names.

```typescript
type EventName<T extends string> = `${T}Changed` | `${T}Clicked`;

type ButtonEvents = EventName<'submit'>;
// 'submitChanged' | 'submitClicked'

// Real-world: model state change events
type StateEvents<T> = {
  [K in keyof T as `on${Capitalize<string & K>}Change`]: (value: T[K]) => void;
};

interface FormState {
  email: string;
  age: number;
}

type FormEvents = StateEvents<FormState>;
// { onEmailChange: (value: string) => void; onAgeChange: (value: number) => void }
```

## Practice Questions

1. What does `keyof { a: string; b: number; c?: boolean }` evaluate to?
1. Using `typeof` on an const object with `as const`, what type do you get?
1. Write an indexed access type that extracts the resolved value type from `Promise<string>` without `infer`.
1. How would you use template literal types with keyof to rename object keys (prefixing each key with "get")?

## LLM Prompts for Deeper Understanding

1. "Explain keyof, typeof, and indexed access types in TypeScript with real-world examples"
1. "Show me how to combine keyof typeof to create types from const objects in TypeScript"
1. "Teach me template literal types in TypeScript 4.1+ with key remapping examples"

## Key Takeaways

- `keyof T` extracts the union of property keys as a type
- `typeof val` in type position captures the static type of a runtime value
- Indexed access `T[K]` extracts property value types — works with unions and nesting
