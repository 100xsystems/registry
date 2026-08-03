---
{
  "title": "Packages",
  "description": "Namespaces and symbols.",
  "type": "lesson",
  "order": 14,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define packages",
    "Export symbols",
    "Use package qualifiers",
    "Manage imports"
  ],
  "knowledge_refs": [
    "common-lisp/common-lisp-14-packages"
  ],
  "prerequisites": [
    "Common Lisp-13: Input/Output"
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

# COMMON-LISP-14-PACKAGES: Packages

## Introduction

Namespaces and symbols. By the end of this lesson you will be able to: Define packages; Export symbols; Use package qualifiers; Manage imports.

## Key Concepts

### 1. Define packages

Target: Define packages. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lisp
(defpackage :my-app
  (:use :cl)
  (:export :main))
```
### 2. Export symbols

Target: Export symbols. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lisp
(in-package :my-app)
```
### 3. Use package qualifiers

Target: Use package qualifiers. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lisp
(defun main () (format t "hello~%"))
```
### 4. Manage imports

Target: Manage imports. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lisp
my-app:main
```

## Practice Questions

1. What is the key idea behind "Packages"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Packages with analogies and real-world examples"
1. "Show me common mistakes beginners make with Packages"
1. "Provide advanced patterns and performance considerations for Packages"

## Key Takeaways

- Master the core ideas of Packages through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
