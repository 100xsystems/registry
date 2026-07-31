---
{
  "title": "Recursion",
  "description": "Recursive functions, factorial, fibonacci, divide-and-conquer.",
  "type": "lesson",
  "order": 16,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write base cases and recursive steps",
    "Understand exponential blowup",
    "Recurse over arrays",
    "Use recursion for binary search"
  ],
  "knowledge_refs": [
    "c/c-16-recursion"
  ],
  "prerequisites": [
    "C-15"
  ],
  "references": [
    {
      "title": "learn-c.org — Recursion",
      "url": "https://learn-c.org/en/Recursion"
    },
    {
      "title": "cppreference — Recursion Notes",
      "url": "https://en.cppreference.com/w/c/language/functions"
    },
    {
      "title": "Khan Academy — Recursion",
      "url": "https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/recursion"
    }
  ]
}
---

# C-16-RECURSION: Recursion

## Introduction

Recursive functions, factorial, fibonacci, divide-and-conquer. By the end of this lesson you will be able to: Write base cases and recursive steps; Understand exponential blowup; Recurse over arrays; Use recursion for binary search.

## Key Concepts

### 1. Write base cases and recursive steps

Target: Write base cases and recursive steps. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```c
#include <stdio.h>

// classic recursion: factorial
long fact(int n) {
    if (n <= 1) return 1;
    return n * fact(n - 1);
}

int main(void) { printf("%ld\n", fact(5)); return 0; }
```
### 2. Understand exponential blowup

Target: Understand exponential blowup. Apply the idiomatic pattern — this is how production C expresses this idea, so study the shape of the code.

```c
#include <stdio.h>

// fibonacci: exponential without memoization
long fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}

int main(void) { printf("%ld\n", fib(10)); return 0; }
```
### 3. Recurse over arrays

Target: Recurse over arrays. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```c
#include <stdio.h>

// recursion over arrays: sum
int sum(int arr[], int n) {
    if (n == 0) return 0;
    return arr[n - 1] + sum(arr, n - 1);
}

int main(void) {
    int nums[] = {1, 2, 3, 4};
    printf("%d\n", sum(nums, 4));   // 10
    return 0;
}
```
### 4. Use recursion for binary search

Target: Use recursion for binary search. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```c
#include <stdio.h>

// recursion for search: binary search
int bsearch_rec(int arr[], int lo, int hi, int target) {
    if (lo > hi) return -1;
    int mid = lo + (hi - lo) / 2;
    if (arr[mid] == target) return mid;
    if (arr[mid] > target) return bsearch_rec(arr, lo, mid - 1, target);
    return bsearch_rec(arr, mid + 1, hi, target);
}

int main(void) {
    int nums[] = {1, 3, 5, 7, 9};
    printf("%d\n", bsearch_rec(nums, 0, 4, 7));   // 3
    return 0;
}
```

## Practice Questions

1. What is the key idea behind "Recursion"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Recursion with analogies and real-world examples"
1. "Show me common mistakes beginners make with Recursion"
1. "Provide advanced patterns and performance considerations for Recursion"

## Key Takeaways

- Master the core ideas of Recursion through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked cppreference docs for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
