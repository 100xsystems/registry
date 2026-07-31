---
{
  "title": "Exception Handling and RAII",
  "description": "try/catch, throwing, custom exceptions, RAII cleanup.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Throw and catch exceptions",
    "Write exception-safe code",
    "Use RAII for resource cleanup",
    "Define custom exception types"
  ],
  "knowledge_refs": [
    "cpp/cpp-17-exceptions"
  ],
  "prerequisites": [
    "CPP-16"
  ],
  "references": [
    {
      "title": "learncpp — Exceptions",
      "url": "https://www.learncpp.com/cpp-tutorial/introduction-to-exceptions/"
    },
    {
      "title": "cppreference — Exceptions",
      "url": "https://en.cppreference.com/w/cpp/language/exceptions"
    },
    {
      "title": "cppreference — try/catch",
      "url": "https://en.cppreference.com/w/cpp/language/try_catch"
    }
  ]
}
---

# CPP-17-EXCEPTIONS: Exception Handling and RAII

## Introduction

try/catch, throwing, custom exceptions, RAII cleanup. By the end of this lesson you will be able to: Throw and catch exceptions; Write exception-safe code; Use RAII for resource cleanup; Define custom exception types.

## Key Concepts

### 1. Throw and catch exceptions

Target: Throw and catch exceptions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cpp
#include <iostream>
#include <stdexcept>

int main() {
    try {
        throw std::runtime_error("something failed");
    } catch (const std::runtime_error &e) {
        std::cout << "caught: " << e.what() << "\n";
    }
    return 0;
}
```
### 2. Write exception-safe code

Target: Write exception-safe code. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cpp
#include <iostream>
#include <stdexcept>

int divide(int a, int b) {
    if (b == 0) throw std::invalid_argument("division by zero");
    return a / b;
}

int main() {
    try {
        divide(10, 0);
    } catch (const std::invalid_argument &e) {
        std::cout << e.what() << "\n";
    }
    return 0;
}
```
### 3. Use RAII for resource cleanup

Target: Use RAII for resource cleanup. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cpp
#include <iostream>
#include <fstream>
#include <string>

// RAII + exceptions: file closes automatically
void write_file(const std::string &path) {
    std::ofstream out(path);
    if (!out) throw std::runtime_error("cannot open " + path);
    out << "hello\n";
}   // out destructor runs here, file closed

int main() {
    try { write_file("/tmp/out.txt"); }
    catch (const std::exception &e) { std::cout << e.what() << "\n"; }
    std::cout << "done\n";
    return 0;
}
```
### 4. Define custom exception types

Target: Define custom exception types. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cpp
#include <iostream>
#include <stdexcept>

// custom exception types
class ValidationError : public std::runtime_error {
public:
    explicit ValidationError(const std::string &field)
        : std::runtime_error("invalid field: " + field) {}
};

int main() {
    try { throw ValidationError("email"); }
    catch (const ValidationError &e) { std::cout << e.what() << "\n"; }
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Exception Handling and RAII"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Exception Handling and RAII with analogies and real-world examples"
1. "Show me common mistakes beginners make with Exception Handling and RAII"
1. "Provide advanced patterns and performance considerations for Exception Handling and RAII"

## Key Takeaways

- Master the core ideas of Exception Handling and RAII through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
