---
{
  "title": "Strings",
  "description": "String operations.",
  "type": "lesson",
  "order": 9,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Concatenate strings",
    "Get string length",
    "Convert cases",
    "Format strings"
  ],
  "knowledge_refs": [
    "scheme/scheme-09-strings"
  ],
  "prerequisites": [
    "Scheme-08: Higher-Order Functions"
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

# SCHEME-09-STRINGS: Strings

## Introduction

String operations. By the end of this lesson you will be able to: Concatenate strings; Get string length; Convert cases; Format strings.

## Key Concepts

### 1. Concatenate strings

Target: Concatenate strings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scheme
(string-append "Hello" " " "World")
```
### 2. Get string length

Target: Get string length. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scheme
(string-length "hello")
```
### 3. Convert cases

Target: Convert cases. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scheme
(string-upcase "hi")
```
### 4. Format strings

Target: Format strings. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scheme
(number->string 42)
```

## Practice Questions

1. What is the key idea behind "Strings"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Strings with analogies and real-world examples"
1. "Show me common mistakes beginners make with Strings"
1. "Provide advanced patterns and performance considerations for Strings"

## Key Takeaways

- Master the core ideas of Strings through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
