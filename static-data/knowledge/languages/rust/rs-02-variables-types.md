---
{
  "slug": "rs-02-variables-types",
  "title": "Variables, Mutability, and Data Types",
  "description": "Variables, mutability, constants, shadowing, scalar types, compound types, and type inference.",
  "type": "lesson",
  "order": 2,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare variables with let and understand mutability",
    "Use constants and shadowing effectively",
    "Work with scalar and compound data types",
    "Understand Rust's type inference system"
  ],
  "knowledge_refs": ["rust/rs-02-variables-types"],
  "prerequisites": ["RS-01"],
  "references": [
    {"title": "The Rust Book — Variables and Mutability", "url": "https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html"},
    {"title": "The Rust Book — Data Types", "url": "https://doc.rust-lang.org/book/ch03-02-data-types.html"},
    {"title": "Rust by Example — Variables", "url": "https://doc.rust-lang.org/stable/rust-by-example/variable_bindings.html"},
    {"title": "Rust by Example — Primitives", "url": "https://doc.rust-lang.org/stable/rust-by-example/primitives.html"}
  ]
}
---

# RS-02: Variables, Mutability, and Data Types

## Introduction

Variables in Rust are immutable by default — one of the core safety guarantees. This section covers variable declarations, mutability, constants, shadowing, and all the built-in data types that form the foundation of Rust programs.

## Key Concepts

### 1. Variables and Mutability

Variables are immutable by default in Rust. Add `mut` to make them mutable. This prevents accidental modifications and makes code easier to reason about.

```rust
fn main() {
    // Immutable by default
    let x = 5;
    // x = 6;  // ERROR: cannot assign to immutable variable

    // Mutable with 'mut' keyword
    let mut y = 5;
    y = 6;  // OK

    // Constants must be explicitly typed
    const MAX_POINTS: u32 = 100_000;
    const PI: f64 = 3.14159;

    // Constants can be declared in any scope
    const SECONDS_IN_HOUR: u32 = 60 * 60;  // compile-time evaluation
}
```

Key differences: `let` creates variables, `const` creates compile-time constants. Constants must always have an explicit type annotation. Constants can be declared in any scope and are inlined at compile time.

### 2. Shadowing

Shadowing allows reusing a variable name by declaring a new `let` with the same name. The new variable can have a different type. This is different from mutation.

```rust
fn main() {
    let x = 5;          // first binding: i32
    let x = x + 1;      // second binding shadows first: i32 = 6
    let x = x * 2;      // third binding: i32 = 12

    // Shadowing with type change
    let spaces = "   ";           // &str
    let spaces = spaces.len();    // usize (different type!)

    // Without shadowing, you'd need different names
    let spaces_str = "   ";
    let spaces_usize = spaces_str.len();

    // Shadowing is scoped
    let y = 1;
    {
        let y = 2;      // shadows outer y only in this block
        println!("{}", y);  // 2
    }
    println!("{}", y);  // 1 (outer y restored)
}
```

### 3. Scalar Types

Rust has four primary scalar types: integers, floating-point numbers, booleans, and characters. Integers come in signed (i8, i16, i32, i64, i128, isize) and unsigned (u8, u16, u32, u64, u128, usize) variants.

```rust
fn main() {
    // Integer types
    let a: i8 = -128;          // 8-bit signed
    let b: u8 = 255;           // 8-bit unsigned
    let c: i32 = -100;         // 32-bit signed (default)
    let d: u64 = 100_000;      // 64-bit unsigned (underscores for readability)
    let e: usize = 0;          // pointer-sized (arch-dependent)

    // Integer literals
    let decimal = 98_222;
    let hex = 0xff;
    let octal = 0o77;
    let binary = 0b1111_0000;
    let byte = b'A';           // u8 only

    // Floating-point
    let f: f64 = 3.14;         // 64-bit (default)
    let g: f32 = 2.0;          // 32-bit

    // Boolean
    let t: bool = true;
    let f: bool = false;

    // Character (4-byte Unicode)
    let c: char = 'z';
    let heart = '❤';
    let emoji = '🦀';
}
```

Type inference: Rust infers types from usage. If a type can't be inferred, you must annotate it. The default integer type is `i32` and default float type is `f64`.

### 4. Compound Types

Compound types group multiple values. Tuples have fixed length and can hold different types. Arrays have fixed length and hold the same type.

```rust
fn main() {
    // Tuple: fixed-length, heterogeneous
    let tup: (i32, f64, u8) = (500, 6.4, 1);
    let (x, y, z) = tup;           // destructuring
    let five_hundred = tup.0;      // index access
    let point = tup.1;             // 6.4

    // Unit type: empty tuple ()
    let unit: () = ();             // function returns () implicitly

    // Array: fixed-length, homogeneous
    let arr: [i32; 3] = [1, 2, 3];
    let first = arr[0];            // index access
    let second = arr[1];

    // Array initialization
    let zeros = [0; 5];            // [0, 0, 0, 0, 0]
    let same = [3; 100];           // 100 elements all = 3

    // Runtime bounds check (panics if out of bounds)
    // let invalid = arr[10];       // panics at runtime
}
```

### 5. Type Inference and Annotations

Rust's type inference is powerful but not magic. The compiler can infer types from context, but sometimes annotations are needed.

```rust
fn main() {
    // Inferred: i32
    let x = 5;

    // Inferred: f64
    let y = 3.14;

    // Must annotate: no context
    let z: u8 = 7;

    // Method calls provide inference
    let vec = Vec::new();           // ERROR: can't infer element type
    let vec: Vec<i32> = Vec::new(); // OK: annotated
    let mut vec = Vec::new();
    vec.push(1);                    // OK: now inferred as Vec<i32>

    // Parse with turbofish
    let parsed: u32 = "42".parse().expect("Not a number!");
    let parsed = "42".parse::<u32>().expect("Not a number!");
}
```

## Practice Questions

1. What is the difference between `let mut x = 5` and `let x = 5`?
2. How does shadowing differ from mutation? Can you change the type of a variable with shadowing?
3. What is the default integer type in Rust? The default float type?
4. What is the unit type? When is it used?
5. What happens if you access an array out of bounds?

## LLM Prompts for Deeper Understanding

1. "Explain Rust's type inference: how the compiler determines types, when annotations are needed, and the turbofish syntax"
2. "Show integer overflow behavior in debug vs release mode"
3. "Teach memory layout: how tuples and arrays are stored in memory"

## Key Takeaways

- Variables are immutable by default; use `mut` for mutability
- Shadowing allows reuse of variable names with possible type changes
- Scalar types: integers (i/u + size), floats (f32/f64), bool, char
- Compound types: tuples (heterogeneous, fixed-length), arrays (homogeneous, fixed-length)
- Type inference is powerful but explicit annotations help with clarity