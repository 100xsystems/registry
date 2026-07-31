---
{
  "title": "Dynamic Memory",
  "description": "malloc, calloc, realloc, free, memory leaks, and heap patterns.",
  "type": "lesson",
  "order": 9,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Allocate with malloc and free",
    "Zero-init with calloc and resize with realloc",
    "Avoid leaks and double-free",
    "Return heap arrays from functions"
  ],
  "knowledge_refs": [
    "c/c-09-memory"
  ],
  "prerequisites": [
    "C-08"
  ],
  "references": [
    {
      "title": "learn-c.org — Dynamic Memory",
      "url": "https://learn-c.org/en/Dynamic_allocation"
    },
    {
      "title": "cppreference — malloc",
      "url": "https://en.cppreference.com/w/c/memory/malloc"
    },
    {
      "title": "cppreference — free",
      "url": "https://en.cppreference.com/w/c/memory/free"
    }
  ]
}
---

# C-09-MEMORY: Dynamic Memory

## Introduction

malloc, calloc, realloc, free, memory leaks, and heap patterns. By the end of this lesson you will be able to: Allocate with malloc and free; Zero-init with calloc and resize with realloc; Avoid leaks and double-free; Return heap arrays from functions.

## Key Concepts

### 1. Allocate with malloc and free

Target: Allocate with malloc and free. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *p = malloc(5 * sizeof(int));   // heap allocation
    if (!p) return 1;                   // check for NULL
    for (int i = 0; i < 5; i++) p[i] = i * i;
    printf("%d\n", p[3]);              // 9
    free(p);                            // MUST free
    return 0;
}
```
### 2. Zero-init with calloc and resize with realloc

Target: Zero-init with calloc and resize with realloc. Apply the idiomatic pattern — this is how production C expresses this idea, so study the shape of the code.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    // calloc: zero-initialized
    int *p = calloc(5, sizeof(int));
    if (!p) return 1;
    printf("%d\n", p[3]);              // 0
    // realloc: resize (may move the block)
    p = realloc(p, 10 * sizeof(int));
    if (!p) return 1;
    memset(p, 0, 10 * sizeof(int));
    printf("%d\n", p[9]);
    free(p);
    return 0;
}
```
### 3. Avoid leaks and double-free

Target: Avoid leaks and double-free. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    // memory leak: forgetting free
    // double free: freeing the same pointer twice (UB!)
    int *a = malloc(sizeof(int));
    int *b = a;             // both point to same block
    free(a);
    // free(b);             // double free — UB, crash
    printf("freed once\n");
    return 0;
}
```
### 4. Return heap arrays from functions

Target: Return heap arrays from functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```c
#include <stdio.h>
#include <stdlib.h>

// typical pattern: allocate and return a heap array
int *make_evens(int n) {
    int *arr = malloc(n * sizeof(int));
    if (!arr) return NULL;
    for (int i = 0; i < n; i++) arr[i] = i * 2;
    return arr;
}

int main(void) {
    int *evens = make_evens(4);
    for (int i = 0; i < 4; i++) printf("%d ", evens[i]);
    printf("\n");   // 0 2 4 6
    free(evens);
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Dynamic Memory"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Dynamic Memory with analogies and real-world examples"
1. "Show me common mistakes beginners make with Dynamic Memory"
1. "Provide advanced patterns and performance considerations for Dynamic Memory"

## Key Takeaways

- Master the core ideas of Dynamic Memory through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked cppreference docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
