---
{
  "slug": "rs-13-smart-pointers",
  "title": "Smart Pointers: Box, Rc, Arc",
  "description": "Box<T> for heap allocation, Rc<T> for shared ownership, RefCell<T> for interior mutability, Arc<T> for thread safety.",
  "type": "lesson",
  "order": 13,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use Box<T> for heap allocation and recursive types",
    "Use Rc<T> for reference-counted shared ownership",
    "Use RefCell<T> for interior mutability",
    "Use Arc<T> for thread-safe shared ownership"
  ],
  "knowledge_refs": ["rust/rs-13-smart-pointers"],
  "prerequisites": ["RS-10"],
  "references": [
    {"title": "The Rust Book — Smart Pointers", "url": "https://doc.rust-lang.org/book/ch15-00-smart-pointers.html"},
    {"title": "std::boxed", "url": "https://doc.rust-lang.org/std/boxed/struct.Box.html"},
    {"title": "std::rc", "url": "https://doc.rust-lang.org/std/rc/struct.Rc.html"},
    {"title": "std::cell", "url": "https://doc.rust-lang.org/std/cell/index.html"}
  ]
}
---

# RS-13: Smart Pointers: Box, Rc, Arc

## Introduction

Smart pointers are data structures that act like pointers but have additional metadata and capabilities. Ownership, borrowing, and reference counting are managed by these types. Box, Rc, Arc, and RefCell are the most common smart pointers in Rust.

## Key Concepts

### 1. Box<T> — Heap Allocation

Box<T> allocates values on the heap. It's the simplest smart pointer, providing ownership with a known size at compile time. Box is essential for recursive types and trait objects.

```rust
fn main() {
    // Box for heap allocation
    let b = Box::new(5);
    println!("b = {}", b);  // Deref to access value

    // Recursive type (enum or struct that contains itself)
    enum List {
        Cons(i32, Box<List>),
        Nil,
    }

    let list = List::Cons(1, Box::new(List::Cons(2, Box::new(List::Nil))));

    // Boxing large data for move efficiency
    let large_data = Box::new([0u8; 1024 * 1024]);  // 1MB on heap
    move_data(large_data);  // cheap: just copies the pointer

    // Trait objects (dynamic dispatch)
    trait Draw {
        fn draw(&self);
    }

    struct Button;
    impl Draw for Button {
        fn draw(&self) { println!("Drawing button"); }
    }

    // Box<dyn Trait> allows storing different types that implement the same trait
    let components: Vec<Box<dyn Draw>> = vec![Box::new(Button)];
}

fn move_data(data: Box<[u8; 1024 * 1024]>) {
    // Only the pointer (8 bytes) is moved, not the 1MB data
    drop(data);
}
```

### 2. Rc<T> — Reference Counting

Rc<T> provides shared ownership via reference counting. Multiple parts of code can own the same data. The data is freed when the last Rc is dropped. Rc is not thread-safe (use Arc for threads).

```rust
use std::rc::Rc;

fn main() {
    let a = Rc::new(String::from("hello"));
    let b = Rc::clone(&a);  // increments reference count
    let c = Rc::clone(&a);  // increments reference count

    // Rc::clone is cheap: only copies the pointer, not the data
    println!("Reference count: {}", Rc::strong_count(&a));  // 3

    // Multiple parts of code share ownership
    let shared = Rc::new(vec![1, 2, 3]);
    let thread1 = shared.clone();
    let thread2 = shared.clone();

    // Weak references (no ownership, prevents cycles)
    use std::rc::Weak;
    let weak: Weak<String> = Rc::downgrade(&a);
    // weak.upgrade() returns Option<Rc<T>>
    if let Some(strong) = weak.upgrade() {
        println!("Still alive: {}", strong);
    }
}
```

### 3. RefCell<T> — Interior Mutability

RefCell<T> enforces borrowing rules at runtime instead of compile time. It allows mutation even when the RefCell itself is immutable. This is called interior mutability.

