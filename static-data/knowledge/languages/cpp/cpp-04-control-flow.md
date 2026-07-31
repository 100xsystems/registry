---
{
  "title": "Control Flow",
  "description": "if/else, switch, loops, range-based for, and jump statements.",
  "type": "lesson",
  "order": 4,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write if/else branching logic",
    "Use switch statements",
    "Use for, while, and do-while loops",
    "Iterate containers with range-based for"
  ],
  "knowledge_refs": [
    "cpp/cpp-04-control-flow"
  ],
  "prerequisites": [
    "CPP-03"
  ],
  "references": [
    {
      "title": "learncpp — If Statements",
      "url": "https://www.learncpp.com/cpp-tutorial/if-statements/"
    },
    {
      "title": "learncpp — For Loops",
      "url": "https://www.learncpp.com/cpp-tutorial/for-statements/"
    },
    {
      "title": "cppreference — Range-based for",
      "url": "https://en.cppreference.com/w/cpp/language/range-for"
    }
  ]
}
---

# CPP-04-CONTROL-FLOW: Control Flow

## Introduction

if/else, switch, loops, range-based for, and jump statements. By the end of this lesson you will be able to: Write if/else branching logic; Use switch statements; Use for, while, and do-while loops; Iterate containers with range-based for.

## Key Concepts

### 1. Write if/else branching logic

Target: Write if/else branching logic. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cpp
#include <iostream>

int main() {
    int score = 85;
    if (score >= 90) std::cout << "A\n";
    else if (score >= 80) std::cout << "B\n";
    else std::cout << "C\n";
    return 0;
}
```
### 2. Use switch statements

Target: Use switch statements. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cpp
#include <iostream>

int main() {
    int day = 3;
    switch (day) {
        case 1: std::cout << "Monday\n"; break;
        case 2: std::cout << "Tuesday\n"; break;
        default: std::cout << "Other\n"; break;
    }
    return 0;
}
```
### 3. Use for, while, and do-while loops

Target: Use for, while, and do-while loops. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cpp
#include <iostream>

int main() {
    for (int i = 0; i < 5; i++) std::cout << i << " ";   // 0 1 2 3 4
    std::cout << "\n";
    int j = 0;
    while (j < 3) { std::cout << j << " "; j++; }        // 0 1 2
    std::cout << "\n";
    return 0;
}
```
### 4. Iterate containers with range-based for

Target: Iterate containers with range-based for. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cpp
#include <iostream>
#include <vector>

int main() {
    // range-based for (C++11): iterate any container
    std::vector<int> v = {10, 20, 30};
    for (int x : v) std::cout << x << " ";
    std::cout << "\n";
    for (auto &x : v) x *= 2;   // modify in place
    std::cout << v[1] << "\n";  // 40
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
