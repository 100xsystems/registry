---
{
  "title": "Concurrency",
  "description": "std::thread, mutex, lock_guard, async/future, condition_variable.",
  "type": "lesson",
  "order": 20,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create and join threads",
    "Synchronize with mutex and lock_guard",
    "Use async and future",
    "Coordinate with condition_variable"
  ],
  "knowledge_refs": [
    "cpp/cpp-20-concurrency"
  ],
  "prerequisites": [
    "CPP-19"
  ],
  "references": [
    {
      "title": "cppreference — Thread Support",
      "url": "https://en.cppreference.com/w/cpp/thread"
    },
    {
      "title": "cppreference — std::thread",
      "url": "https://en.cppreference.com/w/cpp/thread/thread"
    },
    {
      "title": "cppreference — std::async",
      "url": "https://en.cppreference.com/w/cpp/thread/async"
    }
  ]
}
---

# CPP-20-CONCURRENCY: Concurrency

## Introduction

std::thread, mutex, lock_guard, async/future, condition_variable. By the end of this lesson you will be able to: Create and join threads; Synchronize with mutex and lock_guard; Use async and future; Coordinate with condition_variable.

## Key Concepts

### 1. Create and join threads

Target: Create and join threads. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```cpp
#include <iostream>
#include <thread>

void hello() { std::cout << "thread says hi\n"; }

int main() {
    std::thread t(hello);
    t.join();   // wait for the thread
    return 0;
}
```
### 2. Synchronize with mutex and lock_guard

Target: Synchronize with mutex and lock_guard. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```cpp
#include <iostream>
#include <thread>
#include <mutex>

int main() {
    std::mutex m;
    int counter = 0;
    auto worker = [&] {
        for (int i = 0; i < 1000; i++) {
            std::lock_guard<std::mutex> lock(m);   // RAII lock
            counter++;
        }
    };
    std::thread t1(worker), t2(worker);
    t1.join(); t2.join();
    std::cout << counter << "\n";   // 2000
    return 0;
}
```
### 3. Use async and future

Target: Use async and future. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```cpp
#include <iostream>
#include <future>

int main() {
    auto fut = std::async(std::launch::async, [] {
        return 42;
    });
    std::cout << fut.get() << "\n";   // 42 (blocks until ready)
    return 0;
}
```
### 4. Coordinate with condition_variable

Target: Coordinate with condition_variable. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```cpp
#include <iostream>
#include <condition_variable>
#include <mutex>
#include <queue>

int main() {
    std::queue<int> q;
    std::mutex m;
    std::condition_variable cv;
    bool done = false;
    auto producer = [&] {
        { std::lock_guard<std::mutex> l(m); q.push(1); }
        cv.notify_one();
        { std::lock_guard<std::mutex> l(m); done = true; }
        cv.notify_one();
    };
    std::thread p(producer);
    std::unique_lock<std::mutex> lk(m);
    cv.wait(lk, [&] { return done; });
    std::cout << q.size() << "\n";   // 1
    p.join();
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Concurrency"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Concurrency with analogies and real-world examples"
1. "Show me common mistakes beginners make with Concurrency"
1. "Provide advanced patterns and performance considerations for Concurrency"

## Key Takeaways

- Master the core ideas of Concurrency through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
