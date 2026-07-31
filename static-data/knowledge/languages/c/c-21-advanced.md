---
{
  "title": "Advanced: Variadics, Threads, and Atomics",
  "description": "Variadic functions, inline, C11 threads, atomics, low-level control.",
  "type": "lesson",
  "order": 21,
  "duration": "75 min",
  "difficulty": "expert",
  "learning_objectives": [
    "Write variadic functions with stdarg.h",
    "Use inline functions",
    "Create threads with C11 threads.h",
    "Use atomic operations"
  ],
  "knowledge_refs": [
    "c/c-21-advanced"
  ],
  "prerequisites": [
    "C-20"
  ],
  "references": [
    {
      "title": "cppreference — Variadic Functions",
      "url": "https://en.cppreference.com/w/c/variadic"
    },
    {
      "title": "cppreference — threads.h",
      "url": "https://en.cppreference.com/w/c/thread"
    },
    {
      "title": "cppreference — Atomics",
      "url": "https://en.cppreference.com/w/c/atomic"
    }
  ]
}
---

# C-21-ADVANCED: Advanced: Variadics, Threads, and Atomics

## Introduction

Variadic functions, inline, C11 threads, atomics, low-level control. By the end of this lesson you will be able to: Write variadic functions with stdarg.h; Use inline functions; Create threads with C11 threads.h; Use atomic operations.

## Key Concepts

### 1. Write variadic functions with stdarg.h

Target: Write variadic functions with stdarg.h. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```c
#include <stdio.h>
#include <stdarg.h>

// variadic function: printf-like
int sum(int count, ...) {
    va_list args;
    va_start(args, count);
    int total = 0;
    for (int i = 0; i < count; i++) total += va_arg(args, int);
    va_end(args);
    return total;
}

int main(void) {
    printf("%d\n", sum(3, 10, 20, 30));   // 60
    return 0;
}
```
### 2. Use inline functions

Target: Use inline functions. Apply the idiomatic pattern — this is how production C expresses this idea, so study the shape of the code.

```c
#include <stdio.h>

// inline function: hint to the compiler
static inline int clamp(int v, int lo, int hi) {
    if (v < lo) return lo;
    if (v > hi) return hi;
    return v;
}

int main(void) {
    printf("%d %d\n", clamp(150, 0, 100), clamp(-5, 0, 100));
    return 0;
}
```
### 3. Create threads with C11 threads.h

Target: Create threads with C11 threads.h. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```c
#include <stdio.h>
#include <threads.h>   // C11 threads

int worker(void *arg) {
    long id = (long)arg;
    printf("thread %ld\n", id);
    return 0;
}

int main(void) {
    thrd_t t1, t2;
    thrd_create(&t1, worker, (void *)1L);
    thrd_create(&t2, worker, (void *)2L);
    thrd_join(t1, NULL);
    thrd_join(t2, NULL);
    return 0;
}
```
### 4. Use atomic operations

Target: Use atomic operations. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```c
#include <stdio.h>
#include <stdatomic.h>

// atomic types (C11): lock-free ops
int main(void) {
    atomic_int counter = 0;
    atomic_fetch_add(&counter, 5);
    printf("%d\n", atomic_load(&counter));   // 5
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Advanced: Variadics, Threads, and Atomics"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Advanced: Variadics, Threads, and Atomics with analogies and real-world examples"
1. "Show me common mistakes beginners make with Advanced: Variadics, Threads, and Atomics"
1. "Provide advanced patterns and performance considerations for Advanced: Variadics, Threads, and Atomics"

## Key Takeaways

- Master the core ideas of Advanced: Variadics, Threads, and Atomics through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked cppreference docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
