---
{
  "title": "Debugging Tools",
  "description": "trace, step, and inspect.",
  "type": "lesson",
  "order": 19,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Trace functions",
    "Step through code",
    "Inspect values",
    "Use describe"
  ],
  "knowledge_refs": [
    "common-lisp/common-lisp-19-debugging"
  ],
  "prerequisites": [
    "Common Lisp-18: Multiple Values"
  ],
  "references": [
    {
      "title": "Practical Common Lisp",
      "url": "https://gigamonkeys.com/book/",
      "description": "The classic online book"
    },
    {
      "title": "Common Lisp HyperSpec",
      "url": "http://www.lispworks.com/documentation/HyperSpec/Front/Contents.htm",
      "description": "Official standard reference"
    },
    {
      "title": "Common Lisp Cookbook",
      "url": "https://lispcookbook.github.io/cl-cookbook/",
      "description": "Community cookbook"
    }
  ]
}
---

# COMMON-LISP-19-DEBUGGING: Debugging Tools

## Introduction

trace, step, and inspect. By the end of this lesson you will be able to: Trace functions; Step through code; Inspect values; Use describe.

## Key Concepts

### 1. Trace functions

Target: Trace functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lisp
(trace square)
(square 5)
(untrace square)
```
### 2. Step through code

Target: Step through code. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lisp
(step (square 5))
```
### 3. Inspect values

Target: Inspect values. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lisp
(inspect '(1 2 3))
```
### 4. Use describe

Target: Use describe. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lisp
(describe #'square)
```

## Practice Questions

1. What is the key idea behind "Debugging Tools"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Debugging Tools with analogies and real-world examples"
1. "Show me common mistakes beginners make with Debugging Tools"
1. "Provide advanced patterns and performance considerations for Debugging Tools"

## Key Takeaways

- Master the core ideas of Debugging Tools through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
