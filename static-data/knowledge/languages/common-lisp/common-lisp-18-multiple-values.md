---
{
  "title": "Multiple Values",
  "description": "Return and bind several values.",
  "type": "lesson",
  "order": 18,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Return multiple values",
    "Bind with multiple-value-bind",
    "Use values-list",
    "Capture all values"
  ],
  "knowledge_refs": [
    "common-lisp/common-lisp-18-multiple-values"
  ],
  "prerequisites": [
    "Common Lisp-17: Optional and Keyword Arguments"
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

# COMMON-LISP-18-MULTIPLE-VALUES: Multiple Values

## Introduction

Return and bind several values. By the end of this lesson you will be able to: Return multiple values; Bind with multiple-value-bind; Use values-list; Capture all values.

## Key Concepts

### 1. Return multiple values

Target: Return multiple values. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lisp
(defun divmod (a b) (values (floor a b) (mod a b)))
```
### 2. Bind with multiple-value-bind

Target: Bind with multiple-value-bind. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lisp
(multiple-value-bind (q r) (divmod 7 2)
  (list q r))
```
### 3. Use values-list

Target: Use values-list. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lisp
(values 1 2 3)
```
### 4. Capture all values

Target: Capture all values. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lisp
(multiple-value-list (divmod 7 2))
```

## Practice Questions

1. What is the key idea behind "Multiple Values"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Multiple Values with analogies and real-world examples"
1. "Show me common mistakes beginners make with Multiple Values"
1. "Provide advanced patterns and performance considerations for Multiple Values"

## Key Takeaways

- Master the core ideas of Multiple Values through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
