---
{
  "title": "Union and Intersection Types",
  "description": "Create union types with discriminated properties",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Create union types with discriminated properties",
    "Combine types with intersection types",
    "Narrow unions using type guards and discriminated unions",
    "Use never and unknown in union/intersection contexts"
  ],
  "knowledge_refs": [
    "typescript/ts-06-union-intersection"
  ],
  "prerequisites": [
    "TS-02",
    "TS-04"
  ],
  "references": [
    {
      "title": "TS Handbook — Union Types",
      "url": "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#union-types"
    },
    {
      "title": "TS Handbook — Intersection Types",
      "url": "https://www.typescriptlang.org/docs/handbook/2/types-from-types.html"
    },
    {
      "title": "TS Handbook — Narrowing",
      "url": "https://www.typescriptlang.org/docs/handbook/2/narrowing.html"
    }
  ]
}
---

# TS-06-UNION-INTERSECTION: Union and Intersection Types

## Introduction

Union types (`|`) and intersection types (`&`) are the cornerstones of TypeScript's structural type system. Unions represent "one of several possibilities"; intersections represent "all at once." Mastering these unlocks expressive, type-safe modeling.

## Key Concepts

### 1. Union Types — One of Many

A union type accepts a value that could be any one of its members. Primitives, object types, and literals can all be unioned. The only safely accessible properties are those common to all members of the union.

```typescript
type Result = string | number | boolean;
const r1: Result = 'hello';  // OK
const r2: Result = 42;       // OK

// Object unions — only common properties are accessible
type Admin = { role: 'admin'; permissions: string[] };
type User = { role: 'user'; email: string };
type Person = Admin | User;

function getRole(person: Person): string {
  return person.role;  // OK — exists in both
  // person.email;     // Error — does not exist on Admin
}
```

### 2. Intersection Types — All Combined

An intersection type combines all members of its constituents. If any member creates a conflict (like `string & number`), the result is `never`. Intersections are syntactic sugar for `extends` in some cases.

```typescript
type Named = { name: string };
type Aged = { age: number };
type Person = Named & Aged;

const p: Person = { name: 'Alice', age: 30 };  // OK

// Incompatible types produce never
type Impossible = string & number;  // type = never

// Intersection with conflicting property types
type Base = { id: string; value: number };
type Override = { value: string };
// type Merged = Base & Override;  // value: never (number & string)
// Better: use Omit to resolve
type Fixed = Omit<Base, 'value'> & Override;  // value: string
```

### 3. Discriminated Unions — The Killer Pattern

A **discriminated union** uses a common literal property (the "discriminant") to distinguish between members. TypeScript narrows the type automatically when you check the discriminant. This is the most important pattern in TypeScript.

```typescript
type Shape =
  | { kind: 'circle'; radius: number }
  | { kind: 'square'; sideLength: number }
  | { kind: 'triangle'; base: number; height: number };

function area(shape: Shape): number {
  switch (shape.kind) {
    case 'circle':
      return Math.PI * shape.radius ** 2;     // narrowed to circle
    case 'square':
      return shape.sideLength ** 2;             // narrowed to square
    case 'triangle':
      return (shape.base * shape.height) / 2;   // narrowed to triangle
    default:
      const _exhaustive: never = shape;         // ensure all cases handled
      return _exhaustive;
  }
}
```

### 4. Narrowing Unions with Type Guards

Beyond discriminated unions, TypeScript narrows unions using `typeof`, `instanceof`, `in`, and user-defined type predicates. Each narrowing technique reduces the union to a more specific type within a code branch.

```typescript
// typeof narrowing
function format(value: string | number): string {
  if (typeof value === 'string') {
    return value.toUpperCase();      // narrowed to string
  } else {
    return value.toFixed(2);          // narrowed to number
  }
}

// instanceof narrowing
class APIError extends Error {
  constructor(public statusCode: number) { super(); }
}
function handleError(err: Error | APIError) {
  if (err instanceof APIError) {
    console.log(`API ${err.statusCode}`);  // narrowed to APIError
  }
}

// in operator narrowing
type Fish = { swim: () => void };
type Bird = { fly: () => void };
function move(animal: Fish | Bird) {
  if ('swim' in animal) animal.swim();
  else animal.fly();
}
```

### 5. The never Type and Exhaustiveness Checks

`never` is the bottom type — it has no inhabitants. In unions, `never` is absorbed (`string | never` = `string`). Use it in the `default` branch of a switch to ensure all union members are handled; if a new member is added, the default will error.

```typescript
type Event =
  | { type: 'click'; x: number; y: number }
  | { type: 'keypress'; key: string }
  | { type: 'focus' };  // add this later — will trigger error

function handleEvent(event: Event) {
  switch (event.type) {
    case 'click':
      console.log(event.x, event.y);
      break;
    case 'keypress':
      console.log(event.key);
      break;
    // Forgot: case 'focus' — the default will catch it
    default:
      const _exhaustive: never = event;  // Error: Event not assignable to never
      break;
  }
}
```

## Practice Questions

1. What common properties can you safely access on a `string | number[]` union without narrowing?
1. Why does `string & number` produce `never`? Give another example of an impossible intersection.
1. Create a discriminated union for a payment system: `CreditCard`, `PayPal`, and `Crypto`. Each should have a unique discriminant property.
1. What happens in the exhaustiveness check if you add a new member to a union but forget to handle it in the switch?

## LLM Prompts for Deeper Understanding

1. "Explain TypeScript discriminated unions with real-world Redux action examples"
1. "Show me exhaustive type checking patterns with the never type in TypeScript"
1. "Compare intersection types (&) and interface extends in TypeScript — when to use each"

## Key Takeaways

- Union types model "one of many" — access only common properties without narrowing
- Discriminated unions with literal discriminant properties enable automatic narrowing
- Use `never` in default branches for compile-time exhaustiveness checks
