---
{
  "slug": "rs-05-structs-enums",
  "title": "Structs, Enums, and Pattern Matching",
  "description": "Struct definitions, tuple structs, unit structs, enums, Option and Result, match expressions, and if let.",
  "type": "lesson",
  "order": 5,
  "duration": "75 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define and use structs with different variants",
    "Work with enums and the Option/Result types",
    "Use match expressions for pattern matching",
    "Use if let and while let for concise patterns"
  ],
  "knowledge_refs": ["rust/rs-05-structs-enums"],
  "prerequisites": ["RS-02"],
  "references": [
    {"title": "The Rust Book — Structs", "url": "https://doc.rust-lang.org/book/ch05-00-structs.html"},
    {"title": "The Rust Book — Enums", "url": "https://doc.rust-lang.org/book/ch06-00-enums.html"},
    {"title": "The Rust Book — Pattern Matching", "url": "https://doc.rust-lang.org/book/ch18-00-patterns.html"},
    {"title": "Rust by Example — Structures", "url": "https://doc.rust-lang.org/stable/rust-by-example/custom_types/structs.html"}
  ]
}
---

# RS-05: Structs, Enums, and Pattern Matching

## Introduction

Structs and enums are Rust's primary data structures. Structs group related data together. Enums represent data that can be one of several variants. Pattern matching with `match` enables exhaustive handling of all variants, eliminating a whole class of bugs.

## Key Concepts

### 1. Struct Definitions and Usage

Structs have three variants: named-field structs (most common), tuple structs (positional fields), and unit structs (no fields, used for markers).

```rust
// Named-field struct
struct User {
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool,
}

// Tuple struct
struct Color(i32, i32, i32);

// Unit struct (useful for generics and markers)
struct Unit;

fn main() {
    // Create instance
    let user = User {
        username: String::from("alice"),
        email: String::from("alice@example.com"),
        sign_in_count: 1,
        active: true,
    };

    // Mutable fields (entire struct must be mut)
    let mut user2 = User {
        username: String::from("bob"),
        ..user  // struct update syntax: fills remaining fields from user
    };
    user2.email = String::from("bob@example.com");

    // Tuple struct usage
    let black = Color(0, 0, 0);
    println!("R: {}, G: {}, B: {}", black.0, black.1, black.2);

    // Destructuring
    let Color(r, g, b) = black;
    println!("{r} {g} {b}");
}
```

### 2. Enums

Enums define a type that can be one of several variants. Each variant can carry data. Enums are Rust's way of expressing sum types (like algebraic data types in functional languages).

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

fn main() {
    let q = Message::Quit;
    let m = Message::Move { x: 10, y: 20 };
    let w = Message::Write(String::from("hello"));
    let c = Message::ChangeColor(255, 0, 0);

    // Enums with methods
    impl Message {
        fn call(&self) {
            match self {
                Message::Quit => println!("Quit"),
                Message::Move { x, y } => println!("Move to ({}, {})", x, y),
                Message::Write(text) => println!("Write: {}", text),
                Message::ChangeColor(r, g, b) => println!("Color: ({}, {}, {})", r, g, b),
            }
        }
    }

    w.call();
}
```

### 3. Option and Result

`Option<T>` represents a value that may or may not exist (no null!). `Result<T, E>` represents an operation that may succeed or fail. These are the most important enums in Rust.

```rust
// Option<T> — no null pointers!
fn divide(numerator: f64, denominator: f64) -> Option<f64> {
    if denominator == 0.0 {
        None  // no value
    } else {
        Some(numerator / denominator)
    }
}

// Result<T, E> — explicit error handling
fn parse_number(s: &str) -> Result<i32, std::num::ParseIntError> {
    s.parse::<i32>()
}

fn main() {
    // Option usage
    let result = divide(10.0, 2.0);
    match result {
        Some(value) => println!("Result: {}", value),
        None => println!("Cannot divide by zero"),
    }

    // Option combinators
    let doubled = divide(10.0, 2.0)
        .map(|x| x * 2.0)
        .unwrap_or(0.0);  // default on None

    // Result usage
    match parse_number("42") {
        Ok(n) => println!("Number: {}", n),
        Err(e) => println!("Error: {}", e),
    }

    // Result combinators
    let number = parse_number("42")
        .map(|n| n * 2)
        .unwrap_or(0);  // default on Err

    // The ? operator (propagates errors)
    fn process() -> Result<i32, std::num::ParseIntError> {
        let a = parse_number("10")?;  // returns Err if failed
        let b = parse_number("20")?;
        Ok(a + b)
    }
}
```

### 4. Match Expressions

`match` is Rust's pattern matching powerhouse. It must be exhaustive — all possible cases must be handled. The compiler enforces this, preventing forgotten cases.

```rust
enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter,
}

fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => {
            println!("Lucky penny!");
            1
        }
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    }
}

fn main() {
    // Match with Option
    let five = Some(5);
    let six = plus_one(five);
    let none = plus_one(None);

    // Catch-all patterns
    let dice_roll = 9;
    match dice_roll {
        3 => add_fancy_hat(),
        7 => remove_fancy_hat(),
        other => move_player(other),  // catch-all
    }

    // Use _ when you don't need the value
    match dice_roll {
        3 => add_fancy_hat(),
        7 => remove_fancy_hat(),
        _ => (),  // do nothing for all other values
    }
}

fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        None => None,
        Some(i) => Some(i + 1),
    }
}
```

### 5. if let and while let

`if let` and `while let` provide concise syntax for matching a single pattern. They're useful when you only care about one variant.

```rust
fn main() {
    let config_max = Some(3u8);

    // Verbose match
    match config_max {
        Some(max) => println!("The maximum is {}", max),
        _ => (),  // boring boilerplate
    }

    // Concise if let
    if let Some(max) = config_max {
        println!("The maximum is {}", max);
    }

    // if let with else
    let value: Option<i32> = None;
    if let Some(x) = value {
        println!("Got value: {}", x);
    } else {
        println!("No value");
    }

    // while let (loop until pattern fails)
    let mut stack = vec![1, 2, 3];
    while let Some(top) = stack.pop() {
        println!("{}", top);
    }

    // Combining with enums
    enum Status {
        Ready,
        Waiting,
        Done(String),
    }

    let status = Status::Done(String::from("finished"));
    if let Status::Done(msg) = status {
        println!("Completed: {}", msg);
    }
}
```

## Practice Questions

1. What are the three kinds of structs in Rust? When would you use each?
2. What is an enum? How does it differ from a struct?
3. What is the difference between Option and Result?
4. Why must match expressions be exhaustive? What happens if they aren't?
5. What is the difference between `if let` and `match`?

## LLM Prompts for Deeper Understanding

1. "Explain Rust's enum and pattern matching: algebraic data types, exhaustiveness checking, and match ergonomics"
2. "Show Option and Result patterns: combinators (map, and_then, unwrap_or), ?, and custom error handling"
3. "Teach struct patterns: destructuring, update syntax, tuple structs, and unit structs for markers"

## Key Takeaways

- Structs group data: named fields, tuple structs, unit structs
- Enums represent one of several variants, each can carry data
- Option<T> eliminates null pointers; Result<T,E> formalizes error handling
- match is exhaustive and must handle all cases
- if let/while let provide concise syntax for single-pattern matching