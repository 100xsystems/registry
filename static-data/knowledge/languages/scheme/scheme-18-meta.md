---
{
  "title": "Metacircular Evaluators",
  "description": "Write an interpreter.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand eval and apply",
    "Build a mini interpreter",
    "Handle environments",
    "Extend the language"
  ],
  "knowledge_refs": [
    "scheme/scheme-18-meta"
  ],
  "prerequisites": [
    "Scheme-17: Symbolic Computation"
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

# SCHEME-18-META: Metacircular Evaluators

## Introduction

Write an interpreter. By the end of this lesson you will be able to: Understand eval and apply; Build a mini interpreter; Handle environments; Extend the language.

## Key Concepts

### 1. Understand eval and apply

Target: Understand eval and apply. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scheme
(define (my-eval exp env)
  (cond ((number? exp) exp)
        ((symbol? exp) (lookup exp env))
        ((eq? (car exp) 'quote) (cadr exp))
        ((eq? (car exp) 'if) (if (my-eval (cadr exp) env)
                                 (my-eval (caddr exp) env)
                                 (my-eval (cadddr exp) env)))
        ((eq? (car exp) 'lambda) (list 'closure (cadr exp) (cddr exp) env))
        (else (apply-proc (my-eval (car exp) env)
                          (map (lambda (e) (my-eval e env)) (cdr exp))))))
```
### 2. Build a mini interpreter

Target: Build a mini interpreter. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scheme
(define (apply-proc proc args) (car proc))  ; simplified
```
### 3. Handle environments

Target: Handle environments. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scheme
(define env '((x . 10)))
```
### 4. Extend the language

Target: Extend the language. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scheme
(lookup 'x env)
```

## Practice Questions

1. What is the key idea behind "Metacircular Evaluators"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Metacircular Evaluators with analogies and real-world examples"
1. "Show me common mistakes beginners make with Metacircular Evaluators"
1. "Provide advanced patterns and performance considerations for Metacircular Evaluators"

## Key Takeaways

- Master the core ideas of Metacircular Evaluators through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
