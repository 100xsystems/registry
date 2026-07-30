---
{
  "slug": "rs-11-closures-iterators",
  "title": "Closures and Iterators",
  "description": "Closure types (Fn, FnMut, FnOnce), iterator adapters, iterator combinators, consuming producers, and lazy evaluation.",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create and use closures with different capture modes",
    "Use iterator adapters for functional transformations",
    "Chain iterator combinators efficiently",
    "Understand lazy evaluation and zero-cost abstractions"
  ],
  "knowledge_refs": ["rust/rs-11-closures-iterators"],
  "prerequisites": ["RS-09"],
  "references": [
    {"title": "The Rust Book — Closures", "url": "https://doc.rust-lang.org/book/ch13-01-closures.html"},
    {"title": "The Rust Book — Iterators", "url": "https://doc.rust-lang.org/book/ch13-02-iterators.html"},
    {"title": "Rust by Example — Closures", "url": "https://doc.rust-lang.org/stable/rust-by-example/fn/closures.html"},
    {"title": "Iterator Adapters Documentation", "url": "https://doc.rust-lang.org/std/iter/trait.Iterator.html"}
  ]
}
---

# RS-11: Closures and Iterators

## Introduction

Closures are anonymous functions that can capture their environment. Iterators are lazy sequences that produce values on demand. Together, they enable powerful, expressive, functional-style programming with zero runtime overhead through monomorphization.

## Key Concepts

### 1. Closure Basics

Closures are defined with `|params| body` syntax. They can capture variables from their surrounding scope. The compiler infers their parameter and return types.

```rust
fn main() {
    // Simple closure
    let add_one = |x| x + 1;
    println!("{}", add_one(5));  // 6

    // Closure with explicit types
    let add = |x: i32, y: i32| -> i32 { x + y };

    // Closure capturing environment
    let x = 5;
    let equal_to_x = |z| z == x;  // captures x by reference
    println!("{}", equal_to_x(5));  // true

    // Closures can be passed to functions
    let list = vec![1, 2, 3];
    let result: Vec<i32> = list.iter().map(|x| x * 2).collect();
    println!("{:?}", result);  // [2, 4, 6]
}
```

### 2. Closure Trait Bounds: Fn, FnMut, FnOnce

Closures implement one or more of these traits: FnOnce (can be called once), FnMut (can mutate captured state), Fn (can be called multiple times without mutation). The compiler determines which trait a closure implements based on how it captures variables.

```rust
fn main() {
    // FnOnce: consumes captured values
    let x = String::from("hello");
    let consume = || {
        drop(x);  // x is moved into the closure
    };
    consume();
    // consume();  // ERROR: FnOnce can only be called once

    // FnMut: mutates captured state
    let mut count = 0;
    let mut increment = || {
        count += 1;  // captures &mut count
    };
    increment();
    increment();
    println!("Count: {}", count);  // 2

    // Fn: only reads captured state
    let data = vec![1, 2, 3];
    let read = || {
        println!("{:?}", data);  // captures &data
    };
    read();
    read();  // OK: Fn can be called multiple times
}

// Function taking a closure
fn call_once<F: FnOnce()>(f: F) {
    f();
}

fn call_mut<F: FnMut()>(mut f: F) {
    f();
    f();
}

fn call<F: Fn()>(f: F) {
    f();
    f();
}
```

### 3. Iterator Trait and Iterator Adapters

The Iterator trait requires a `next` method. Many types implement Iterator (Vec, HashMap, String, etc.). Iterator adapters transform one iterator into another.

