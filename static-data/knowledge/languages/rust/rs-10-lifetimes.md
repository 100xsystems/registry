---
{
  "slug": "rs-10-lifetimes",
  "title": "Lifetimes",
  "description": "Lifetime annotations, lifetime elision rules, struct lifetimes, static lifetime, and lifetime subtyping.",
  "type": "lesson",
  "order": 10,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand lifetime annotations and their syntax",
    "Apply lifetime elision rules",
    "Use lifetimes in struct definitions",
    "Work with the 'static lifetime"
  ],
  "knowledge_refs": ["rust/rs-10-lifetimes"],
  "prerequisites": ["RS-09"],
  "references": [
    {"title": "The Rust Book — Lifetimes", "url": "https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html"},
    {"title": "Rust by Example — Lifetimes", "url": "https://doc.rust-lang.org/stable/rust-by-example/scope/lifetime.html"},
    {"title": "The Rust Reference — Lifetimes", "url": "https://doc.rust-lang.org/reference/lifetime-elision.html"},
    {"title": "Rustonomicon — Lifetimes", "url": "https://doc.rust-lang.org/nomicon/lifetimes.html"}
  ]
}
---

# RS-10: Lifetimes

## Introduction

Lifetimes are Rust's mechanism for ensuring that references are always valid. They are a compile-time concept — they have no runtime cost. The borrow checker uses lifetimes to prevent dangling references, use-after-free, and other memory safety bugs.

## Key Concepts

### 1. Lifetime Annotations

Lifetime annotations use an apostrophe prefix: `'a`, `'b`, etc. They describe the relationship between the lifetimes of references. The compiler infers lifetimes in many cases using elision rules.

```rust
// Explicit lifetime: the returned reference lives as long as both inputs
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}

fn main() {
    let string1 = String::from("long string is long");
    {
        let string2 = String::from("xyz");
        let result = longest(string1.as_str(), string2.as_str());
        println!("The longest string is {}", result);
    }

    // This wouldn't compile: string2 doesn't live long enough
    // let result;
    // {
    //     let string2 = String::from("xyz");
    //     result = longest(string1.as_str(), string2.as_str());
    // }
    // println!("{}", result);  // ERROR: string2 dropped here
}
```

### 2. Lifetime Elision Rules

Rust has three elision rules that allow omitting lifetime annotations in common cases. The compiler follows these rules to infer lifetimes automatically.

```rust
// Rule 1: Each input reference gets its own lifetime
// Rule 2: If there's one input lifetime, all output references get that lifetime
// Rule 3: If there are multiple input lifetimes, but one is &self or &mut self,
//          the output lifetime is the same as &self

// The compiler transforms these automatically:

// fn first_word(s: &str) -> &str
// Elided: inputs get 'a, output gets 'a (Rule 1 + Rule 2)
// Expanded: fn first_word<'a>(s: &'a str) -> &'a str

// fn f(x: &str, y: &str) -> &str
// ERROR: multiple inputs, ambiguous output lifetimes
// fn f<'a, 'b>(x: &'a str, y: &'b str) -> &str  // which lifetime?

// fn get(&self, x: &str) -> &str
// Elided: &self gets 'a, x gets 'b, output gets 'a (Rule 3)
// Expanded: fn get<'a, 'b>(&'a self, x: &'b str) -> &'a str

// Static methods: no self parameter
// fn parse(s: &str) -> &str
// ERROR: one input reference, but needs explicit lifetime in some cases
```

### 3. Lifetimes in Structs

When a struct holds references, it must have lifetime annotations. The struct cannot outlive the references it holds.

