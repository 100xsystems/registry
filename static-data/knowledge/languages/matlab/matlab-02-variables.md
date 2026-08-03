---
{
  "title": "Variables and Data Types",
  "description": "Numbers, strings, and logicals.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Create numeric variables",
    "Create strings and char arrays",
    "Use logical values",
    "Use who and whos"
  ],
  "knowledge_refs": [
    "matlab/matlab-02-variables"
  ],
  "prerequisites": [
    "Matlab-01: Getting Started with MATLAB"
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

# MATLAB-02-VARIABLES: Variables and Data Types

## Introduction

Numbers, strings, and logicals. By the end of this lesson you will be able to: Create numeric variables; Create strings and char arrays; Use logical values; Use who and whos.

## Key Concepts

### 1. Create numeric variables

Target: Create numeric variables. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```matlab
x = 42;
y = 3.14;
```
### 2. Create strings and char arrays

Target: Create strings and char arrays. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```matlab
s = "hello";
c = char("hello");
```
### 3. Use logical values

Target: Use logical values. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```matlab
flag = true;
notFlag = false;
```
### 4. Use who and whos

Target: Use who and whos. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```matlab
who
exists("x")
```

## Practice Questions

1. What is the key idea behind "Variables and Data Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables and Data Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables and Data Types"
1. "Provide advanced patterns and performance considerations for Variables and Data Types"

## Key Takeaways

- Master the core ideas of Variables and Data Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
