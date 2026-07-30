---
{
  "slug": "rs-01-getting-started",
  "title": "Getting Started with Rust",
  "description": "Install Rust, understand Cargo, create projects, write Hello World, and explore the toolchain.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install Rust and configure the toolchain",
    "Create and manage projects with Cargo",
    "Write and run Hello World",
    "Understand Rust's compilation model"
  ],
  "knowledge_refs": ["rust/rs-01-getting-started"],
  "prerequisites": [],
  "references": [
    {"title": "The Rust Book — Getting Started", "url": "https://doc.rust-lang.org/book/ch01-00-getting-started.html"},
    {"title": "Rust by Example — Hello World", "url": "https://doc.rust-lang.org/stable/rust-by-example/hello.html"},
    {"title": "Cargo Documentation", "url": "https://doc.rust-lang.org/cargo/"},
    {"title": "Rust Playground", "url": "https://play.rust-lang.org/"}
  ]
}
---

# RS-01: Getting Started with Rust

## Introduction

Rust is a systems programming language focused on safety, speed, and concurrency without a garbage collector. It guarantees memory safety through its ownership system, prevents data races at compile time, and compiles to native code that runs as fast as C++.

## Key Concepts

### 1. Installing Rust and the Toolchain

The recommended way to install Rust is via `rustup`, the official Rust toolchain installer. It manages multiple Rust versions and provides the compiler (`rustc`), package manager (`cargo`), and documentation (`rustdoc`).

```rust
// Install Rust (macOS/Linux/Windows via WSL)
$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

// Verify installation
$ rustc --version    // rustc 1.80.0 (051478957 2024-07-21)
$ cargo --version    // cargo 1.80.0 (376030c3f 2024-07-16)

// Update Rust
$ rustup update

// View documentation locally
$ rustup doc         // opens The Book in your browser
```

The Rust toolchain includes: `rustc` (compiler), `cargo` (package manager/build tool), `rustfmt` (code formatter), `clippy` (linter), and `rust-analyzer` (LSP for IDE support).

### 2. Hello World with Cargo

Cargo is Rust's build system and package manager. Create a new project, write your first program, and understand the compilation workflow.

```rust
// Create a new binary project
$ cargo new hello_rust
$ cd hello_rust

// Project structure:
// hello_rust/
//   Cargo.toml   (manifest with metadata and dependencies)
//   src/
//     main.rs    (entry point)

// src/main.rs
fn main() {
    println!("Hello, World!");
    println!("Welcome to Rust!");
}

// Build and run
$ cargo build        // debug build -> target/debug/hello_rust
$ cargo run          // build + run
$ cargo check        // fast compilation check (no binary)
$ cargo build --release  // optimized release build
```

Key points: `cargo check` is fastest for development, `cargo build` produces a binary, `cargo run` builds and runs in one step. The `--release` flag enables optimizations.

### 3. Cargo.toml and Dependencies

Cargo.toml is the manifest file that defines your project metadata, dependencies, and build configuration. Dependencies come from crates.io (the Rust package registry).

```toml
[package]
name = "hello_rust"
version = "0.1.0"
edition = "2021"

[dependencies]
serde = { version = "1.0", features = ["derive"] }
anyhow = "1.0"
```

```rust
// Adding dependencies
$ cargo add serde     // adds to Cargo.toml
$ cargo add anyhow    // adds error handling crate

// Using a dependency
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
struct Config {
    name: String,
    port: u16,
}
```

Cargo.lock locks dependency versions for reproducible builds. Always commit Cargo.lock for binary projects, but not for library projects.

### 4. Rust's Compilation Model

Rust compiles to native machine code via LLVM. The compiler performs: type checking, borrow checking, lifetime elision, monomorphization of generics, and optimization passes.

```rust
// Rust is AOT (Ahead-of-Time) compiled
// No runtime or garbage collector needed

// Compilation stages:
// 1. Lexing & Parsing -> AST
// 2. Name Resolution -> HIR (High-Level IR)
// 3. Type Checking & Borrow Checking -> THIR (Typed HIR)
// 4. Lowering -> MIR (Mid-Level IR)
// 5. Optimization -> LLVM IR
// 6. Code Generation -> Native code

// View MIR (for debugging)
// $ cargo rustc -- -Z mir-opt-level=0 --emit mir

// View LLVM IR
// $ cargo rustc -- --emit llvm-ir

// View assembly
// $ cargo rustc -- --emit asm
```

### 5. Idiomatic Rust: Formatting and Linting

Rust has strong conventions enforced by `rustfmt` (formatting) and `clippy` (linting). These tools ensure consistent code style across the entire ecosystem.

```rust
// Format code
$ cargo fmt          // auto-format according to Rust style
$ cargo fmt --check  // check formatting in CI

// Clippy lints
$ cargo clippy       // run linter
$ cargo clippy -- -D warnings  // deny warnings in CI

// Example: Clippy catches common mistakes
// Before
let x = 5;
let y = 5;
if x == y { /* ... */ }

// Clippy warning: 'comparison of identical values'
// Clippy catches this at compile time!
```

## Practice Questions

1. What is the difference between `cargo check`, `cargo build`, and `cargo run`?
2. What is the purpose of Cargo.toml vs Cargo.lock?
3. How do you add a dependency to a Rust project?
4. What is the Rust edition system? Why is edition = "2021" important?
5. What tools are included in the Rust toolchain besides rustc?

## LLM Prompts for Deeper Understanding

1. "Explain Rust's compilation model: AST -> HIR -> THIR -> MIR -> LLVM IR -> native code"
2. "Show Cargo workspace management and dependency resolution"
3. "Teach rustfmt and clippy conventions for idiomatic Rust code"

## Key Takeaways

- Rust is an AOT-compiled language with no GC, using LLVM for code generation
- Cargo manages projects, dependencies, builds, and tests
- Use `cargo new`, `cargo build`, `cargo run`, `cargo check` for development
- `rustfmt` and `clippy` enforce consistent, idiomatic Rust code