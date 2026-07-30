---
{
  "slug": "rs-07-collections",
  "title": "Vectors, Strings, and HashMaps",
  "description": "Vec<T> operations, String vs &str, HashMap and HashSet, iterating collections, and collection performance.",
  "type": "lesson",
  "order": 7,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create and manipulate vectors (Vec<T>)",
    "Work with String and &str efficiently",
    "Use HashMap and HashSet for key-value storage",
    "Understand collection performance characteristics"
  ],
  "knowledge_refs": ["rust/rs-07-collections"],
  "prerequisites": ["RS-04"],
  "references": [
    {"title": "The Rust Book — Common Collections", "url": "https://doc.rust-lang.org/book/ch08-00-common-collections.html"},
    {"title": "Rust std::vec", "url": "https://doc.rust-lang.org/std/vec/struct.Vec.html"},
    {"title": "Rust std::collections", "url": "https://doc.rust-lang.org/std/collections/index.html"},
    {"title": "Rust by Example — Vectors", "url": "https://doc.rust-lang.org/stable/rust-by-example/std/vec.html"}
  ]
}
---

# RS-07: Vectors, Strings, and HashMaps

## Introduction

Rust's standard library provides three primary collections: Vec<T> (growable arrays), String (UTF-8 text), and HashMap<K,V> (key-value maps). Each has specific performance characteristics and use cases. Understanding them is essential for writing efficient Rust code.

## Key Concepts

### 1. Vectors (Vec<T>)

Vec<T> is a growable, heap-allocated array. It stores elements contiguously in memory. Access is O(1) by index, push/pop at the end are amortized O(1).

```rust
fn main() {
    // Creating vectors
    let mut v: Vec<i32> = Vec::new();
    let v2 = vec![1, 2, 3];      // vec! macro

    // Adding and removing
    v.push(5);
    v.push(6);
    v.push(7);
    v.pop();                     // removes last element (Some(7))

    // Accessing elements
    let third: &i32 = &v[2];     // direct access (panics if out of bounds)
    let third: Option<&i32> = v.get(2);  // safe access (returns None)

    // Safe access pattern
    match v.get(10) {
        Some(val) => println!("Got: {}", val),
        None => println!("Index out of bounds"),
    }

    // Iterating
    for i in &v {
        println!("{}", i);
    }

    // Mutable iteration
    for i in &mut v {
        *i *= 2;  // double each element
    }

    // Vec methods
    v.sort();
    v.reverse();
    v.contains(&10);             // false
    v.len();                     // number of elements
    v.is_empty();                // false
    v.capacity();                // allocated capacity

    // Collect from iterator
    let squares: Vec<i32> = (1..=5).map(|x| x * x).collect();
    println!("{:?}", squares);   // [1, 4, 9, 16, 25]
}
```

### 2. String vs &str

String is an owned, heap-allocated, growable UTF-8 string. &str is a borrowed reference to a string slice. Understanding the difference is crucial for performance.

```rust
fn main() {
    // Creating strings
    let mut s = String::new();
    let s2 = String::from("hello");
    let s3 = "hello".to_string();

    // Appending
    s.push_str("hello");      // append &str
    s.push('!');              // append char

    // Concatenation
    let s1 = String::from("Hello, ");
    let s2 = String::from("world!");
    let s3 = s1 + &s2;        // s1 is moved, s2 is borrowed
    // println!("{}", s1);    // ERROR: s1 moved

    // Better: format!
    let greet = format!("{}{}", "Hello, ", "world!");

    // String indexing (NOT supported — UTF-8)
    let hello = "Здравствуйте";
    // let c = &hello[0];     // ERROR: cannot index into String

    // Iterating over characters
    for c in "hello".chars() {
        println!("{}", c);    // h, e, l, l, o
    }

    // Iterating over bytes
    for b in "hello".bytes() {
        println!("{}", b);    // 104, 101, 108, 108, 111
    }

    // String slicing (careful with UTF-8)
    let s = "Hello 🦀";
    let slice = &s[0..5];     // "Hello" (safe: ASCII)
    // let bad = &s[6..7];     // panics: not a char boundary
}
```

### 3. HashMap and HashSet

HashMap<K,V> stores key-value pairs with O(1) average lookup. HashSet<T> is a set of unique values (just HashMap<T, ()> under the hood).

