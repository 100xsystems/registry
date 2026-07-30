---
{
  "slug": "rs-08-error-handling",
  "title": "Error Handling: Result and Option",
  "description": "Result<T, E>, Option<T>, the ? operator, combinators (map, and_then, unwrap_or), custom error types, and error conversion.",
  "type": "lesson",
  "order": 8,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use Result and Option for error handling",
    "Compose operations with combinators",
    "Create custom error types",
    "Use the ? operator for error propagation"
  ],
  "knowledge_refs": ["rust/rs-08-error-handling"],
  "prerequisites": ["RS-05"],
  "references": [
    {"title": "The Rust Book — Error Handling", "url": "https://doc.rust-lang.org/book/ch09-00-error-handling.html"},
    {"title": "Rust by Example — Error Handling", "url": "https://doc.rust-lang.org/stable/rust-by-example/error.html"},
    {"title": "std::result", "url": "https://doc.rust-lang.org/std/result/"},
    {"title": "anyhow crate", "url": "https://docs.rs/anyhow/"}
  ]
}
---

# RS-08: Error Handling: Result and Option

## Introduction

Rust doesn't have exceptions. Instead, it uses the Result<T, E> type for recoverable errors and panic! for unrecoverable errors. The ? operator and combinators provide ergonomic, composable error handling without the overhead of exceptions.

## Key Concepts

### 1. Result<T, E> and Option<T>

Result<T, E> represents success (Ok(T)) or failure (Err(E)). Option<T> represents a value (Some(T)) or no value (None). These are the primary error handling types.

```rust
fn main() {
    // Opening a file (Result)
    let file = std::fs::File::open("hello.txt");
    let file = match file {
        Ok(f) => f,
        Err(e) => match e.kind() {
            std::io::ErrorKind::NotFound => {
                panic!("File not found: {}", e)
            }
            _ => {
                panic!("Error opening file: {}", e)
            }
        },
    };

    // Option example
    fn find_user(id: u32) -> Option<String> {
        let users = vec![1, 2, 3];
        if users.contains(&id) {
            Some(format!("User {}", id))
        } else {
            None
        }
    }

    let user = find_user(1);
    match user {
        Some(name) => println!("Found: {}", name),
        None => println!("User not found"),
    }
}
```

### 2. The ? Operator

The `?` operator is the most ergonomic way to propagate errors. It unwraps Ok values and returns Err early. It can be used with both Result and Option.

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut file = File::open("username.txt")?;  // returns Err early
    let mut username = String::new();
    file.read_to_string(&mut username)?;         // returns Err early
    Ok(username)
}

// Even shorter
fn read_username() -> Result<String, io::Error> {
    let mut username = String::new();
    File::open("username.txt")?.read_to_string(&mut username)?;
    Ok(username)
}

// Shortest: use std::fs::read_to_string
fn read_username_short() -> Result<String, io::Error> {
    std::fs::read_to_string("username.txt")
}

// ? with Option
fn last_char_of_first_line(text: &str) -> Option<char> {
    text.lines().next()?.chars().last()
}

// ? in main (Rust 1.26+)
fn main() -> Result<(), Box<dyn std::error::Error>> {
    let username = read_username()?;
    println!("{}", username);
    Ok(())
}
```

### 3. Combinators: map, and_then, unwrap_or

Combinators compose operations without explicit match statements. They enable functional-style error handling.

```rust
fn main() {
    // map: transform Ok value
    let result: Result<i32, &str> = Ok(5);
    let doubled = result.map(|x| x * 2);  // Ok(10)

    // map_err: transform Err value
    let result: Result<i32, &str> = Err("error");
    let mapped = result.map_err(|e| format!("Custom: {}", e));  // Err("Custom: error")

    // and_then: chain operations that return Result
    fn parse(s: &str) -> Result<i32, String> {
        s.parse().map_err(|_| format!("Cannot parse: {}", s))
    }
    fn double(n: i32) -> Result<i32, String> {
        Ok(n * 2)
    }

    let result = parse("10").and_then(double);  // Ok(20)
    let result = parse("abc").and_then(double); // Err("Cannot parse: abc")

    // unwrap_or: default on error
    let value = parse("10").unwrap_or(0);        // 10
    let value = parse("abc").unwrap_or(0);       // 0

    // unwrap_or_else: lazy default
    let value = parse("abc").unwrap_or_else(|_| 42);  // 42

    // Combinator patterns
    let result = parse("10")
        .map(|x| x * 2)
        .and_then(|x| Ok(x + 1))
        .unwrap_or(0);  // 21
}
```

### 4. Custom Error Types

For production code, define custom error types that implement std::error::Error. This provides richer error information and enables `?` operator conversion.

```rust
use std::fmt;
use std::error::Error;

