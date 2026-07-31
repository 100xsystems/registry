---
{
  "title": "Constructors, Destructors, and Copy Semantics",
  "description": "RAII, copy constructors, move semantics, rule of three.",
  "type": "lesson",
  "order": 9,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write constructors and destructors (RAII)",
    "Write copy constructors",
    "Write move constructors",
    "Apply the rule of three"
  ],
  "knowledge_refs": [
    "cpp/cpp-09-copy-move"
  ],
  "prerequisites": [
    "CPP-08"
  ],
  "references": [
    {
      "title": "learncpp — Destructors",
      "url": "https://www.learncpp.com/cpp-tutorial/destructors/"
    },
    {
      "title": "learncpp — Move Semantics",
      "url": "https://www.learncpp.com/cpp-tutorial/move-semantics-and-stdmove/"
    },
    {
      "title": "cppreference — Rule of three/five/zero",
      "url": "https://en.cppreference.com/w/cpp/language/rule_of_three"
    }
  ]
}
---

# CPP-09-COPY-MOVE: Constructors, Destructors, and Copy Semantics

## Introduction

RAII, copy constructors, move semantics, rule of three. By the end of this lesson you will be able to: Write constructors and destructors (RAII); Write copy constructors; Write move constructors; Apply the rule of three.

## Key Concepts

### 1. Write constructors and destructors (RAII)

Target: Write constructors and destructors (RAII). Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cpp
#include <iostream>

class Resource {
public:
    Resource() { std::cout << "acquire\n"; }
    ~Resource() { std::cout << "release\n"; }   // destructor
};

int main() {
    Resource r;   // RAII: constructor acquires, destructor releases
    std::cout << "in scope\n";
    return 0;
}
```
### 2. Write copy constructors

Target: Write copy constructors. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cpp
#include <iostream>
#include <string>

class Person {
public:
    Person(std::string name, int age) : name_(name), age_(age) {}
    std::string name() const { return name_; }
    int age() const { return age_; }
private:
    std::string name_;
    int age_;
};

int main() {
    Person alice("Alice", 30);
    Person copy = alice;          // copy constructor
    std::cout << copy.name() << " " << copy.age() << "\n";
    return 0;
}
```
### 3. Write move constructors

Target: Write move constructors. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cpp
#include <iostream>
#include <vector>

class Container {
public:
    Container(std::vector<int> data) : data_(std::move(data)) {}
    // move constructor (C++11): steal resources, no copy
    Container(Container &&other) noexcept : data_(std::move(other.data_)) {}
    int size() const { return data_.size(); }
private:
    std::vector<int> data_;
};

int main() {
    Container a({1, 2, 3});
    Container b = std::move(a);   // move
    std::cout << b.size() << "\n";   // 3
    return 0;
}
```
### 4. Apply the rule of three

Target: Apply the rule of three. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cpp
#include <iostream>
#include <algorithm>

// rule of three: destructor, copy ctor, copy assignment
class Buffer {
public:
    Buffer(int size) : size_(size), data_(new int[size]) {}
    ~Buffer() { delete[] data_; }
    Buffer(const Buffer &other) : size_(other.size_), data_(new int[other.size_]) {
        std::copy(other.data_, other.data_ + size_, data_);
    }
    int *data() { return data_; }
private:
    int size_;
    int *data_;
};

int main() {
    Buffer a(4);
    Buffer b = a;   // deep copy, no double-free
    std::cout << (b.data() != a.data()) << "\n";   // 1 (distinct buffers)
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Constructors, Destructors, and Copy Semantics"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Constructors, Destructors, and Copy Semantics with analogies and real-world examples"
1. "Show me common mistakes beginners make with Constructors, Destructors, and Copy Semantics"
1. "Provide advanced patterns and performance considerations for Constructors, Destructors, and Copy Semantics"

## Key Takeaways

- Master the core ideas of Constructors, Destructors, and Copy Semantics through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