```rust
use std::cell::RefCell;

fn main() {
    // RefCell allows mutation through immutable reference
    let data = RefCell::new(5);

    // Borrow immutably (multiple borrows allowed at runtime)
    let r1 = data.borrow();
    let r2 = data.borrow();
    println!("{}, {}", r1, r2);

    // Borrow mutably (only one at runtime, panics if violated)
    let mut r3 = data.borrow_mut();
    *r3 += 1;
    // drop(r3);  // borrow ends here
    // println!("{}", data.borrow());  // OK after r3 is dropped

    // Practical: Rc<RefCell<T>> for shared mutable state
    use std::rc::Rc;

    let shared = Rc::new(RefCell::new(42));
    let shared_clone = shared.clone();

    *shared.borrow_mut() += 1;  // modify through Rc
    println!("{}", shared_clone.borrow());  // 43 — both see the change
}
```

### 4. Arc<T> — Atomic Reference Counting

Arc<T> is the thread-safe version of Rc<T>. It uses atomic operations for reference counting, making it safe to share across threads. Arc has a small performance cost compared to Rc.

```rust
use std::sync::Arc;
use std::thread;

fn main() {
    let data = Arc::new(vec![1, 2, 3, 4, 5]);
    let mut handles = vec![];

    for i in 0..3 {
        let data_clone = Arc::clone(&data);
        handles.push(thread::spawn(move || {
            println!("Thread {}: {:?}", i, data_clone);
        }));
    }

    for handle in handles {
        handle.join().unwrap();
    }

    // Arc<RwLock<T>> for shared mutable access
    use std::sync::RwLock;

    let shared = Arc::new(RwLock::new(42));
    let shared_clone = Arc::clone(&shared);

    let writer = thread::spawn(move || {
        *shared_clone.write().unwrap() += 1;
    });

    writer.join().unwrap();
    println!("Value: {}", *shared.read().unwrap());  // 43
}
```

### 5. Smart Pointer Patterns

Common patterns combining smart pointers for different use cases.

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::sync::{Arc, Mutex};

// Pattern 1: Rc<RefCell<T>> for single-threaded shared mutable state
struct Node {
    value: i32,
    children: Vec<Rc<RefCell<Node>>>,
}

// Pattern 2: Arc<Mutex<T>> for multi-threaded shared mutable state
struct SharedCounter {
    counter: Arc<Mutex<i32>>,
}

impl SharedCounter {
    fn new() -> Self {
        SharedCounter {
            counter: Arc::new(Mutex::new(0)),
        }
    }

    fn increment(&self) {
        let mut count = self.counter.lock().unwrap();
        *count += 1;
    }

    fn get(&self) -> i32 {
        *self.counter.lock().unwrap()
    }
}

// Pattern 3: Arc<RwLock<T>> for read-heavy workloads
use std::sync::RwLock;

struct Cache {
    data: Arc<RwLock<HashMap<String, String>>>,
}

impl Cache {
    fn get(&self, key: &str) -> Option<String> {
        self.data.read().unwrap().get(key).cloned()
    }

    fn set(&self, key: String, value: String) {
        self.data.write().unwrap().insert(key, value);
    }
}

// Pattern 4: Cell<T> for Copy types (no borrow checking overhead)
use std::cell::Cell;

struct Counter {
    count: Cell<i32>,
}

impl Counter {
    fn increment(&self) {
        self.count.set(self.count.get() + 1);
    }
}
```

## Practice Questions

1. What is the difference between Box<T> and a regular reference &T?
2. What is the difference between Rc<T> and Arc<T>? When would you use each?
3. What is interior mutability? How does RefCell<T> achieve it?
4. What is the difference between Cell<T> and RefCell<T>?
5. What is a reference cycle? How do Weak<T> references prevent them?

## LLM Prompts for Deeper Understanding

1. "Explain Box<T>: heap allocation, recursive types, trait objects, and Deref trait"
2. "Show Rc<T> and Arc<T>: reference counting, clone semantics, and Weak<T> for preventing cycles"
3. "Teach interior mutability: RefCell<T>, Cell<T>, and the borrow checking at runtime"

## Key Takeaways

- Box<T> allocates on the heap; essential for recursive types and trait objects
- Rc<T> provides shared ownership via reference counting (single-threaded)
- Arc<T> is the thread-safe version of Rc (uses atomic operations)
- RefCell<T> enables interior mutability with runtime borrow checking
- Common patterns: Rc<RefCell<T>> for single-threaded, Arc<Mutex<T>> for multi-threaded