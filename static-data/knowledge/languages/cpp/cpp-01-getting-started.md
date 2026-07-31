---
{
  "title": "Getting Started with C++",
  "description": "Set up a C++ toolchain with g++, compile/run, namespaces, and I/O streams.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install g++ and compile your first C++ program",
    "Use main with argc/argv",
    "Use namespaces to organize code",
    "Read and write with iostream"
  ],
  "knowledge_refs": [
    "cpp/cpp-01-getting-started"
  ],
  "prerequisites": [],
  "references": [
    {
      "title": "learncpp — Introduction",
      "url": "https://www.learncpp.com/"
    },
    {
      "title": "cppreference — Tutorial",
      "url": "https://en.cppreference.com/w/cpp/language"
    },
    {
      "title": "cppreference — iostream",
      "url": "https://en.cppreference.com/w/cpp/header/iostream"
    }
  ]
}
---

# CPP-01-GETTING-STARTED: Getting Started with C++

## Introduction

Set up a C++ toolchain with g++, compile/run, namespaces, and I/O streams. By the end of this lesson you will be able to: Install g++ and compile your first C++ program; Use main with argc/argv; Use namespaces to organize code; Read and write with iostream.

## Key Concepts

### 1. Install g++ and compile your first C++ program

Target: Install g++ and compile your first C++ program. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, 100X Systems!" << std::endl;
    return 0;
}
// compile: g++ -Wall -Wextra -std=c++20 -o hello hello.cpp
```
### 2. Use main with argc/argv

Target: Use main with argc/argv. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cpp
#include <iostream>

int main(int argc, char *argv[]) {
    std::cout << "argc = " << argc << "\n";
    for (int i = 0; i < argc; i++) std::cout << argv[i] << "\n";
    return 0;
}
```
### 3. Use namespaces to organize code

Target: Use namespaces to organize code. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cpp
#include <iostream>

// namespaces organize code and avoid collisions
namespace math {
    int add(int a, int b) { return a + b; }
}

int main() {
    std::cout << math::add(2, 3) << "\n";
    using std::cout;   // bring a name into scope
    cout << "using declaration\n";
    return 0;
}
```
### 4. Read and write with iostream

Target: Read and write with iostream. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cpp
#include <iostream>
#include <string>

int main() {
    // type-safe I/O streams
    std::string name;
    std::cout << "Enter name: ";
    std::getline(std::cin, name);
    std::cout << "Hello, " << name << "!\n";
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Getting Started with C++"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with C++ with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with C++"
1. "Provide advanced patterns and performance considerations for Getting Started with C++"

## Key Takeaways

- Master the core ideas of Getting Started with C++ through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
