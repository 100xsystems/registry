---
{
  "title": "Ranges and Algorithms",
  "description": "Lazy iteration and std.algorithm.",
  "type": "lesson",
  "order": 12,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand range concept",
    "Chain algorithms",
    "Use filter and map",
    "Build lazy pipelines"
  ],
  "knowledge_refs": [
    "d/d-12-ranges"
  ],
  "prerequisites": [
    "D-11: Exceptions"
  ],
  "references": [
    {
      "title": "D Language Reference",
      "url": "https://dlang.org/spec/spec.html",
      "description": "Official language spec"
    },
    {
      "title": "D Programming Tour",
      "url": "https://tour.dlang.org/",
      "description": "Interactive language tour"
    },
    {
      "title": "D Wiki",
      "url": "https://wiki.dlang.org/",
      "description": "Community wiki"
    },
    {
      "title": "DUB Package Manager",
      "url": "https://code.dlang.org/",
      "description": "Package registry"
    }
  ]
}
---

# D-12-RANGES: Ranges and Algorithms

## Introduction

Lazy iteration and std.algorithm. By the end of this lesson you will be able to: Understand range concept; Chain algorithms; Use filter and map; Build lazy pipelines.

## Key Concepts

### 1. Understand range concept

Target: Understand range concept. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```d
import std.stdio;
import std.algorithm;
import std.range;

void main() {
    auto r = iota(1, 11).filter!(n => n % 2 == 0).map!(n => n * n);
    writeln(r);
}
```
### 2. Chain algorithms

Target: Chain algorithms. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```d
auto sum = iota(1, 101).sum;
writeln(sum);
```
### 3. Use filter and map

Target: Use filter and map. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```d
int[] arr = [3, 1, 4, 1, 5];
arr.sort();
writeln(arr);
```
### 4. Build lazy pipelines

Target: Build lazy pipelines. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```d
auto first3 = iota(1, 100).take(3);
writeln(first3);
```

## Practice Questions

1. What is the key idea behind "Ranges and Algorithms"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Ranges and Algorithms with analogies and real-world examples"
1. "Show me common mistakes beginners make with Ranges and Algorithms"
1. "Provide advanced patterns and performance considerations for Ranges and Algorithms"

## Key Takeaways

- Master the core ideas of Ranges and Algorithms through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
