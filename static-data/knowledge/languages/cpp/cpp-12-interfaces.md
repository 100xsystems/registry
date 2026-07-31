---
{
  "title": "Interfaces and Abstract Classes",
  "description": "Abstract classes as interfaces, multiple inheritance, polymorphic collections.",
  "type": "lesson",
  "order": 12,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Design abstract base classes",
    "Implement interfaces with pure virtual methods",
    "Use multiple inheritance",
    "Store polymorphic objects with unique_ptr"
  ],
  "knowledge_refs": [
    "cpp/cpp-12-interfaces"
  ],
  "prerequisites": [
    "CPP-11"
  ],
  "references": [
    {
      "title": "learncpp — Pure Virtual Functions",
      "url": "https://www.learncpp.com/cpp-tutorial/pure-virtual-functions-abstract-base-classes-and-interface-classes/"
    },
    {
      "title": "cppreference — Abstract Classes",
      "url": "https://en.cppreference.com/w/cpp/language/abstract_class"
    },
    {
      "title": "cppreference — Multiple Inheritance",
      "url": "https://en.cppreference.com/w/cpp/language/multiple_inheritance"
    }
  ]
}
---

# CPP-12-INTERFACES: Interfaces and Abstract Classes

## Introduction

Abstract classes as interfaces, multiple inheritance, polymorphic collections. By the end of this lesson you will be able to: Design abstract base classes; Implement interfaces with pure virtual methods; Use multiple inheritance; Store polymorphic objects with unique_ptr.

## Key Concepts

### 1. Design abstract base classes

Target: Design abstract base classes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cpp
#include <iostream>

class Shape {   // abstract with pure virtual
public:
    virtual double area() const = 0;
    virtual ~Shape() = default;
};

int main() {
    // Shape s;  // error: cannot instantiate abstract class
    std::cout << "abstract classes cannot be instantiated\n";
    return 0;
}
```
### 2. Implement interfaces with pure virtual methods

Target: Implement interfaces with pure virtual methods. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cpp
#include <iostream>

// interfaces in C++ = abstract classes with only pure virtuals
class Drawable {
public:
    virtual void draw() const = 0;
    virtual ~Drawable() = default;
};

class Circle : public Drawable {
public:
    void draw() const override { std::cout << "draw circle\n"; }
};

int main() {
    Circle c;
    Drawable &d = c;
    d.draw();
    return 0;
}
```
### 3. Use multiple inheritance

Target: Use multiple inheritance. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cpp
#include <iostream>

// multiple inheritance
struct Printable { virtual void print() const = 0; };
struct Serializable { virtual void save() const = 0; };

class Doc : public Printable, public Serializable {
public:
    void print() const override { std::cout << "print doc\n"; }
    void save() const override { std::cout << "save doc\n"; }
};

int main() {
    Doc d;
    d.print();
    d.save();
    return 0;
}
```
### 4. Store polymorphic objects with unique_ptr

Target: Store polymorphic objects with unique_ptr. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cpp
#include <iostream>
#include <memory>
#include <vector>

struct Animal { virtual std::string speak() const = 0; virtual ~Animal() = default; };
struct Dog : Animal { std::string speak() const override { return "Woof"; } };
struct Cat : Animal { std::string speak() const override { return "Meow"; } };

int main() {
    std::vector<std::unique_ptr<Animal>> animals;
    animals.push_back(std::make_unique<Dog>());
    animals.push_back(std::make_unique<Cat>());
    for (auto &a : animals) std::cout << a->speak() << " ";
    std::cout << "\n";   // Woof Meow
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Interfaces and Abstract Classes"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Interfaces and Abstract Classes with analogies and real-world examples"
1. "Show me common mistakes beginners make with Interfaces and Abstract Classes"
1. "Provide advanced patterns and performance considerations for Interfaces and Abstract Classes"

## Key Takeaways

- Master the core ideas of Interfaces and Abstract Classes through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
