---
{
  "title": "Conditions and Restarts",
  "description": "Signals and handlers.",
  "type": "lesson",
  "order": 12,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Signal conditions",
    "Handle with handler-case",
    "Use restarts",
    "Write custom conditions"
  ],
  "knowledge_refs": [
    "common-lisp/common-lisp-12-conditions"
  ],
  "prerequisites": [
    "Common Lisp-11: Macros"
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

# COMMON-LISP-12-CONDITIONS: Conditions and Restarts

## Introduction

Signals and handlers. By the end of this lesson you will be able to: Signal conditions; Handle with handler-case; Use restarts; Write custom conditions.

## Key Concepts

### 1. Signal conditions

Target: Signal conditions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lisp
(handler-case (/ 10 0)
  (division-by-zero () "caught"))
```
### 2. Handle with handler-case

Target: Handle with handler-case. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lisp
(define-condition my-error (error)
  ((message :initarg :message :reader err-msg)))
```
### 3. Use restarts

Target: Use restarts. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lisp
(signal (make-condition 'my-error :message "boom"))
```
### 4. Write custom conditions

Target: Write custom conditions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lisp
(restart-case (error "fail")
  (retry () "retried"))
```

## Practice Questions

1. What is the key idea behind "Conditions and Restarts"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Conditions and Restarts with analogies and real-world examples"
1. "Show me common mistakes beginners make with Conditions and Restarts"
1. "Provide advanced patterns and performance considerations for Conditions and Restarts"

## Key Takeaways

- Master the core ideas of Conditions and Restarts through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
