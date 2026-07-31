---
{
  "title": "Functions and Overloading",
  "description": "Declarations vs definitions, overloading, default arguments, const references.",
  "type": "lesson",
  "order": 5,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare and define functions",
    "Overload functions by signature",
    "Use default arguments",
    "Pass by const reference"
  ],
  "knowledge_refs": [
    "cpp/cpp-05-functions"
  ],
  "prerequisites": [
    "CPP-04"
  ],
  "references": [
    {
      "title": "learncpp — Functions",
      "url": "https://www.learncpp.com/cpp-tutorial/introduction-to-functions/"
    },
    {
      "title": "learncpp — Function Overloading",
      "url": "https://www.learncpp.com/cpp-tutorial/introduction-to-function-overloading/"
    },
    {
      "title": "cppreference — Functions",
      "url": "https://en.cppreference.com/w/cpp/language/functions"
    }
  ]
}
---

# CPP-05-FUNCTIONS: Functions and Overloading

## Introduction

Declarations vs definitions, overloading, default arguments, const references. By the end of this lesson you will be able to: Declare and define functions; Overload functions by signature; Use default arguments; Pass by const reference.

## Key Concepts

### 1. Declare and define functions

Target: Declare and define functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cpp
#include <iostream>

int add(int a, int b);   // declaration

int main() {
    std::cout << add(2, 3) << "\n";
    return 0;
}

int add(int a, int b) { return a + b; }   // definition
```
### 2. Overload functions by signature

Target: Overload functions by signature. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cpp
#include <iostream>

// function overloading: same name, different signatures
int max(int a, int b) { return a > b ? a : b; }
double max(double a, double b) { return a > b ? a : b; }
int max(int a, int b, int c) { return max(max(a, b), c); }

int main() {
    std::cout << max(3, 7) << " " << max(2.5, 1.5) << " " << max(1, 5, 3) << "\n";
    return 0;
}
```
### 3. Use default arguments

Target: Use default arguments. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cpp
#include <iostream>
#include <string>

// default arguments + reference parameters
void greet(const std::string &name, const std::string &prefix = "Hello") {
    std::cout << prefix << ", " << name << "!\n";
}

int main() {
    greet("Alice");          // uses default prefix
    greet("Bob", "Hi");
    return 0;
}
```
### 4. Pass by const reference

Target: Pass by const reference. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cpp
#include <iostream>
#include <string>

// const reference: read without copying
int length(const std::string &s) { return s.size(); }

int main() {
    std::string s = "hello";
    std::cout << length(s) << "\n";   // 5
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Functions and Overloading"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions and Overloading with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions and Overloading"
1. "Provide advanced patterns and performance considerations for Functions and Overloading"

## Key Takeaways

- Master the core ideas of Functions and Overloading through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
