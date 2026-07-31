---
{
  "title": "Modern C++: C++17/20 Features",
  "description": "constexpr, structured bindings, variant, optional, modern idioms.",
  "type": "lesson",
  "order": 21,
  "duration": "75 min",
  "difficulty": "expert",
  "learning_objectives": [
    "Use constexpr functions",
    "Use structured bindings",
    "Use std::variant and std::optional",
    "Apply modern C++ idioms"
  ],
  "knowledge_refs": [
    "cpp/cpp-21-modern"
  ],
  "prerequisites": [
    "CPP-20"
  ],
  "references": [
    {
      "title": "cppreference — C++20 Features",
      "url": "https://en.cppreference.com/w/cpp/20"
    },
    {
      "title": "cppreference — C++17 Features",
      "url": "https://en.cppreference.com/w/cpp/17"
    },
    {
      "title": "cppreference — std::variant",
      "url": "https://en.cppreference.com/w/cpp/utility/variant"
    }
  ]
}
---

# CPP-21-MODERN: Modern C++: C++17/20 Features

## Introduction

constexpr, structured bindings, variant, optional, modern idioms. By the end of this lesson you will be able to: Use constexpr functions; Use structured bindings; Use std::variant and std::optional; Apply modern C++ idioms.

## Key Concepts

### 1. Use constexpr functions

Target: Use constexpr functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cpp
#include <iostream>

// constexpr: evaluated at compile time
constexpr int square(int x) { return x * x; }

int main() {
    constexpr int val = square(5);   // computed at compile time
    std::cout << val << "\n";   // 25
    return 0;
}
```
### 2. Use structured bindings

Target: Use structured bindings. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cpp
#include <iostream>
#include <string>

int main() {
    std::string s = "hello";
    auto [first, last] = std::pair<int, std::string>{1, "one"};  // structured binding
    std::cout << first << " " << last << "\n";   // 1 one
    return 0;
}
```
### 3. Use std::variant and std::optional

Target: Use std::variant and std::optional. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cpp
#include <iostream>
#include <variant>
#include <string>

int main() {
    // C++17 std::variant: type-safe union
    std::variant<int, std::string> v = 42;
    std::cout << std::get<int>(v) << "\n";
    v = "now a string";
    std::cout << std::get<std::string>(v) << "\n";
    return 0;
}
```
### 4. Apply modern C++ idioms

Target: Apply modern C++ idioms. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cpp
#include <iostream>
#include <optional>
#include <string>

int main() {
    // C++17 std::optional: value or nothing
    std::optional<std::string> maybe = "present";
    if (maybe) std::cout << *maybe << "\n";
    std::cout << maybe.value_or("fallback") << "\n";
    std::optional<int> none;
    std::cout << none.value_or(-1) << "\n";   // -1
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Modern C++: C++17/20 Features"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Modern C++: C++17/20 Features with analogies and real-world examples"
1. "Show me common mistakes beginners make with Modern C++: C++17/20 Features"
1. "Provide advanced patterns and performance considerations for Modern C++: C++17/20 Features"

## Key Takeaways

- Master the core ideas of Modern C++: C++17/20 Features through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
