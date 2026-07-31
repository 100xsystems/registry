---
{
  "title": "Bit Manipulation",
  "description": "Bitwise operators, bit flags, bit tricks, and bitfields.",
  "type": "lesson",
  "order": 13,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Apply bitwise AND/OR/XOR/NOT",
    "Use bit flags with masks",
    "Apply power-of-2 and counting tricks",
    "Extract and set individual bits"
  ],
  "knowledge_refs": [
    "c/c-13-bit-manipulation"
  ],
  "prerequisites": [
    "C-12"
  ],
  "references": [
    {
      "title": "cppreference — Bitwise Operators",
      "url": "https://en.cppreference.com/w/c/language/operator_arithmetic"
    },
    {
      "title": "learn-c.org — Bitwise Operators",
      "url": "https://learn-c.org/en/Bitwise_operators"
    },
    {
      "title": "Bit Twiddling Hacks",
      "url": "https://graphics.stanford.edu/~seander/bithacks.html"
    }
  ]
}
---

# C-13-BIT-MANIPULATION: Bit Manipulation

## Introduction

Bitwise operators, bit flags, bit tricks, and bitfields. By the end of this lesson you will be able to: Apply bitwise AND/OR/XOR/NOT; Use bit flags with masks; Apply power-of-2 and counting tricks; Extract and set individual bits.

## Key Concepts

### 1. Apply bitwise AND/OR/XOR/NOT

Target: Apply bitwise AND/OR/XOR/NOT. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```c
#include <stdio.h>

int main(void) {
    unsigned x = 0b1100;   // 12
    printf("%u\n", x & 0b1010);   // 8
    printf("%u\n", x | 0b0001);   // 13
    printf("%u\n", x ^ 0b1111);   // 3
    printf("%u\n", ~x);           // bitwise complement
    return 0;
}
```
### 2. Use bit flags with masks

Target: Use bit flags with masks. Apply the idiomatic pattern — this is how production C expresses this idea, so study the shape of the code.

```c
#include <stdio.h>

// bit flags: each bit is an independent on/off switch
#define FLAG_READ  (1 << 0)   // 0b0001
#define FLAG_WRITE (1 << 1)   // 0b0010
#define FLAG_EXEC  (1 << 2)   // 0b0100

int main(void) {
    unsigned perms = FLAG_READ | FLAG_WRITE;
    if (perms & FLAG_READ) printf("can read\n");
    if (perms & FLAG_EXEC) printf("can exec\n");
    perms |= FLAG_EXEC;              // add a flag
    perms &= ~FLAG_WRITE;            // remove a flag
    printf("exec now: %d\n", !!(perms & FLAG_EXEC));
    return 0;
}
```
### 3. Apply power-of-2 and counting tricks

Target: Apply power-of-2 and counting tricks. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```c
#include <stdio.h>

// power-of-2 checks and bit tricks
int is_pow2(unsigned x) { return x && !(x & (x - 1)); }
int count_ones(unsigned x) {
    int c = 0;
    while (x) { x &= (x - 1); c++; }   // Brian Kernighan's trick
    return c;
}

int main(void) {
    printf("%d %d\n", is_pow2(8), is_pow2(9));   // 1 0
    printf("%d\n", count_ones(0b101101));        // 4
    return 0;
}
```
### 4. Extract and set individual bits

Target: Extract and set individual bits. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```c
#include <stdio.h>

// extract and set bitfields
#define GET_BIT(x, n) (((x) >> (n)) & 1)
#define SET_BIT(x, n) ((x) | (1u << (n)))

int main(void) {
    unsigned x = 0b1010;
    printf("%d\n", GET_BIT(x, 1));   // 1
    printf("%u\n", SET_BIT(x, 4));   // 0b11110 = 30
    // bitfield struct members (implementation-defined packing)
    struct Flags { unsigned a : 1; unsigned b : 3; };
    struct Flags f = {1, 5};
    printf("%d %d\n", f.a, f.b);
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Bit Manipulation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Bit Manipulation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Bit Manipulation"
1. "Provide advanced patterns and performance considerations for Bit Manipulation"

## Key Takeaways

- Master the core ideas of Bit Manipulation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked cppreference docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
