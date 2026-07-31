---
{
  "title": "Variables and Data Types",
  "description": "Integral and floating types, fixed-width types, sizeof, and enumeration.",
  "type": "lesson",
  "order": 2,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use int, unsigned, float, double, char, _Bool",
    "Use fixed-width types from stdint.h",
    "Understand signed vs unsigned overflow",
    "Use enum and limits.h constants"
  ],
  "knowledge_refs": [
    "c/c-02-variables-types"
  ],
  "prerequisites": [
    "C-01"
  ],
  "references": [
    {
      "title": "cppreference — Fundamental Types",
      "url": "https://en.cppreference.com/w/c/language/type"
    },
    {
      "title": "learn-c.org — Variables and Types",
      "url": "https://learn-c.org/en/Variables_and_Types"
    },
    {
      "title": "cppreference — Integer Types",
      "url": "https://en.cppreference.com/w/c/language/arithmetic_types"
    }
  ]
}
---

# C-02-VARIABLES-TYPES: Variables and Data Types

## Introduction

Integral and floating types, fixed-width types, sizeof, and enumeration. By the end of this lesson you will be able to: Use int, unsigned, float, double, char, _Bool; Use fixed-width types from stdint.h; Understand signed vs unsigned overflow; Use enum and limits.h constants.

## Key Concepts

### 1. Use int, unsigned, float, double, char, _Bool

Target: Use int, unsigned, float, double, char, _Bool. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```c
#include <stdio.h>

int main(void) {
    int i = 42;              // signed integer (usually 32-bit)
    unsigned u = 42u;        // unsigned
    long l = 42L;            // at least 32-bit, often 64
    float f = 3.14f;         // single precision
    double d = 3.14;         // double precision
    char c = 'A';            // single byte
    _Bool b = 1;             // boolean
    printf("%d %u %ld %.2f %.2f %c %d\n", i, u, l, f, d, c, b);
    return 0;
}
```
### 2. Use fixed-width types from stdint.h

Target: Use fixed-width types from stdint.h. Apply the idiomatic pattern — this is how production C expresses this idea, so study the shape of the code.

```c
#include <stdio.h>
#include <inttypes.h>   // PRId32 / PRIu64 macros (includes stdint.h)

int main(void) {
    // fixed-width types
    int32_t x = -100;         // exactly 32 bits
    uint64_t y = 100ULL;      // exactly 64 bits
    printf("%" PRId32 " %" PRIu64 "\n", x, y);
    // sizeof returns bytes
    printf("int=%zu char=%zu ptr=%zu\n", sizeof(int), sizeof(char), sizeof(void *));
    return 0;
}
```
### 3. Understand signed vs unsigned overflow

Target: Understand signed vs unsigned overflow. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```c
#include <stdio.h>

int main(void) {
    // signed vs unsigned overflow behavior
    int s = 2147483647;
    unsigned u = 4294967295U;
    printf("s+1 = %d\n", s + 1);   // UB: signed overflow
    printf("u+1 = %u\n", u + 1);   // defined: wraps to 0
    return 0;
}
```
### 4. Use enum and limits.h constants

Target: Use enum and limits.h constants. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```c
#include <stdio.h>
#include <limits.h>

int main(void) {
    printf("INT_MAX=%d INT_MIN=%d\n", INT_MAX, INT_MIN);
    printf("CHAR_BIT=%d\n", CHAR_BIT);
    // enumerations: named integer constants
    enum Color { RED, GREEN, BLUE };
    enum Color c = GREEN;
    printf("%d\n", c);   // 1
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Variables and Data Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables and Data Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables and Data Types"
1. "Provide advanced patterns and performance considerations for Variables and Data Types"

## Key Takeaways

- Master the core ideas of Variables and Data Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked cppreference docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
