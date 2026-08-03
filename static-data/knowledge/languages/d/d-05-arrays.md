---
{
  "title": "Arrays and Slices",
  "description": "Dynamic arrays and slice semantics.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create dynamic arrays",
    "Slice arrays",
    "Append elements",
    "Iterate arrays"
  ],
  "knowledge_refs": [
    "d/d-05-arrays"
  ],
  "prerequisites": [
    "D-04: Strings"
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

# D-05-ARRAYS: Arrays and Slices

## Introduction

Dynamic arrays and slice semantics. By the end of this lesson you will be able to: Create dynamic arrays; Slice arrays; Append elements; Iterate arrays.

## Key Concepts

### 1. Create dynamic arrays

Target: Create dynamic arrays. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```d
import std.stdio;

void main() {
    int[] nums = [1, 2, 3];
    nums ~= 4;
    writeln(nums);
}
```
### 2. Slice arrays

Target: Slice arrays. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```d
int[] a = [1, 2, 3, 4, 5];
int[] b = a[1..3];
writeln(b);   // [2, 3]
```
### 3. Append elements

Target: Append elements. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```d
foreach (i, n; nums) {
    writeln(i, ": ", n);
}
```
### 4. Iterate arrays

Target: Iterate arrays. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```d
int[] arr = new int[100];
arr[] = 5;   // fill all
```

## Practice Questions

1. What is the key idea behind "Arrays and Slices"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arrays and Slices with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arrays and Slices"
1. "Provide advanced patterns and performance considerations for Arrays and Slices"

## Key Takeaways

- Master the core ideas of Arrays and Slices through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
