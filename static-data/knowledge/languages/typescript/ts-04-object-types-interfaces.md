---
{
  "title": "Object Types and Interfaces",
  "description": "Define object types with type aliases and interfaces",
  "type": "lesson",
  "order": 4,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define object types with type aliases and interfaces",
    "Use optional, readonly, and index signature properties",
    "Extend interfaces and merge declarations",
    "Choose between type and interface appropriately"
  ],
  "knowledge_refs": [
    "typescript/ts-04-object-types-interfaces"
  ],
  "prerequisites": [
    "TS-02"
  ],
  "references": [
    {
      "title": "TS Handbook — Object Types",
      "url": "https://www.typescriptlang.org/docs/handbook/2/objects.html"
    },
    {
      "title": "TS Handbook — Interfaces",
      "url": "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#interfaces"
    },
    {
      "title": "TypeScript Deep Dive — Interfaces",
      "url": "https://basarat.gitbook.io/typescript/type-system/interfaces"
    }
  ]
}
---

# TS-04-OBJECT-TYPES-INTERFACES: Object Types and Interfaces

## Introduction

TypeScript gives you two primary tools for shaping objects: `type` aliases and `interface` declarations. Knowing when to use each and how to leverage their unique capabilities (excess property checks, declaration merging, mapped types) is a foundational skill.

## Key Concepts

### 1. Object Type Literals

An object type describes the shape of a JavaScript object. You can define it inline with a `type` alias or an `interface`. Both support optional (`?`), readonly (`readonly`), and method signatures.

```typescript
// Type alias
type User = {
  id: number;
  name: string;
  email?: string;       // optional
  readonly createdAt: Date;
  greet(): string;      // method signature
};

// Interface (equivalent shape)
interface IUser {
  id: number;
  name: string;
  email?: string;
  readonly createdAt: Date;
  greet(): string;
}
```

### 2. Index Signatures

When you don't know the property names ahead of time, use an **index signature**. The key must be `string` or `number`. This is common for dictionary or map-like objects.

```typescript
interface StringMap {
  [key: string]: string | undefined;
}

const env: StringMap = {
  NODE_ENV: 'development',
  PORT: '3000',
};

// Combining known and unknown properties
interface Config {
  port: number;
  host: string;
  [key: string]: string | number;  // index signature
}
```

### 3. Excess Property Checks

When you assign an object literal directly to a typed location, TypeScript performs **excess property checks** — it warns about properties that don't exist on the target type. This catches typos and API mismatches early.

```typescript
interface Point {
  x: number;
  y: number;
}

// Error: 'z' does not exist in type 'Point'
const p1: Point = { x: 1, y: 2, z: 3 };

// OK: assign via intermediate variable (bypasses excess check)
const raw = { x: 1, y: 2, z: 3 };
const p2: Point = raw;  // structural check only

// OK: use spread to pick properties
const p3: Point = { x: raw.x, y: raw.y };
```

### 4. Interface Extension and Declaration Merging

Interfaces can **extend** other interfaces (including multiple) and can be **merged** — if you declare the same interface name twice, TypeScript merges their members automatically.

```typescript
interface BasicAnimal {
  name: string;
  age: number;
}

interface Dog extends BasicAnimal {
  breed: string;
  bark(): void;
}

// Declaration merging — both declarations combine
interface Box {
  width: number;
}
interface Box {
  height: number;
  depth: number;
}
const b: Box = { width: 10, height: 20, depth: 30 };  // all required
```

### 5. Type vs Interface: When to Use Which

The rule of thumb: use `interface` for public API shapes (benefits from declaration merging), and `type` for everything else (unions, intersections, mapped types, primitives). Interfaces can only describe objects; types can describe any shape.

```typescript
// Use type for:
type ID = string | number;              // union
type Status = 'active' | 'inactive';    // literal union
type Point3D = Point & { z: number };   // intersection (type)
type Readonly<T> = { readonly [K in keyof T]: T[K] };  // mapped

// Use interface for:
interface ApiResponse<T> {               // generics work with both
  data: T;
  status: number;
}
// Consumers can extend:
interface PaginatedResponse<T> extends ApiResponse<T> {
  nextPage: string | null;
}
```

## Practice Questions

1. What is the difference between an index signature and a regular property in an interface?
1. Why does `{ x: 1, y: 2, z: 3 }` fail when assigned to `Point { x: number; y: number }` but succeed when assigned via an intermediate variable?
1. Given two interfaces with the same name in different files, how does declaration merging affect the final type?
1. Rewrite the following type alias as an interface and discuss any limitations: `type Callback = (err: Error | null, result?: string) => void`.

## LLM Prompts for Deeper Understanding

1. "Explain TypeScript excess property checking with examples of when it helps and when it gets in the way"
1. "Compare and contrast TypeScript `type` aliases vs `interface` declarations with 5 specific scenarios"
1. "Show me how declaration merging works in TypeScript with module augmentation examples"

## Key Takeaways

- Object types can be defined with `type` or `interface` — interfaces support declaration merging and extension
- Excess property checks only apply to object literals, not intermediate variables
- Index signatures let you model dictionary-like objects with dynamic keys
