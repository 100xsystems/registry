---
{
  "title": "Operators and Expressions",
  "description": "Arithmetic, comparison, logical, bitwise operators, and precedence.",
  "type": "lesson",
  "order": 3,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use arithmetic and comparison operators",
    "Understand short-circuit logical operators",
    "Use bitwise operators",
    "Master assignment and increment operators"
  ],
  "knowledge_refs": [
    "c/c-03-operators"
  ],
  "prerequisites": [
    "C-02"
  ],
  "references": [
    {
      "title": "cppreference — Operator Precedence",
      "url": "https://en.cppreference.com/w/c/language/operator_precedence"
    },
    {
      "title": "learn-c.org — Operators",
      "url": "https://learn-c.org/en/Operators"
    },
    {
      "title": "cppreference — Arithmetic Operators",
      "url": "https://en.cppreference.com/w/c/language/operator_arithmetic"
    }
  ]
}
---

# C-03-OPERATORS: Operators and Expressions

## Introduction

Arithmetic, comparison, logical, bitwise operators, and precedence. By the end of this lesson you will be able to: Use arithmetic and comparison operators; Understand short-circuit logical operators; Use bitwise operators; Master assignment and increment operators.

## Key Concepts

### 1. Use arithmetic and comparison operators

Target: Use arithmetic and comparison operators. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```c
#include <stdio.h>

int main(void) {
    int a = 17, b = 5;
    printf("%d %d %d %d %d\n", a + b, a - b, a * b, a / b, a % b);
    // 22 12 85 3 2 (integer division truncates toward zero)
    printf("%d\n", -17 / 5);  // -3 (C99 truncates toward zero)
    return 0;
}
```
### 2. Understand short-circuit logical operators

Target: Understand short-circuit logical operators. Apply the idiomatic pattern — this is how production C expresses this idea, so study the shape of the code.

```c
#include <stdio.h>

int main(void) {
    int a = 5, b = 3;
    printf("%d %d %d %d\n", a == b, a != b, a < b, a >= b);
    // logical && and || short-circuit: second operand may be skipped
    int x = 10;
    int zero = 0;
    if (zero != 0 && (x = a / b)) ;   // first operand false -> x NOT assigned
    printf("x unchanged: %d\n", x);   // 10 (short-circuit worked)
    if (b != 0 || (x = 99)) ;          // first operand true -> x NOT assigned
    printf("x still: %d\n", x);       // 10
    return 0;
}
```
### 3. Use bitwise operators

Target: Use bitwise operators. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```c
#include <stdio.h>

int main(void) {
    // bitwise operators
    unsigned a = 0b1100, b = 0b1010;  // 12, 10
    printf("%u %u %u\n", a & b, a | b, a ^ b);   // 8, 14, 6
    printf("%u %u\n", a << 1, a >> 1);           // 24, 6
    printf("%u\n", ~a);                          // bitwise NOT
    return 0;
}
```
### 4. Master assignment and increment operators

Target: Master assignment and increment operators. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```c
#include <stdio.h>

int main(void) {
    // assignment + compound assignment
    int x = 10;
    x += 5;        // x = 15
    x *= 2;        // x = 30
    // increment/decrement: prefix vs postfix
    int i = 5;
    int pre = ++i;    // i becomes 6, pre = 6
    int post = i++;   // post = 6, i becomes 7
    printf("%d %d %d\n", pre, post, i);
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Operators and Expressions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Operators and Expressions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Operators and Expressions"
1. "Provide advanced patterns and performance considerations for Operators and Expressions"

## Key Takeaways

- Master the core ideas of Operators and Expressions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked cppreference docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
