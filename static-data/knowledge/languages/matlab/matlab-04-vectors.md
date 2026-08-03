---
{
  "title": "Vectors",
  "description": "Row and column vectors.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Create row vectors",
    "Create column vectors",
    "Use colon operator",
    "Index vectors"
  ],
  "knowledge_refs": [
    "matlab/matlab-04-vectors"
  ],
  "prerequisites": [
    "Matlab-03: Arithmetic Operations"
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

# MATLAB-04-VECTORS: Vectors

## Introduction

Row and column vectors. By the end of this lesson you will be able to: Create row vectors; Create column vectors; Use colon operator; Index vectors.

## Key Concepts

### 1. Create row vectors

Target: Create row vectors. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```matlab
v = [1 2 3];     % row
```
### 2. Create column vectors

Target: Create column vectors. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```matlab
v = [1; 2; 3];   % column
```
### 3. Use colon operator

Target: Use colon operator. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```matlab
x = 1:0.5:5;     % colon operator
```
### 4. Index vectors

Target: Index vectors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```matlab
v(2)             % second element
```

## Practice Questions

1. What is the key idea behind "Vectors"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Vectors with analogies and real-world examples"
1. "Show me common mistakes beginners make with Vectors"
1. "Provide advanced patterns and performance considerations for Vectors"

## Key Takeaways

- Master the core ideas of Vectors through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
