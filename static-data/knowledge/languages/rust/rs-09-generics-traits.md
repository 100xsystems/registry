---
{
  "slug": "rs-09-generics-traits",
  "title": "Generics and Traits",
  "description": "Generic functions and structs, trait definitions, trait bounds, impl Trait, and blanket implementations.",
  "type": "lesson",
  "order": 9,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write generic functions and structs",
    "Define and implement traits",
    "Use trait bounds for type constraints",
    "Use impl Trait and where clauses"
  ],
  "knowledge_refs": ["rust/rs-09-generics-traits"],
  "prerequisites": ["RS-06"],
  "references": [
    {"title": "The Rust Book — Generics", "url": "https://doc.rust-lang.org/book/ch10-00-generics.html"},
    {"title": "The Rust Book — Traits", "url": "https://doc.rust-lang.org/book/ch10-02-traits.html"},
    {"title": "Rust by Example — Generics", "url": "https://doc.rust-lang.org/stable/rust-by-example/generics.html"},
    {"title": "Rust by Example — Traits", "url": "https://doc.rust-lang.org/stable/rust-by-example/trait.html"}
  ]
}
---

# RS-09: Generics and Traits

## Introduction

Generics allow writing code that works with multiple types without duplicating code. Traits define shared behavior that types can implement. Together, generics and traits enable powerful, type-safe abstractions with zero runtime cost through monomorphization.

## Key Concepts

### 1. Generic Functions

Generic functions use type parameters in angle brackets. The compiler generates specialized code for each concrete type (monomorphization), resulting in zero runtime overhead.

```rust
// Generic function: finds the largest element
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut largest = &list[0];
    for item in list {
        if item > largest {
            largest = item;
        }
    }
    largest
}

fn main() {
    let numbers = vec![34, 50, 25, 100, 65];
    let result = largest(&numbers);
    println!("Largest: {}", result);  // 100

    let chars = vec!['y', 'm', 'a', 'q'];
    let result = largest(&chars);
    println!("Largest: {}", result);  // 'y'

    // Generic function with multiple type parameters
    fn point<T, U>(x: T, y: U) -> (T, U) {
        (x, y)
    }
    let p = point(1, 2.0);  // (i32, f64)
}
```

### 2. Generic Structs and Methods

Structs and enums can also be generic. Methods on generic structs can add additional type parameters or constraints.

```rust
struct Point<T> {
    x: T,
    y: T,
}

// Generic impl — works for all T
impl<T> Point<T> {
    fn x(&self) -> &T {
        &self.x
    }
}

// Specialized impl — only for f64
impl Point<f64> {
    fn distance_from_origin(&self) -> f64 {
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }
}

// Multiple generic types
struct Pair<X, Y> {
    first: X,
    second: Y,
}

impl<X, Y> Pair<X, Y> {
    fn new(first: X, second: Y) -> Self {
        Pair { first, second }
    }
}

// Mixing generic type params with method params
impl<T: Display + PartialOrd> Point<T> {
    fn compare_and_display(&self, other: &Point<T>) {
        if self.x > other.x {
            println!("{} is larger", self.x);
        }
    }
}
```

### 3. Trait Definitions and Implementations

Traits define method signatures that implementors must provide. Traits can provide default implementations. Types can implement multiple traits.

```rust
// Trait definition
trait Summary {
    fn summarize(&self) -> String;

    // Default implementation
    fn summary_author(&self) -> String {
        String::from("(unknown)")
    }
}

struct Article {
    headline: String,
    author: String,
    content: String,
}

// Implementing a trait
impl Summary for Article {
    fn summarize(&self) -> String {
        format!("{} by {}", self.headline, self.author)
    }
}

struct Tweet {
    username: String,
    content: String,
    reply: bool,
    retweet: bool,
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("@{}: {}", self.username, self.content)
    }

    // Override default
    fn summary_author(&self) -> String {
        format!("@{}", self.username)
    }
}

// Orphan rule: you can implement a trait for a type
// only if either the trait or the type is local to your crate
```

### 4. Trait Bounds and Where Clauses

Trait bounds restrict generic types to those that implement specific traits. The `where` clause provides cleaner syntax for complex bounds.

```rust
// Simple trait bound
fn notify<T: Summary>(item: &T) {
    println!("Breaking: {}", item.summarize());
}

// Multiple trait bounds
fn notify2<T: Summary + Display>(item: &T) {
    println!("{}: {}", item, item.summarize());
}

// Where clause (cleaner for complex bounds)
fn some_function<T, U>(t: &T, u: &U) -> i32
where
    T: Display + Clone,
    U: Clone + Debug,
{
    // ...
    0
}

// Return type with impl Trait
fn returns_summarizable() -> impl Summary {
    Tweet {
        username: String::from("horse_ebooks"),
        content: String::from("of course, as you probably already know, people"),
        reply: false,
        retweet: false,
    }
}

// Conditional trait methods with where
struct Pair<T> {
    x: T,
    y: T,
}

impl<T> Pair<T> {
    fn new(x: T, y: T) -> Self {
        Self { x, y }
    }
}

// cmp_display only available when T implements Display + PartialOrd
impl<T: Display + PartialOrd> Pair<T> {
    fn cmp_display(&self) {
        if self.x >= self.y {
            println!("Largest: {}", self.x);
        } else {
            println!("Largest: {}", self.y);
        }
    }
}
```

### 5. Blanket Implementations and Trait Coherence

Blanket implementations implement a trait for all types that satisfy a bound. The coherence rules ensure there's no ambiguity about which implementation applies.

```rust
// Blanket implementation: implement ToString for all Display types
// (this is in the standard library)
// impl<T: Display> ToString for T {
//     fn to_string(&self) -> String {
//         // ...
//     }
// }

// This means any type implementing Display gets .to_string() for free
let s = 3.to_string();  // "3" — i32 implements Display
let s = true.to_string();  // "true" — bool implements Display

// Marker traits: traits with no methods
trait Validatable {}
impl Validatable for i32 {}
impl Validatable for String {}

fn process<T: Validatable>(val: T) {
    // any Validatable type can be processed
}

// Auto traits (automatically implemented)
// Send and Sync are auto traits:
// - Send: types that can be transferred across thread boundaries
// - Sync: types that can be shared across threads
// Most types are automatically Send and Sync

// Negative trait bounds (nightly)
// fn process<T: !Send>(val: T) { ... }
```

## Practice Questions

1. What is monomorphization? Why does it result in zero runtime cost?
2. What is the difference between a trait bound and an impl Trait parameter?
3. When should you use a where clause instead of inline trait bounds?
4. What is the orphan rule? Why does it exist?
5. What is a blanket implementation? Give an example from the standard library.

## LLM Prompts for Deeper Understanding

1. "Explain generics: monomorphization, type parameters, generic structs, and conditional methods"
2. "Show traits: definition, implementation, default methods, trait bounds, and where clauses"
3. "Teach advanced concepts: blanket implementations, orphan rule, coherence, and auto traits"

## Key Takeaways

- Generics enable type-safe, zero-cost abstraction via monomorphization
- Traits define shared behavior; types can implement multiple traits
- Trait bounds constrain generic types; `where` clauses for complex bounds
- `impl Trait` in return position for opaque return types
- Blanket implementations provide functionality for all types implementing a trait