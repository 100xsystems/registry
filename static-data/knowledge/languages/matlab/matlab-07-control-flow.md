---
{
  "title": "Control Flow",
  "description": "if, for, and while.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write if/elseif/else",
    "Use for loops",
    "Use while loops",
    "Use break and continue"
  ],
  "knowledge_refs": [
    "matlab/matlab-07-control-flow"
  ],
  "prerequisites": [
    "Matlab-06: Functions"
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

# MATLAB-07-CONTROL-FLOW: Control Flow

## Introduction

if, for, and while. By the end of this lesson you will be able to: Write if/elseif/else; Use for loops; Use while loops; Use break and continue.

## Key Concepts

### 1. Write if/elseif/else

Target: Write if/elseif/else. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```matlab
score = 85;
if score >= 90
    disp("A")
elseif score >= 80
    disp("B")
else
    disp("C")
end
```
### 2. Use for loops

Target: Use for loops. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```matlab
for i = 1:5
    disp(i)
end
```
### 3. Use while loops

Target: Use while loops. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```matlab
n = 0;
while n < 3
    n = n + 1;
end
```
### 4. Use break and continue

Target: Use break and continue. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```matlab
for i = 1:10
    if mod(i, 2) == 0
        continue
    end
    disp(i)
end
```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
