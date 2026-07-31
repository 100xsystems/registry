---
{
  "title": "STL Algorithms and Iterators",
  "description": "sort, reverse, find, count_if, accumulate, lower_bound, binary_search.",
  "type": "lesson",
  "order": 15,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Sort and reverse containers",
    "Search with find and binary_search",
    "Accumulate with std::accumulate",
    "Use lower_bound for sorted ranges"
  ],
  "knowledge_refs": [
    "cpp/cpp-15-stl-algorithms"
  ],
  "prerequisites": [
    "CPP-14"
  ],
  "references": [
    {
      "title": "cppreference — Algorithms",
      "url": "https://en.cppreference.com/w/cpp/algorithm"
    },
    {
      "title": "cppreference — std::sort",
      "url": "https://en.cppreference.com/w/cpp/algorithm/sort"
    },
    {
      "title": "learncpp — Algorithms",
      "url": "https://www.learncpp.com/cpp-tutorial/introduction-to-standard-library-algorithms/"
    }
  ]
}
---

# CPP-15-STL-ALGORITHMS: STL Algorithms and Iterators

## Introduction

sort, reverse, find, count_if, accumulate, lower_bound, binary_search. By the end of this lesson you will be able to: Sort and reverse containers; Search with find and binary_search; Accumulate with std::accumulate; Use lower_bound for sorted ranges.

## Key Concepts

### 1. Sort and reverse containers

Target: Sort and reverse containers. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> v = {5, 2, 8, 1};
    std::sort(v.begin(), v.end());
    std::reverse(v.begin(), v.end());
    for (int x : v) std::cout << x << " ";
    std::cout << "\n";   // 8 5 2 1
    return 0;
}
```
### 2. Search with find and binary_search

Target: Search with find and binary_search. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};
    auto it = std::find(v.begin(), v.end(), 4);
    std::cout << (it != v.end()) << " " << *it << "\n";   // 1 4
    int count = std::count_if(v.begin(), v.end(), [](int x) { return x > 2; });
    std::cout << count << "\n";   // 3
    return 0;
}
```
### 3. Accumulate with std::accumulate

Target: Accumulate with std::accumulate. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cpp
#include <iostream>
#include <vector>
#include <numeric>

int main() {
    std::vector<int> v = {1, 2, 3, 4};
    int total = std::accumulate(v.begin(), v.end(), 0);
    int product = std::accumulate(v.begin(), v.end(), 1, [](int a, int b) { return a * b; });
    std::cout << total << " " << product << "\n";   // 10 24
    return 0;
}
```
### 4. Use lower_bound for sorted ranges

Target: Use lower_bound for sorted ranges. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};
    auto it = std::lower_bound(v.begin(), v.end(), 3);   // first >= 3
    std::cout << *it << "\n";   // 3
    std::cout << std::binary_search(v.begin(), v.end(), 4) << "\n";   // 1
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "STL Algorithms and Iterators"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain STL Algorithms and Iterators with analogies and real-world examples"
1. "Show me common mistakes beginners make with STL Algorithms and Iterators"
1. "Provide advanced patterns and performance considerations for STL Algorithms and Iterators"

## Key Takeaways

- Master the core ideas of STL Algorithms and Iterators through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
