---
{
  "title": "Arithmetic Operations",
  "description": "Matrix vs element-wise math.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use basic arithmetic",
    "Understand matrix ops",
    "Use element-wise .*",
    "Use rounding functions"
  ],
  "knowledge_refs": [
    "matlab/matlab-03-arithmetic"
  ],
  "prerequisites": [
    "Matlab-02: Variables and Data Types"
  ],
  "references": [
    {
      "title": "MATLAB Documentation",
      "url": "https://www.mathworks.com/help/matlab/",
      "description": "Official docs"
    },
    {
      "title": "MATLAB Onramp",
      "url": "https://www.mathworks.com/learn/tutorials/matlab-onramp.html",
      "description": "Official intro course"
    },
    {
      "title": "MATLAB Central",
      "url": "https://www.mathworks.com/matlabcentral/",
      "description": "Community Q&A"
    }
  ]
}
---

# MATLAB-03-ARITHMETIC: Arithmetic Operations

## Introduction

Matrix vs element-wise math. By the end of this lesson you will be able to: Use basic arithmetic; Understand matrix ops; Use element-wise .*; Use rounding functions.

## Key Concepts

### 1. Use basic arithmetic

Target: Use basic arithmetic. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```matlab
a = 10; b = 3;
a + b
a - b
a * b
a / b
```
### 2. Understand matrix ops

Target: Understand matrix ops. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```matlab
A = [1 2; 3 4];
B = [5 6; 7 8];
A * B      % matrix multiply
```
### 3. Use element-wise .*

Target: Use element-wise .*. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```matlab
A .* B     % element-wise
```
### 4. Use rounding functions

Target: Use rounding functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```matlab
round(3.7)
floor(3.7)
ceil(3.2)
```

## Practice Questions

1. What is the key idea behind "Arithmetic Operations"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arithmetic Operations with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arithmetic Operations"
1. "Provide advanced patterns and performance considerations for Arithmetic Operations"

## Key Takeaways

- Master the core ideas of Arithmetic Operations through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