```rust
struct Excerpt<'a> {
    part: &'a str,  // the struct cannot outlive this reference
}

impl<'a> Excerpt<'a> {
    fn announce_and_return_part(&self, announcement: &str) -> &str {
        println!("Attention: {}", announcement);
        self.part  // Rule 3: output is &'a str (same as &self)
    }
}

fn main() {
    let novel = String::from("Call me Ishmael. Some years ago...");
    let first_sentence = novel.split('.').next().expect("Could not find a '.'");
    let excerpt = Excerpt {
        part: first_sentence,
    };

    // excerpt outlives? It borrows from novel
    // If novel is dropped first, excerpt cannot be used
    drop(novel);
    // println!("{}", excerpt.part);  // ERROR: novel dropped, borrow invalid
}

// Multiple lifetime parameters
struct MultiRef<'a, 'b> {
    x: &'a str,
    y: &'b str,
}

impl<'a, 'b> MultiRef<'a, 'b> {
    fn longest(&self) -> &str where 'a: 'b  // 'a lives at least as long as 'b
    {
        if self.x.len() > self.y.len() { self.x } else { self.y }
    }
}
```

### 4. The 'static Lifetime

`'static` is a special lifetime that lasts for the entire program. String literals and const values have `'static` lifetime. `'static` bounds are common in generic code.

```rust
// String literals have 'static lifetime
let s: &'static str = "hello world";
// This string is stored directly in the binary's read-only section

// 'static as a trait bound
fn print_it<T: Debug + 'static>(item: &T) {
    println!("{:?}", item);
}

// 'static bounds: T must not contain any non-'static references
fn process<T: 'static>(item: T) {
    // T can be owned or contain only 'static references
    drop(item);  // T can be dropped safely
}

// Common patterns with 'static
fn spawn_thread() {
    // Data must be 'static to be sent to another thread
    let data = vec![1, 2, 3];
    std::thread::spawn(move || {
        println!("{:?}", data);  // data is moved, must be 'static
    });
}

// Box<dyn Trait> requires 'static for owned types
fn create_trait_object() -> Box<dyn Fn() + 'static> {
    let x = 42;
    Box::new(move || println!("{}", x))  // closure captures x
}
```

### 5. Advanced Lifetime Topics

Lifetime subtyping, variance, and higher-ranked trait bounds (HRTB) are advanced concepts for complex lifetime scenarios.

```rust
// Lifetime subtyping: 'a: 'b means 'a lives at least as long as 'b
struct Context<'a> {
    data: &'a str,
}

struct Parser<'a, 'b: 'a> {
    context: &'a Context<'b>,
}

// Higher-ranked trait bounds (HRTB): for<'a>
// "for all lifetimes 'a"
fn call_with_ref<F>(f: F)
where
    F: for<'a> Fn(&'a str) -> &'a str,
{
    let s = "hello";
    let result = f(s);
    println!("{}", result);
}

// Example: Fn(&str) -> &str is equivalent to for<'a> Fn(&'a str) -> &'a str

// Variance: how lifetimes behave with containers
// - Covariant: &'a T when T is invariant (most collections)
// - Invariant: &mut T must have exact lifetime
// - Contravariant: Fn(T) lifetime relationship

// Lifetime bounds in trait impls
trait Trait<'a> {
    fn method(&'a self);
}

impl<'a, T: 'a> Trait<'a> for T {
    fn method(&'a self) {
        // ...
    }
}
```

## Practice Questions

1. What is the purpose of lifetime annotations in Rust?
2. What are the three lifetime elision rules?
3. Why must structs that hold references have lifetime annotations?
4. What is the 'static lifetime? What types have it?
5. What is the difference between `'a: 'b` and `for<'a>`?

## LLM Prompts for Deeper Understanding

1. "Explain Rust lifetimes: annotations, elision rules, struct lifetimes, and the borrow checker"
2. "Show 'static lifetime: string literals, thread spawning, and trait objects"
3. "Teach advanced lifetimes: subtyping, variance, HRTB, and lifetime bounds"

## Key Takeaways

- Lifetime annotations describe relationships between reference lifetimes
- Three elision rules automatically infer lifetimes in common cases
- Structs with references need lifetime annotations
- 'static lifetime lasts for the entire program
- Lifetimes are a compile-time concept with zero runtime cost