---
{
  "title": "Function Pointers and Callbacks",
  "description": "Function pointer syntax, callbacks, qsort comparators, dispatch tables.",
  "type": "lesson",
  "order": 14,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Declare and call function pointers",
    "Pass callbacks as arguments",
    "Write qsort comparators",
    "Build dispatch tables"
  ],
  "knowledge_refs": [
    "c/c-14-function-pointers"
  ],
  "prerequisites": [
    "C-13"
  ],
  "references": [
    {
      "title": "learn-c.org — Function Pointers",
      "url": "https://learn-c.org/en/Function_Pointers"
    },
    {
      "title": "cppreference — qsort",
      "url": "https://en.cppreference.com/w/c/algorithm/qsort"
    },
    {
      "title": "Beej’s Guide — Function Pointers",
      "url": "https://beej.us/guide/bgc/html/split/pointers-part-ii.html"
    }
  ]
}
---

# C-14-FUNCTION-POINTERS: Function Pointers and Callbacks

## Introduction

Function pointer syntax, callbacks, qsort comparators, dispatch tables. By the end of this lesson you will be able to: Declare and call function pointers; Pass callbacks as arguments; Write qsort comparators; Build dispatch tables.

## Key Concepts

### 1. Declare and call function pointers

Target: Declare and call function pointers. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```c
#include <stdio.h>

int add(int a, int b) { return a + b; }
int mul(int a, int b) { return a * b; }

int main(void) {
    int (*op)(int, int) = add;    // function pointer
    printf("%d\n", op(2, 3));     // 5
    op = mul;
    printf("%d\n", op(2, 3));     // 6
    return 0;
}
```
### 2. Pass callbacks as arguments

Target: Pass callbacks as arguments. Apply the idiomatic pattern — this is how production C expresses this idea, so study the shape of the code.

```c
#include <stdio.h>

// function pointers as arguments (callbacks)
int apply(int (*f)(int), int x) { return f(x); }
int square(int x) { return x * x; }
int cube(int x) { return x * x * x; }

int main(void) {
    printf("%d %d\n", apply(square, 4), apply(cube, 3));
    return 0;
}
```
### 3. Write qsort comparators

Target: Write qsort comparators. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```c
#include <stdio.h>
#include <stdlib.h>

// qsort takes a comparator callback
int cmp(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

int main(void) {
    int nums[] = {5, 2, 8, 1};
    qsort(nums, 4, sizeof(int), cmp);
    for (int i = 0; i < 4; i++) printf("%d ", nums[i]);
    printf("\n");   // 1 2 5 8
    return 0;
}
```
### 4. Build dispatch tables

Target: Build dispatch tables. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```c
#include <stdio.h>

// table of function pointers: dispatch pattern
int add(int a, int b) { return a + b; }
int sub(int a, int b) { return a - b; }
int mul(int a, int b) { return a * b; }

int main(void) {
    int (*ops[])(int, int) = {add, sub, mul};
    for (int i = 0; i < 3; i++) printf("%d ", ops[i](10, 3));
    printf("\n");   // 13 7 30
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Function Pointers and Callbacks"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Function Pointers and Callbacks with analogies and real-world examples"
1. "Show me common mistakes beginners make with Function Pointers and Callbacks"
1. "Provide advanced patterns and performance considerations for Function Pointers and Callbacks"

## Key Takeaways

- Master the core ideas of Function Pointers and Callbacks through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked cppreference docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
