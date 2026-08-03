---
{
  "title": "Functions",
  "description": "defun, lambdas, and higher-order.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define functions with defun",
    "Write lambdas",
    "Pass functions",
    "Use apply and funcall"
  ],
  "knowledge_refs": [
    "common-lisp/common-lisp-04-functions"
  ],
  "prerequisites": [
    "Common Lisp-03: Variables and Bindings"
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

# COMMON-LISP-04-FUNCTIONS: Functions

## Introduction

defun, lambdas, and higher-order. By the end of this lesson you will be able to: Define functions with defun; Write lambdas; Pass functions; Use apply and funcall.

## Key Concepts

### 1. Define functions with defun

Target: Define functions with defun. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lisp
(defun square (x) (* x x))
(square 5)
```
### 2. Write lambdas

Target: Write lambdas. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lisp
(mapcar (lambda (x) (* x 2)) '(1 2 3))
```
### 3. Pass functions

Target: Pass functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lisp
(funcall #'square 4)
(apply #'+ '(1 2 3))
```
### 4. Use apply and funcall

Target: Use apply and funcall. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lisp
(defun add (a b) (+ a b))
```

## Practice Questions

1. What is the key idea behind "Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions"
1. "Provide advanced patterns and performance considerations for Functions"

## Key Takeaways

- Master the core ideas of Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
