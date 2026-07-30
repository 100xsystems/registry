---
{
  "slug": "rs-14-concurrency",
  "title": "Concurrency: Threads and Message Passing",
  "description": "Thread spawning, join handles, message passing with channels (mpsc), shared state with Arc, Send and Sync traits.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Spawn threads and join handles",
    "Use channels for message passing",
    "Share state with Arc<Mutex<T>>",
    "Understand Send and Sync traits"
  ],
  "knowledge_refs": ["rust/rs-14-concurrency"],
  "prerequisites": ["RS-13"],
  "references": [
    {"title": "The Rust Book — Concurrency", "url": "https://doc.rust-lang.org/book/ch16-00-concurrency.html"},
    {"title": "Rust by Example — Threads", "url": "https://doc.rust-lang.org/stable/rust-by-example/std_misc/threads.html"},
    {"title": "std::thread", "url": "https://doc.rust-lang.org/std/thread/"},
    {"title": "std::sync", "url": "https://doc.rust-lang.org/std/sync/index.html"}
  ]
}
---

# RS-14: Concurrency: Threads and Message Passing

## Introduction

Rust's concurrency model is built on fearless concurrency: the type system prevents data races at compile time. The Send and Sync traits, along with ownership and borrowing, ensure that concurrent code is safe without sacrificing performance.

## Key Concepts

### 1. Thread Spawning and Joining

std::thread::spawn creates new OS threads. The closure passed to spawn must be 'static. JoinHandle::join() waits for the thread to complete.

```rust
use std::thread;
use std::time::Duration;

fn main() {
    // Spawn a thread
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("Thread: {}", i);
            thread::sleep(Duration::from_millis(1));
        }
    });

    // Main thread continues
    for i in 1..5 {
        println!("Main: {}", i);
        thread::sleep(Duration::from_millis(1));
    }

    // Wait for spawned thread
    handle.join().unwrap();

    // Move data into thread
    let v = vec![1, 2, 3];
    let handle = thread::spawn(move || {
        println!("Vector: {:?}", v);
        // v is moved into the thread
    });
    handle.join().unwrap();
    // println!("{:?}", v);  // ERROR: v moved
}
```

### 2. Message Passing with Channels

Channels are used for message passing between threads. Rust's standard library provides mpsc (multiple producer, single consumer) channels.

```rust
use std::sync::mpsc;
use std::thread;
use std::time::Duration;

fn main() {
    // Create channel
    let (tx, rx) = mpsc::channel();

    // Spawn producer thread
    thread::spawn(move || {
        let vals = vec![
            String::from("hello"),
            String::from("world"),
            String::from("from"),
            String::from("rust"),
        ];
        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(Duration::from_millis(100));
        }
    });

    // Receive messages
    for received in rx {
        println!("Got: {}", received);
    }

    // Multiple producers (clone tx)
    let (tx, rx) = mpsc::channel();
    let tx1 = tx.clone();

    thread::spawn(move || {
        tx1.send("Producer 1".to_string()).unwrap();
    });

    thread::spawn(move || {
        tx.send("Producer 2".to_string()).unwrap();
    });

    for received in rx {
        println!("{}", received);
    }
}
```

### 3. Shared State with Arc<Mutex<T>>

Mutex<T> provides mutual exclusion. Only one thread can access the data at a time. Arc<T> enables shared ownership across threads. Together, they implement shared mutable state.

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    // Arc<Mutex<T>> for shared mutable state
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();
            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Result: {}", *counter.lock().unwrap());  // 10

    // Deadlock: two mutexes locked in different order
    // let lock1 = Arc::new(Mutex::new(0));
    // let lock2 = Arc::new(Mutex::new(0));
    // Thread 1: lock1 -> lock2
    // Thread 2: lock2 -> lock1  // DEADLOCK!
}
```

### 4. RwLock and Barrier

RwLock allows multiple readers or one writer. Barrier synchronizes multiple threads at a specific point in execution.

```rust
use std::sync::{Arc, RwLock, Barrier};
use std::thread;

fn main() {
    // RwLock: multiple readers, single writer
    let data = Arc::new(RwLock::new(vec![1, 2, 3]));
    let mut handles = vec![];

    // Readers
    for _ in 0..5 {
        let data = Arc::clone(&data);
        handles.push(thread::spawn(move || {
            let read = data.read().unwrap();
            println!("Read: {:?}", *read);
        }));
    }

    // Writer
    let data = Arc::clone(&data);
    handles.push(thread::spawn(move || {
        let mut write = data.write().unwrap();
        write.push(4);
        println!("Write: added 4");
    }));

    // Barrier: synchronize threads at a point
    let barrier = Arc::new(Barrier::new(3));
    let mut handles = vec![];

    for i in 0..3 {
        let barrier = Arc::clone(&barrier);
        handles.push(thread::spawn(move || {
            println!("Thread {} waiting", i);
            barrier.wait();  // all threads wait here
            println!("Thread {} continuing", i);
        }));
    }
}
```

### 5. Send and Sync Traits

Send: types that can be transferred across threads. Sync: types that can be shared across threads. Most types are automatically Send and Sync. Raw pointers and Rc are not Send.

```rust
use std::rc::Rc;
use std::sync::{Arc, Mutex};

// Rc is NOT Send (use Arc for threads)
// fn will_not_compile() {
//     let rc = Rc::new(5);
//     thread::spawn(move || {
//         println!("{}", rc);  // ERROR: Rc is not Send
//     });
// }

// Arc is Send + Sync
fn will_compile() {
    let arc = Arc::new(5);
    thread::spawn(move || {
        println!("{}", arc);  // OK: Arc is Send
    });
}

// Mutex<T> is Sync when T is Send
// Arc<Mutex<T>> is the standard way to share mutable state

// Implementing Send/Sync manually (unsafe)
struct MyType {
    // fields must be Send/Sync
}

// unsafe impl Send for MyType {}
// unsafe impl Sync for MyType {}

// Cell and RefCell are not Sync (use Mutex for threads)
// fn refcell_not_sync() {
//     let cell = std::cell::RefCell::new(5);
//     let arc = Arc::new(cell);
//     // ERROR: RefCell is not Sync
// }
```

## Practice Questions

1. What is the difference between thread::spawn and thread::scope?
2. What is the mpsc channel? What does mpsc stand for?
3. What is the difference between Mutex<T> and RwLock<T>?
4. What are the Send and Sync traits? Why are they automatically implemented?
5. What is a deadlock? How can you prevent it?

## LLM Prompts for Deeper Understanding

1. "Explain Rust threads: spawn, join, move closures, and scoped threads"
2. "Show channels: mpsc, multi-producer patterns, and channel use cases"
3. "Teach shared state: Arc<Mutex<T>>, RwLock, deadlock prevention, and Send/Sync traits"

## Key Takeaways

- thread::spawn creates OS threads; join waits for completion
- mpsc channels enable message passing between threads
- Arc<Mutex<T>> provides shared mutable state across threads
- RwLock allows multiple readers or one writer
- Send and Sync traits are automatically implemented for most types, ensuring data race safety