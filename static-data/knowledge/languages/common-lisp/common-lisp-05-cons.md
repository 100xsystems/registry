---
{
  "title": "Cons Cells and Lists",
  "description": "The building blocks of Lisp data.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Build cons cells",
    "Use car and cdr",
    "Build lists",
    "Destructure lists"
  ],
  "knowledge_refs": [
    "common-lisp/common-lisp-05-cons"
  ],
  "prerequisites": [
    "Common Lisp-04: Functions"
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

# COMMON-LISP-05-CONS: Cons Cells and Lists

## Introduction

The building blocks of Lisp data. By the end of this lesson you will be able to: Build cons cells; Use car and cdr; Build lists; Destructure lists.

## Key Concepts

### 1. Build cons cells

Target: Build cons cells. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lisp
(cons 1 2)      ; (1 . 2)
(car '(1 2 3))   ; 1
(cdr '(1 2 3))   ; (2 3)
```
### 2. Use car and cdr

Target: Use car and cdr. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lisp
(list 1 2 3)    ; (1 2 3)
```
### 3. Build lists

Target: Build lists. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lisp
(cons 1 '(2 3)) ; (1 2 3)
```
### 4. Destructure lists

Target: Destructure lists. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lisp
(cadr '(1 2 3)) ; 2
(caddr '(1 2 3)) ; 3
```

## Practice Questions

1. What is the key idea behind "Cons Cells and Lists"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Cons Cells and Lists with analogies and real-world examples"
1. "Show me common mistakes beginners make with Cons Cells and Lists"
1. "Provide advanced patterns and performance considerations for Cons Cells and Lists"

## Key Takeaways

- Master the core ideas of Cons Cells and Lists through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
