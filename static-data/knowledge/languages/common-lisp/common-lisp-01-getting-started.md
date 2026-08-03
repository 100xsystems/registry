---
{
  "title": "Getting Started with Common Lisp",
  "description": "SBCL, REPL, and hello world.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install SBCL",
    "Use the REPL",
    "Evaluate expressions",
    "Write a first file"
  ],
  "knowledge_refs": [
    "common-lisp/common-lisp-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
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

# COMMON-LISP-01-GETTING-STARTED: Getting Started with Common Lisp

## Introduction

SBCL, REPL, and hello world. By the end of this lesson you will be able to: Install SBCL; Use the REPL; Evaluate expressions; Write a first file.

## Key Concepts

### 1. Install SBCL

Target: Install SBCL. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lisp
(format t "Hello, World!~%")
```
### 2. Use the REPL

Target: Use the REPL. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lisp
sbcl
* (+ 1 2)
3
```
### 3. Evaluate expressions

Target: Evaluate expressions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lisp
(defun hello () (format t "Hello!~%"))
(hello)
```
### 4. Write a first file

Target: Write a first file. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lisp
(format t "Hello, ~a!~%" "Ada")
```

## Practice Questions

1. What is the key idea behind "Getting Started with Common Lisp"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Common Lisp with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Common Lisp"
1. "Provide advanced patterns and performance considerations for Getting Started with Common Lisp"

## Key Takeaways

- Master the core ideas of Getting Started with Common Lisp through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
