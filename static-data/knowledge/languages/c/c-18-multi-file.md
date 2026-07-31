---
{
  "title": "Multi-file Projects and Headers",
  "description": "Header files, include guards, separate compilation, static linkage.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Split code into .h and .c files",
    "Write include guards",
    "Compile multiple translation units",
    "Use static for internal linkage"
  ],
  "knowledge_refs": [
    "c/c-18-multi-file"
  ],
  "prerequisites": [
    "C-17"
  ],
  "references": [
    {
      "title": "cppreference — Source Files",
      "url": "https://en.cppreference.com/w/c/language/translation_phases"
    },
    {
      "title": "Beej’s Guide — Multi-file",
      "url": "https://beej.us/guide/bgc/html/split/header-files.html"
    },
    {
      "title": "learn-c.org — Header Files",
      "url": "https://learn-c.org/en/Header_Files"
    }
  ]
}
---

# C-18-MULTI-FILE: Multi-file Projects and Headers

## Introduction

Header files, include guards, separate compilation, static linkage. By the end of this lesson you will be able to: Split code into .h and .c files; Write include guards; Compile multiple translation units; Use static for internal linkage.

## Key Concepts

### 1. Split code into .h and .c files

Target: Split code into .h and .c files. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```c
// point.h — declaration (interface)
#ifndef POINT_H
#define POINT_H
struct Point { int x; int y; };
int dist2(struct Point *p);
#endif
```
### 2. Write include guards

Target: Write include guards. Apply the idiomatic pattern — this is how production C expresses this idea, so study the shape of the code.

```c
// point.c — implementation
#include "point.h"
int dist2(struct Point *p) { return p->x * p->x + p->y * p->y; }
```
### 3. Compile multiple translation units

Target: Compile multiple translation units. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```c
// main.c — includes the header
#include <stdio.h>
#include "point.h"
int main(void) {
    struct Point p = {3, 4};
    printf("%d\n", dist2(&p));   // 25
    return 0;
}
// compile: gcc main.c point.c -o app
```
### 4. Use static for internal linkage

Target: Use static for internal linkage. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```c
#include <stdio.h>

// static: internal linkage — visible only in this file
static int counter = 0;
static void bump(void) { counter++; }

int main(void) {
    bump(); bump();
    printf("%d\n", counter);   // 2
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Multi-file Projects and Headers"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Multi-file Projects and Headers with analogies and real-world examples"
1. "Show me common mistakes beginners make with Multi-file Projects and Headers"
1. "Provide advanced patterns and performance considerations for Multi-file Projects and Headers"

## Key Takeaways

- Master the core ideas of Multi-file Projects and Headers through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked cppreference docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
