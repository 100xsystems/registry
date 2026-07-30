---
title: "Memory Management, GC, and Performance"
description: "JavaScript memory management, garbage collection algorithms, memory leak patterns, and performance optimization techniques."
type: lesson
order: 16
duration: "75 min"
difficulty: expert
learning_objectives:
  - "Understand V8's garbage collection: generational GC, mark-sweep, mark-compact"
  - "Identify and fix common memory leak patterns: closures, DOM references, timers, event listeners"
  - "Use Chrome DevTools Performance and Memory tabs for profiling"
  - "Apply performance optimization patterns: object pools, inline caching, hidden classes"
knowledge_refs:
  - languages/javascript/js-16-memory-performance
prerequisites:
  - "JS-01 through JS-14"
references:
    - title: "MDN Web Docs"
      url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_management"
      sections: "Memory Management — full guide | Memory Management in V8"
      description: "Authoritative reference on JS memory management"
    - title: "V8 Developer Blog"
      url: "https://v8.dev/blog"
      sections: "Design Elements, Fast Properties, Inline Caching, Concurrent Marking"
      description: "Official V8 blog posts on engine internals and optimization"
    - title: "The Modern JavaScript Tutorial"
      url: "https://javascript.info/garbage-collection"
      sections: "Garbage collection | Object references and copying"
      description: "Introduction to GC concepts with practical examples"
    - title: "Exploring JS: JavaScript for Programmers"
      url: "https://exploringjs.com/js/ch_memory.html"
      chapters: "[Ch. 17: Memory and Performance](https://exploringjs.com/js/ch_memory.html)"
      description: "Deep coverage of memory management and optimization"
---

# JS-16: Memory Management, GC, and Performance

## Introduction

JavaScript engines use sophisticated garbage collection algorithms that run
concurrently with your program. Understanding how memory is allocated, tracked,
and freed is essential for building high-performance applications that don't
leak or jank.

## Subtopics

### 1. Stack vs Heap

- **Stack**: Primitive values, function call frames, references to heap objects
  — fast, limited size, automatic cleanup when function returns
- **Heap**: Objects, arrays, closures — dynamic allocation, GC-managed
- *Reference:* MDN — Memory Management | [javascript.info — Garbage collection](https://javascript.info/service-workersservice-workersgarbage-collection)

### 2. V8 Garbage Collection

- **Generational GC**: Young generation (nursery) and old generation
- **Minor GC (Scavenger)**: Frequent, fast — collects young objects
- **Major GC (Mark-Sweep-Compact)**: Infrequent, slower — collects old generation
- **Orinoco**: V8's concurrent GC — minimizes main thread pauses
- **Marking**: GC traces from roots (global, stack, Registers) marking reachable objects
- **Sweep/Compact**: Unmarked objects removed, survivors compacted
- *Reference:* V8 blog — Concurrent marking, Memory management

### 3. Memory Leak Patterns

- **Accidental globals**: Assigning to undeclared variable creates global
- **Forgotten timers**: `setInterval` with reference to DOM node prevents GC
- **Detached DOM nodes**: Remove node from DOM but JS still references it
- **Closure over large data**: Closure keeps entire scope chain alive
- **Event listeners**: Add but never remove — listener holds reference to element
- **Circular references with DOM**: Old IE issue, modern GCs handle cycles
- *Reference:* MDN — Memory management: Detecting leaks | DevTools Memory tab

### 4. Performance Optimization

- **Hidden classes**: V8 creates hidden classes for objects with the same property layout
- **Inline caching (IC)**: V8 caches property lookup results at call sites
- **Monomorphic vs polymorphic**: Functions perform best when called with same-shaped objects
- **Object pools**: Reuse objects instead of creating new ones in hot paths
- **Avoid `delete`**: Deleting properties prevents hidden class optimization
- **Prefer monomorphic calls**: Always pass objects with the same property shapes
- *Reference:* V8 blog — Design Elements, Fast Properties, Inline Caching

### 5. Profiling and Analysis

- **Chrome DevTools Performance tab**: Record and analyze frame rate, FPS, GC pauses
- **Chrome DevTools Memory tab**: Heap snapshots, allocation instrumentation, allocation timelines
- **`performance.memory`**: `usedJSHeapSize`, `totalJSHeapSize`, `jsHeapSizeLimit`
- **`console.memory`**: V8-specific memory info
- *Reference:* Chrome DevTools Documentation — Performance, Memory

## Practice Questions

1. Why does attaching a `setInterval` that references `this.widget` cause a memory leak?
2. How can you force an object to be garbage collected?
3. What is a "detached DOM tree" and why does it leak memory?
4. Explain the difference between mark-sweep and mark-compact GC phases.

## Key Takeaways

- JS memory is managed automatically via garbage collection
- Memory leaks happen when objects are still referenced but no longer needed
- V8 uses generational GC — young generation collected frequently, old infrequently
- Hidden classes and inline caching make monomorphic code faster
- Use DevTools Memory tab to identify leaks via heap snapshots

## Further Reading

- MDN: Memory Management
- V8 Blog: Design Elements, Fast Properties, Concurrent Marking
- Chrome DevTools: Memory Profiling documentation
