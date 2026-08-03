---
{
  "title": "S-expressions and Forms",
  "description": "Parentheses, symbols, and evaluation.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Understand S-expressions",
    "Quote data with quote",
    "Distinguish code and data",
    "Use symbols"
  ],
  "knowledge_refs": [
    "common-lisp/common-lisp-02-forms"
  ],
  "prerequisites": [
    "Common Lisp-01: Getting Started with Common Lisp"
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

# COMMON-LISP-02-FORMS: S-expressions and Forms

## Introduction

Parentheses, symbols, and evaluation. By the end of this lesson you will be able to: Understand S-expressions; Quote data with quote; Distinguish code and data; Use symbols.

## Key Concepts

### 1. Understand S-expressions

Target: Understand S-expressions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lisp
(+ 1 2)       ; 3
(- 10 4)      ; 6
(* 3 4)        ; 12
```
### 2. Quote data with quote

Target: Quote data with quote. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lisp
'(a b c)      ; quoted list
```
### 3. Distinguish code and data

Target: Distinguish code and data. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lisp
'symbol       ; the symbol itself
```
### 4. Use symbols

Target: Use symbols. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lisp
(list 1 2 3)  ; (1 2 3)
```

## Practice Questions

1. What is the key idea behind "S-expressions and Forms"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain S-expressions and Forms with analogies and real-world examples"
1. "Show me common mistakes beginners make with S-expressions and Forms"
1. "Provide advanced patterns and performance considerations for S-expressions and Forms"

## Key Takeaways

- Master the core ideas of S-expressions and Forms through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
