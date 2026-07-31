---
{
  "title": "Preprocessor and Macros",
  "description": "#define, function-like macros, include guards, conditional compilation.",
  "type": "lesson",
  "order": 10,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define object-like macros",
    "Write function-like macros safely",
    "Use include guards",
    "Compile conditionally with #ifdef"
  ],
  "knowledge_refs": [
    "c/c-10-preprocessor"
  ],
  "prerequisites": [
    "C-09"
  ],
  "references": [
    {
      "title": "cppreference — Preprocessor",
      "url": "https://en.cppreference.com/w/c/preprocessor"
    },
    {
      "title": "learn-c.org — Preprocessor",
      "url": "https://learn-c.org/en/Preprocessor"
    },
    {
      "title": "cppreference — Conditional Inclusion",
      "url": "https://en.cppreference.com/w/c/preprocessor/conditional"
    }
  ]
}
---

# C-10-PREPROCESSOR: Preprocessor and Macros

## Introduction

#define, function-like macros, include guards, conditional compilation. By the end of this lesson you will be able to: Define object-like macros; Write function-like macros safely; Use include guards; Compile conditionally with #ifdef.

## Key Concepts

### 1. Define object-like macros

Target: Define object-like macros. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```c
#include <stdio.h>

#define PI 3.14159
#define SQUARE(x) ((x) * (x))

int main(void) {
    printf("%.5f\n", PI);
    printf("%d\n", SQUARE(5));      // 25
    printf("%d\n", SQUARE(1 + 1));  // 4 (parentheses matter!)
    return 0;
}
```
### 2. Write function-like macros safely

Target: Write function-like macros safely. Apply the idiomatic pattern — this is how production C expresses this idea, so study the shape of the code.

```c
#include <stdio.h>

// include guards prevent multiple inclusion
#ifndef MY_HEADER_H
#define MY_HEADER_H
int helper(void) { return 42; }
#endif

int main(void) {
    printf("%d\n", helper());
    return 0;
}
```
### 3. Use include guards

Target: Use include guards. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```c
#include <stdio.h>

// conditional compilation
#ifdef DEBUG
#define LOG(msg) printf("[DEBUG] %s\n", msg)
#else
#define LOG(msg)
#endif

int main(void) {
    LOG("build with -DDEBUG to see this");
    printf("done\n");
    return 0;
}
```
### 4. Compile conditionally with #ifdef

Target: Compile conditionally with #ifdef. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```c
#include <stdio.h>

// stringification and token pasting
#define STR(x) #x
#define CAT(a, b) a##b

int main(void) {
    printf("%s\n", STR(hello));     // "hello"
    int CAT(my, var) = 7;            // int myvar = 7;
    printf("%d\n", myvar);
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Preprocessor and Macros"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Preprocessor and Macros with analogies and real-world examples"
1. "Show me common mistakes beginners make with Preprocessor and Macros"
1. "Provide advanced patterns and performance considerations for Preprocessor and Macros"

## Key Takeaways

- Master the core ideas of Preprocessor and Macros through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked cppreference docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