```rust
fn main() {
    let numbers = vec![1, 2, 3, 4, 5];

    // Basic iteration
    let mut iter = numbers.iter();
    assert_eq!(iter.next(), Some(&1));
    assert_eq!(iter.next(), Some(&2));
    assert_eq!(iter.next(), Some(&3));

    // Iterator adapters (lazy!)
    let doubled: Vec<i32> = numbers.iter()
        .map(|x| x * 2)       // lazy: nothing happens yet
        .collect();            // consume: actually processes

    // Filter: keep elements matching predicate
    let evens: Vec<&i32> = numbers.iter()
        .filter(|x| *x % 2 == 0)
        .collect();
    println!("{:?}", evens);  // [2, 4]

    // Chain: combine two iterators
    let a = vec![1, 2, 3];
    let b = vec![4, 5, 6];
    let chained: Vec<i32> = a.iter().chain(b.iter()).copied().collect();
    // [1, 2, 3, 4, 5, 6]

    // Zip: pair elements from two iterators
    let names = vec!["Alice", "Bob"];
    let scores = vec![42, 50];
    let pairs: Vec<(&str, i32)> = names.iter().copied().zip(scores.iter().copied()).collect();
    // [("Alice", 42), ("Bob", 50)]
}
```

### 4. Consuming and Producing Iterators

Some adapters consume the iterator (collect, sum, count, fold). Others produce new iterators (map, filter, take, skip). The IntoIterator trait converts types into iterators.

```rust
fn main() {
    let numbers = vec![1, 2, 3, 4, 5];

    // Consuming adapters
    let sum: i32 = numbers.iter().sum();       // 15
    let count = numbers.iter().count();        // 5
    let max = numbers.iter().max();            // Some(&5)
    let min = numbers.iter().min();            // Some(&1)

    // fold: reduce with accumulator
    let product = numbers.iter().fold(1, |acc, x| acc * x);
    println!("{}", product);  // 120

    // any/all: boolean checks
    let has_even = numbers.iter().any(|x| x % 2 == 0);  // true
    let all_positive = numbers.iter().all(|x| x > 0);   // true

    // take/skip: limit iteration
    let first3: Vec<&i32> = numbers.iter().take(3).collect();
    let after2: Vec<&i32> = numbers.iter().skip(2).collect();

    // IntoIterator for consuming iteration
    let text = "hello world".to_string();
    for word in text.split_whitespace() {
        println!("{}", word);
    }
}
```

### 5. Custom Iterators and Performance

Implementing Iterator for custom types. Iterators are zero-cost abstractions — they compile to the same code as hand-written loops.

```rust
struct Fibonacci {
    curr: u64,
    next: u64,
}

impl Fibonacci {
    fn new() -> Self {
        Fibonacci { curr: 0, next: 1 }
    }
}

impl Iterator for Fibonacci {
    type Item = u64;

    fn next(&mut self) -> Option<Self::Item> {
        let current = self.curr;
        self.curr = self.next;
        self.next = current + self.next;
        Some(current)  // infinite iterator
    }
}

fn main() {
    // Take first 10 Fibonacci numbers
    let fib: Vec<u64> = Fibonacci::new().take(10).collect();
    println!("{:?}", fib);  // [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    // Iterator performance: zero-cost abstraction
    // This chain: map -> filter -> sum
    let sum: i32 = (1..=1000)
        .map(|x| x * 2)
        .filter(|x| x % 3 == 0)
        .sum();

    // Is equivalent to the hand-written loop:
    let mut sum2 = 0;
    for x in 1..=1000 {
        let doubled = x * 2;
        if doubled % 3 == 0 {
            sum2 += doubled;
        }
    }
    // The compiler generates the same code for both!
}
```

## Practice Questions

1. What are the three closure traits? How does the compiler determine which one a closure implements?
2. What does it mean that iterator adapters are lazy?
3. What is the difference between `iter()`, `iter_mut()`, and `into_iter()`?
4. How does `fold` work? What is its relationship to `reduce`?
5. Why are iterators called a zero-cost abstraction in Rust?

## LLM Prompts for Deeper Understanding

1. "Explain closures: Fn, FnMut, FnOnce, capturing modes, and move semantics"
2. "Show iterator adapters: map, filter, fold, take, skip, chain, zip — lazy evaluation"
3. "Teach iterator performance: zero-cost abstractions, custom iterators, and IntoIterator trait"

## Key Takeaways

- Closures capture environment with Fn, FnMut, or FnOnce semantics
- Iterators are lazy sequences; adapters transform until consumed
- Common adapters: map, filter, fold, take, skip, chain, zip
- Iterators are zero-cost abstractions — compile to optimized loop code
- Implement Iterator for custom types to enable functional-style processing