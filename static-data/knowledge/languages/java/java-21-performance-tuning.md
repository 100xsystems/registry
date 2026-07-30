---
{
  "title": "Performance Tuning and Java Best Practices",
  "description": "Profile CPU and memory with async-profiler and JFR",
  "type": "lesson",
  "order": 21,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Profile CPU and memory with async-profiler and JFR",
    "Apply Java performance best practices",
    "Write efficient string, collection, and I/O code",
    "Understand JIT compilation and warmup"
  ],
  "knowledge_refs": [
    "java/java-21-performance-tuning"
  ],
  "prerequisites": [
    "JV-11",
    "JV-13"
  ],
  "references": [
    {
      "title": "Oracle — JFR",
      "url": "https://docs.oracle.com/en/java/javase/21/jfapi/"
    },
    {
      "title": "Async Profiler",
      "url": "https://github.com/async-profiler/async-profiler"
    },
    {
      "title": "Baeldung — Java Profiling",
      "url": "https://www.baeldung.com/java-profiling"
    },
    {
      "title": "Effective Java Performance Tips",
      "url": "https://www.oreilly.com/library/view/effective-java-3rd/9780134686097/"
    }
  ]
}
---

# JAVA-21-PERFORMANCE-TUNING: Performance Tuning and Java Best Practices

## Introduction

Java performance tuning involves profiling CPU, memory, and GC. The JVM JIT compiles hot methods. JFR (Java Flight Recorder) provides low-overhead profiling. async-profiler shows CPU and allocation hot spots.

## Key Concepts

### 1. Profiling with async-profiler and JFR

async-profiler: CPU and allocation profiling with FlameGraphs. JFR: built-in low-overhead event recording. jcmd commands for on-demand JFR. Analyze in Java Mission Control.

```java
# async-profiler
$ java -agentpath:libasyncProfiler.so=start,event=cpu,file=profile.html -jar app.jar

# JFR recording
$ java -XX:StartFlightRecording=filename=recording.jfr,duration=60s -jar app.jar

# jcmd for on-demand JFR
$ jcmd <pid> JFR.start name=profile duration=60s filename=profile.jfr
$ jcmd <pid> JFR.dump name=profile filename=exported.jfr

# jstack for thread dumps
$ jstack <pid> > threaddump.txt
```

### 2. String and Collection Performance

Use StringBuilder for concatenation in loops. Pre-size collections when possible. Use primitive collections (int[] vs Integer[]). Choose right collection: ArrayList for random access, LinkedList for queue.

```java
// BAD: String concatenation in loop
String result = "";
for (String s : items) {
    result += s;  // creates new String each iteration
}

// GOOD: StringBuilder
StringBuilder sb = new StringBuilder(items.size() * 10);
for (String s : items) {
    sb.append(s);
}
String result = sb.toString();

// Pre-size collections
List<String> list = new ArrayList<>(expectedSize);
Map<String, String> map = new HashMap<>(expectedSize / 0.75f + 1);
```

### 3. JIT Compilation and Warmup

JIT (Just-In-Time) compilation converts hot bytecode to native code. -XX:+PrintCompilation shows compilation. Tiered compilation (client + server). Warmup: let JIT optimize before load testing.

```java
// JIT compilation flags
-XX:+PrintCompilation         // print compiled methods
-XX:CompileThreshold=10000    // iterations before compile

// Warmup approach
// 1. Start the application and let it stabilize
// 2. Run a smaller batch of requests to warm JIT
// 3. Begin actual performance measurement

// AOT compilation (GraalVM native-image)
// Pre-compiles to native executable — no JIT warmup needed
// Startup is instant, but peak performance may be lower
```

### 4. Memory and GC Optimization

Avoid unnecessary object creation. Use primitive fields. Pool expensive objects. Right-size heap: not too small (frequent GC), not too large (long GC pauses). Monitor GC logs.

```java
// Avoid auto-boxing in hot paths
// BAD: List<Integer> with autoboxing
List<Integer> values = new ArrayList<>();
for (int i = 0; i < 1000000; i++) {
    values.add(i);  // autoboxing creates Integer objects
}

// GOOD: primitive array or specialized collection
int[] values = new int[1000000];

// Object pooling for expensive objects
// Use ThreadLocal for per-thread caching
ThreadLocal<SimpleDateFormat> dateFormat =
    ThreadLocal.withInitial(() -> new SimpleDateFormat("yyyy-MM-dd"));
```

### 5. Concurrency Best Practices

Use ExecutorService (not Thread directly). Use ConcurrentHashMap, not synchronized Map. Limit synchronized blocks to minimum. Use volatile for flags, Atomic* for counters, Lock for complex coordination.

```java
// Prefer ConcurrentHashMap over synchronized HashMap
Map<String, String> config = new ConcurrentHashMap<>();  // thread-safe

// Atomic counter vs synchronized
private AtomicInteger counter = new AtomicInteger();  // lock-free

// Use CompletableFuture for async composition
CompletableFuture.supplyAsync(() -> fetchData(), executor)
    .orTimeout(5, TimeUnit.SECONDS)
    .exceptionally(ex -> fallback());

// Avoid synchronized on hot paths
// Use StampedLock for read-heavy workloads
StampedLock lock = new StampedLock();
```

### 6. Effective Java Best Practices Summary

Follow Effective Java 3rd Edition guidelines: min access, favor immutability, prefer interfaces to abstract classes, use try-with-resources, check parameters, document thread safety.

```java
// Item 15: Minimize access
private static final int MAX_SIZE = 1000;

// Item 17: Favor immutability
public final class ImmutablePoint {
    private final int x;
    private final int y;
    // no setters, defensive copies in constructor
}

// Item 9: try-with-resources
try (InputStream in = new FileInputStream("file")) {
    // auto-closed
}

// Item 49: Check parameters
public void deposit(double amount) {
    Objects.requireNonNull(amount, "amount must not be null");
    if (amount <= 0) throw new IllegalArgumentException();
}
```

## Practice Questions

1. What does JIT compilation do? How does warmup help performance?
1. Why is StringBuilder better than + for loop concatenation?
1. What is async-profiler? How does it create FlameGraphs?
1. What are the key best practices from Effective Java?

## LLM Prompts for Deeper Understanding

1. "Explain JIT compilation, tiered compilation, and GraalVM AOT"
1. "Show async-profiler and JFR for CPU, allocation, and lock profiling"
1. "Teach Java performance patterns from Effective Java 3rd Edition"

## Key Takeaways

- JIT compiles hot methods to native code; warmup is essential for benchmarks
- Use StringBuilder for loops, pre-size collections, avoid autoboxing
- JFR and async-profiler provide low-overhead CPU and allocation profiling