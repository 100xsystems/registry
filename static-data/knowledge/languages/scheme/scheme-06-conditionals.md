---
{
  "title": "Conditionals",
  "description": "if and cond.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use if",
    "Use cond",
    "Use boolean logic",
    "Use predicates"
  ],
  "knowledge_refs": [
    "scheme/scheme-06-conditionals"
  ],
  "prerequisites": [
    "Scheme-05: Lists"
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

# SCHEME-06-CONDITIONALS: Conditionals

## Introduction

if and cond. By the end of this lesson you will be able to: Use if; Use cond; Use boolean logic; Use predicates.

## Key Concepts

### 1. Use if

Target: Use if. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scheme
(if (> 3 2) "yes" "no")
```
### 2. Use cond

Target: Use cond. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scheme
(cond ((> x 0) "positive")
      ((< x 0) "negative")
      (else "zero"))
```
### 3. Use boolean logic

Target: Use boolean logic. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scheme
(and #t #f)
(or #t #f)
(not #t)
```
### 4. Use predicates

Target: Use predicates. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scheme
(number? 5)
(string? "hi")
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
