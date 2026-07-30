---
{
  "title": "Classes in TypeScript",
  "description": "Use parameter properties, access modifiers, and readonly",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use parameter properties, access modifiers, and readonly",
    "Implement interfaces and abstract classes",
    "Understand this typing and method overloading",
    "Use getters/setters with private backing fields"
  ],
  "knowledge_refs": [
    "typescript/ts-11-classes"
  ],
  "prerequisites": [
    "TS-07",
    "TS-08"
  ],
  "references": [
    {
      "title": "TS Handbook — Classes",
      "url": "https://www.typescriptlang.org/docs/handbook/2/classes.html"
    },
    {
      "title": "TS Handbook — Private vs Protected",
      "url": "https://www.typescriptlang.org/docs/handbook/2/classes.html#member-visibility"
    },
    {
      "title": "TypeScript Deep Dive — Classes",
      "url": "https://basarat.gitbook.io/typescript/type-system/classes"
    }
  ]
}
---

# TS-11-CLASSES: Classes in TypeScript

## Introduction

TypeScript builds on JavaScript classes with type annotations, access modifiers (`public`, `private`, `protected`), abstract classes, parameter properties, and type-level `this` control. These features make classes a powerful tool for OOP in TypeScript.

## Key Concepts

### 1. Parameter Properties — Declare and Initialize in One Step

TypeScript's **parameter properties** let you declare a constructor parameter AND a class property simultaneously by prefixing with `public`, `private`, `protected`, or `readonly`. This eliminates repetitive boilerplate.

```typescript
class User {
  constructor(
    public name: string,           // auto-creates this.name
    private id: string,             // auto-creates this.id
    readonly createdAt: Date,      // auto-creates this.createdAt (readonly)
    protected role: string = 'user' // auto-creates this.role
  ) {}
}

// Equivalent to:
class UserVerbose {
  public name: string;
  private id: string;
  readonly createdAt: Date;
  protected role: string;

  constructor(name: string, id: string, createdAt: Date, role: string = 'user') {
    this.name = name;
    this.id = id;
    this.createdAt = createdAt;
    this.role = role;
  }
}
```

### 2. Access Modifiers: public, private, protected

TypeScript offers three access levels. `public` (default) — accessible everywhere. `protected` — accessible within the class and subclasses. `private` — only within the class. TypeScript also supports the `#` private field syntax from ES2022.

```typescript
class Animal {
  public name: string;
  private dna: string;            // TypeScript private
  #weight: number;                // ES2022 hard private
  protected sound: string;

  constructor(name: string, dna: string, weight: number, sound: string) {
    this.name = name;
    this.dna = dna;
    this.#weight = weight;
    this.sound = sound;
  }

  public getInfo(): string {
    return `${this.name} says ${this.sound}`;
  }
}

class Dog extends Animal {
  constructor(name: string) {
    super(name, 'ATCG', 10, 'Woof');
    console.log(this.sound);  // OK — protected
    // console.log(this.dna); // Error — private
  }
}
```

### 3. Abstract Classes — Partial Implementation

Abstract classes can define both abstract methods (no body — must be implemented by subclasses) and concrete methods (with body). They cannot be instantiated directly. Use them when shared implementation is needed alongside contracts.

```typescript
abstract class Shape {
  abstract area(): number;      // no body — subclass must implement
  abstract perimeter(): number;

  // Concrete shared method
  describe(): string {
    return `Area: ${this.area()}, Perimeter: ${this.perimeter()}`;
  }
}

class Circle extends Shape {
  constructor(private radius: number) { super(); }

  area(): number {
    return Math.PI * this.radius ** 2;
  }
  perimeter(): number {
    return 2 * Math.PI * this.radius;
  }
}

const c = new Circle(5);
console.log(c.describe());  // Area: 78.54, Perimeter: 31.42
```

### 4. this Typing — Method Parameter for Context

You can type the `this` parameter explicitly to prevent methods from losing their context. The `this` parameter is a "fake" parameter — it tells TypeScript what `this` should be when the method is called.

```typescript
class Counter {
  count = 0;

  // 'this' parameter ensures correct context
  increment(this: Counter): void {
    this.count++;
  }

  // Without this parameter, 'this' defaults to 'any'
  badIncrement(): void {
    this.count++;  // risky — could be called with wrong context
  }
}

const c = new Counter();
const fn = c.increment;
// fn();  // Error: The 'this' context of type 'void' is not assignable to 'Counter'

// Works correctly when called on the right object
const safe = c.increment.bind(c);
safe();  // OK

// Arrow functions capture this lexically
class SafeCounter {
  count = 0;
  increment = () => { this.count++; };  // lexical this
}
```

### 5. Getters, Setters, and Method Overloading

TypeScript supports getters/setters (accessors) that behave like properties but execute code. Method overloading allows multiple call signatures for the same function — useful for polymorphic APIs.

```typescript
class Temperature {
  constructor(private _celsius: number = 0) {}

  get celsius(): number {
    return this._celsius;
  }
  set celsius(value: number) {
    if (value < -273.15) throw new Error('Below absolute zero');
    this._celsius = value;
  }

  get fahrenheit(): number {
    return this._celsius * 9 / 5 + 32;
  }
  set fahrenheit(value: number) {
    this._celsius = (value - 32) * 5 / 9;
  }
}

// Method overloading — multiple call signatures
class EventBus {
  // Overload signatures
  on(event: 'click', handler: (x: number, y: number) => void): void;
  on(event: 'keypress', handler: (key: string) => void): void;
  // Implementation signature (not publicly visible)
  on(event: string, handler: (...args: any[]) => void): void {
    console.log(`Registering handler for ${event}`);
  }
}
```

## Practice Questions

1. What is the difference between `private` (TypeScript) and `#` (ES2022) private fields?
1. Why can't you instantiate an abstract class directly? What is its purpose?
1. How does the `this` parameter prevent context loss? Write an example where it catches a bug.
1. Write a class with a getter that derives a value from a private field and a setter that validates input.

## LLM Prompts for Deeper Understanding

1. "Explain TypeScript parameter properties vs explicit field declarations with examples"
1. "Show me TypeScript abstract class patterns with template method design pattern"
1. "Teach me this-typing and method overloading in TypeScript classes"

## Key Takeaways

- Parameter properties combine declaration and initialization in one step
- Abstract classes provide partial implementation — subclasses fill in abstract methods
- The `this` parameter prevents method context loss at the type level
