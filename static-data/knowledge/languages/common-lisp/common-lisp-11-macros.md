---
{
  "title": "Macros",
  "description": "Code generation and DSLs.",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write defmacro",
    "Use backquote",
    "Manage variable capture",
    "Build DSLs"
  ],
  "knowledge_refs": [
    "common-lisp/common-lisp-11-macros"
  ],
  "prerequisites": [
    "Common Lisp-10: CLOS: Classes and Objects"
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

# COMMON-LISP-11-MACROS: Macros

## Introduction

Code generation and DSLs. By the end of this lesson you will be able to: Write defmacro; Use backquote; Manage variable capture; Build DSLs.

## Key Concepts

### 1. Write defmacro

Target: Write defmacro. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lisp
(defmacro twice (expr)
  '(progn ,expr ,expr))
```
### 2. Use backquote

Target: Use backquote. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lisp
(defmacro my-when (test &body body)
  \`(if ,test (progn ,@body)))
```
### 3. Manage variable capture

Target: Manage variable capture. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lisp
(defmacro incf2 (var) \`(setf ,var (+ ,var 2)))
```
### 4. Build DSLs

Target: Build DSLs. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lisp
(defmacro unless (test &body body)
  \`(if (not ,test) (progn ,@body)))
```

## Practice Questions

1. What is the key idea behind "Macros"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Macros with analogies and real-world examples"
1. "Show me common mistakes beginners make with Macros"
1. "Provide advanced patterns and performance considerations for Macros"

## Key Takeaways

- Master the core ideas of Macros through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
