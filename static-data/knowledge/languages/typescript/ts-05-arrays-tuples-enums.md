---
{
  "title": "Arrays, Tuples, and Enums",
  "description": "Declare and manipulate typed arrays with generics",
  "type": "lesson",
  "order": 5,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare and manipulate typed arrays with generics",
    "Create fixed-length tuples with labeled elements",
    "Use numeric, string, and const enums effectively",
    "Understand enum runtime behavior and alternatives"
  ],
  "knowledge_refs": [
    "typescript/ts-05-arrays-tuples-enums"
  ],
  "prerequisites": [
    "TS-02"
  ],
  "references": [
    {
      "title": "TS Handbook — Array Types",
      "url": "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#arrays"
    },
    {
      "title": "TS Handbook — Tuple Types",
      "url": "https://www.typescriptlang.org/docs/handbook/2/objects.html#tuple-types"
    },
    {
      "title": "TS Handbook — Enums",
      "url": "https://www.typescriptlang.org/docs/handbook/enums.html"
    }
  ]
}
---

# TS-05-ARRAYS-TUPLES-ENUMS: Arrays, Tuples, and Enums

## Introduction

Arrays, tuples, and enums are the workhorses of TypeScript data modeling. Arrays describe homogeneous lists; tuples describe fixed-position heterogeneous lists; enums give meaningful names to sets of numeric or string constants.

## Key Concepts

### 1. Typed Arrays

TypeScript arrays are generic. The two syntaxes — `T[]` and `Array<T>` — are equivalent. Arrays inherit all the standard JavaScript methods with proper type inference for `map`, `filter`, `reduce`, and more.

```typescript
const names: string[] = ['Alice', 'Bob', 'Charlie'];
const numbers: Array<number> = [1, 2, 3];

// TypeScript infers callback parameter types
const lengths: number[] = names.map(n => n.length);
const evens: number[] = numbers.filter(n => n % 2 === 0);

// ReadonlyArray prevents mutation
const fixed: ReadonlyArray<string> = ['a', 'b'];
// fixed.push('c');  // Error!
```

### 2. Tuple Types — Fixed Length, Heterogeneous

Tuples let you specify the exact type at each position. They're ideal for function return pairs (e.g., `[error, data]`) and CSV rows. Accessing out-of-bounds indices causes errors.

```typescript
// Basic tuple
let pair: [string, number];
pair = ['age', 30];       // OK
pair = [30, 'age'];       // Error: number not assignable to string

// Tuples with optional and rest elements
type CsvRow = [string, number?, ...string[]];
const row1: CsvRow = ['Alice'];          // OK
const row2: CsvRow = ['Bob', 25];        // OK
const row3: CsvRow = ['Carol', 30, 'NY', 'USA'];  // OK

// Destructuring tuples
function divide(a: number, b: number): [number, number] {
  return [Math.floor(a / b), a % b];
}
const [quotient, remainder] = divide(10, 3);
```

### 3. Labeled Tuples (TS 4.0+)

TypeScript 4.0 added **labeled tuples**, giving semantic meaning to each position. This improves readability and tooling feedback.

```typescript
type Range = [start: number, end: number];
type HttpResponse = [status: number, body: string, headers?: Record<string, string>];

function fetchUser(id: number): HttpResponse {
  return [200, JSON.stringify({ id }), { 'content-type': 'application/json' }];
}

const [status, body] = fetchUser(1);
// status: number, body: string
```

### 4. Numeric and String Enums

Enums define a set of named constants. **Numeric enums** auto-increment from 0 (or from a custom start). **String enums** require explicit values. String enums are more readable in logs and network payloads.

```typescript
// Numeric enum (auto-incrementing)
enum Direction {
  Up,      // 0
  Down,    // 1
  Left,    // 2
  Right,   // 3
}

// Numeric enum with explicit start
enum StatusCode {
  OK = 200,
  Created = 201,
  BadRequest = 400,
  NotFound = 404,
}

// String enum (all values must be initialized)
enum Color {
  Red = '#FF0000',
  Green = '#00FF00',
  Blue = '#0000FF',
}

// Usage
function move(direction: Direction): void {
  console.log(`Moving ${Direction[direction]}`);  // reverse mapping
}
```

### 5. Const Enums and Enum Alternatives

**Const enums** are compiled away entirely — their members are inlined at use sites, zero runtime overhead. For string unions, consider `as const` objects instead; they provide similar safety without the enum baggage.

```typescript
// Const enum — removed at compile time
const enum HttpMethod {
  GET = 'GET',
  POST = 'POST',
  PUT = 'PUT',
  DELETE = 'DELETE',
}
const method = HttpMethod.GET;  // compiles to: const method = "GET";

// Alternative: as const objects
const Methods = {
  GET: 'GET',
  POST: 'POST',
  PUT: 'PUT',
  DELETE: 'DELETE',
} as const;
type Method = (typeof Methods)[keyof typeof Methods];  // "GET" | "POST" | "PUT" | "DELETE"
```

## Practice Questions

1. What is the difference between `string[]` and `[string, string]`?
1. How do you define a tuple where the last element is optional?
1. When would you choose a `const enum` over a regular enum, and what are the trade-offs?
1. Why might you prefer `as const` objects over enums in a library's public API?

## LLM Prompts for Deeper Understanding

1. "Explain TypeScript tuple types with variadic tuple syntax and labeled tuples"
1. "Compare numeric enums, string enums, const enums, and as const alternatives in TypeScript"
1. "Show me real-world patterns using ReadonlyArray and tuple types for API responses"

## Key Takeaways

- Arrays use `T[]` or `Array<T>` with full generic method support
- Tuples model fixed-position heterogeneous data with optional and rest elements
- String enums are more explicit than numeric; const enums have zero runtime cost
