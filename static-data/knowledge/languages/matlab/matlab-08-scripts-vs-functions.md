---
{
  "title": "Scripts vs Functions",
  "description": "Choose the right file type.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write scripts",
    "Write functions",
    "Understand workspace sharing",
    "Use functions for reuse"
  ],
  "knowledge_refs": [
    "matlab/matlab-08-scripts-vs-functions"
  ],
  "prerequisites": [
    "Matlab-07: Control Flow"
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

# MATLAB-08-SCRIPTS-VS-FUNCTIONS: Scripts vs Functions

## Introduction

Choose the right file type. By the end of this lesson you will be able to: Write scripts; Write functions; Understand workspace sharing; Use functions for reuse.

## Key Concepts

### 1. Write scripts

Target: Write scripts. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```matlab
% script.m — shares the base workspace
x = 5;
y = x * 2;
```
### 2. Write functions

Target: Write functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```matlab
% function.m — has its own workspace
function y = doubleIt(x)
    y = x * 2;
end
```
### 3. Understand workspace sharing

Target: Understand workspace sharing. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```matlab
clear all   % clears workspace
```
### 4. Use functions for reuse

Target: Use functions for reuse. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```matlab
help myFunction
```

## Practice Questions

1. What is the key idea behind "Scripts vs Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Scripts vs Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Scripts vs Functions"
1. "Provide advanced patterns and performance considerations for Scripts vs Functions"

## Key Takeaways

- Master the core ideas of Scripts vs Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
