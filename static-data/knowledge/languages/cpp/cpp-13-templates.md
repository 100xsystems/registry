---
{
  "title": "Templates",
  "description": "Function templates, class templates, concepts, variadic templates.",
  "type": "lesson",
  "order": 13,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write function templates",
    "Write class templates",
    "Constrain templates with concepts (C++20)",
    "Write variadic templates"
  ],
  "knowledge_refs": [
    "cpp/cpp-13-templates"
  ],
  "prerequisites": [
    "CPP-12"
  ],
  "references": [
    {
      "title": "learncpp — Templates",
      "url": "https://www.learncpp.com/cpp-tutorial/function-templates/"
    },
    {
      "title": "cppreference — Templates",
      "url": "https://en.cppreference.com/w/cpp/language/templates"
    },
    {
      "title": "cppreference — Concepts",
      "url": "https://en.cppreference.com/w/cpp/language/constraints"
    }
  ]
}
---

# CPP-13-TEMPLATES: Templates

## Introduction

Function templates, class templates, concepts, variadic templates. By the end of this lesson you will be able to: Write function templates; Write class templates; Constrain templates with concepts (C++20); Write variadic templates.

## Key Concepts

### 1. Write function templates

Target: Write function templates. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cpp
#include <iostream>

template <typename T>
T max_of(T a, T b) { return a > b ? a : b; }

int main() {
    std::cout << max_of(3, 7) << " " << max_of(2.5, 1.5) << "\n";
    return 0;
}
```
### 2. Write class templates

Target: Write class templates. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cpp
#include <iostream>

template <typename T>
class Box {
public:
    Box(T value) : value_(value) {}
    T get() const { return value_; }
private:
    T value_;
};

int main() {
    Box<int> ib(42);
    Box<std::string> sb("hello");
    std::cout << ib.get() << " " << sb.get() << "\n";
    return 0;
}
```
### 3. Constrain templates with concepts (C++20)

Target: Constrain templates with concepts (C++20). Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cpp
#include <iostream>
#include <concepts>

// C++20 concepts: constrained templates
template <typename T>
requires std::integral<T>
T square(T x) { return x * x; }

int main() {
    std::cout << square(5) << "\n";
    return 0;
}
```
### 4. Write variadic templates

Target: Write variadic templates. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cpp
#include <iostream>

// variadic templates (C++11)
template <typename T>
T sum(T v) { return v; }

template <typename T, typename... Rest>
T sum(T first, Rest... rest) { return first + sum(rest...); }

int main() {
    std::cout << sum(1, 2, 3, 4) << "\n";   // 10
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Templates"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Templates with analogies and real-world examples"
1. "Show me common mistakes beginners make with Templates"
1. "Provide advanced patterns and performance considerations for Templates"

## Key Takeaways

- Master the core ideas of Templates through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
