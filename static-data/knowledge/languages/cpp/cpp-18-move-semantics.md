---
{
  "title": "Move Semantics and Rvalue References",
  "description": "std::move, rvalue references, perfect forwarding, move constructors.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Move objects with std::move",
    "Bind rvalue references",
    "Forward perfectly with std::forward",
    "Write move constructors"
  ],
  "knowledge_refs": [
    "cpp/cpp-18-move-semantics"
  ],
  "prerequisites": [
    "CPP-17"
  ],
  "references": [
    {
      "title": "learncpp — Move Semantics",
      "url": "https://www.learncpp.com/cpp-tutorial/move-semantics-and-stdmove/"
    },
    {
      "title": "cppreference — Rvalue References",
      "url": "https://en.cppreference.com/w/cpp/language/reference"
    },
    {
      "title": "cppreference — std::move",
      "url": "https://en.cppreference.com/w/cpp/utility/move"
    }
  ]
}
---

# CPP-18-MOVE-SEMANTICS: Move Semantics and Rvalue References

## Introduction

std::move, rvalue references, perfect forwarding, move constructors. By the end of this lesson you will be able to: Move objects with std::move; Bind rvalue references; Forward perfectly with std::forward; Write move constructors.

## Key Concepts

### 1. Move objects with std::move

Target: Move objects with std::move. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cpp
#include <iostream>
#include <utility>
#include <string>

int main() {
    std::string a = "hello";
    std::string b = std::move(a);   // steal buffer
    std::cout << b << "\n";        // hello
    std::cout << a.size() << "\n"; // 0 (moved-from: valid but empty)
    return 0;
}
```
### 2. Bind rvalue references

Target: Bind rvalue references. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cpp
#include <iostream>
#include <string>

// rvalue references &&: bind only to temporaries
void take(std::string &&s) {
    std::cout << "got: " << s << "\n";
}

int main() {
    take(std::string("temp"));   // binds to rvalue
    return 0;
}
```
### 3. Forward perfectly with std::forward

Target: Forward perfectly with std::forward. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cpp
#include <iostream>
#include <utility>
#include <vector>

// perfect forwarding with std::forward (C++11)
template <typename T, typename... Args>
T *make(Args &&... args) {
    return new T(std::forward<Args>(args)...);
}

int main() {
    auto p = make<std::vector<int>>(5, 42);   // 5 copies of 42
    std::cout << p->size() << " " << (*p)[0] << "\n";   // 5 42
    delete p;
    return 0;
}
```
### 4. Write move constructors

Target: Write move constructors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cpp
#include <iostream>
#include <vector>

class Big {
public:
    Big() { std::cout << "default\n"; }
    Big(const Big &) { std::cout << "copy\n"; }
    Big(Big &&) noexcept { std::cout << "move\n"; }
};

int main() {
    std::vector<Big> v;
    v.reserve(2);
    v.push_back(Big{});   // move, not copy
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Move Semantics and Rvalue References"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Move Semantics and Rvalue References with analogies and real-world examples"
1. "Show me common mistakes beginners make with Move Semantics and Rvalue References"
1. "Provide advanced patterns and performance considerations for Move Semantics and Rvalue References"

## Key Takeaways

- Master the core ideas of Move Semantics and Rvalue References through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
