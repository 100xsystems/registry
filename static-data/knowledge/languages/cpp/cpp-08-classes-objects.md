---
{
  "title": "Classes and Objects",
  "description": "Class definitions, access specifiers, constructors, static members, this.",
  "type": "lesson",
  "order": 8,
  "duration": "75 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define classes with private data and public methods",
    "Write constructors with initializer lists",
    "Use static members",
    "Write const methods and use this"
  ],
  "knowledge_refs": [
    "cpp/cpp-08-classes-objects"
  ],
  "prerequisites": [
    "CPP-07"
  ],
  "references": [
    {
      "title": "learncpp — Classes",
      "url": "https://www.learncpp.com/cpp-tutorial/introduction-to-classes/"
    },
    {
      "title": "learncpp — Constructors",
      "url": "https://www.learncpp.com/cpp-tutorial/constructors/"
    },
    {
      "title": "cppreference — Classes",
      "url": "https://en.cppreference.com/w/cpp/language/classes"
    }
  ]
}
---

# CPP-08-CLASSES-OBJECTS: Classes and Objects

## Introduction

Class definitions, access specifiers, constructors, static members, this. By the end of this lesson you will be able to: Define classes with private data and public methods; Write constructors with initializer lists; Use static members; Write const methods and use this.

## Key Concepts

### 1. Define classes with private data and public methods

Target: Define classes with private data and public methods. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cpp
#include <iostream>

class BankAccount {
private:
    double balance_ = 0.0;
public:
    void deposit(double amount) { balance_ += amount; }
    double balance() const { return balance_; }
};

int main() {
    BankAccount acct;
    acct.deposit(100);
    std::cout << acct.balance() << "\n";   // 100
    return 0;
}
```
### 2. Write constructors with initializer lists

Target: Write constructors with initializer lists. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cpp
#include <iostream>

class Point {
public:
    Point(int x, int y) : x_(x), y_(y) {}   // constructor init list
    void print() const { std::cout << "(" << x_ << ", " << y_ << ")\n"; }
private:
    int x_, y_;
};

int main() {
    Point p(3, 4);
    p.print();
    return 0;
}
```
### 3. Use static members

Target: Use static members. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cpp
#include <iostream>

class Counter {
public:
    Counter() { instances_++; }
    static int instances() { return instances_; }
private:
    static int instances_;
};

int Counter::instances_ = 0;

int main() {
    Counter a, b, c;
    std::cout << Counter::instances() << "\n";   // 3 (static member)
    return 0;
}
```
### 4. Write const methods and use this

Target: Write const methods and use this. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cpp
#include <iostream>

// const methods + this pointer
class Square {
public:
    Square(int side) : side_(side) {}
    int area() const { return side_ * side_; }
    Square *grow() { side_ *= 2; return this; }
private:
    int side_;
};

int main() {
    Square s(4);
    s.grow()->grow();
    std::cout << s.area() << "\n";   // 256
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Classes and Objects"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Classes and Objects with analogies and real-world examples"
1. "Show me common mistakes beginners make with Classes and Objects"
1. "Provide advanced patterns and performance considerations for Classes and Objects"

## Key Takeaways

- Master the core ideas of Classes and Objects through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