```rust
use std::collections::HashMap;

fn main() {
    // Creating HashMap
    let mut scores = HashMap::new();
    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 50);

    // From iterator of tuples
    let teams = vec![String::from("Blue"), String::from("Yellow")];
    let initial_scores = vec![10, 50];
    let scores: HashMap<_, _> = teams.iter().zip(initial_scores.iter()).collect();

    // Accessing values
    let team_name = String::from("Blue");
    let score = scores.get(&team_name);  // Option<&i32>

    // Entry API (idiomatic insert/update)
    scores.entry(String::from("Blue")).or_insert(50);  // insert if missing
    scores.entry(String::from("Red")).or_insert(30);

    // Update based on existing value
    let text = "hello world wonderful world";
    let mut map = HashMap::new();
    for word in text.split_whitespace() {
        let count = map.entry(word).or_insert(0);
        *count += 1;  // increment count
    }
    println!("{:?}", map);  // {"hello": 1, "world": 2, "wonderful": 1}

    // Iterating
    for (key, value) in &scores {
        println!("{}: {}", key, value);
    }
}

// HashSet example
use std::collections::HashSet;

fn dedup(items: Vec<i32>) -> Vec<i32> {
    let mut seen = HashSet::new();
    items.into_iter().filter(|x| seen.insert(*x)).collect()
}
```

### 4. Collection Performance

Understanding performance characteristics helps choose the right collection for the task.

```rust
fn main() {
    // Vec: O(1) index, O(n) insert/remove at front
    let mut vec = Vec::with_capacity(100);  // pre-allocate
    vec.push(1);    // amortized O(1)
    vec.pop();      // O(1)
    vec.insert(0, 5);  // O(n) — shifts elements

    // VecDeque: O(1) push/pop at both ends
    use std::collections::VecDeque;
    let mut deque = VecDeque::new();
    deque.push_front(1);  // O(1)
    deque.push_back(2);   // O(1)
    deque.pop_front();    // O(1)
    deque.pop_back();     // O(1)

    // LinkedList: O(1) insert/remove at known position
    // (rarely used in Rust — cache-unfriendly)
    use std::collections::LinkedList;

    // HashMap: O(1) average, O(n) worst case
    use std::collections::HashMap;
    // Use with_capacity for known sizes
    let mut map = HashMap::with_capacity(1000);

    // BTreeMap: O(log n) sorted map
    use std::collections::BTreeMap;
    // Use when you need sorted keys or range queries
}
```

### 5. Common Collection Patterns

Idiomatic patterns for working with collections efficiently.

```rust
fn main() {
    // Extend Vec from iterator
    let mut vec = vec![1, 2, 3];
    vec.extend([4, 5, 6]);  // vec is now [1,2,3,4,5,6]

    // Drain: remove elements and use them
    let mut vec = vec![1, 2, 3, 4, 5];
    let drained: Vec<_> = vec.drain(1..3).collect();  // [2, 3]
    println!("{:?}, {:?}", vec, drained);  // [1, 4, 5], [2, 3]

    // Retain: keep elements matching predicate
    vec.retain(|x| x % 2 == 0);  // keep only even

    // Split off: split at index
    let mut vec = vec![1, 2, 3, 4, 5];
    let right = vec.split_off(3);  // vec=[1,2,3], right=[4,5]

    // Windows and chunks
    let arr = [1, 2, 3, 4, 5];
    for window in arr.windows(3) {
        println!("{:?}", window);  // [1,2,3], [2,3,4], [3,4,5]
    }

    // Group by (nightly)
    // let mut map = HashMap::new();
    // for item in items {
    //     map.entry(item.category()).or_insert(vec![]).push(item);
    // }
}
```

## Practice Questions

1. What is the difference between `Vec<T>` and an array `[T; N]`?
2. Why can't you index into a String directly?
3. What is the Entry API in HashMap? When would you use it?
4. What is the performance difference between Vec::push and Vec::insert?
5. When would you use VecDeque over Vec?

## LLM Prompts for Deeper Understanding

1. "Explain Vec<T> internals: memory layout, capacity, growth strategy, and the allocator API"
2. "Show String vs &str: UTF-8 encoding, indexing, slicing, and performance tradeoffs"
3. "Teach HashMap: hashing, SipHash, the Entry API, and custom hash functions"

## Key Takeaways

- Vec<T> is a growable array with O(1) push/pop at end, O(n) insert at front
- String is owned UTF-8; &str is borrowed; cannot index into String (UTF-8)
- HashMap provides O(1) average lookup; Entry API for insert-or-update
- Pre-allocate with `with_capacity` for known sizes
- Use VecDeque when you need efficient push/pop at both ends