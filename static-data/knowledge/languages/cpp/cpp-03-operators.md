---
{
  "title": "Operators and Expressions",
  "description": "Arithmetic, comparison, logical, bitwise operators, precedence.",
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
    "cpp/cpp-03-operators"
  ],
  "prerequisites": [
    "CPP-02"
  ],
  "references": [
    {
      "title": "learncpp — Operators",
      "url": "https://www.learncpp.com/cpp-tutorial/introduction-to-operators/"
    },
    {
      "title": "cppreference — Operator Precedence",
      "url": "https://en.cppreference.com/w/cpp/language/operator_precedence"
    },
    {
      "title": "cppreference — Arithmetic Operators",
      "url": "https://en.cppreference.com/w/cpp/language/operator_arithmetic"
    }
  ]
}
---

# CPP-03-OPERATORS: Operators and Expressions

## Introduction

Arithmetic, comparison, logical, bitwise operators, precedence. By the end of this lesson you will be able to: Use arithmetic and comparison operators; Understand short-circuit logical operators; Use bitwise operators; Master assignment and increment operators.

## Key Concepts

### 1. Use arithmetic and comparison operators

Target: Use arithmetic and comparison operators. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cpp
#include <iostream>

int main() {
    int a = 17, b = 5;
    std::cout << a + b << " " << a - b << " " << a * b << " " << a / b << " " << a % b << "\n";
    // 22 12 85 3 2
    std::cout << 17.0 / 5.0 << "\n";   // 3.4 (float division)
    return 0;
}
```
### 2. Understand short-circuit logical operators

Target: Understand short-circuit logical operators. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cpp
#include <iostream>

int main() {
    int a = 5, b = 3;
    std::cout << (a == b) << (a != b) << (a < b) << (a >= b) << "\n";
    bool both = a > 0 && b > 0;
    bool either = a > 100 || b > 0;
    std::cout << both << " " << either << "\n";
    return 0;
}
```
### 3. Use bitwise operators

Target: Use bitwise operators. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cpp
#include <iostream>

int main() {
    unsigned a = 0b1100, b = 0b1010;
    std::cout << (a & b) << " " << (a | b) << " " << (a ^ b) << "\n";  // 8 14 6
    std::cout << (a << 1) << " " << (a >> 1) << "\n";                  // 24 6
    return 0;
}
```
### 4. Master assignment and increment operators

Target: Master assignment and increment operators. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cpp
#include <iostream>

int main() {
    int x = 10;
    x += 5;   // 15
    x *= 2;   // 30
    std::cout << x << "\n";
    int i = 5;
    ++i;
    std::cout << i << " ";   // 6 (prefix)
    std::cout << i++ << " ";   // 6 (postfix: returns old value)
    std::cout << i << "\n";   // 7 (i already incremented)
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
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
