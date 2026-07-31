---
{
  "title": "Lambdas and Functional Programming",
  "description": "Lambda expressions, captures, std::function, higher-order patterns.",
  "type": "lesson",
  "order": 19,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write lambda expressions",
    "Capture variables by value and reference",
    "Use std::function",
    "Combine with STL algorithms"
  ],
  "knowledge_refs": [
    "cpp/cpp-19-lambdas"
  ],
  "prerequisites": [
    "CPP-18"
  ],
  "references": [
    {
      "title": "learncpp — Lambdas",
      "url": "https://www.learncpp.com/cpp-tutorial/introduction-to-lambdas-anonymous-functions/"
    },
    {
      "title": "cppreference — Lambda Expressions",
      "url": "https://en.cppreference.com/w/cpp/language/lambda"
    },
    {
      "title": "cppreference — std::function",
      "url": "https://en.cppreference.com/w/cpp/utility/functional/function"
    }
  ]
}
---

# CPP-19-LAMBDAS: Lambdas and Functional Programming

## Introduction

Lambda expressions, captures, std::function, higher-order patterns. By the end of this lesson you will be able to: Write lambda expressions; Capture variables by value and reference; Use std::function; Combine with STL algorithms.

## Key Concepts

### 1. Write lambda expressions

Target: Write lambda expressions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cpp
#include <iostream>
#include <algorithm>
#include <vector>

int main() {
    std::vector<int> v = {1, 2, 3, 4};
    auto square = [](int x) { return x * x; };   // lambda
    std::transform(v.begin(), v.end(), v.begin(), square);
    std::cout << v[2] << "\n";   // 9
    return 0;
}
```
### 2. Capture variables by value and reference

Target: Capture variables by value and reference. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int limit = 3;
    std::vector<int> v = {1, 2, 3, 4, 5};
    // capture by value [limit]
    auto count = std::count_if(v.begin(), v.end(), [limit](int x) { return x > limit; });
    std::cout << count << "\n";   // 2 (4, 5)
    return 0;
}
```
### 3. Use std::function

Target: Use std::function. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cpp
#include <iostream>
#include <functional>
#include <algorithm>
#include <vector>

int main() {
    std::function<int(int)> fib = [&](int n) {   // recursive lambda via std::function
        return n <= 1 ? n : fib(n - 1) + fib(n - 2);
    };
    std::cout << fib(10) << "\n";   // 55
    return 0;
}
```
### 4. Combine with STL algorithms

Target: Combine with STL algorithms. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cpp
#include <iostream>
#include <algorithm>
#include <vector>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};
    auto even = [](int x) { return x % 2 == 0; };
    v.erase(std::remove_if(v.begin(), v.end(), even), v.end());
    for (int x : v) std::cout << x << " ";
    std::cout << "\n";   // 1 3 5
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Lambdas and Functional Programming"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Lambdas and Functional Programming with analogies and real-world examples"
1. "Show me common mistakes beginners make with Lambdas and Functional Programming"
1. "Provide advanced patterns and performance considerations for Lambdas and Functional Programming"

## Key Takeaways

- Master the core ideas of Lambdas and Functional Programming through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
