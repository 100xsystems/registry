---
{
  "title": "Expressions and Values",
  "description": "Prefix notation and evaluation.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use prefix notation",
    "Evaluate arithmetic",
    "Use literals",
    "Quote expressions"
  ],
  "knowledge_refs": [
    "scheme/scheme-02-expressions"
  ],
  "prerequisites": [
    "Scheme-01: Getting Started with Scheme"
  ],
  "references": [
    {
      "title": "Scheme Reports",
      "url": "https://small.r7rs.org/",
      "description": "The R7RS specification"
    },
    {
      "title": "Structure and Interpretation of Computer Programs",
      "url": "https://mitp-press.mit.edu/sites/default/files/sicp/full-text/book/book.html",
      "description": "SICP — the classic book"
    },
    {
      "title": "The Scheme Programming Language",
      "url": "https://www.scheme.com/tspl4/",
      "description": "Dybvig's book"
    }
  ]
}
---

# SCHEME-02-EXPRESSIONS: Expressions and Values

## Introduction

Prefix notation and evaluation. By the end of this lesson you will be able to: Use prefix notation; Evaluate arithmetic; Use literals; Quote expressions.

## Key Concepts

### 1. Use prefix notation

Target: Use prefix notation. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scheme
(+ 1 2)
(- 10 4)
(* 3 4)
(/ 10 2)
```
### 2. Evaluate arithmetic

Target: Evaluate arithmetic. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scheme
(sqrt 16)
```
### 3. Use literals

Target: Use literals. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scheme
'(1 2 3)
```
### 4. Quote expressions

Target: Quote expressions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scheme
(display (* 2 (+ 3 4)))
```

## Practice Questions

1. What is the key idea behind "Expressions and Values"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Expressions and Values with analogies and real-world examples"
1. "Show me common mistakes beginners make with Expressions and Values"
1. "Provide advanced patterns and performance considerations for Expressions and Values"

## Key Takeaways

- Master the core ideas of Expressions and Values through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
