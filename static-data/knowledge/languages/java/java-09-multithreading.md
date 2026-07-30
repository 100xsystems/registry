---
{
  "title": "Multithreading and Concurrency",
  "description": "Create threads with Thread and Runnable",
  "type": "lesson",
  "order": 9,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create threads with Thread and Runnable",
    "Use synchronized and Locks for thread safety",
    "Use ExecutorService for thread pooling",
    "Understand volatile, atomic, and happens-before"
  ],
  "knowledge_refs": [
    "java/java-09-multithreading"
  ],
  "prerequisites": [
    "JV-07"
  ],
  "references": [
    {
      "title": "Oracle Tutorial — Concurrency",
      "url": "https://docs.oracle.com/javase/tutorial/essential/concurrency/index.html"
    },
    {
      "title": "Oracle Docs — ExecutorService",
      "url": "https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/ExecutorService.html"
    },
    {
      "title": "Effective Java — Ch 11: Concurrency",
      "url": "https://www.oreilly.com/library/view/effective-java-3rd/9780134686097/"
    },
    {
      "title": "Baeldung — Java Concurrency",
      "url": "https://www.baeldung.com/java-concurrency"
    }
  ]
}
---

# JAVA-09-MULTITHREADING: Multithreading and Concurrency

## Introduction

Java provides built-in threading support since version 1.0. The java.util.concurrent package (Java 5+) offers high-level constructs: ExecutorService, Locks, Atomic classes, Concurrent collections, and synchronizers.

## Key Concepts

### 1. Thread Creation: Thread and Runnable

Two ways: extend Thread or implement Runnable (prefer Runnable/functional). Thread states: NEW, RUNNABLE, BLOCKED, WAITING, TIMED_WAITING, TERMINATED. join() waits for thread completion.

```java
// Implement Runnable (preferred)
Runnable task = () -> {
    String name = Thread.currentThread().getName();
    System.out.println("Running in: " + name);
};

Thread t1 = new Thread(task, "worker-1");
t1.start();  // begins execution
t1.join();   // waits for completion

// Thread states
System.out.println(t1.getState());  // TERMINATED after join

// Thread with result via Callable
Callable<Integer> compute = () -> {
    Thread.sleep(1000);
    return 42;
};
```

### 2. Synchronization: synchronized and Lock

synchronized keyword on methods or blocks provides mutual exclusion. Each object has an intrinsic lock. ReentrantLock provides more flexibility: tryLock, fairness, multiple conditions.

```java
// Synchronized method
public class Counter {
    private int count = 0;

    public synchronized void increment() {
        count++;
    }

    public synchronized int getCount() {
        return count;
    }
}

// ReentrantLock (more flexible)
Lock lock = new ReentrantLock();
lock.lock();
try {
    // critical section
} finally {
    lock.unlock();  // must unlock in finally
}
```

### 3. ExecutorService — Thread Pool Management

ExecutorService manages thread lifecycle. newFixedThreadPool, newCachedThreadPool, newSingleThreadExecutor. submit() returns Future<T>. invokeAll runs multiple Callables. shutdown() stops accepting tasks.

```java
ExecutorService executor = Executors.newFixedThreadPool(4);

// Submit tasks and get Future results
Future<String> future = executor.submit(() -> {
    Thread.sleep(1000);
    return "Task complete";
});

// Get result (blocks until done)
String result = future.get(2, TimeUnit.SECONDS);  // with timeout

// Submit multiple tasks
List<Callable<Integer>> tasks = List.of(
    () -> 1, () -> 2, () -> 3
);
List<Future<Integer>> results = executor.invokeAll(tasks);

executor.shutdown();  // graceful shutdown
```

### 4. Atomic Variables and volatile

java.util.concurrent.atomic provides lock-free thread-safe variables: AtomicInteger, AtomicLong, AtomicReference. compareAndSet (CAS) provides atomic updates. volatile ensures visibility across threads.

```java
// AtomicInteger — no synchronization needed
private AtomicInteger counter = new AtomicInteger(0);

// Thread-safe increment
counter.incrementAndGet();
counter.addAndGet(5);
counter.compareAndSet(expected, newValue);  // CAS operation

// volatile — visibility guarantee
private volatile boolean running = true;

// Thread 1:
public void stop() { running = false; }

// Thread 2: guaranteed to see the change immediately
while (running) {
    // do work
}
```

### 5. Concurrent Collections and CompletableFuture

ConcurrentHashMap for thread-safe maps. CopyOnWriteArrayList for safe iteration. BlockingQueue for producer-consumer. CompletableFuture (Java 8+) for async composition.

```java
// ConcurrentHashMap — thread-safe without locking whole map
ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();
map.putIfAbsent("key", 1);
map.computeIfAbsent("key", k -> 42);

// BlockingQueue — producer-consumer
BlockingQueue<String> queue = new LinkedBlockingQueue<>(100);
queue.put("item");    // blocks if full
String item = queue.take();  // blocks if empty

// CompletableFuture — async composition
CompletableFuture.supplyAsync(() -> fetchData())
    .thenApplyAsync(String::toUpperCase)
    .thenAccept(System.out::println)
    .exceptionally(ex -> {
        System.err.println("Failed: " + ex);
        return null;
    });
```

## Practice Questions

1. What are the two ways to create a thread? Which is preferred?
1. What is the difference between synchronized and ReentrantLock?
1. What does ExecutorService.shutdown() do?
1. What is CAS? How does AtomicInteger use it?

## LLM Prompts for Deeper Understanding

1. "Explain Java memory model with happens-before and volatile guarantees"
1. "Show ExecutorService patterns with Callable, Future, invokeAll"
1. "Teach CompletableFuture with composition, error handling, threading"

## Key Takeaways

- Prefer Runnable/Callable over extending Thread
- java.util.concurrent provides high-level constructs: ExecutorService, Locks, Atomic*
- CompletableFuture enables async functional composition (Java 8+)