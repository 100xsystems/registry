---
{
  "title": "File I/O",
  "description": "Read and write data files.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read text files",
    "Write text files",
    "Load and save MAT files",
    "Use readtable"
  ],
  "knowledge_refs": [
    "matlab/matlab-12-file-io"
  ],
  "prerequisites": [
    "Matlab-11: Plotting"
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

# MATLAB-12-FILE-IO: File I/O

## Introduction

Read and write data files. By the end of this lesson you will be able to: Read text files; Write text files; Load and save MAT files; Use readtable.

## Key Concepts

### 1. Read text files

Target: Read text files. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```matlab
data = load("data.txt");
```
### 2. Write text files

Target: Write text files. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```matlab
data = readmatrix("data.csv");
```
### 3. Load and save MAT files

Target: Load and save MAT files. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```matlab
save("mydata.mat", "x", "y")
load("mydata.mat")
```
### 4. Use readtable

Target: Use readtable. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```matlab
writematrix(M, "out.csv")
```

## Practice Questions

1. What is the key idea behind "File I/O"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain File I/O with analogies and real-world examples"
1. "Show me common mistakes beginners make with File I/O"
1. "Provide advanced patterns and performance considerations for File I/O"

## Key Takeaways

- Master the core ideas of File I/O through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
