---
{
  "title": "Functions and Prototypes",
  "description": "Function declarations, pass-by-value, pass-by-pointer, and recursion.",
  "type": "lesson",
  "order": 5,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare functions with prototypes",
    "Understand pass-by-value semantics",
    "Pass pointers to mutate caller state",
    "Write recursive functions"
  ],
  "knowledge_refs": [
    "c/c-05-functions"
  ],
  "prerequisites": [
    "C-04"
  ],
  "references": [
    {
      "title": "learn-c.org — Functions",
      "url": "https://learn-c.org/en/Functions"
    },
    {
      "title": "cppreference — Function Declarations",
      "url": "https://en.cppreference.com/w/c/language/functions"
    },
    {
      "title": "Beej’s Guide — Functions",
      "url": "https://beej.us/guide/bgc/html/split/function-basics.html"
    }
  ]
}
---

# C-05-FUNCTIONS: Functions and Prototypes

## Introduction

Function declarations, pass-by-value, pass-by-pointer, and recursion. By the end of this lesson you will be able to: Declare functions with prototypes; Understand pass-by-value semantics; Pass pointers to mutate caller state; Write recursive functions.

## Key Concepts

### 1. Declare functions with prototypes

Target: Declare functions with prototypes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```c
#include <stdio.h>

// function prototype (declaration)
int add(int a, int b);

int main(void) {
    printf("%d\n", add(2, 3));
    return 0;
}

// function definition
int add(int a, int b) { return a + b; }
```
### 2. Understand pass-by-value semantics

Target: Understand pass-by-value semantics. Apply the idiomatic pattern — this is how production C expresses this idea, so study the shape of the code.

```c
#include <stdio.h>

// pass-by-value: modifications do NOT affect the caller
void try_swap(int a, int b) {
    int t = a; a = b; b = t;
}

int main(void) {
    int x = 1, y = 2;
    try_swap(x, y);
    printf("%d %d\n", x, y);   // 1 2 (unchanged)
    return 0;
}
```
### 3. Pass pointers to mutate caller state

Target: Pass pointers to mutate caller state. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```c
#include <stdio.h>

// pass-by-pointer: modifications DO affect the caller
void swap(int *a, int *b) {
    int t = *a; *a = *b; *b = t;
}

int main(void) {
    int x = 1, y = 2;
    swap(&x, &y);
    printf("%d %d\n", x, y);   // 2 1
    return 0;
}
```
### 4. Write recursive functions

Target: Write recursive functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```c
#include <stdio.h>

// recursion: function calls itself
long fact(int n) {
    if (n <= 1) return 1;
    return n * fact(n - 1);
}

int main(void) {
    printf("%ld\n", fact(6));  // 720
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Functions and Prototypes"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions and Prototypes with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions and Prototypes"
1. "Provide advanced patterns and performance considerations for Functions and Prototypes"

## Key Takeaways

- Master the core ideas of Functions and Prototypes through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked cppreference docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
