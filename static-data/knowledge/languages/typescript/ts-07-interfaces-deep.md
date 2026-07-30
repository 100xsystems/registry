---
{
  "title": "Interfaces Deep Dive",
  "description": "Use interface extends with multiple inheritance",
  "type": "lesson",
  "order": 7,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use interface extends with multiple inheritance",
    "Implement interfaces in classes",
    "Leverage declaration merging for module augmentation",
    "Use interface call/construct signatures and index types"
  ],
  "knowledge_refs": [
    "typescript/ts-07-interfaces-deep"
  ],
  "prerequisites": [
    "TS-04"
  ],
  "references": [
    {
      "title": "TS Handbook — Interfaces",
      "url": "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#interfaces"
    },
    {
      "title": "TS Handbook — Declaration Merging",
      "url": "https://www.typescriptlang.org/docs/handbook/declaration-merging.html"
    },
    {
      "title": "TS Handbook — Class Types",
      "url": "https://www.typescriptlang.org/docs/handbook/2/classes.html"
    }
  ]
}
---

# TS-07-INTERFACES-DEEP: Interfaces Deep Dive

## Introduction

Interfaces in TypeScript go far beyond simple object shapes. They can describe function signatures, constructors, indexable types, and hybrid types. Declaration merging allows interfaces to be augmented across files — a critical feature for library augmentation.

## Key Concepts

### 1. Interface Extension (Multiple Inheritance)

Unlike classes (which can only extend one class), interfaces can extend **multiple** interfaces. This makes them highly composable. Extending a type alias is also supported via intersections.

```typescript
interface Named {
  name: string;
}
interface Aged {
  age: number;
}
interface Contact {
  email: string;
  phone?: string;
}

// Multiple inheritance
interface Person extends Named, Aged, Contact {
  id: string;
}

const alice: Person = {
  id: 'u1',
  name: 'Alice',
  age: 30,
  email: 'alice@example.com',
};
```

### 2. Call Signatures and Construct Signatures

Interfaces can describe functions (call signatures) and constructor functions (construct signatures with `new`). This is essential for describing factory patterns and typed function APIs.

```typescript
// Call signature
interface StringFormatter {
  (input: string, ...args: string[]): string;
}
const format: StringFormatter = (input, ...args) => {
  return input.replace(/%s/g, () => args.shift() || '');
};

// Construct signature
interface TimestampConstructor {
  new (): Date;
  new (value: number): Date;
  new (value: string): Date;
}
// Date already satisfies this interface

// Hybrid type — both callable and has properties
interface Counter {
  (start: number): string;
  increment(): void;
  count: number;
}
```

### 3. Declaration Merging and Module Augmentation

When you declare an interface with the same name twice in the same scope, TypeScript **merges** both declarations. This is how libraries like `express` let you extend `Request`: via module augmentation.

```typescript
// Original library declaration
interface Request {
  body: any;
  params: Record<string, string>;
}

// Your augmentation (in a .d.ts or module)
interface Request {
  user?: { id: string; role: string };
}

// Now Request has BOTH sets of properties
function handler(req: Request) {
  console.log(req.body);   // from original
  console.log(req.user);   // from augmentation
}

// Module augmentation pattern
declare module 'express-session' {
  interface SessionData {
    userId?: string;
    roles?: string[];
  }
}
```

### 4. Interfaces vs Abstract Classes

Interfaces define **contracts** (no implementation). Abstract classes can define **partial implementation** with method bodies. Use interfaces for cross-cutting contracts; use abstract classes when shared implementation is needed.

```typescript
// Interface — pure contract
interface Serializer {
  serialize(data: unknown): string;
  deserialize<T>(input: string): T;
}

// Abstract class — shared implementation
abstract class StreamSerializer implements Serializer {
  abstract serialize(data: unknown): string;
  abstract deserialize<T>(input: string): T;

  // Shared implementation
  writeToStream(data: unknown, stream: NodeJS.WritableStream): void {
    stream.write(this.serialize(data));
  }
}
```

### 5. Recursive and Self-Referencing Interfaces

Interfaces can reference themselves to model recursive structures like trees, linked lists, or nested comments. TypeScript handles recursive types efficiently.

```typescript
interface TreeNode<T> {
  value: T;
  children: TreeNode<T>[];
}

const tree: TreeNode<number> = {
  value: 1,
  children: [
    { value: 2, children: [] },
    { value: 3, children: [{ value: 4, children: [] }] },
  ],
};

// Linked list
interface LinkedList<T> {
  value: T;
  next: LinkedList<T> | null;
}

function walk<T>(list: LinkedList<T> | null): T[] {
  const result: T[] = [];
  let current = list;
  while (current) {
    result.push(current.value);
    current = current.next;
  }
  return result;
}
```

## Practice Questions

1. How does interface declaration merging enable library augmentation? Give a real example.
1. What is the difference between an interface extending multiple interfaces and a class implementing multiple interfaces?
1. Write a call signature interface for a function that takes a string and returns a number.
1. Why might you choose an abstract class over an interface when both could define the same contract?

## LLM Prompts for Deeper Understanding

1. "Explain TypeScript declaration merging with module augmentation examples for Express.js"
1. "Compare abstract classes vs interfaces in TypeScript with code examples"
1. "Show me how to define recursive interfaces for JSON AST representation"

## Key Takeaways

- Interfaces support multiple extension and declaration merging
- Call signatures and construct signatures let interfaces describe functions and classes
- Module augmentation via declaration merging is essential for extending third-party libraries
