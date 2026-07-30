---
title: "Concurrency: Threads and Executors"
description: "Thread class, Runnable, synchronized, locks, ExecutorService, CompletableFuture."
type: lesson
order: 13
duration: "75 min"
difficulty: advanced
learning_objectives:
  - "Create threads with Thread and Runnable"\n  - "Synchronize with synchronized and Lock"\n  - "Use ExecutorService for thread pools"\n  - "Write async code with CompletableFuture"
knowledge_refs:
  - java/java-13-concurrency
prerequisites:
  - "JAVA-08"
references:
    - title: "Oracle - Concurrency"\n      url: "https://docs.oracle.com/javase/tutorial/essential/concurrency/index.html"\n    - title: "Oracle - Executors"\n      url: "https://docs.oracle.com/javase/tutorial/essential/concurrency/executors.html"
---

# JAVA-13-CONCURRENCY: Concurrency: Threads and Executors

## Threads

```java
// Via Runnable
Thread thread = new Thread(() ->
    System.out.println("In: " + Thread.currentThread().getName()));
thread.start();
```

## Synchronization

```java
public class Counter {
    private int count = 0;
    public synchronized void increment() {
        count++;  // Thread-safe
    }
}
```

## ExecutorService

```java
ExecutorService exec = Executors.newFixedThreadPool(4);
Future<Integer> future = exec.submit(() -> {
    Thread.sleep(1000);
    return 42;
});
Integer result = future.get();  // Blocks until done
exec.shutdown();
```

## CompletableFuture

```java
CompletableFuture.supplyAsync(() -> fetchUser(123))
    .thenApply(user -> user.withLastLogin(LocalDateTime.now()))
    .thenAccept(user -> cache(user))
    .exceptionally(ex -> { log.error("Failed", ex); return null; });
```

