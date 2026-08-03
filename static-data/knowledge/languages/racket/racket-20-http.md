---
{
  "title": "Web Servers",
  "description": "Serve HTTP with Racket.",
  "type": "lesson",
  "order": 20,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Start a web server",
    "Serve responses",
    "Define routes",
    "Serve JSON"
  ],
  "knowledge_refs": [
    "racket/racket-20-http"
  ],
  "prerequisites": [
    "Racket-19: GUI Programming"
  ],
  "references": [
    {
      "title": "Racket Documentation",
      "url": "https://docs.racket-lang.org/",
      "description": "Official docs"
    },
    {
      "title": "How to Design Programs",
      "url": "https://htdp.org/",
      "description": "The classic textbook"
    },
    {
      "title": "Racket Guide",
      "url": "https://docs.racket-lang.org/guide/",
      "description": "Official language guide"
    }
  ]
}
---

# RACKET-20-HTTP: Web Servers

## Introduction

Serve HTTP with Racket. By the end of this lesson you will be able to: Start a web server; Serve responses; Define routes; Serve JSON.

## Key Concepts

### 1. Start a web server

Target: Start a web server. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```racket
#lang racket
(require web-server/servlet
         web-server/servlet-env)

(define (start request)
  (response/xexpr #:mime-type "text/html"
                  '(html (body (p "Hello, World!")))))

(run-web-server start)(response/xexpr #:mime-type "application/json"
                (jsexpr->xexpr (list "key" "value")))
```
### 2. Serve responses

Target: Serve responses. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```racket
(serve/servlet start #:port 8080)
```
### 3. Define routes

Target: Define routes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```racket
(response/output #:mime-type "text/plain"
                (lambda (out) (display "hello" out)))
```
### 4. Serve JSON

Target: Serve JSON. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```racket
#lang racket
(require web-server/servlet
         web-server/servlet-env)

(define (start request)
  (response/xexpr #:mime-type "text/html"
                  '(html (body (p "Hello, World!")))))

(run-web-server start)(response/xexpr #:mime-type "application/json"
                (jsexpr->xexpr (list "key" "value")))
```

## Practice Questions

1. What is the key idea behind "Web Servers"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Web Servers with analogies and real-world examples"
1. "Show me common mistakes beginners make with Web Servers"
1. "Provide advanced patterns and performance considerations for Web Servers"

## Key Takeaways

- Master the core ideas of Web Servers through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
