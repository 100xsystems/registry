---
{
  "title": "Variables and Fundamental Types",
  "description": "Fundamental types, const/constexpr, auto deduction, fixed-width integers.",
  "type": "lesson",
  "order": 2,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use fundamental numeric and boolean types",
    "Use const and constexpr",
    "Deduce types with auto",
    "Use fixed-width integers"
  ],
  "knowledge_refs": [
    "cpp/cpp-02-variables-types"
  ],
  "prerequisites": [
    "CPP-01"
  ],
  "references": [
    {
      "title": "learncpp — Fundamental Data Types",
      "url": "https://www.learncpp.com/cpp-tutorial/fundamental-data-types/"
    },
    {
      "title": "cppreference — Fundamental Types",
      "url": "https://en.cppreference.com/w/cpp/language/types"
    },
    {
      "title": "cppreference — constexpr",
      "url": "https://en.cppreference.com/w/cpp/language/constexpr"
    }
  ]
}
---

# CPP-02-VARIABLES-TYPES: Variables and Fundamental Types

## Introduction

Fundamental types, const/constexpr, auto deduction, fixed-width integers. By the end of this lesson you will be able to: Use fundamental numeric and boolean types; Use const and constexpr; Deduce types with auto; Use fixed-width integers.

## Key Concepts

### 1. Use fundamental numeric and boolean types

Target: Use fundamental numeric and boolean types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cpp
#include <iostream>

int main() {
    int i = 42;
    unsigned u = 42u;
    long long ll = 42LL;
    float f = 3.14f;
    double d = 3.14;
    bool b = true;
    char c = 'A';
    std::cout << i << " " << u << " " << ll << " " << f << " " << d << " " << b << " " << c << "\n";
    std::cout << "sizeof(int)=" << sizeof(int) << " sizeof(double)=" << sizeof(double) << "\n";
    return 0;
}
```
### 2. Use const and constexpr

Target: Use const and constexpr. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cpp
#include <iostream>

int main() {
    // const: value never changes; constexpr: compile-time constant
    const int days = 7;
    constexpr double pi = 3.14159265;
    std::cout << days << " " << pi << "\n";
    return 0;
}
```
### 3. Deduce types with auto

Target: Deduce types with auto. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cpp
#include <iostream>

int main() {
    // auto deduces the type
    auto x = 42;          // int
    auto y = 3.14;        // double
    auto s = "hello";     // const char*
    std::cout << x << " " << y << " " << s << "\n";
    return 0;
}
```
### 4. Use fixed-width integers

Target: Use fixed-width integers. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cpp
#include <iostream>
#include <cstdint>

int main() {
    // fixed-width integer types
    std::int32_t a = -100;
    std::uint64_t b = 100ULL;
    std::cout << a << " " << b << "\n";
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Variables and Fundamental Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables and Fundamental Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables and Fundamental Types"
1. "Provide advanced patterns and performance considerations for Variables and Fundamental Types"

## Key Takeaways

- Master the core ideas of Variables and Fundamental Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
