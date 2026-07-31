---
{
  "title": "Operator Overloading",
  "description": "Overload operators, comparison operators, increment/decrement.",
  "type": "lesson",
  "order": 10,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Overload arithmetic operators",
    "Overload comparison operators",
    "Overload prefix and postfix increment",
    "Use overloaded operators with STL algorithms"
  ],
  "knowledge_refs": [
    "cpp/cpp-10-operator-overloading"
  ],
  "prerequisites": [
    "CPP-09"
  ],
  "references": [
    {
      "title": "learncpp — Operator Overloading",
      "url": "https://www.learncpp.com/cpp-tutorial/introduction-to-operator-overloading/"
    },
    {
      "title": "cppreference — Operator Overloading",
      "url": "https://en.cppreference.com/w/cpp/language/operators"
    },
    {
      "title": "cppreference — Comparison Operators",
      "url": "https://en.cppreference.com/w/cpp/language/operator_comparison"
    }
  ]
}
---

# CPP-10-OPERATOR-OVERLOADING: Operator Overloading

## Introduction

Overload operators, comparison operators, increment/decrement. By the end of this lesson you will be able to: Overload arithmetic operators; Overload comparison operators; Overload prefix and postfix increment; Use overloaded operators with STL algorithms.

## Key Concepts

### 1. Overload arithmetic operators

Target: Overload arithmetic operators. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cpp
#include <iostream>

class Complex {
public:
    Complex(double re, double im) : re_(re), im_(im) {}
    Complex operator+(const Complex &o) const {
        return Complex(re_ + o.re_, im_ + o.im_);
    }
    void print() const { std::cout << re_ << "+" << im_ << "i\n"; }
private:
    double re_, im_;
};

int main() {
    Complex a(1, 2), b(3, 4);
    (a + b).print();   // 4+6i (operator overload)
    return 0;
}
```
### 2. Overload comparison operators

Target: Overload comparison operators. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cpp
#include <iostream>

class Fraction {
public:
    Fraction(int n, int d) : n_(n), d_(d) {}
    bool operator<(const Fraction &o) const { return n_ * o.d_ < o.n_ * d_; }
    int num() const { return n_; }
private:
    int n_, d_;
};

int main() {
    Fraction a(1, 3), b(1, 2);
    std::cout << (a < b) << "\n";   // 1 (1/3 < 1/2)
    return 0;
}
```
### 3. Overload prefix and postfix increment

Target: Overload prefix and postfix increment. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cpp
#include <iostream>

class Counter {
public:
    Counter &operator++() { value_++; return *this; }     // prefix
    Counter operator++(int) { Counter t = *this; ++value_; return t; }  // postfix
    int value() const { return value_; }
private:
    int value_ = 0;
};

int main() {
    Counter c;
    c++;
    ++c;
    std::cout << c.value() << "\n";   // 2
    return 0;
}
```
### 4. Use overloaded operators with STL algorithms

Target: Use overloaded operators with STL algorithms. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

class Book {
public:
    Book(std::string t, int p) : title_(t), pages_(p) {}
    bool operator<(const Book &o) const { return pages_ < o.pages_; }
    std::string title() const { return title_; }
private:
    std::string title_;
    int pages_;
};

int main() {
    std::vector<Book> books = {{"A", 100}, {"B", 50}, {"C", 200}};
    std::sort(books.begin(), books.end());   // uses operator<
    std::cout << books[0].title() << "\n";   // B
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Operator Overloading"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Operator Overloading with analogies and real-world examples"
1. "Show me common mistakes beginners make with Operator Overloading"
1. "Provide advanced patterns and performance considerations for Operator Overloading"

## Key Takeaways

- Master the core ideas of Operator Overloading through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
