---
{
  "title": "Functions",
  "description": "Write .m functions.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write function files",
    "Use multiple outputs",
    "Pass arguments",
    "Use local functions"
  ],
  "knowledge_refs": [
    "matlab/matlab-06-functions"
  ],
  "prerequisites": [
    "Matlab-05: Matrices"
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

# MATLAB-06-FUNCTIONS: Functions

## Introduction

Write .m functions. By the end of this lesson you will be able to: Write function files; Use multiple outputs; Pass arguments; Use local functions.

## Key Concepts

### 1. Write function files

Target: Write function files. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```matlab
function y = square(x)
    y = x * x;
end
```
### 2. Use multiple outputs

Target: Use multiple outputs. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```matlab
function [summ, prod] = stats(a, b)
    summ = a + b;
    prod = a * b;
end
```
### 3. Pass arguments

Target: Pass arguments. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```matlab
[s, p] = stats(2, 3);
```
### 4. Use local functions

Target: Use local functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```matlab
function y = add(a, b)
    y = a + b;
end
```

## Practice Questions

1. What is the key idea behind "Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions"
1. "Provide advanced patterns and performance considerations for Functions"

## Key Takeaways

- Master the core ideas of Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
