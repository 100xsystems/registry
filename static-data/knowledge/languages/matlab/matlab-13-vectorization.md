---
{
  "title": "Vectorization",
  "description": "Faster code without loops.",
  "type": "lesson",
  "order": 13,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Replace loops with vector ops",
    "Use element-wise operations",
    "Use logical indexing",
    "Avoid loops in hot paths"
  ],
  "knowledge_refs": [
    "matlab/matlab-13-vectorization"
  ],
  "prerequisites": [
    "Matlab-12: File I/O"
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

# MATLAB-13-VECTORIZATION: Vectorization

## Introduction

Faster code without loops. By the end of this lesson you will be able to: Replace loops with vector ops; Use element-wise operations; Use logical indexing; Avoid loops in hot paths.

## Key Concepts

### 1. Replace loops with vector ops

Target: Replace loops with vector ops. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```matlab
x = 1:100000;
y = x .* 2;        % no loop
```
### 2. Use element-wise operations

Target: Use element-wise operations. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```matlab
v = [1 2 3 4 5];
v(v > 2)          % logical indexing
```
### 3. Use logical indexing

Target: Use logical indexing. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```matlab
sum(x)
mean(x)
max(x)
```
### 4. Avoid loops in hot paths

Target: Avoid loops in hot paths. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```matlab
tic; result = x.^2; toc
```

## Practice Questions

1. What is the key idea behind "Vectorization"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Vectorization with analogies and real-world examples"
1. "Show me common mistakes beginners make with Vectorization"
1. "Provide advanced patterns and performance considerations for Vectorization"

## Key Takeaways

- Master the core ideas of Vectorization through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
