---
{
  "title": "STL Containers",
  "description": "vector, map, unordered_map, set, deque, queue, stack.",
  "type": "lesson",
  "order": 14,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use vector and map",
    "Use unordered_map and set",
    "Use queue and stack adaptors",
    "Emplace elements efficiently"
  ],
  "knowledge_refs": [
    "cpp/cpp-14-stl-containers"
  ],
  "prerequisites": [
    "CPP-13"
  ],
  "references": [
    {
      "title": "cppreference — Containers",
      "url": "https://en.cppreference.com/w/cpp/container"
    },
    {
      "title": "cppreference — std::map",
      "url": "https://en.cppreference.com/w/cpp/container/map"
    },
    {
      "title": "learncpp — STL Containers",
      "url": "https://www.learncpp.com/cpp-tutorial/introduction-to-stl-containers/"
    }
  ]
}
---

# CPP-14-STL-CONTAINERS: STL Containers

## Introduction

vector, map, unordered_map, set, deque, queue, stack. By the end of this lesson you will be able to: Use vector and map; Use unordered_map and set; Use queue and stack adaptors; Emplace elements efficiently.

## Key Concepts

### 1. Use vector and map

Target: Use vector and map. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <string>

int main() {
    std::vector<int> v = {3, 1, 2};          // dynamic array
    std::map<std::string, int> ages = {{"A", 30}};   // ordered tree map
    std::unordered_map<std::string, int> h = {{"A", 30}};  // hash map
    std::set<int> s = {3, 1, 2, 1};          // unique sorted
    std::cout << v[0] << " " << ages["A"] << " " << h["A"] << " " << s.size() << "\n";
    return 0;
}
```
### 2. Use unordered_map and set

Target: Use unordered_map and set. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cpp
#include <iostream>
#include <map>
#include <string>

int main() {
    std::map<std::string, int> freq;
    freq["apple"]++;
    freq["apple"]++;
    freq["banana"]++;
    for (const auto &[k, v] : freq)   // structured bindings (C++17)
        std::cout << k << "=" << v << " ";
    std::cout << "\n";   // apple=2 banana=1
    return 0;
}
```
### 3. Use queue and stack adaptors

Target: Use queue and stack adaptors. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cpp
#include <iostream>
#include <deque>
#include <queue>
#include <stack>

int main() {
    std::deque<int> d = {1, 2};
    d.push_front(0);
    std::queue<int> q;   // FIFO
    q.push(1); q.push(2);
    std::stack<int> st;  // LIFO
    st.push(1); st.push(2);
    std::cout << d[0] << " " << q.front() << " " << st.top() << "\n";  // 0 1 2
    return 0;
}
```
### 4. Emplace elements efficiently

Target: Emplace elements efficiently. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cpp
#include <iostream>
#include <vector>

int main() {
    // emplace_back constructs in place (no copy)
    std::vector<std::pair<int, int>> v;
    v.emplace_back(1, 2);
    v.emplace_back(3, 4);
    std::cout << v.size() << " " << v[1].second << "\n";   // 2 4
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "STL Containers"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain STL Containers with analogies and real-world examples"
1. "Show me common mistakes beginners make with STL Containers"
1. "Provide advanced patterns and performance considerations for STL Containers"

## Key Takeaways

- Master the core ideas of STL Containers through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
