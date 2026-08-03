---
{
  "title": "Optional and Keyword Arguments",
  "description": "Flexible function signatures.",
  "type": "lesson",
  "order": 17,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use &optional",
    "Use &rest",
    "Use &key",
    "Use &aux"
  ],
  "knowledge_refs": [
    "common-lisp/common-lisp-17-optional-keywords"
  ],
  "prerequisites": [
    "Common Lisp-16: Sequence Functions"
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

# COMMON-LISP-17-OPTIONAL-KEYWORDS: Optional and Keyword Arguments

## Introduction

Flexible function signatures. By the end of this lesson you will be able to: Use &optional; Use &rest; Use &key; Use &aux.

## Key Concepts

### 1. Use &optional

Target: Use &optional. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lisp
(defun f (a &optional (b 10)) (+ a b))
```
### 2. Use &rest

Target: Use &rest. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lisp
(defun sum (&rest nums) (reduce #'+ nums))
```
### 3. Use &key

Target: Use &key. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lisp
(defun configure (&key host (port 80)) (list host port))
```
### 4. Use &aux

Target: Use &aux. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lisp
(defun g (&optional (x 0) &rest rest) ...)
```

## Practice Questions

1. What is the key idea behind "Optional and Keyword Arguments"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Optional and Keyword Arguments with analogies and real-world examples"
1. "Show me common mistakes beginners make with Optional and Keyword Arguments"
1. "Provide advanced patterns and performance considerations for Optional and Keyword Arguments"

## Key Takeaways

- Master the core ideas of Optional and Keyword Arguments through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
