---
{
  "slug": "rs-12-modules-cargo",
  "title": "Modules, Crates, and Cargo",
  "description": "Modules and paths, module file system, external crates, Cargo.toml, features, and workspaces.",
  "type": "lesson",
  "order": 12,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Organize code with modules and paths",
    "Use the module file system convention",
    "Manage external dependencies with Cargo",
    "Use features and workspaces"
  ],
  "knowledge_refs": ["rust/rs-12-modules-cargo"],
  "prerequisites": ["RS-01"],
  "references": [
    {"title": "The Rust Book — Modules", "url": "https://doc.rust-lang.org/book/ch07-00-packages-crates.html"},
    {"title": "The Rust Book — Cargo", "url": "https://doc.rust-lang.org/book/ch14-00-more-about-cargo.html"},
    {"title": "Cargo Reference", "url": "https://doc.rust-lang.org/cargo/"},
    {"title": "Rust by Example — Modules", "url": "https://doc.rust-lang.org/stable/rust-by-example/mod.html"}
  ]
}
---

# RS-12: Modules, Crates, and Cargo

## Introduction

Modules organize code into logical groups. Crates are packages of Rust code. Cargo manages dependencies, builds, and publishing. The module system provides privacy control and code organization without runtime overhead.

## Key Concepts

### 1. Modules and Paths

Modules define boundaries and control visibility. Items are private by default. Use `pub` to make items public. Use `use` to bring items into scope.

```rust
// lib.rs (crate root)
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
        fn seat_at_table() {}  // private: only accessible within hosting
    }

    mod serving {
        fn take_order() {}
        fn serve_order() {}
        fn take_payment() {}
    }
}

pub fn eat_at_restaurant() {
    // Absolute path
    crate::front_of_house::hosting::add_to_waitlist();

    // Relative path
    front_of_house::hosting::add_to_waitlist();
}

// Use keyword for shorter paths
use crate::front_of_house::hosting;

pub fn eat_at_restaurant_v2() {
    hosting::add_to_waitlist();
}

// Re-exporting
pub use crate::front_of_house::hosting;
// Now external code can use my_crate::hosting::add_to_waitlist()

// External packages
use std::collections::HashMap;
```

### 2. Module File System

Rust supports two conventions for module files: `mod.rs` (older) and the module name file (newer, Rust 2018+). Modules can be defined inline or in separate files.

```rust
// lib.rs (crate root)
mod front_of_house;  // loads front_of_house.rs or front_of_house/mod.rs

// front_of_house.rs
pub mod hosting;  // loads front_of_house/hosting.rs

// front_of_house/hosting.rs
pub fn add_to_waitlist() {}

// Alternative: main.rs as crate root for binary crates
// src/main.rs and src/lib.rs can coexist in the same package
```

### 3. External Dependencies

Cargo.toml manages dependencies from crates.io. Use `cargo add` to add dependencies. Semantic versioning is used for version management.

```toml
[package]
name = "my_app"
version = "0.1.0"
edition = "2021"

[dependencies]
serde = { version = "1.0", features = ["derive"] }
anyhow = "1.0"
tokio = { version = "1", features = ["full"] }
reqwest = { version = "0.12", features = ["json"] }

[dev-dependencies]
criterion = "0.5"

[build-dependencies]
built = "0.7"
```

```rust
// Using dependencies
use serde::{Serialize, Deserialize};
use anyhow::Result;

#[derive(Serialize, Deserialize)]
struct Config {
    name: String,
    port: u16,
}

async fn fetch_data() -> Result<String> {
    let resp = reqwest::get("https://api.example.com/data").await?;
    Ok(resp.text().await?)
}
```

### 4. Features and Conditional Compilation

Features enable conditional compilation of optional functionality. They are defined in Cargo.toml and checked with `#[cfg(feature = "...")]`.

```toml
[features]
default = ["std"]
std = []
serde_support = ["dep:serde"]

[dependencies]
serde = { version = "1.0", optional = true }
```

```rust
#[cfg(feature = "serde_support")]
use serde::{Serialize, Deserialize};

#[cfg_attr(feature = "serde_support", derive(Serialize, Deserialize))]
struct Config {
    name: String,
}

#[cfg(not(feature = "std"))]
fn process() {
    // no_std version
}

#[cfg(target_os = "linux")]
fn platform_specific() {
    // Linux-specific code
}
```

### 5. Workspaces and Publishing

Workspaces manage multiple related crates in a single repository. Publishing to crates.io shares your crate with the community.

```toml
# Cargo.toml (workspace root)
[workspace]
members = [
    "crate-a",
    "crate-b",
    "crate-c",
]
```

```rust
// Publishing to crates.io
// $ cargo publish          // publish current crate
// $ cargo publish --dry-run  // check before publishing
// $ cargo yank --vers 1.0.0  // remove a version from crates.io

// Pre-publish checklist:
// 1. Update version in Cargo.toml
// 2. Run cargo test
// 3. Run cargo doc --no-deps
// 4. Create README.md and LICENSE
// 5. Update CHANGELOG.md
// 6. Git tag and push
// 7. cargo publish
```

## Practice Questions

1. What is the difference between a package and a crate?
2. What are the two file system conventions for modules?
3. How do you add a dependency with features?
4. What is the purpose of `pub use`?
5. How do workspaces work in Cargo?

## LLM Prompts for Deeper Understanding

1. "Explain Rust modules: paths, privacy, file system conventions, and re-exports"
2. "Show Cargo dependency management: features, dev-dependencies, build-dependencies, workspaces"
3. "Teach crate publishing: documentation, versioning, CHANGELOG, and CI best practices"

## Key Takeaways

- Modules organize code with privacy control; `pub` makes items public
- Module files use `mod.rs` or the module name as filename
- Cargo.toml manages dependencies, features, and workspace configuration
- Features enable optional compilation with `#[cfg(feature = "...")]`
- Workspaces manage multiple crates in a single repository