---
{
  "title": "Pointers",
  "description": "Address-of, dereference, pointer arithmetic, pointer-to-pointer, void*.",
  "type": "lesson",
  "order": 7,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Take addresses and dereference pointers",
    "Do pointer arithmetic with arrays",
    "Use pointer-to-pointer",
    "Work with NULL and void*"
  ],
  "knowledge_refs": [
    "c/c-07-pointers"
  ],
  "prerequisites": [
    "C-06"
  ],
  "references": [
    {
      "title": "learn-c.org — Pointers",
      "url": "https://learn-c.org/en/Pointers"
    },
    {
      "title": "cppreference — Pointer Declarations",
      "url": "https://en.cppreference.com/w/c/language/pointer"
    },
    {
      "title": "Beej’s Guide — Pointers",
      "url": "https://beej.us/guide/bgc/html/split/pointers.html"
    }
  ]
}
---

# C-07-POINTERS: Pointers

## Introduction

Address-of, dereference, pointer arithmetic, pointer-to-pointer, void*. By the end of this lesson you will be able to: Take addresses and dereference pointers; Do pointer arithmetic with arrays; Use pointer-to-pointer; Work with NULL and void*.

## Key Concepts

### 1. Take addresses and dereference pointers

Target: Take addresses and dereference pointers. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```c
#include <stdio.h>

int main(void) {
    int x = 42;
    int *p = &x;             // p holds the address of x
    printf("x=%d *p=%d\n", x, *p);   // 42 42 (dereference)
    *p = 100;                // write through the pointer
    printf("x=%d\n", x);    // 100
    return 0;
}
```
### 2. Do pointer arithmetic with arrays

Target: Do pointer arithmetic with arrays. Apply the idiomatic pattern — this is how production C expresses this idea, so study the shape of the code.

```c
#include <stdio.h>

int main(void) {
    int nums[4] = {10, 20, 30, 40};
    int *p = nums;           // array decays to pointer
    printf("%d %d\n", *p, *(p + 1));   // 10 20 (pointer arithmetic)
    printf("%d %d\n", p[0], p[2]);     // indexing through pointer
    p++;                     // move to next element
    printf("%d\n", *p);     // 20
    return 0;
}
```
### 3. Use pointer-to-pointer

Target: Use pointer-to-pointer. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```c
#include <stdio.h>

int main(void) {
    int x = 42;
    int *p = &x;
    int **pp = &p;           // pointer-to-pointer
    printf("%d %d %d\n", x, *p, **pp);   // 42 42 42
    **pp = 99;
    printf("%d\n", x);      // 99
    return 0;
}
```
### 4. Work with NULL and void*

Target: Work with NULL and void*. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```c
#include <stdio.h>

int main(void) {
    // null pointer checks
    int *p = NULL;
    if (p) printf("valid\n");
    else printf("null\n");
    // void *: generic pointer, must cast to use
    int x = 7;
    void *v = &x;
    int *back = (int *)v;
    printf("%d\n", *back);  // 7
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Pointers"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Pointers with analogies and real-world examples"
1. "Show me common mistakes beginners make with Pointers"
1. "Provide advanced patterns and performance considerations for Pointers"

## Key Takeaways

- Master the core ideas of Pointers through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked cppreference docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
