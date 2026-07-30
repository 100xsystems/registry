---
{
  "title": "Decorators and Metaprogramming",
  "description": "Understand decorator syntax and stages (legacy vs TC39)",
  "type": "lesson",
  "order": 19,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand decorator syntax and stages (legacy vs TC39)",
    "Implement class, method, accessor, and property decorators",
    "Use metadata reflection for runtime type information",
    "Understand when decorators are appropriate vs alternatives"
  ],
  "knowledge_refs": [
    "typescript/ts-19-decorators-mixins"
  ],
  "prerequisites": [
    "TS-11"
  ],
  "references": [
    {
      "title": "TS Handbook — Decorators",
      "url": "https://www.typescriptlang.org/docs/handbook/decorators.html"
    },
    {
      "title": "TC39 Decorators Proposal",
      "url": "https://github.com/tc39/proposal-decorators"
    },
    {
      "title": "TypeScript 5.0 Decorators",
      "url": "https://devblogs.microsoft.com/typescript/announcing-typescript-5-0/#decorators"
    }
  ]
}
---

# TS-19-DECORATORS-MIXINS: Decorators and Metaprogramming

## Introduction

Decorators provide a way to add annotations and metaprogramming to class declarations. TypeScript supports both the legacy experimental decorators (used by Angular, NestJS, TypeORM) and the new TC39 standard decorators (TS 5.0+). They are patterns for cross-cutting concerns like logging, caching, and authorization.

## Key Concepts

### 1. Legacy Decorators (experimentalDecorators)

TypeScript's original decorator implementation (enabled by `experimentalDecorators: true`) wraps the target with a function. These intercept class construction, property assignment, and method invocation. Use `reflect-metadata` for metadata annotations.

```typescript
// Enable in tsconfig.json: "experimentalDecorators": true

function log(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
  const originalMethod = descriptor.value;
  descriptor.value = function (...args: any[]) {
    console.log(`Calling ${propertyKey} with`, args);
    const result = originalMethod.apply(this, args);
    console.log(`Result from ${propertyKey}:`, result);
    return result;
  };
  return descriptor;
}

class Calculator {
  @log
  add(a: number, b: number): number {
    return a + b;
  }
}

const calc = new Calculator();
calc.add(2, 3);  // logs: "Calling add with [2, 3]" then "Result from add: 5"
```

### 2. TC39 Standard Decorators (TS 5.0+)

TypeScript 5.0+ supports the TC39 stage 3 decorator proposal. These decorators have different signatures and capabilities. They cannot modify the return type of the decorated method (pure metaprogramming).

```typescript
// TS 5.0+ decorator syntax (no experimentalDecorators needed)
function logged<T extends (...args: unknown[]) => unknown>(
  target: unknown,
  context: ClassMethodDecoratorContext
) {
  const methodName = String(context.name);

  function replacement(this: unknown, ...args: unknown[]) {
    console.log(`Calling ${methodName}`);
    const result = target.apply(this, args) as ReturnType<T>;
    console.log(`Finished ${methodName}`);
    return result;
  }

  return replacement;
}

class Service {
  @logged
  fetchData(id: string): Promise<string> {
    return Promise.resolve(`data-${id}`);
  }
}
```

### 3. Property and Accessor Decorators

Property decorators can observe property definitions. Accessor decorators (getters/setters) can wrap access. Use cases include computed properties, caching, and validation on set.

```typescript
// Caching decorator — memoize computed values
function cached(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
  const originalGet = descriptor.get!;
  let cache: { value: unknown; dirty: boolean } = { value: undefined, dirty: true };

  descriptor.get = function () {
    if (cache.dirty) {
      cache.value = originalGet.call(this);
      cache.dirty = false;
    }
    return cache.value;
  };

  // Mark cache dirty on dependent property set
  const originalSet = Object.getOwnPropertyDescriptor(target.constructor.prototype, '_data')?.set;
  if (originalSet) {
    // Inject cache invalidation
  }
}

// Property decorator for validation
function validate(target: any, propertyKey: string): void {
  let value: string;
  const key = `_${propertyKey}`;

  Object.defineProperty(target, propertyKey, {
    get() { return this[key]; },
    set(newVal: string) {
      if (newVal.length < 3) {
        throw new Error(`${propertyKey} must be at least 3 characters`);
      }
      this[key] = newVal;
    },
    enumerable: true,
    configurable: true,
  });
}
```

### 4. Metadata Reflection with reflect-metadata

`reflect-metadata` stores type annotations as metadata at runtime. Libraries like TypeORM, class-validator, and NestJS use this heavily for dependency injection, validation rules, and ORM decorators.

```typescript
import 'reflect-metadata';

const METADATA_KEY = Symbol('validation:required');

function required(target: Object, propertyKey: string | symbol) {
  Reflect.defineMetadata(METADATA_KEY, true, target, propertyKey);
}

function validate(obj: any): string[] {
  const errors: string[] = [];
  const prototype = Object.getPrototypeOf(obj);

  // Iterate over decorated properties
  const keys = Reflect.ownKeys(obj);
  for (const key of keys) {
    const isRequired = Reflect.getMetadata(METADATA_KEY, prototype, key);
    if (isRequired && (obj[key] === undefined || obj[key] === null || obj[key] === '')) {
      errors.push(`${String(key)} is required`);
    }
  }
  return errors;
}

class UserInput {
  @required
  name!: string;

  @required
  email!: string;

  age?: number;
}

const input = new UserInput();
input.name = 'Alice';
// input.email is undefined
console.log(validate(input));  // ['email is required']
```

### 5. Mixins — Composing Behaviors

Mixins compose class behaviors without inheritance chains. A mixin is a function that takes a base class and returns an extended class. TypeScript supports mixins well with generics.

```typescript
// Mixin pattern — type-safe
// Constructor type helper
type Constructor<T = {}> = new (...args: any[]) => T;

function Timestamped<TBase extends Constructor>(Base: TBase) {
  return class extends Base {
    createdAt = new Date();
    updatedAt?: Date;

    touch(): void {
      this.updatedAt = new Date();
    }
  };
}

function Activatable<TBase extends Constructor>(Base: TBase) {
  return class extends Base {
    isActive = false;

    activate(): void { this.isActive = true; }
    deactivate(): void { this.isActive = false; }
  };
}

// Compose mixins
class Person {
  constructor(public name: string) {}
}

const TimestampedPerson = Timestamped(Activatable(Person));
const user = new TimestampedPerson('Alice');

user.name;        // from Person
user.createdAt;   // from Timestamped
user.isActive;    // from Activatable
user.activate();  // from Activatable
```

## Practice Questions

1. What is the difference between legacy decorators and TC39 standard decorators?
1. How does `reflect-metadata` enable runtime type reflection that's not possible with plain JavaScript?
1. When would you use a mixin instead of multiple inheritance or interfaces?
1. Write a decorator that measures and logs the execution time of a method.

## LLM Prompts for Deeper Understanding

1. "Explain TypeScript decorators — legacy vs TC39 standard, with comparison table"
1. "Show me NestJS-style decorator patterns with reflect-metadata for validation"
1. "Teach me the mixin pattern in TypeScript for composing class behaviors"

## Key Takeaways

- Legacy decorators can modify behavior; TC39 decorators are pure metaprogramming
- `reflect-metadata` enables runtime annotations for validation, DI, and ORMs
- Mixins compose class behaviors without deep inheritance hierarchies
