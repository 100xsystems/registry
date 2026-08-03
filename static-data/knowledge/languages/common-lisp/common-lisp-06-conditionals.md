---
{
  "title": "Conditionals",
  "description": "if, cond, and when.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use if",
    "Use cond",
    "Use when and unless",
    "Combine conditions"
  ],
  "knowledge_refs": [
    "common-lisp/common-lisp-06-conditionals"
  ],
  "prerequisites": [
    "Common Lisp-05: Cons Cells and Lists"
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

# COMMON-LISP-06-CONDITIONALS: Conditionals

## Introduction

if, cond, and when. By the end of this lesson you will be able to: Use if; Use cond; Use when and unless; Combine conditions.

## Key Concepts

### 1. Use if

Target: Use if. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lisp
(if (> 3 2) "yes" "no")
```
### 2. Use cond

Target: Use cond. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lisp
(cond ((> x 0) "positive")
      ((< x 0) "negative")
      (t "zero"))
```
### 3. Use when and unless

Target: Use when and unless. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lisp
(when (> x 0) (format t "positive~%"))
```
### 4. Combine conditions

Target: Combine conditions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lisp
(unless (= x 0) (format t "not zero~%"))
```

## Practice Questions

1. What is the key idea behind "Conditionals"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Conditionals with analogies and real-world examples"
1. "Show me common mistakes beginners make with Conditionals"
1. "Provide advanced patterns and performance considerations for Conditionals"

## Key Takeaways

- Master the core ideas of Conditionals through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
