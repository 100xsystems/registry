---
{
  "title": "Loops",
  "description": "do, loop, and iteration.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use loop macro",
    "Use dolist",
    "Use dotimes",
    "Use do"
  ],
  "knowledge_refs": [
    "common-lisp/common-lisp-07-loops"
  ],
  "prerequisites": [
    "Common Lisp-06: Conditionals"
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

# COMMON-LISP-07-LOOPS: Loops

## Introduction

do, loop, and iteration. By the end of this lesson you will be able to: Use loop macro; Use dolist; Use dotimes; Use do.

## Key Concepts

### 1. Use loop macro

Target: Use loop macro. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lisp
(loop for i from 1 to 5 do (format t "~a " i))
```
### 2. Use dolist

Target: Use dolist. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lisp
(dolist (item '(a b c)) (format t "~a " item))
```
### 3. Use dotimes

Target: Use dotimes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lisp
(dotimes (i 3) (format t "~a " i))
```
### 4. Use do

Target: Use do. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lisp
(loop for i from 1 to 10
      when (evenp i)
      collect i)
```

## Practice Questions

1. What is the key idea behind "Loops"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Loops with analogies and real-world examples"
1. "Show me common mistakes beginners make with Loops"
1. "Provide advanced patterns and performance considerations for Loops"

## Key Takeaways

- Master the core ideas of Loops through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
