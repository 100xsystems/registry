---
{
  "title": "Code Performance",
  "description": "Profile and accelerate.",
  "type": "lesson",
  "order": 20,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use the profiler",
    "Preallocate arrays",
    "Use parfor",
    "Benchmark with tic/toc"
  ],
  "knowledge_refs": [
    "matlab/matlab-20-performance"
  ],
  "prerequisites": [
    "Matlab-19: Machine Learning"
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

# MATLAB-20-PERFORMANCE: Code Performance

## Introduction

Profile and accelerate. By the end of this lesson you will be able to: Use the profiler; Preallocate arrays; Use parfor; Benchmark with tic/toc.

## Key Concepts

### 1. Use the profiler

Target: Use the profiler. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```matlab
profile on
myFunction()
profile viewer
```
### 2. Preallocate arrays

Target: Preallocate arrays. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```matlab
result = zeros(1, 10000);
for i = 1:10000
    result(i) = i;
end
```
### 3. Use parfor

Target: Use parfor. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```matlab
parfor i = 1:100
    result(i) = heavyWork(i);
end
```
### 4. Benchmark with tic/toc

Target: Benchmark with tic/toc. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```matlab
tic; ...; toc
```

## Practice Questions

1. What is the key idea behind "Code Performance"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Code Performance with analogies and real-world examples"
1. "Show me common mistakes beginners make with Code Performance"
1. "Provide advanced patterns and performance considerations for Code Performance"

## Key Takeaways

- Master the core ideas of Code Performance through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
