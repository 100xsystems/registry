---
{
  "title": "Built-in Utility Types",
  "description": "Use Partial, Required, Readonly, Pick, Omit",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use Partial, Required, Readonly, Pick, Omit",
    "Use Extract, Exclude, NonNullable for union filtering",
    "Use Record, PickByType, and property mapping patterns",
    "Implement custom utility types using mapped and conditional types"
  ],
  "knowledge_refs": [
    "typescript/ts-14-utility-types"
  ],
  "prerequisites": [
    "TS-08",
    "TS-10"
  ],
  "references": [
    {
      "title": "TS Handbook — Utility Types",
      "url": "https://www.typescriptlang.org/docs/handbook/utility-types.html"
    },
    {
      "title": "TS Handbook — Mapped Types",
      "url": "https://www.typescriptlang.org/docs/handbook/2/mapped-types.html"
    },
    {
      "title": "TypeScript Deep Dive — Utility Types",
      "url": "https://basarat.gitbook.io/typescript/type-system/utility-types"
    }
  ]
}
---

# TS-14-UTILITY-TYPES: Built-in Utility Types

## Introduction

TypeScript ships with a rich set of built-in utility types that transform other types. Mastering these — `Partial`, `Pick`, `Omit`, `Record`, `Exclude`, `NonNullable`, `ReturnType`, and others — eliminates boilerplate and makes type definitions more maintainable.

## Key Concepts

### 1. Partial, Required, Readonly — Modifier Utilities

These utilities flip type modifiers: `Partial<T>` makes all properties optional; `Required<T>` makes them required; `Readonly<T>` makes them readonly. They are the most commonly used utilities.

```typescript
interface Config {
  host: string;
  port: number;
  ssl: boolean;
}

// All optional — for partial updates
function updateConfig(config: Partial<Config>): void {
  if (config.host) console.log(`Updating host to ${config.host}`);
}
updateConfig({ port: 8080 });  // only specify what changed

// All required — even if source has optionals
interface FormValues {
  name?: string;
  email?: string;
  age?: number;
}
type RequiredForm = Required<FormValues>;
// { name: string; email: string; age: number }

// All readonly — for frozen objects
type ImmutableConfig = Readonly<Config>;
// { readonly host: string; readonly port: number; readonly ssl: boolean }
```

### 2. Pick and Omit — Subtype Selection

`Pick<T, K>` selects a subset of properties; `Omit<T, K>` removes properties. These are essential for creating derived types from a base type without duplication.

```typescript
interface User {
  id: string;
  name: string;
  email: string;
  password: string;
  role: 'admin' | 'user';
  createdAt: Date;
}

// Public user profile — pick specific fields
type PublicProfile = Pick<User, 'id' | 'name' | 'email' | 'role'>;

// User creation input — omit auto-generated fields
type CreateUserInput = Omit<User, 'id' | 'createdAt'>;

// Nested pick with dot notation (homegrown)
type NestedPick<T, K extends string> = T extends Record<string, any>
  ? K extends `${infer F}.${infer R}`
    ? { [P in F]: NestedPick<T[F], R> }
    : Pick<T, K & keyof T>
  : never;

// Combine Omit with Partial for update payloads
type UpdateUserInput = Partial<Omit<User, 'id' | 'createdAt'>>;
```

### 3. Record — Dictionary/Object Type

`Record<K, V>` creates an object type where keys are `K` and values are `V`. It's the standard way to type dictionaries, maps, lookup tables, and enum-to-value mappings.

```typescript
// Basic dictionary
type UserMap = Record<string, User>;
const users: UserMap = {
  'user-1': { id: 'user-1', name: 'Alice', /* ... */ },
};

// Union keys for finite maps
type Status = 'active' | 'inactive' | 'pending';
type StatusMessages = Record<Status, string>;
const messages: StatusMessages = {
  active: 'User is active',
  inactive: 'User is inactive',
  pending: 'User is pending',
};

// Value as complex type
type RolePermissions = Record<'admin' | 'user' | 'guest', string[]>;
const permissions: RolePermissions = {
  admin: ['read', 'write', 'delete'],
  user: ['read', 'write'],
  guest: ['read'],
};
```

### 4. Extract, Exclude, NonNullable — Union Filtering

These utilities prune union types. `Extract<T, U>` keeps members assignable to `U`; `Exclude<T, U>` removes them; `NonNullable<T>` removes `null | undefined`.

```typescript
// Extract — keep matching
type Numbers = 'a' | 'b' | 'c' | 1 | 2 | 3;
type StringsOnly = Extract<Numbers, string>;  // 'a' | 'b' | 'c'

// Exclude — remove matching
type RemoveAdmin = Exclude<'admin' | 'user' | 'guest', 'admin'>;
// 'user' | 'guest'

// NonNullable — remove null/undefined
type Maybe = string | null | undefined | number;
type Definite = NonNullable<Maybe>;  // string | number

// Real-world: filter event types
type AllEvents = 'click' | 'hover' | 'focus' | 'blur' | 'scroll';
type MouseEvents = Extract<AllEvents, 'click' | 'hover'>;
type FocusEvents = Exclude<AllEvents, 'click' | 'hover' | 'scroll'>;
// 'focus' | 'blur'

```

### 5. ReturnType, Parameters, InstanceType — Function Utilities

These utilities extract types from function and class types. `ReturnType<T>` gets the return type; `Parameters<T>` gets the parameter tuple; `InstanceType<T>` gets the instance type from a constructor type.

```typescript
function createUser(name: string, age: number): { id: string; name: string } {
  return { id: crypto.randomUUID(), name, age: age };
}

type CreateUserReturn = ReturnType<typeof createUser>;
// { id: string; name: string }

type CreateUserParams = Parameters<typeof createUser>;
// [string, number]

// ConstructorParameters and InstanceType
class Service {
  constructor(private apiKey: string, private endpoint: string) {}
  fetch(path: string): Promise<unknown> { return fetch(`${this.endpoint}/${path}`); }
}

type ServiceParams = ConstructorParameters<typeof Service>;
// [string, string]
type ServiceInstance = InstanceType<typeof Service>;
// Service

// Awaited (TS 4.5+)
type AsyncResult = Awaited<Promise<string>>;  // string
type Deep = Awaited<Promise<Promise<number>>>;  // number
```

## Practice Questions

1. What is the difference between `Partial<T>` and `Pick<T, keyof T>`? Are they equivalent?
1. Why can't `Omit<T, K>` prevent you from omitting a non-existent key? How would you fix this?
1. Write a type that extracts the resolved value type from a Promise (like the built-in `Awaited`).
1. Create a `PickByValue<T, V>` utility that keeps only properties where the value type matches `V`.

## LLM Prompts for Deeper Understanding

1. "Explain all TypeScript built-in utility types with practical examples for each"
1. "Show me how to combine Omit, Partial, and Pick for type-safe API payloads in TypeScript"
1. "Teach me how to create custom utility types: PickByValue, DeepPartial, and NonFunctionKeys"

## Key Takeaways

- `Partial`, `Pick`, `Omit`, and `Record` cover 80% of type transformation needs
- `Exclude` and `Extract` filter union members; `NonNullable` removes null/undefined
- `ReturnType` and `Parameters` extract function type components at the type level
