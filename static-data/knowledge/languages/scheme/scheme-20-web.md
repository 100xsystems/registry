---
{
  "title": "Web Development",
  "description": "Serve web pages.",
  "type": "lesson",
  "order": 20,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create HTTP servers",
    "Serve HTML",
    "Handle routes",
    "Read request data"
  ],
  "knowledge_refs": [
    "scheme/scheme-20-web"
  ],
  "prerequisites": [
    "Scheme-19: Interfacing with C"
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

# SCHEME-20-WEB: Web Development

## Introduction

Serve web pages. By the end of this lesson you will be able to: Create HTTP servers; Serve HTML; Handle routes; Read request data.

## Key Concepts

### 1. Create HTTP servers

Target: Create HTTP servers. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scheme
;; Guile:
(use-modules (web server) (web response))
```
### 2. Serve HTML

Target: Serve HTML. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scheme
(define (handler request body)
  (values (build-response #:code 200)
          (string->utf8 "Hello, World!")))
```
### 3. Handle routes

Target: Handle routes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scheme
(run-server handler)
```
### 4. Read request data

Target: Read request data. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scheme
(define (handler req body)
  (values (build-response #:content-type 'text/html)
          (string->utf8 "<h1>Hello</h1>")))
```

## Practice Questions

1. What is the key idea behind "Web Development"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Web Development with analogies and real-world examples"
1. "Show me common mistakes beginners make with Web Development"
1. "Provide advanced patterns and performance considerations for Web Development"

## Key Takeaways

- Master the core ideas of Web Development through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
