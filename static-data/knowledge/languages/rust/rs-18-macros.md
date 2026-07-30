---
{
  "slug": "rs-18-macros",
  "title": "Macros",
  "description": "Declarative macros (macro_rules!), procedural macros, derive macros, attribute macros, and function-like macros.",
  "type": "lesson",
  "order": 18,
  "duration": "75 min",
  "difficulty": "expert",
  "learning_objectives": [
    "Write declarative macros with macro_rules!",
    "Understand procedural macros",
    "Create custom derive macros",
    "Use attribute and function-like macros"
  ],
  "knowledge_refs": ["rust/rs-18-macros"],
  "prerequisites": ["RS-09"],
  "references": [
    {"title": "The Rust Book — Macros", "url": "https://doc.rust-lang.org/book/ch19-06-macros.html"},
    {"title": "Rust by Example — Macros", "url": "https://doc.rust-lang.org/stable/rust-by-example/macro_rules.html"},
    {"title": "The Little Book of Rust Macros", "url": "https://veykril.github.io/tlborm/"},
    {"title": "proc_macro crate", "url": "https://doc.rust-lang.org/proc_macro/"}
  ]
}
---

# RS-18: Macros

## Introduction

Macros are a form of metaprogramming that generates code at compile time. Rust has two kinds of macros: declarative macros (macro_rules!) and procedural macros (derive, attribute, and function-like). Macros operate on the AST and can produce any valid Rust code.

## Key Concepts

### 1. Declarative Macros (macro_rules!)

Declarative macros match patterns and generate code. They are similar to match expressions but operate on the token stream. Macros are hygienic — they don't accidentally capture variables from the calling scope.

```rust
// Simple macro: create a vector with a given value repeated n times
macro_rules! vec_of {
    ($val:expr, $n:expr) => {{
        let mut v = Vec::new();
        for _ in 0..$n {
            v.push($val);
        }
        v
    }};
}

fn main() {
    let v = vec_of!(42, 3);
    println!("{:?}", v);  // [42, 42, 42]
}

// Macro with multiple patterns
macro_rules! calculate {
    (add $a:expr, $b:expr) => { $a + $b };
    (sub $a:expr, $b:expr) => { $a - $b };
    (mul $a:expr, $b:expr) => { $a * $b };
    (div $a:expr, $b:expr) => { $a / $b };
}

fn main() {
    println!("{}", calculate!(add 10, 5));   // 15
    println!("{}", calculate!(sub 10, 5));   // 5
    println!("{}", calculate!(mul 10, 5));   // 50
}
```

### 2. Repetition in Macros

Macros can handle variable numbers of arguments using repetition syntax: `$($pattern),*` (zero or more), `$(pattern),+` (one or more), and `$(pattern),?` (zero or one).

```rust
// Macro that calculates the minimum of multiple values
macro_rules! min_of {
    ($x:expr) => { $x };
    ($x:expr, $($y:expr),+) => {
        std::cmp::min($x, min_of!($($y),+))
    };
}

fn main() {
    println!("{}", min_of!(5));           // 5
    println!("{}", min_of!(5, 3, 8, 1));  // 1
}

// vec! macro implementation (simplified)
macro_rules! my_vec {
    ($($x:expr),*) => {
        {
            let mut temp_vec = Vec::new();
            $(
                temp_vec.push($x);
            )*
            temp_vec
        }
    };
    ($($x:expr),+ ,) => {  // trailing comma
        my_vec!($($x),+)
    };
}

// Designator types:
// expr: expression
// ident: identifier
// ty: type
// pat: pattern
// stmt: statement
// block: block expression
// item: item
// meta: meta item
// tt: single token tree
```

### 3. Procedural Macros

Procedural macros are functions that operate on the token stream at compile time. They are defined in a separate crate with `proc-macro = true`. There are three kinds: derive, attribute, and function-like.

```rust
// Custom derive macro (in a separate crate)
// my_derive/Cargo.toml
// [lib]
// proc-macro = true

// my_derive/src/lib.rs
// use proc_macro::TokenStream;
//
// #[proc_macro_derive(HelloMacro)]
// pub fn hello_macro_derive(input: TokenStream) -> TokenStream {
//     // Parse the input token stream
//     let ast = syn::parse(input).unwrap();
//
//     // Build the implementation
//     impl_hello_macro(&ast)
// }
//
// fn impl_hello_macro(ast: &syn::DeriveInput) -> TokenStream {
//     let name = &ast.ident;
//     let gen = quote::quote! {
//         impl HelloMacro for #name {
//             fn hello_macro() {
//                 println!("Hello, Macro! My name is {}!", stringify!(#name));
//             }
//         }
//     };
//     gen.into()
// }

// Usage
// #[derive(HelloMacro)]
// struct Pancakes;
//
// Pancakes::hello_macro();  // "Hello, Macro! My name is Pancakes!"
```

### 4. Attribute and Function-Like Macros

Attribute macros modify items (functions, structs). Function-like macros take a token stream and return a token stream.

```rust
// Attribute macro (in a separate crate)
// #[proc_macro_attribute]
// pub fn route(attr: TokenStream, item: TokenStream) -> TokenStream {
//     // attr: the route path (e.g., "/")
//     // item: the function definition
//     // return modified function
// }

// Usage
// #[route(GET, "/")]
// fn index() -> &'static str {
//     "Hello, World!"
// }

// Function-like macro
// #[proc_macro]
// pub fn sql(input: TokenStream) -> TokenStream {
//     // Parse the SQL-like syntax
//     // Generate type-safe Rust code
// }

// Usage
// let users = sql!(SELECT * FROM users WHERE id = 1);
// // Generates type-safe query code

// Practical: compile-time string formatting
macro_rules! compile_time_string {
    ($($arg:tt)*) => {{
        let s = format!($($arg)*);
        &s[..]  // returns &str
    }};
}
```

### 5. Hygiene and Debugging

Macros are hygienic: they create new identifiers that don't conflict with the calling scope. Debugging macros can be challenging — use `cargo expand` to see the expanded code.

```rust
// Hygiene: macro creates its own scope
macro_rules! create_var {
    () => {
        let x = 42;  // this x is in the macro's scope
        println!("Inside macro: {}", x);
    };
}

fn main() {
    let x = 10;
    create_var!();  // prints "Inside macro: 42"
    println!("Outside: {}", x);  // prints "Outside: 10" (no conflict!)

    // Debugging macros
    // $ cargo install cargo-expand
    // $ cargo expand    // shows the expanded macro code
}

// Debugging marcos with log_syntax!
macro_rules! debug_macro {
    ($($arg:tt)*) => {
        {
            // log_syntax!($($arg)*);  // prints tokens at compile time
            // trace_macros!(true);     // trace all macro expansions
            $($arg)*
        }
    };
}
```

## Practice Questions

1. What is the difference between declarative and procedural macros?
2. What are the different token designators in macro_rules!?
3. What is macro hygiene? Why is it important?
4. What are the three kinds of procedural macros?
5. How do you debug macro expansions?

## LLM Prompts for Deeper Understanding

1. "Explain macro_rules!: patterns, repetition, designators, and hygiene"
2. "Show procedural macros: derive, attribute, function-like, and the syn/quote crates"
3. "Teach macro debugging: cargo expand, trace_macros, log_syntax, and common pitfalls"

## Key Takeaways

- macro_rules! creates declarative macros with pattern matching
- Procedural macros operate on token streams at compile time
- Three kinds: derive, attribute, and function-like macros
- Macros are hygienic: no identifier conflicts with calling scope
- Use `cargo expand` to debug macro expansions