#[derive(Debug)]
struct AppError {
    kind: ErrorKind,
    message: String,
}

#[derive(Debug)]
enum ErrorKind {
    NotFound,
    PermissionDenied,
    InvalidInput,
}

impl fmt::Display for AppError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:?}: {}", self.kind, self.message)
    }
}

impl Error for AppError {}

// Conversion from std::io::Error
impl From<std::io::Error> for AppError {
    fn from(err: std::io::Error) -> AppError {
        AppError {
            kind: ErrorKind::NotFound,
            message: err.to_string(),
        }
    }
}

fn read_config() -> Result<String, AppError> {
    let content = std::fs::read_to_string("config.toml")?;  // auto-converts
    Ok(content)
}

// Using thiserror crate (much less boilerplate)
// use thiserror::Error;
//
// #[derive(Error, Debug)]
// enum AppError {
//     #[error("file not found: {0}")]
//     NotFound(#[from] std::io::Error),
//     #[error("invalid input: {0}")]
//     InvalidInput(String),
// }
```

### 5. Error Handling Patterns

Common patterns for robust error handling in real applications.

```rust
use std::num::ParseIntError;

// Pattern 1: Type alias for common Result
type Result<T> = std::result::Result<T, AppError>;

// Pattern 2: Box<dyn Error> for prototyping
type BoxResult<T> = Result<T, Box<dyn std::error::Error>>;

// Pattern 3: Combining different error types
fn process_data() -> Result<i32, Box<dyn std::error::Error>> {
    let file = std::fs::read_to_string("data.txt")?;  // io::Error -> Box<dyn Error>
    let num: i32 = file.trim().parse()?;               // ParseIntError -> Box<dyn Error>
    Ok(num * 2)
}

// Pattern 4: Option combinators
fn get_first_user() -> Option<String> {
    let users = vec!["alice", "bob"];
    users.first().map(|s| s.to_string())
}

// Pattern 5: Result <-> Option conversion
fn find_user(id: u32) -> Option<String> {
    // ...
    None
}

fn get_user(id: u32) -> Result<String, String> {
    find_user(id).ok_or_else(|| format!("User {} not found", id))
}

// Pattern 6: Logging and continuing
fn process_items(items: &[i32]) -> Vec<i32> {
    items.iter().filter_map(|&x| {
        if x > 0 { Some(x * 2) } else { None }
    }).collect()
}
```

## Practice Questions

1. What is the difference between Result<T, E> and Option<T>?
2. How does the ? operator work? What types can it be used with?
3. What is the difference between `map` and `and_then`?
4. How do you create a custom error type? What traits must it implement?
5. What is `Box<dyn Error>` and when should you use it?

## LLM Prompts for Deeper Understanding

1. "Explain Rust error handling: Result, Option, the ? operator, and combinators"
2. "Show custom error types: implementing Error, Display, From, and using thiserror"
3. "Teach error handling patterns: Box<dyn Error>, Result alias, filter_map, ok_or"

## Key Takeaways

- Result<T,E> for recoverable errors; Option<T> for optional values
- `?` operator propagates errors ergonomically
- Combinators (map, and_then, unwrap_or) compose operations functionally
- Custom error types implement std::error::Error for rich error information
- Box<dyn Error> is convenient for prototyping but custom types are better for production