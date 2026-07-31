---
{
  "title": "Arrays, Strings, and Vectors",
  "description": "C arrays, std::string, std::vector, and multi-dimensional arrays.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use std::vector with push_back",
    "Manipulate std::string",
    "Use C-style arrays and range-based for",
    "Work with multi-dimensional arrays"
  ],
  "knowledge_refs": [
    "cpp/cpp-06-containers"
  ],
  "prerequisites": [
    "CPP-05"
  ],
  "references": [
    {
      "title": "learncpp — Vectors",
      "url": "https://www.learncpp.com/cpp-tutorial/introduction-to-stdvector-and-list-constructors/"
    },
    {
      "title": "cppreference — std::vector",
      "url": "https://en.cppreference.com/w/cpp/container/vector"
    },
    {
      "title": "cppreference — std::string",
      "url": "https://en.cppreference.com/w/cpp/string/basic_string"
    }
  ]
}
---

# CPP-06-CONTAINERS: Arrays, Strings, and Vectors

## Introduction

C arrays, std::string, std::vector, and multi-dimensional arrays. By the end of this lesson you will be able to: Use std::vector with push_back; Manipulate std::string; Use C-style arrays and range-based for; Work with multi-dimensional arrays.

## Key Concepts

### 1. Use std::vector with push_back

Target: Use std::vector with push_back. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {1, 2, 3};
    v.push_back(4);
    v.insert(v.begin(), 0);
    std::cout << v.size() << " " << v[0] << " " << v.back() << "\n";  // 5 0 4
    return 0;
}
```
### 2. Manipulate std::string

Target: Manipulate std::string. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cpp
#include <iostream>
#include <string>

int main() {
    std::string s = "hello";
    s += " world";
    s.push_back('!');
    std::cout << s << "\n";                    // hello world!
    std::cout << s.substr(0, 5) << "\n";      // hello
    std::cout << (s.find("world") != std::string::npos) << "\n";  // 1
    return 0;
}
```
### 3. Use C-style arrays and range-based for

Target: Use C-style arrays and range-based for. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cpp
#include <iostream>

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    for (int i = 0; i < 5; i++) std::cout << arr[i] << " ";
    std::cout << "\n";
    // range-based for over C array
    for (int x : arr) std::cout << x << " ";
    std::cout << "\n";
    return 0;
}
```
### 4. Work with multi-dimensional arrays

Target: Work with multi-dimensional arrays. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cpp
#include <iostream>

int main() {
    // multi-dimensional array
    int grid[2][3] = {{1, 2, 3}, {4, 5, 6}};
    std::cout << grid[1][0] << "\n";   // 4
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Arrays, Strings, and Vectors"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arrays, Strings, and Vectors with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arrays, Strings, and Vectors"
1. "Provide advanced patterns and performance considerations for Arrays, Strings, and Vectors"

## Key Takeaways

- Master the core ideas of Arrays, Strings, and Vectors through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
