---
{
  "slug": "rs-04-slices",
  "title": "Slices and References",
  "description": "String slices, array slices, string vs &str, slice patterns, and dangling reference prevention.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Create and use string slices (&str)",
    "Work with array slices",
    "Understand String vs &str differences",
    "Use slice patterns for safe indexing"
  ],
  "knowledge_refs": ["rust/rs-04-slices"],
  "prerequisites": ["RS-03"],
  "references": [
    {"title": "The Rust Book — Slices", "url": "https://doc.rust-lang.org/book/ch04-03-slices.html"},
    {"title": "Rust by Example — Slices", "url": "https://doc.rust-lang.org/stable/rust-by-example/primitives.html#array-and-slice"},
    {"title": "Rust std::slice", "url": "https://doc.rust-lang.org/std/primitive.slice.html"},
    {"title": "Rust std::str", "url": "https://doc.rust-lang.org/std/primitive.str.html"}
  ]
}
---

# RS-04: Slices and References

## Introduction

Slices are references to a contiguous sequence of elements in a collection. They are a view into a portion of a String, array, or Vec. Slices are a fundamental Rust concept that enables safe, efficient data access without copying.

## Key Concepts

### 1. String Slices (&str)

A string slice `&str` is a reference to a portion of a String. It consists of a pointer to the start of the slice and a length. String slices are UTF-8 encoded and are the most common string type in Rust.

```rust
fn main() {
    let s = String::from("hello world");

    let hello = &s[0..5];    // "hello"
    let world = &s[6..11];   // "world"

    // Shorthand syntax
    let slice = &s[..5];       // from start: &s[0..5]
    let tail = &s[6..];        // to end: &s[6..len]
    let whole = &s[..];        // entire string: &s[0..len]

    // String literals are &str
    let literal: &str = "hello world";
    // This is a string slice pointing to the binary's read-only memory

    // &str as function parameter (preferred over &String)
    fn first_word(s: &str) -> &str {
        let bytes = s.as_bytes();
        for (i, &byte) in bytes.iter().enumerate() {
            if byte == b' ' {
                return &s[..i];
            }
        }
        &s[..]
    }

    let word = first_word(&s);     // pass &String (auto-deref)
    let word = first_word(literal); // pass &str directly
}
```

### 2. Array Slices

Array slices work similarly to string slices. They are references to a portion of an array or Vec. The type is `&[T]`.

```rust
fn main() {
    let arr = [1, 2, 3, 4, 5];

    let slice = &arr[1..3];     // [2, 3]
    let first = &arr[..2];      // [1, 2]
    let last = &arr[3..];       // [4, 5]

    // Slices implement iteration
    for item in slice {
        println!("{}", item);
    }

    // Slice as function parameter
    fn sum(slice: &[i32]) -> i32 {
        slice.iter().sum()
    }

    println!("{}", sum(&arr[..]));      // 15
    println!("{}", sum(&arr[1..4]));    // 9

    // Vec can be sliced
    let vec = vec![10, 20, 30, 40];
    let v_slice = &vec[..2];           // [10, 20]

    // Mutable slice
    let mut data = [1, 2, 3, 4, 5];
    let mut_slice = &mut data[1..4];   // mutable reference to elements 1..4
    mut_slice[0] = 10;                 // modifies data[1]
    println!("{:?}", data);            // [1, 10, 3, 4, 5]
}
```

### 3. String vs &str

String is an owned, heap-allocated, growable UTF-8 string. `&str` is a borrowed reference to a string slice. Understanding the difference is crucial for Rust performance.

```rust
fn main() {
    // String: owned, heap-allocated, mutable
    let mut s = String::from("hello");
    s.push_str(" world");           // can grow
    s.push('!');

    // &str: borrowed, fixed-size, immutable
    let slice: &str = &s[..5];      // "hello"
    // slice is a view, cannot be modified

    // Converting between them
    let str_from_string: &str = &s;  // &String -> &str (auto-deref)
    let string_from_str: String = slice.to_string();  // &str -> String
    let string_from_str: String = slice.to_owned();   // also works

    // Practical: using &str in structs (requires lifetime)
    struct Config<'a> {
        name: &'a str,              // borrowed, no allocation
    }

    // Using String in structs (owned)
    struct OwnedConfig {
        name: String,               // owned, can live independently
    }
}
```

### 4. Slice Patterns and Safety

Slices include bounds checking at runtime. Accessing out-of-bounds indexes causes a panic, preventing memory unsafety.

```rust
fn main() {
    let data = [1, 2, 3, 4, 5];

    // Safe indexing: runtime bounds check
    match data.get(10) {
        Some(val) => println!("{}", val),
        None => println!("Index out of bounds"),
    }

    // Panic on out of bounds
    // let bad = &data[10];  // panics: index out of bounds

    // Pattern matching with slices
    match data {
        [first, second, rest @ ..] => {
            println!("First: {}, Second: {}, Rest: {:?}", first, second, rest);
        }
    }

    // Fixed-size patterns
    if let [a, b, c] = data[..3] {
        println!("a={}, b={}, c={}", a, b, c);
    }

    // Empty slice check
    if !data.is_empty() {
        println!("First element: {}", data[0]);
    }
}
```

### 5. Slicing Strings Safely (UTF-8)

String slicing must respect UTF-8 character boundaries. Slicing in the middle of a multi-byte character causes a panic.

```rust
fn main() {
    let s = String::from("hello 🦀 world");

    // Safe: ASCII characters
    let hello = &s[..5];       // "hello"

    // Safe: slicing at character boundaries
    let crab = &s[6..10];      // "🦀" (4 bytes)

    // Panic: slicing in middle of multi-byte character
    // let bad = &s[6..8];     // panics: byte 8 is not a char boundary

    // Safe alternatives
    if let Some(crab) = s.get(6..10) {
        println!("Safe slice: {}", crab);  // "🦀"
    }

    // Using char_indices for safe iteration
    for (i, c) in s.char_indices() {
        println!("Byte {}: char '{}'", i, c);
    }

    // Split into graphemes (requires unicode-segmentation crate)
    // use unicode_segmentation::UnicodeSegmentation;
    // for g in s.graphemes(true) { println!("{}", g); }
}
```

## Practice Questions

1. What is a string slice? How does it differ from String?
2. What is the type of a string literal in Rust?
3. How do you create a slice of an array?
4. Why does Rust panic when slicing strings at non-UTF-8 boundaries?
5. What does `data.get(10)` return vs `&data[10]`?

## LLM Prompts for Deeper Understanding

1. "Explain slices: memory layout, pointer + length, bounds checking, and UTF-8 safety"
2. "Show String vs &str: ownership, allocation, when to use each in function parameters"
3. "Teach slice patterns: destructuring, range syntax, get vs indexing, and matched on slices"

## Key Takeaways

- Slices are references to contiguous sequences: `&str`, `&[T]`, `&mut [T]`
- String literals are `&str` pointing to read-only memory
- `String` is owned, heap-allocated, growable; `&str` is borrowed, fixed-size
- Slicing strings must respect UTF-8 character boundaries
- Use `.get()` for safe indexing that returns Option instead of panicking