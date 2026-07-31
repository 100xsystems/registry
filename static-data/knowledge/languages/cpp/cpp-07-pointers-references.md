---
{
  "title": "Pointers and References",
  "description": "Pointer vs reference semantics, pointer arithmetic, nullptr.",
  "type": "lesson",
  "order": 7,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Dereference pointers and use references",
    "Pass by reference",
    "Do pointer arithmetic",
    "Use nullptr and pointer-to-pointer"
  ],
  "knowledge_refs": [
    "cpp/cpp-07-pointers-references"
  ],
  "prerequisites": [
    "CPP-06"
  ],
  "references": [
    {
      "title": "learncpp — References",
      "url": "https://www.learncpp.com/cpp-tutorial/introduction-to-references/"
    },
    {
      "title": "learncpp — Pointers",
      "url": "https://www.learncpp.com/cpp-tutorial/introduction-to-pointers/"
    },
    {
      "title": "cppreference — Pointers",
      "url": "https://en.cppreference.com/w/cpp/language/pointer"
    }
  ]
}
---

# CPP-07-POINTERS-REFERENCES: Pointers and References

## Introduction

Pointer vs reference semantics, pointer arithmetic, nullptr. By the end of this lesson you will be able to: Dereference pointers and use references; Pass by reference; Do pointer arithmetic; Use nullptr and pointer-to-pointer.

## Key Concepts

### 1. Dereference pointers and use references

Target: Dereference pointers and use references. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cpp
#include <iostream>

int main() {
    int x = 42;
    int *p = &x;                  // pointer
    int &r = x;                   // reference (alias)
    *p = 100;
    std::cout << x << " " << r << "\n";   // 100 100
    return 0;
}
```
### 2. Pass by reference

Target: Pass by reference. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cpp
#include <iostream>

// references cannot be null and always alias something
void swap(int &a, int &b) {
    int t = a; a = b; b = t;
}

int main() {
    int x = 1, y = 2;
    swap(x, y);
    std::cout << x << " " << y << "\n";   // 2 1
    return 0;
}
```
### 3. Do pointer arithmetic

Target: Do pointer arithmetic. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cpp
#include <iostream>

int main() {
    int nums[4] = {10, 20, 30, 40};
    int *p = nums;                 // array decays to pointer
    std::cout << *p << " " << *(p + 2) << "\n";   // 10 30
    p++;
    std::cout << *p << "\n";      // 20
    return 0;
}
```
### 4. Use nullptr and pointer-to-pointer

Target: Use nullptr and pointer-to-pointer. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cpp
#include <iostream>

// pointer-to-pointer and nullptr (C++11)
int main() {
    int x = 42;
    int *p = &x;
    int **pp = &p;
    std::cout << **pp << "\n";    // 42
    int *q = nullptr;
    if (q) std::cout << "non-null\n";
    else std::cout << "null\n";
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Pointers and References"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Pointers and References with analogies and real-world examples"
1. "Show me common mistakes beginners make with Pointers and References"
1. "Provide advanced patterns and performance considerations for Pointers and References"

## Key Takeaways

- Master the core ideas of Pointers and References through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
