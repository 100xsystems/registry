---
{
  "title": "Variables and Bindings",
  "description": "defvar, let, and scope.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define global variables",
    "Bind with let",
    "Use setf to mutate",
    "Understand dynamic scope"
  ],
  "knowledge_refs": [
    "common-lisp/common-lisp-03-variables"
  ],
  "prerequisites": [
    "Common Lisp-02: S-expressions and Forms"
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

# COMMON-LISP-03-VARIABLES: Variables and Bindings

## Introduction

defvar, let, and scope. By the end of this lesson you will be able to: Define global variables; Bind with let; Use setf to mutate; Understand dynamic scope.

## Key Concepts

### 1. Define global variables

Target: Define global variables. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lisp
(defvar *name* "Ada")
*name*
```
### 2. Bind with let

Target: Bind with let. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lisp
(let ((x 10) (y 20)) (+ x y))
```
### 3. Use setf to mutate

Target: Use setf to mutate. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lisp
(defvar *count* 0)
(setf *count* (+ *count* 1))
```
### 4. Understand dynamic scope

Target: Understand dynamic scope. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lisp
(let ((x 5))
  (setf x 10)
  x)
```

## Practice Questions

1. What is the key idea behind "Variables and Bindings"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables and Bindings with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables and Bindings"
1. "Provide advanced patterns and performance considerations for Variables and Bindings"

## Key Takeaways

- Master the core ideas of Variables and Bindings through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
