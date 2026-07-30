---
{
  "slug": "rs-15-async-await",
  "title": "Async/Await and Tokio",
  "description": "Async functions, await syntax, futures, Tokio runtime, async I/O, tasks, and async patterns.",
  "type": "lesson",
  "order": 15,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write async functions and use the await syntax",
    "Understand Futures and the async runtime",
    "Use Tokio for async I/O and task management",
    "Implement common async patterns"
  ],
  "knowledge_refs": ["rust/rs-15-async-await"],
  "prerequisites": ["RS-14"],
  "references": [
    {"title": "The Rust Book — Async/Await", "url": "https://doc.rust-lang.org/book/ch16-04-extensible-concurrency.html"},
    {"title": "Tokio Documentation", "url": "https://docs.rs/tokio/"},
    {"title": "Async Book", "url": "https://rust-lang.github.io/async-book/"},
    {"title": "std::future", "url": "https://doc.rust-lang.org/std/future/index.html"}
  ]
}
---

# RS-15: Async/Await and Tokio

## Introduction

Async/await in Rust enables cooperative concurrency. Unlike OS threads, async tasks are lightweight and multiplexed onto a small number of threads. Tokio is the most popular async runtime, providing async I/O, timers, and task management.

## Key Concepts

### 1. Async Functions and .await

Async functions return Futures. The .await keyword yields control back to the runtime until the Future is ready. Async functions are syntactic sugar for state machines.

```rust
use std::time::Duration;

async fn hello() -> String {
    "Hello, async!".to_string()
}

async fn delayed_greeting(name: &str) -> String {
    // tokio::time::sleep(Duration::from_millis(100)).await;
    format!("Hello, {}!", name)
}

// #[tokio::main] is macro that sets up the Tokio runtime
#[tokio::main]
async fn main() {
    // Calling an async function returns a Future
    let future = hello();

    // .await runs the future to completion
    let result = future.await;
    println!("{}", result);

    // Await multiple futures
    let greeting = delayed_greeting("Alice").await;
    println!("{}", greeting);
}
```

### 2. Futures and Executors

A Future represents a value that may not be ready yet. The poll method checks if the value is ready. Executors (like Tokio) manage polling and scheduling.

```rust
use std::future::Future;
use std::pin::Pin;
use std::task::{Context, Poll};

// Simplified Future trait
// trait Future {
//     type Output;
//     fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output>;
// }

// #[tokio::main] expands to:
fn main() {
    tokio::runtime::Runtime::new()
        .unwrap()
        .block_on(async {
            println!("Hello from async!");
        });
}

// Manual executor (simplified)
struct SimpleExecutor;

impl SimpleExecutor {
    fn block_on<F: Future>(&mut self, mut future: F) -> F::Output
    where
        F: Future + Unpin,
    {
        let waker = futures::task::noop_waker();
        let mut cx = Context::from_waker(&waker);

        loop {
            match Pin::new(&mut future).poll(&mut cx) {
                Poll::Ready(val) => return val,
                Poll::Pending => {}  // would yield to runtime
            }
        }
    }
}
```

### 3. Tokio Tasks

tokio::spawn creates lightweight tasks that run concurrently. Tasks are similar to threads but much cheaper. Tasks can be joined and can return values.

```rust
use tokio::time::{sleep, Duration};

#[tokio::main]
async fn main() {
    // Spawn a task
    let handle = tokio::spawn(async {
        sleep(Duration::from_millis(100)).await;
        "Task completed".to_string()
    });

    // Do other work while task runs
    println!("Main thread working...");

    // Await the task result
    let result = handle.await.unwrap();
    println!("{}", result);

    // Multiple tasks
    let mut handles = vec![];
    for i in 0..5 {
        handles.push(tokio::spawn(async move {
            sleep(Duration::from_millis(50)).await;
            i
        }));
    }

    // Await all tasks
    for handle in handles {
        println!("Task: {}", handle.await.unwrap());
    }
}
```

### 4. Async I/O with Tokio

Tokio provides async versions of standard I/O operations: files, networking, timers, and process management.

```rust
use tokio::fs::File;
use tokio::io::{self, AsyncReadExt, AsyncWriteExt};
use tokio::net::TcpListener;
use tokio::time::{sleep, Duration};

#[tokio::main]
async fn main() -> io::Result<()> {
    // Async file read
    let mut file = File::open("hello.txt").await?;
    let mut contents = String::new();
    file.read_to_string(&mut contents).await?;
    println!("File: {}", contents);

    // Async TCP server
    let listener = TcpListener::bind("127.0.0.1:8080").await?;
    loop {
        let (socket, addr) = listener.accept().await?;
        tokio::spawn(async move {
            handle_connection(socket).await;
        });
    }
}

async fn handle_connection(mut socket: tokio::net::TcpStream) {
    let mut buf = [0; 1024];
    socket.read(&mut buf).await.unwrap();
    socket.write_all(b"HTTP/1.1 200 OK\r\n\r\nHello").await.unwrap();
}
```

### 5. Async Patterns: Join, Select, and Cancellation

Common async patterns for running multiple futures concurrently.

```rust
use tokio::time::{sleep, Duration, timeout};

#[tokio::main]
async fn main() {
    // Join: run multiple futures concurrently
    let (a, b, c) = tokio::join!(
        async { sleep(Duration::from_millis(100)).await; "A" },
        async { sleep(Duration::from_millis(200)).await; "B" },
        async { sleep(Duration::from_millis(50)).await; "C" },
    );
    println!("{}, {}, {}", a, b, c);  // C, A, B (in order of completion speed)

    // Select: await the first future to complete
    tokio::select! {
        result = sleep(Duration::from_millis(100)) => {
            println!("Timeout reached");
        }
        result = async { sleep(Duration::from_millis(50)).await; "Data" } => {
            println!("Got: {}", result);
        }
    }

    // Timeout: cancel a future if it takes too long
    let result = timeout(Duration::from_millis(100), async {
        sleep(Duration::from_millis(200)).await;
        "Done"
    }).await;

    match result {
        Ok(val) => println!("{}", val),
        Err(_) => println!("Timed out!"),
    }

    // Cancellation: drop a JoinHandle to cancel a task
    let handle = tokio::spawn(async {
        loop {
            sleep(Duration::from_secs(1)).await;
            println!("Still running...");
        }
    });
    sleep(Duration::from_secs(3)).await;
    handle.abort();  // cancel the task
}
```

## Practice Questions

1. What is a Future? How does the poll method work?
2. What is the difference between async/await and threads?
3. What is the Tokio runtime? What does #[tokio::main] do?
4. What is the difference between tokio::join! and tokio::select!?
5. How do you cancel a running async task?

## LLM Prompts for Deeper Understanding

1. "Explain async/await: Futures, poll, Pin, Waker, and the async runtime ecosystem"
2. "Show Tokio: tasks, async I/O, timers, and the runtime architecture"
3. "Teach async patterns: join, select, timeout, cancellation, and graceful shutdown"

## Key Takeaways

- Async functions return Futures; .await drives them to completion
- Tokio is the primary async runtime with task scheduling and async I/O
- tokio::spawn creates lightweight tasks; join! runs multiple concurrently
- select! awaits the first completed future; timeout! cancels slow futures
- Async/await enables cooperative concurrency with lightweight tasks