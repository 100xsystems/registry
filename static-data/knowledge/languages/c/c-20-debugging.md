---
{
  "title": "Undefined Behavior and Debugging",
  "description": "OOB access, signed overflow, use-after-free, volatile, restrict, sanitizers.",
  "type": "lesson",
  "order": 20,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Recognize out-of-bounds undefined behavior",
    "Understand signed overflow UB",
    "Avoid use-after-free",
    "Use volatile, restrict, and sanitizers"
  ],
  "knowledge_refs": [
    "c/c-20-debugging"
  ],
  "prerequisites": [
    "C-19"
  ],
  "references": [
    {
      "title": "cppreference — Undefined Behavior",
      "url": "https://en.cppreference.com/w/c/language/behavior"
    },
    {
      "title": "gcc -fsanitize docs",
      "url": "https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html"
    },
    {
      "title": "Valgrind Manual",
      "url": "https://valgrind.org/docs/manual/mc-manual.html"
    }
  ]
}
---

# C-20-DEBUGGING: Undefined Behavior and Debugging

## Introduction

OOB access, signed overflow, use-after-free, volatile, restrict, sanitizers. By the end of this lesson you will be able to: Recognize out-of-bounds undefined behavior; Understand signed overflow UB; Avoid use-after-free; Use volatile, restrict, and sanitizers.

## Key Concepts

### 1. Recognize out-of-bounds undefined behavior

Target: Recognize out-of-bounds undefined behavior. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```c
#include <stdio.h>

int main(void) {
    // out-of-bounds read — undefined behavior
    int arr[3] = {1, 2, 3};
    printf("%d\n", arr[5]);   // UB! reads past the array
    return 0;
}
```
### 2. Understand signed overflow UB

Target: Understand signed overflow UB. Apply the idiomatic pattern — this is how production C expresses this idea, so study the shape of the code.

```c
#include <stdio.h>

int main(void) {
    // signed overflow is UB
    int x = 2147483647;
    int y = x + 1;            // UB (compile with -fsanitize=signed-integer-overflow)
    printf("%d\n", y);
    return 0;
}
```
### 3. Avoid use-after-free

Target: Avoid use-after-free. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    // use-after-free — UB
    int *p = malloc(sizeof(int));
    *p = 42;
    free(p);
    printf("%d\n", *p);      // UB! reading freed memory
    return 0;
}
// detect with: valgrind ./app  or  -fsanitize=address
```
### 4. Use volatile, restrict, and sanitizers

Target: Use volatile, restrict, and sanitizers. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```c
#include <stdio.h>

// volatile: tells the compiler the value may change externally
volatile int flag = 0;

// restrict: no aliasing promise (optimizer aid)
void scale(int *restrict dst, const int *restrict src, int n, int k) {
    for (int i = 0; i < n; i++) dst[i] = src[i] * k;
}

int main(void) {
    int a[3] = {1, 2, 3}, b[3];
    scale(b, a, 3, 10);
    printf("%d %d %d\n", b[0], b[1], b[2]);
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Undefined Behavior and Debugging"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Undefined Behavior and Debugging with analogies and real-world examples"
1. "Show me common mistakes beginners make with Undefined Behavior and Debugging"
1. "Provide advanced patterns and performance considerations for Undefined Behavior and Debugging"

## Key Takeaways

- Master the core ideas of Undefined Behavior and Debugging through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked cppreference docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
