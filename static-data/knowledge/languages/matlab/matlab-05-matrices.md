---
{
  "title": "Matrices",
  "description": "Build and manipulate 2-D data.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Create matrices",
    "Index rows and columns",
    "Transpose matrices",
    "Get dimensions"
  ],
  "knowledge_refs": [
    "matlab/matlab-05-matrices"
  ],
  "prerequisites": [
    "Matlab-04: Vectors"
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

# MATLAB-05-MATRICES: Matrices

## Introduction

Build and manipulate 2-D data. By the end of this lesson you will be able to: Create matrices; Index rows and columns; Transpose matrices; Get dimensions.

## Key Concepts

### 1. Create matrices

Target: Create matrices. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```matlab
M = [1 2 3; 4 5 6];
```
### 2. Index rows and columns

Target: Index rows and columns. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```matlab
M(1, 2)          % row 1, col 2
```
### 3. Transpose matrices

Target: Transpose matrices. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```matlab
M.'             % transpose
```
### 4. Get dimensions

Target: Get dimensions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```matlab
size(M)
numel(M)
```

## Practice Questions

1. What is the key idea behind "Matrices"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Matrices with analogies and real-world examples"
1. "Show me common mistakes beginners make with Matrices"
1. "Provide advanced patterns and performance considerations for Matrices"

## Key Takeaways

- Master the core ideas of Matrices through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
