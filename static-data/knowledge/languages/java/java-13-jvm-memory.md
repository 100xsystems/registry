---
{
  "title": "JVM Memory and Garbage Collection",
  "description": "Understand JVM memory model (heap, stack, metaspace)",
  "type": "lesson",
  "order": 13,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand JVM memory model (heap, stack, metaspace)",
    "Describe garbage collection algorithms",
    "Tune GC with JVM flags",
    "Monitor memory with jstat, jmap, VisualVM"
  ],
  "knowledge_refs": [
    "java/java-13-jvm-memory"
  ],
  "prerequisites": [
    "JV-01"
  ],
  "references": [
    {
      "title": "Oracle — JVM Tuning Guide",
      "url": "https://docs.oracle.com/en/java/javase/21/vm/java-virtual-machine-guide.pdf"
    },
    {
      "title": "Baeldung — JVM Parameters",
      "url": "https://www.baeldung.com/jvm-parameters"
    },
    {
      "title": "Baeldung — Garbage Collection",
      "url": "https://www.baeldung.com/java-garbage-collection"
    },
    {
      "title": "Oracle — GC Tuning",
      "url": "https://docs.oracle.com/en/java/javase/21/gctuning/"
    }
  ]
}
---

# JAVA-13-JVM-MEMORY: JVM Memory and Garbage Collection

## Introduction

Understanding JVM memory management is essential for writing performant Java applications. The JVM divides memory into regions, uses generational garbage collection, and provides extensive tuning flags.

## Key Concepts

### 1. JVM Memory Regions

Heap: young generation (Eden, S0, S1) + old generation. Metaspace (Java 8+) replaces PermGen for class metadata. Stack: per-thread, stores primitives and references. Native memory: direct buffers.

```java
// JVM memory regions
// Heap: -Xms (initial), -Xmx (max)
// Young Gen: -Xmn or -XX:NewRatio
// Metaspace: -XX:MaxMetaspaceSize

// View memory usage programmatically
Runtime runtime = Runtime.getRuntime();
long totalMemory = runtime.totalMemory();
long freeMemory = runtime.freeMemory();
long maxMemory = runtime.maxMemory();
long usedMemory = totalMemory - freeMemory;
```

### 2. Garbage Collection Generations

Young GC (Minor) — collects short-lived objects in Eden. Moves survivors to S0/S1, then to Old Gen. Old GC (Major) — collects old generation. Full GC — collects entire heap including metaspace.

```java
// GC types and flags
// G1GC (default since Java 9): -XX:+UseG1GC
// Region-based, predictable pause times

// Heap sizing for 4GB heap
// -Xms4g -Xmx4g -XX:NewRatio=2 -XX:SurvivorRatio=8

// G1 GC tuning
// -XX:MaxGCPauseMillis=200  (target pause time)
// -XX:G1HeapRegionSize=16m  (region size)
// -XX:InitiatingHeapOccupancyPercent=45
```

### 3. GC Algorithms: G1, ZGC, Shenandoah

G1 GC: default since Java 9, region-based, low-pause. ZGC (Java 15+): sub-millisecond pauses, concurrent, scalable to multi-TB heaps. Shenandoah (Java 15+): concurrent compaction, low-pause.

```java
// G1 GC — default, good balance
// $ java -XX:+UseG1GC -Xmx8g -jar app.jar

// ZGC — ultra-low latency (<1ms pauses)
// $ java -XX:+UseZGC -Xmx16g -jar app.jar
// Best for: large heaps, sub-millisecond pause requirements

// Shenandoah — concurrent compaction
// $ java -XX:+UseShenandoahGC -Xmx8g -jar app.jar
// Best for: applications needing consistent response times
```

### 4. Memory Leaks and Monitoring

Common leaks: unclosed streams, static collections, ThreadLocals, Inner classes holding references, String.intern(). Tools: jstat, jmap, jhat, VisualVM, Eclipse MAT, async-profiler.

```java
// Common leak patterns
// 1. static collection growing unbounded
private static List<byte[]> cache = new ArrayList<>();

// 2. Unclosed resources
InputStream is = new FileInputStream("file");
// is never closed — finalizer may never run

// 3. ThreadLocal without removal
private ThreadLocal<byte[]> local = new ThreadLocal<>();
// In web apps: thread pool reuses threads — old data persists!
// Always: local.remove() in finally block

// Monitoring commands
// $ jstat -gcutil <pid> 1000  (GC stats every second)
// $ jmap -histo <pid>     (object histogram)
// $ jmap -dump:format=b,file=heap.hprof <pid>
```

### 5. JVM Tuning Best Practices

Set -Xms and -Xmx equal to avoid resize pauses. Choose GC based on requirements (throughput vs latency). Monitor GC logs. Use -XX:+PrintGCDetails and -XX:+PrintGCTimeStamps.

```java
// Tuning for throughput (batch processing)
// -Xms4g -Xmx4g -XX:+UseParallelGC
// -XX:ParallelGCThreads=4

// Tuning for latency (web servers)
// -Xms4g -Xmx4g -XX:+UseG1GC
// -XX:MaxGCPauseMillis=100
// -XX:+UnlockExperimentalVMOptions -XX:+UseZGC

// GC logging
// -Xlog:gc*:file=gc.log::filecount=5,filesize=50m
// (Java 9+ unified logging)
```

## Practice Questions

1. What memory regions exist in the JVM heap?
1. What is the difference between Minor, Major, and Full GC?
1. When would you choose ZGC over G1?
1. How can you monitor JVM heap usage at runtime?

## LLM Prompts for Deeper Understanding

1. "Explain JVM memory model: heap regions, stack, metaspace, native memory"
1. "Show garbage collection algorithms: generational, G1, ZGC, Shenandoah"
1. "Teach JVM tuning flags for throughput vs latency tradeoffs"

## Key Takeaways

- Heap: Eden -> Survivor -> Old Gen; Metaspace for class metadata
- G1 is default GC; ZGC for sub-millisecond pauses
- Match -Xms and -Xmx to avoid resize pauses; enable GC logging