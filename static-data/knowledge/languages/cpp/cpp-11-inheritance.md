---
{
  "title": "Inheritance and Polymorphism",
  "description": "Base/derived classes, virtual functions, abstract classes.",
  "type": "lesson",
  "order": 11,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create derived classes",
    "Use virtual functions for polymorphism",
    "Use pure virtual functions (abstract classes)",
    "Compose with base class references"
  ],
  "knowledge_refs": [
    "cpp/cpp-11-inheritance"
  ],
  "prerequisites": [
    "CPP-10"
  ],
  "references": [
    {
      "title": "learncpp — Inheritance",
      "url": "https://www.learncpp.com/cpp-tutorial/introduction-to-inheritance/"
    },
    {
      "title": "learncpp — Virtual Functions",
      "url": "https://www.learncpp.com/cpp-tutorial/virtual-functions/"
    },
    {
      "title": "cppreference — Virtual Functions",
      "url": "https://en.cppreference.com/w/cpp/language/virtual"
    }
  ]
}
---

# CPP-11-INHERITANCE: Inheritance and Polymorphism

## Introduction

Base/derived classes, virtual functions, abstract classes. By the end of this lesson you will be able to: Create derived classes; Use virtual functions for polymorphism; Use pure virtual functions (abstract classes); Compose with base class references.

## Key Concepts

### 1. Create derived classes

Target: Create derived classes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cpp
#include <iostream>

class Animal {
public:
    virtual std::string speak() const { return "..."; }
    virtual ~Animal() = default;
};

class Dog : public Animal {
public:
    std::string speak() const override { return "Woof"; }
};

int main() {
    Animal *a = new Dog();
    std::cout << a->speak() << "\n";   // Woof (virtual dispatch)
    delete a;
    return 0;
}
```
### 2. Use virtual functions for polymorphism

Target: Use virtual functions for polymorphism. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cpp
#include <iostream>
#include <memory>

class Animal {
public:
    virtual std::string speak() const = 0;   // pure virtual
    virtual ~Animal() = default;
};

class Cat : public Animal {
public:
    std::string speak() const override { return "Meow"; }
};

int main() {
    std::unique_ptr<Animal> a = std::make_unique<Cat>();
    std::cout << a->speak() << "\n";   // Meow
    return 0;
}
```
### 3. Use pure virtual functions (abstract classes)

Target: Use pure virtual functions (abstract classes). Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cpp
#include <iostream>

class Base {
public:
    Base(int x) : x_(x) {}
    void show() const { std::cout << "Base " << x_ << "\n"; }
protected:
    int x_;
};

class Derived : public Base {
public:
    Derived(int x, int y) : Base(x), y_(y) {}   // base ctor
    void show() const { Base::show(); std::cout << "Derived " << y_ << "\n"; }
private:
    int y_;
};

int main() {
    Derived d(1, 2);
    d.show();
    return 0;
}
```
### 4. Compose with base class references

Target: Compose with base class references. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cpp
#include <iostream>

class Shape {                       // abstract base
public:
    virtual double area() const = 0;
    virtual ~Shape() = default;
};

class Circle : public Shape {
public:
    Circle(double r) : r_(r) {}
    double area() const override { return 3.14159 * r_ * r_; }
private:
    double r_;
};

class Square : public Shape {
public:
    Square(double s) : s_(s) {}
    double area() const override { return s_ * s_; }
private:
    double s_;
};

int main() {
    Circle c(2);
    Square sq(3);
    std::cout << c.area() << " " << sq.area() << "\n";
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Inheritance and Polymorphism"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Inheritance and Polymorphism with analogies and real-world examples"
1. "Show me common mistakes beginners make with Inheritance and Polymorphism"
1. "Provide advanced patterns and performance considerations for Inheritance and Polymorphism"

## Key Takeaways

- Master the core ideas of Inheritance and Polymorphism through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
