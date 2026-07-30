---
{
  "title": "Advanced Patterns: Branding, Builder, Fluent APIs",
  "description": "Implement nominal typing with branded types",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Implement nominal typing with branded types",
    "Build type-safe builder and fluent API patterns",
    "Use satisfies operator for precise type inference",
    "Implement discriminated union async state machines"
  ],
  "knowledge_refs": [
    "typescript/ts-17-advanced-patterns"
  ],
  "prerequisites": [
    "TS-08",
    "TS-10",
    "TS-14"
  ],
  "references": [
    {
      "title": "TS Handbook — satisfies",
      "url": "https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-9.html#the-satisfies-operator"
    },
    {
      "title": "TypeScript Deep Dive — Branded Types",
      "url": "https://basarat.gitbook.io/typescript/main-1/branding"
    },
    {
      "title": "TS Handbook — Template Literals",
      "url": "https://www.typescriptlang.org/docs/handbook/2/template-literal-types.html"
    }
  ]
}
---

# TS-17-ADVANCED-PATTERNS: Advanced Patterns: Branding, Builder, Fluent APIs

## Introduction

Beyond basic types, TypeScript enables sophisticated patterns: branded types for nominal typing, builder patterns for step-by-step construction, fluent APIs for composable pipelines, and the `satisfies` operator for precise type checking with broad inference.

## Key Concepts

### 1. Branded Types — Nominal Typing

TypeScript uses structural typing (duck typing), but sometimes you need distinct types for the same structure (e.g., `UserId` vs `OrderId`). **Branding** adds a unique phantom property that doesn't exist at runtime but enforces type safety.

```typescript
// Branded type pattern
type Brand<T, B> = T & { __brand: B };

type UserId = Brand<string, 'UserId'>;
type OrderId = Brand<string, 'OrderId'>;
type Email = Brand<string, 'Email'>;

function getUser(id: UserId): User { /* ... */ }
function getOrder(id: OrderId): Order { /* ... */ }

// These are NOT interchangeable:
const uid = 'user-123' as UserId;
const oid = 'order-456' as OrderId;

getUser(uid);  // OK
getUser(oid);  // Error: Brand<'OrderId'> not assignable to Brand<'UserId'>

// Alternative: branded type with creation guard
function createUserId(value: string): UserId {
  if (!value.startsWith('user-')) {
    throw new Error('Invalid user ID format');
  }
  return value as UserId;
}
```

### 2. Builder Pattern with Typed Steps

A **builder** constructs complex objects step by step. With TypeScript generics and conditional types, you can enforce that steps are called in order — making invalid states unrepresentable at compile time.

```typescript
// Type-safe builder with step enforcement
interface Car {
  engine: string;
  wheels: number;
  color: string;
  sunroof: boolean;
}

class CarBuilder {
  private car: Partial<Car> = {};

  setEngine(engine: string): this {
    this.car.engine = engine;
    return this;
  }

  setWheels(count: number): this {
    this.car.wheels = count;
    return this;
  }

  setColor(color: string): this {
    this.car.color = color;
    return this;
  }

  addSunroof(): this {
    this.car.sunroof = true;
    return this;
  }

  build(): Car {
    if (!this.car.engine || !this.car.wheels || !this.car.color) {
      throw new Error('Missing required fields');
    }
    return this.car as Car;
  }
}

const car = new CarBuilder()
  .setEngine('V8')
  .setWheels(4)
  .setColor('red')
  .addSunroof()
  .build();
```

### 3. Fluent API Pipeline

Fluent APIs chain operations while transforming the type at each step. This is common in query builders, data processing pipelines, and validation chains.

```typescript
// Type-safe pipeline
class Pipeline<I, O> {
  constructor(private transform: (input: I) => O) {}

  then<T>(next: (value: O) => T): Pipeline<I, T> {
    return new Pipeline((input: I) => next(this.transform(input)));
  }

  execute(input: I): O {
    return this.transform(input);
  }
}

function from<I>() {
  return new Pipeline<I, I>((x) => x);
}

// Usage — type flows through each step
const pipeline = from<string>()
  .then(s => s.trim())
  .then(s => s.toLowerCase())
  .then(s => s.split(' '))
  .then(arr => arr.filter(w => w.length > 0))
  .then(arr => arr.length);

const count = pipeline.execute('  Hello World  ');  // number: 2
```

### 4. The satisfies Operator (TS 4.9+)

`satisfies` checks that a value's type matches a pattern without widening the value's type. This preserves the narrow literal types for use (like `as const` does) while ensuring structural compatibility.

```typescript
// Without satisfies — type widens
const palette1 = {
  red: [255, 0, 0],
  green: '#00ff00',
  blue: [0, 0, 255],
};
// palette1.red is number[] (wide)

// With satisfies + as const — type is checked AND kept narrow
const palette2 = {
  red: [255, 0, 0],
  green: '#00ff00',
  blue: [0, 0, 255],
} as const satisfies Record<string, readonly string | readonly number[]>;

// palette2.red is readonly [255, 0, 0] (narrow tuple!)
// palette2.blue is readonly [0, 0, 255]

// Error if value doesn't match:
const bad = {
  red: 42,  // Error: number not assignable to readonly number[]
} as const satisfies Record<string, readonly string | readonly number[]>;

// Without as const — satisfies checks but types are widened
// (readonly [number, number, number] becomes readonly number[])
const palette3 = {
  red: [255, 0, 0],
  green: '#00ff00',
  blue: [0, 0, 255],
} satisfies Record<string, string | number[]>;
// palette3.red is number[] (not tuple — no as const)
```

### 5. Typed State Machines (Discriminated Union State)

Model async operations as a state machine using discriminated unions. Each state has its own data — the impossible state (loading + error data simultaneously) is impossible to represent.

```typescript
// Async state as discriminated union
type AsyncState<T> =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: T; timestamp: number }
  | { status: 'error'; error: Error; retryCount: number };

// React-like usage
class StateManager<T> {
  private state: AsyncState<T> = { status: 'idle' };

  getState(): Readonly<AsyncState<T>> {
    return this.state;
  }

  async load(fetcher: () => Promise<T>): Promise<void> {
    this.state = { status: 'loading' };

    try {
      const data = await fetcher();
      this.state = { status: 'success', data, timestamp: Date.now() };
    } catch (err) {
      const currentState = this.state;
      this.state = {
        status: 'error',
        error: err instanceof Error ? err : new Error(String(err)),
        retryCount: currentState.status === 'error' ? currentState.retryCount + 1 : 0,
      };
    }
  }

  // Type-safe state access
  getData(): T | undefined {
    if (this.state.status === 'success') return this.state.data;
    return undefined;
  }
}
```

## Practice Questions

1. How does branded typing simulate nominal typing in TypeScript? What is the runtime cost?
1. Why does `satisfies` preserve narrow types while direct annotations widen them?
1. Model a type-safe state machine for a file upload process: idle, selecting, uploading, paused, completed, error.
1. What are the benefits of making impossible states unrepresentable in a discriminated union?

## LLM Prompts for Deeper Understanding

1. "Explain branded types in TypeScript for nominal typing with real-world examples"
1. "Show me the satisfies operator in TypeScript 4.9+ with comparison to direct type annotations"
1. "Teach me typed state machine patterns with discriminated unions for React applications"

## Key Takeaways

- Branded types simulate nominal typing with zero runtime overhead
- `satisfies` checks structure while preserving the narrow inferred type
- Discriminated union states make impossible states unrepresentable at compile time
