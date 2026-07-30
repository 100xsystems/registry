---
{
  "title": "Type Guards and Narrowing",
  "description": "Define user-defined type predicates (is)",
  "type": "lesson",
  "order": 13,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define user-defined type predicates (is)",
    "Use switch/case with discriminated unions exhaustively",
    "Implement asserts functions for custom validation",
    "Combine typeof, instanceof, in, and Array.isArray checks"
  ],
  "knowledge_refs": [
    "typescript/ts-13-type-guards"
  ],
  "prerequisites": [
    "TS-06"
  ],
  "references": [
    {
      "title": "TS Handbook — Narrowing",
      "url": "https://www.typescriptlang.org/docs/handbook/2/narrowing.html"
    },
    {
      "title": "TS Handbook — Type Predicates",
      "url": "https://www.typescriptlang.org/docs/handbook/2/narrowing.html#using-type-predicates"
    },
    {
      "title": "TS Handbook — Assertion Functions",
      "url": "https://www.typescriptlang.org/docs/handbook/2/narrowing.html#assertion-functions"
    }
  ]
}
---

# TS-13-TYPE-GUARDS: Type Guards and Narrowing

## Introduction

Narrowing is how TypeScript refines a broad type (like a union) to a more specific type within a code branch. Built-in guards (`typeof`, `instanceof`, `in`, discriminated unions) cover most cases. For custom logic, you can write user-defined type predicates.

## Key Concepts

### 1. User-Defined Type Predicates (is)

A **type predicate** is a function that returns `value is Type`. When it returns `true`, TypeScript narrows the argument to that type in the calling scope. This is the standard pattern for runtime type checks.

```typescript
interface Cat { meow(): void; sleep(): void; }
interface Dog { bark(): void; sleep(): void; }

// User-defined type predicate
function isCat(pet: Cat | Dog): pet is Cat {
  return (pet as Cat).meow !== undefined;
}

function play(pet: Cat | Dog) {
  if (isCat(pet)) {
    pet.meow();  // narrowed to Cat
  } else {
    pet.bark();  // narrowed to Dog
  }
}

// Multiple predicates
function isStringArray(arr: unknown[]): arr is string[] {
  return arr.every(item => typeof item === 'string');
}
```

### 2. Exhaustive Switch — Never at Default

The `never` type in the default branch of a switch ensures every union member is handled. If a new member is added, TypeScript will error at the default branch — a compile-time safety net.

```typescript
type Status = 'idle' | 'loading' | 'success' | 'error';

function handleStatus(status: Status): string {
  switch (status) {
    case 'idle':
      return 'Waiting...';
    case 'loading':
      return 'Loading...';
    case 'success':
      return 'Done!';
    case 'error':
      return 'Failed.';
    default:
      // If a new status is added to the union, this line will error
      const _exhaustive: never = status;
      return _exhaustive;
  }
}

// With discriminated union
type ApiResult =
  | { status: 'pending' }
  | { status: 'success'; data: unknown }
  | { status: 'error'; error: Error };

function handleResult(result: ApiResult) {
  switch (result.status) {
    case 'pending': return 'Please wait...';
    case 'success': return `Data: ${result.data}`;
    case 'error': return `Error: ${result.error.message}`;
    default:
      const _: never = result;  // compile-time exhaustiveness
  }
}
```

### 3. Assertion Functions — Shorthand Validation

An **assertion function** (`asserts value is Type`) throws if the value is not of the expected type. After it passes, TypeScript narrows the type in the calling scope. Great for validation functions.

```typescript
// Basic assertion
function assertString(value: unknown): asserts value is string {
  if (typeof value !== 'string') {
    throw new TypeError('Expected string');
  }
}

function process(input: unknown) {
  assertString(input);
  console.log(input.toUpperCase());  // narrowed to string
}

// Assert condition
interface User { name: string; email: string }
function assertUser(obj: unknown): asserts obj is User {
  if (typeof obj !== 'object' || obj === null) throw new Error('Not object');
  if (!('name' in obj) || !('email' in obj)) throw new Error('Missing props');
}

function handleObj(obj: unknown) {
  assertUser(obj);
  console.log(obj.name);  // narrowed to User
}
```

### 4. Built-in Guards: typeof, instanceof, in, Array.isArray

TypeScript understands all JavaScript runtime type-checking constructs. `typeof` for primitives, `instanceof` for class instances, `in` for property existence, `Array.isArray` for arrays — each narrows the type accordingly.

```typescript
function process(value: string | number | Date | string[] | null) {
  // null check
  if (value === null) return;

  // typeof for primitives
  if (typeof value === 'string') {
    return value.toUpperCase();       // narrowed to string
  }
  if (typeof value === 'number') {
    return value.toFixed(2);           // narrowed to number
  }

  // instanceof for class instances
  if (value instanceof Date) {
    return value.toISOString();        // narrowed to Date
  }

  // Array.isArray
  if (Array.isArray(value)) {
    return value.join(', ');          // narrowed to string[]
  }
}

// in operator narrowing
type Response = { data: unknown } | { error: string };
function handleResponse(res: Response) {
  if ('data' in res) {
    console.log(res.data);  // narrowed to { data: unknown }
  } else {
    console.error(res.error);  // narrowed to { error: string }
  }
}
```

### 5. Custom Guards with Zod, io-ts, or Validators

For complex runtime validation, libraries like **Zod** or **io-ts** generate type predicates from schemas. They parse unknown data and narrow the type — the gold standard for API boundary validation.

```typescript
// Using a generic validator pattern
interface Validator<T> {
  parse(data: unknown): T;
  schema: object;
}

function createValidator<T>(schema: object): Validator<T> {
  return {
    parse(data: unknown): T {
      // Simple validation — in practice use Zod
      if (typeof data !== 'object' || data === null) {
        throw new Error('Invalid data');
      }
      return data as T;
    },
    schema,
  };
}

const UserValidator = createValidator<User>({
  name: 'string',
  email: 'string',
});

// In an API handler:
function handleApiData(raw: unknown): void {
  const user = UserValidator.parse(raw);  // now typed as User
  console.log(user.name);
}
```

## Practice Questions

1. Write a type predicate function that checks if a value is a non-empty string (`str is string`).
1. What happens in the `default` branch of the exhaustiveness check if you add a new member to the union?
1. How does `asserts value is Type` differ from `value is Type` in a return type? When would you use each?
1. Why does `typeof null === "object"` matter when writing type guards for nullable types?

## LLM Prompts for Deeper Understanding

1. "Explain TypeScript type predicates and assertion functions with real-world validation examples"
1. "Show me exhaustive type checking patterns with discriminated unions and the never type"
1. "Teach me how to build runtime type validation with Zod that integrates with TypeScript narrowing"

## Key Takeaways

- User-defined type predicates (`value is Type`) enable custom narrowing logic
- Exhaustiveness checking with `never` in default branches catches unhandled union members
- Assertion functions (`asserts value is Type`) throw on invalid input and narrow after
