---
{
  "slug": "rs-03-ownership",
  "title": "Ownership and Borrowing",
  "description": "Ownership rules, move semantics, borrowing with references, mutable references, and the borrow checker.",
  "type": "lesson",
  "order": 3,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Understand ownership rules and memory management",
    "Use move semantics and the Copy trait",
    "Borrow values with references",
    "Work with mutable references and their restrictions"
  ],
  "knowledge_refs": ["rust/rs-03-ownership"],
  "prerequisites": ["RS-02"],
  "references": [
    {"title": "The Rust Book — Ownership", "url": "https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html"},
    {"title": "The Rust Book — References and Borrowing", "url": "https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html"},
    {"title": "Rust by Example — Ownership", "url": "https://doc.rust-lang.org/stable/rust-by-example/scope/move.html"},
    {"title": "Rust by Example — Borrowing", "url": "https://doc.rust-lang.org/stable/rust-by-example/scope/borrow.html"}
  ]
}
---

# RS-03: Ownership and Borrowing

## Introduction

Ownership is Rust's most unique feature — it enables memory safety without a garbage collector. Every value has a single owner. When the owner goes out of scope, the value is dropped. This simple rule, combined with borrowing and lifetimes, prevents memory bugs at compile time.

## Key Concepts

### 1. Ownership Rules

The three ownership rules: 1) Each value has one owner. 2) Only one owner at a time. 3) When the owner goes out of scope, the value is dropped (freed).

```rust
fn main() {
    // String is owned by s
    let s = String::from("hello");
    // s owns the heap-allocated string

    // When s goes out of scope, drop() is called
    // Memory is freed automatically
    // No garbage collector needed!
}  // s goes out of scope -> drop() frees memory

fn ownership_example() {
    let s = String::from("hello");  // s owns the string

    takes_ownership(s);             // ownership moves to the function
    // s is no longer valid here!
    // println!("{}", s);  // ERROR: borrow of moved value

    let x = 5;                      // i32 implements Copy
    makes_copy(x);                  // x is copied, not moved
    println!("{}", x);              // OK: x still valid
}

fn takes_ownership(s: String) {
    println!("{}", s);
}  // s is dropped here, memory freed

fn makes_copy(n: i32) {
    println!("{}", n);
}
```

### 2. Move Semantics

When a value is assigned to another variable or passed to a function, ownership is moved. The original variable is no longer valid. This prevents double-free errors.

```rust
fn main() {
    // Move on assignment
    let s1 = String::from("hello");
    let s2 = s1;  // ownership moved from s1 to s2
    // s1 is now invalid
    // println!("{}", s1);  // ERROR: borrow of moved value

    // Clone for deep copy
    let s3 = String::from("hello");
    let s4 = s3.clone();  // deep copy: both s3 and s4 are valid
    println!("s3 = {}, s4 = {}", s3, s4);  // OK

    // Copy trait for stack-only types
    let x = 5;
    let y = x;  // Copy: x is still valid
    println!("x = {}, y = {}", x, y);  // OK

    // Types that implement Copy: integers, floats, bool, char, tuples of Copy types
    let tuple = (1, 2.0, true);  // all Copy
    let tuple2 = tuple;          // Copy, not move
    println!("{:?}", tuple);     // OK
}
```

Behind the scenes: When a move happens, Rust invalidates the original binding. The compiler tracks this — any use of a moved value is a compile error.

### 3. Borrowing with References

References allow you to use a value without taking ownership. Use `&` to create a reference. The original owner keeps ownership. The reference must not outlive the borrowed value.

```rust
fn main() {
    let s = String::from("hello");

    // Borrowing: & creates a reference
    let len = calculate_length(&s);
    println!("The length of '{}' is {}.", s, len);  // s still valid

    // Multiple immutable borrows are allowed
    let r1 = &s;
    let r2 = &s;
    println!("{} and {}", r1, r2);  // OK: multiple immutable references

    // Dangling references are prevented at compile time
    // fn dangle() -> &String {
    //     let s = String::from("hello");
    //     &s  // ERROR: returns reference to local variable
    // }  // s is dropped, reference would be dangling
}

fn calculate_length(s: &String) -> usize {
    s.len()
}  // s is not dropped: reference goes out of scope, but String keeps ownership
```

### 4. Mutable References

Mutable references allow modifying borrowed data. Only one mutable reference to a value is allowed at a time. This prevents data races at compile time.

```rust
fn main() {
    let mut s = String::from("hello");

    // Mutable reference
    change(&mut s);
    println!("{}", s);  // "hello, world"

    // Only one mutable reference at a time
    let r1 = &mut s;
    // let r2 = &mut s;  // ERROR: cannot borrow s as mutable more than once
    println!("{}", r1);

    // Combine immutable and mutable: NOT allowed
    let r1 = &s;       // immutable borrow
    // let r2 = &mut s;  // ERROR: cannot borrow s as mutable because it's also borrowed as immutable
    println!("{}", r1);  // immutable borrow used here

    // But separately scoped: OK
    let r1 = &s;       // immutable borrow
    println!("{}", r1);  // immutable borrow ends here
    let r2 = &mut s;   // OK: no active immutable borrows
    println!("{}", r2);
}

fn change(s: &mut String) {
    s.push_str(", world");  // modifies the borrowed String
}
```

### 5. The Borrow Checker

The borrow checker is the part of the compiler that enforces ownership rules. It tracks: 1) Scope of each variable, 2) When references are created, 3) When references are used, 4) When ownership is moved.

```rust
fn main() {
    // The borrow checker tracks lifetimes
    let r;                   // ---------+-- 'a
    {                        //          |
        let x = 5;           // -+-- 'b  |
        r = &x;              //  |       |
    }                        // -+       |
    // println!("{}", r);    // ERROR: 'x' does not live long enough
                             // ---------+

    // Correct: borrow from longer-lived scope
    let x = 5;               // ---------+-- 'b
    let r = &x;              // --+-- 'a |
    println!("{}", r);       //   |       |
                             // ---------+

    // NLL (Non-Lexical Lifetimes): borrows end when last used
    let mut s = String::from("hello");
    let r = &mut s;          // mutable borrow starts
    r.push_str(" world");     // last use of r
    // r's borrow ends here (NLL)
    let s2 = s;               // OK: s is no longer borrowed
}
```

## Practice Questions

1. What are the three ownership rules in Rust?
2. What is the difference between a move and a copy? Which types implement Copy?
3. What is a reference? How does borrowing differ from ownership?
4. Why can you only have one mutable reference at a time?
5. What does the borrow checker do? What is NLL?

## LLM Prompts for Deeper Understanding

1. "Explain Rust's ownership system: move semantics, Copy trait, and the borrow checker"
2. "Show mutable vs immutable references: restrictions, NLL, and common errors"
3. "Teach how Rust prevents dangling pointers, double-free, and data races at compile time"

## Key Takeaways

- Each value has exactly one owner; when owner goes out of scope, value is dropped
- Move transfers ownership; Clone creates a deep copy; Copy is for stack-only types
- References (`&`) borrow without ownership; only one mutable reference at a time
- The borrow checker enforces all rules at compile time with zero runtime cost