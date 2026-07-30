---
{
  "slug": "rs-06-methods",
  "title": "Methods and Associated Functions",
  "description": "Method syntax, self parameters, associated functions, method chaining, and traits for shared behavior.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define methods on structs and enums",
    "Understand self, &self, and &mut self",
    "Write associated functions (constructors)",
    "Chain methods for clean APIs"
  ],
  "knowledge_refs": ["rust/rs-06-methods"],
  "prerequisites": ["RS-05"],
  "references": [
    {"title": "The Rust Book — Method Syntax", "url": "https://doc.rust-lang.org/book/ch05-03-method-syntax.html"},
    {"title": "Rust by Example — Methods", "url": "https://doc.rust-lang.org/stable/rust-by-example/fn/methods.html"},
    {"title": "Rust std::ops", "url": "https://doc.rust-lang.org/std/ops/index.html"},
    {"title": "Rust Design Patterns", "url": "https://rust-unofficial.github.io/patterns/" }
  ]
}
---

# RS-06: Methods and Associated Functions

## Introduction

Methods in Rust are functions defined within the context of a struct (or enum) using `impl` blocks. They take `self` as their first parameter. Associated functions don't take `self` and serve as constructors. Methods enable clean, object-oriented-like APIs.

## Key Concepts

### 1. Defining Methods

Methods are defined in `impl` blocks. The first parameter is always `self`, `&self`, or `&mut self`. `self` takes ownership, `&self` borrows immutably, `&mut self` borrows mutably.

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    // Method: borrows self immutably
    fn area(&self) -> u32 {
        self.width * self.height
    }

    // Method: borrows self mutably
    fn set_width(&mut self, width: u32) {
        self.width = width;
    }

    // Method: takes ownership
    fn consume(self) -> String {
        format!("Rectangle {}x{}", self.width, self.height)
    }

    // Associated function (constructor, no self)
    fn square(size: u32) -> Rectangle {
        Rectangle {
            width: size,
            height: size,
        }
    }
}

fn main() {
    let mut rect = Rectangle {
        width: 30,
        height: 50,
    };

    println!("Area: {}", rect.area());    // 1500
    rect.set_width(40);
    println!("New area: {}", rect.area()); // 2000

    let square = Rectangle::square(10);   // associated function
    println!("Square area: {}", square.area());
}
```

### 2. Multiple impl Blocks

Structs can have multiple `impl` blocks. This is useful for organizing code and separates concerns. Generic types often use multiple impl blocks for different type constraints.

```rust
struct Point<T> {
    x: T,
    y: T,
}

impl<T> Point<T> {
    fn x(&self) -> &T {
        &self.x
    }
}

// Methods only for f64 type
impl Point<f64> {
    fn distance_from_origin(&self) -> f64 {
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }
}

fn main() {
    let p = Point { x: 5, y: 10 };
    println!("p.x = {}", p.x());

    let p_float = Point { x: 3.0, y: 4.0 };
    println!("Distance: {}", p_float.distance_from_origin());

    // This doesn't compile: distance_from_origin only for f64
    // let p_int = Point { x: 5, y: 10 };
    // p_int.distance_from_origin();  // ERROR!
}
```

### 3. Method Chaining

Methods that return `self` enable chaining. This is a common pattern for builder APIs and configuration.

```rust
struct Calculator {
    value: i32,
}

impl Calculator {
    fn new() -> Self {
        Calculator { value: 0 }
    }

    fn add(mut self, n: i32) -> Self {
        self.value += n;
        self
    }

    fn multiply(mut self, n: i32) -> Self {
        self.value *= n;
        self
    }

    fn get(&self) -> i32 {
        self.value
    }
}

fn main() {
    let result = Calculator::new()
        .add(5)
        .multiply(3)
        .add(10)
        .get();

    println!("Result: {}", result);  // (0 + 5) * 3 + 10 = 25

    // Builder pattern example
    struct Config {
        host: String,
        port: u16,
        debug: bool,
    }

    struct ConfigBuilder {
        host: String,
        port: u16,
        debug: bool,
    }

    impl ConfigBuilder {
        fn new() -> Self {
            ConfigBuilder {
                host: String::from("localhost"),
                port: 8080,
                debug: false,
            }
        }
        fn host(mut self, host: &str) -> Self {
            self.host = host.to_string();
            self
        }
        fn port(mut self, port: u16) -> Self {
            self.port = port;
            self
        }
        fn debug(mut self, debug: bool) -> Self {
            self.debug = debug;
            self
        }
        fn build(self) -> Config {
            Config {
                host: self.host,
                port: self.port,
                debug: self.debug,
            }
        }
    }
}
```

### 4. Traits for Shared Behavior

Traits define shared behavior across types. They're similar to interfaces in other languages but with more power (associated types, default methods, etc.).

```rust
trait Summary {
    fn summarize(&self) -> String;

    // Default implementation
    fn summary_author(&self) -> String {
        String::from("(unknown author)")
    }
}

struct Article {
    headline: String,
    author: String,
    content: String,
}

impl Summary for Article {
    fn summarize(&self) -> String {
        format!("{} by {}", self.headline, self.author)
    }
}

struct Tweet {
    username: String,
    content: String,
    retweets: u64,
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("@{}: {}", self.username, self.content)
    }
}

// Trait as parameter
fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}

// Trait bound syntax
fn notify2<T: Summary>(item: &T) {
    println!("{}", item.summarize());
}

// Multiple trait bounds
fn notify3(item: &(impl Summary + Display)) {
    // ...
}

fn main() {
    let article = Article {
        headline: String::from("Rust is amazing!"),
        author: String::from("Alice"),
        content: String::from("..."),
    };
    notify(&article);

    let tweet = Tweet {
        username: String::from("@rustacean"),
        content: String::from("Learning Rust!"),
        retweets: 42,
    };
    notify(&tweet);
}
```

## Practice Questions

1. What is the difference between `self`, `&self`, and `&mut self`?
2. What is an associated function? How does it differ from a method?
3. Why would you use multiple impl blocks for a single struct?
4. How does method chaining work? What pattern does it enable?
5. What is a trait? How is it similar to interfaces in other languages?

## LLM Prompts for Deeper Understanding

1. "Explain Rust methods: self parameters, ownership, borrowing, and method resolution"
2. "Show method chaining and the builder pattern for fluent APIs"
3. "Teach traits: definition, implementation, default methods, trait bounds, and impl Trait"

## Key Takeaways

- Methods are defined in `impl` blocks with `self`, `&self`, or `&mut self`
- Associated functions (no `self`) serve as constructors
- Multiple `impl` blocks allow organizing code by concern
- Method chaining enables fluent builder APIs
- Traits define shared behavior across types with default implementations