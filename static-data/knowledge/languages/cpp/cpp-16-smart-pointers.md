---
{
  "title": "Smart Pointers",
  "description": "unique_ptr, shared_ptr, weak_ptr, ownership semantics.",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use unique_ptr for exclusive ownership",
    "Use shared_ptr for shared ownership",
    "Use weak_ptr to break cycles",
    "Store polymorphic objects safely"
  ],
  "knowledge_refs": [
    "cpp/cpp-16-smart-pointers"
  ],
  "prerequisites": [
    "CPP-15"
  ],
  "references": [
    {
      "title": "learncpp — Smart Pointers",
      "url": "https://www.learncpp.com/cpp-tutorial/introduction-to-smart-pointers-and-move-semantics/"
    },
    {
      "title": "cppreference — unique_ptr",
      "url": "https://en.cppreference.com/w/cpp/memory/unique_ptr"
    },
    {
      "title": "cppreference — shared_ptr",
      "url": "https://en.cppreference.com/w/cpp/memory/shared_ptr"
    }
  ]
}
---

# CPP-16-SMART-POINTERS: Smart Pointers

## Introduction

unique_ptr, shared_ptr, weak_ptr, ownership semantics. By the end of this lesson you will be able to: Use unique_ptr for exclusive ownership; Use shared_ptr for shared ownership; Use weak_ptr to break cycles; Store polymorphic objects safely.

## Key Concepts

### 1. Use unique_ptr for exclusive ownership

Target: Use unique_ptr for exclusive ownership. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cpp
#include <iostream>
#include <memory>

int main() {
    std::unique_ptr<int> p = std::make_unique<int>(42);   // exclusive ownership
    std::cout << *p << "\n";   // 42
    // auto q = p;   // error: cannot copy unique_ptr
    std::unique_ptr<int> q = std::move(p);   // transfer ownership
    std::cout << *q << "\n";   // 42
    return 0;
}
```
### 2. Use shared_ptr for shared ownership

Target: Use shared_ptr for shared ownership. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cpp
#include <iostream>
#include <memory>

int main() {
    std::shared_ptr<int> a = std::make_shared<int>(10);
    std::shared_ptr<int> b = a;   // shared ownership
    std::cout << a.use_count() << "\n";   // 2
    b.reset();
    std::cout << a.use_count() << "\n";   // 1
    return 0;
}
```
### 3. Use weak_ptr to break cycles

Target: Use weak_ptr to break cycles. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cpp
#include <iostream>
#include <memory>

// weak_ptr: observe without owning (breaks cycles)
int main() {
    std::shared_ptr<int> s = std::make_shared<int>(7);
    std::weak_ptr<int> w = s;
    std::cout << w.expired() << "\n";   // 0 (still alive)
    if (auto sp = w.lock()) std::cout << *sp << "\n";   // 7
    s.reset();
    std::cout << w.expired() << "\n";   // 1 (gone)
    return 0;
}
```
### 4. Store polymorphic objects safely

Target: Store polymorphic objects safely. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cpp
#include <iostream>
#include <memory>
#include <vector>

int main() {
    std::vector<std::shared_ptr<int>> items;
    for (int i = 0; i < 3; i++)
        items.push_back(std::make_shared<int>(i * 10));
    for (auto &p : items) std::cout << *p << " ";
    std::cout << "\n";   // 0 10 20
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Smart Pointers"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Smart Pointers with analogies and real-world examples"
1. "Show me common mistakes beginners make with Smart Pointers"
1. "Provide advanced patterns and performance considerations for Smart Pointers"

## Key Takeaways

- Master the core ideas of Smart Pointers through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
