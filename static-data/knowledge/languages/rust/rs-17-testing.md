---
{
  "slug": "rs-17-testing",
  "title": "Testing and Documentation",
  "description": "Unit tests, integration tests, doc tests, test organization, benchmarks, and documentation with rustdoc.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write unit tests and integration tests",
    "Use doc tests for documentation examples",
    "Organize tests effectively",
    "Write documentation with rustdoc"
  ],
  "knowledge_refs": ["rust/rs-17-testing"],
  "prerequisites": ["RS-01"],
  "references": [
    {"title": "The Rust Book — Testing", "url": "https://doc.rust-lang.org/book/ch11-00-testing.html"},
    {"title": "Rust by Example — Testing", "url": "https://doc.rust-lang.org/stable/rust-by-example/testing.html"},
    {"title": "Rustdoc Documentation", "url": "https://doc.rust-lang.org/rustdoc/"},
    {"title": "std::test", "url": "https://doc.rust-lang.org/std/test/index.html"}
  ]
}
---

# RS-17: Testing and Documentation

## Introduction

Rust has built-in testing support with test functions, benchmarks, and documentation tests. The test framework is part of the standard library. Documentation is generated from code comments using rustdoc, and doc tests ensure examples stay correct.

## Key Concepts

### 1. Unit Tests

Unit tests are defined with the `#[test]` attribute in the same file as the code. They test individual functions in isolation. Test functions can be in a separate `tests` module with `#[cfg(test)]` to exclude from release builds.

```rust
pub fn add(left: usize, right: usize) -> usize {
    left + right
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }

    #[test]
    fn test_add_negative() {
        let result = add(0, 0);
        assert_eq!(result, 0);
    }

    #[test]
    #[should_panic(expected = "overflow")]
    fn test_overflow() {
        // This test expects a panic
        add(usize::MAX, 1);
    }

    #[test]
    fn test_with_result() -> Result<(), String> {
        if add(2, 2) == 4 {
            Ok(())
        } else {
            Err(String::from("two plus two doesn't equal four"))
        }
    }
}
```

### 2. Integration Tests

Integration tests are in the `tests/` directory (separate from source code). Each file in `tests/` is compiled as a separate crate. Integration tests test the public API of your library.

```rust
// tests/integration_test.rs
use my_crate::add;

#[test]
fn test_add_integration() {
    assert_eq!(add(2, 2), 4);
}

// tests/common/mod.rs
pub fn setup() {
    // shared setup code
}

// tests/integration_test.rs
mod common;

#[test]
fn test_with_setup() {
    common::setup();
    // run test
}
```

### 3. Doc Tests

Documentation examples are automatically tested by `cargo test`. This ensures that code examples in documentation stay correct. Doc tests are run with `cargo test --doc`.

```rust
/// Adds two numbers.
///
/// # Examples
///
/// ```
/// use my_crate::add;
///
/// let result = add(2, 3);
/// assert_eq!(result, 5);
/// ```
///
/// # Panics
///
/// Panics if the result overflows.
///
/// ```should_panic
/// use my_crate::add;
/// add(usize::MAX, 1);
/// ```
pub fn add(left: usize, right: usize) -> usize {
    left + right
}

/// Hides documentation from the output
/// but still runs the code as a test.
///
/// ```ignore
/// // This code is not tested (e.g., requires network)
/// let result = networking::fetch();
/// ```

/// ```no_run
/// // This code is compiled but not run
/// loop {
///     println!("Infinite loop");
/// }
/// ```
```

### 4. Test Organization and Attributes

Various test attributes control test behavior: `#[ignore]` for slow tests, `#[should_panic]` for expected failures, and `#[cfg(test)]` for conditional compilation.

```rust
#[cfg(test)]
mod tests {
    #[test]
    #[ignore = "too slow for CI"]
    fn expensive_test() {
        // takes hours to run
    }

    #[test]
    fn test_with_filter() {
        // Run: cargo test test_with_filter
        // Or: cargo test test_with  (matches any test with "test_with" in name)
    }

    // Substring matching
    // cargo test add  — runs all tests with "add" in the name
    // cargo test -- --nocapture  — shows println output
    // cargo test test_add -- --test-threads=1  — single-threaded

    #[test]
    fn assert_macros() {
        assert!(true);
        assert_eq!(1, 1);
        assert_ne!(1, 2);
        assert!(true, "Custom message: {}", "hello");

        // Debug assertions (only in debug builds)
        debug_assert!(true);
        debug_assert_eq!(1, 1);
    }
}
```

### 5. Documentation with rustdoc

Rust documentation is written as Markdown in code comments. `///` for item docs, `//!` for module docs. `cargo doc` generates HTML documentation.

```rust
//! # My Crate
//!
//! `my_crate` is a collection of utilities for math operations.
//!
//! ## Getting Started
//!
//! Add this to your `Cargo.toml`:
//!
//! ```toml
//! [dependencies]
//! my_crate = "0.1.0"
//! ```

/// Calculates the factorial of a number.
///
/// # Arguments
///
/// * `n` - A non-negative integer
///
/// # Returns
///
/// The factorial of `n` (n!)
///
/// # Examples
///
/// ```
/// use my_crate::factorial;
/// assert_eq!(factorial(5), 120);
/// ```
///
/// # Panics
///
/// Panics if `n` is greater than 20 (overflow).
///
/// # Safety
///
/// This function is safe for n <= 20.
pub fn factorial(n: u64) -> u64 {
    (1..=n).product()
}

// Generate docs: cargo doc --open
// Generate and open: cargo doc --open --no-deps
```

## Practice Questions

1. What is the difference between a unit test and an integration test?
2. How do you mark a test to ignore? How do you run ignored tests?
3. What is a doc test? How does cargo test --doc work?
4. How do you organize tests in the tests/ directory?
5. What attributes control test behavior?

## LLM Prompts for Deeper Understanding

1. "Explain Rust testing: #[test], #[cfg(test)], assert_eq, #[should_panic], and Result tests"
2. "Show test organization: unit tests, integration tests, doc tests, and test helpers"
3. "Teach documentation: rustdoc, Markdown, doc tests, module docs, and cargo doc"

## Key Takeaways

- `#[test]` marks test functions; `cargo test` runs all tests
- Unit tests in source files; integration tests in `tests/` directory
- Doc tests (`///`) ensure documentation examples remain correct
- `#[ignore]` skips tests; `#[should_panic]` expects panics
- `cargo doc` generates HTML documentation from doc comments