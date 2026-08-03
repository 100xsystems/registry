---
{
  "title": "Sequence Functions",
  "description": "find, position, count, subseq.",
  "type": "lesson",
  "order": 16,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Find elements",
    "Get positions",
    "Count occurrences",
    "Slice sequences"
  ],
  "knowledge_refs": [
    "common-lisp/common-lisp-16-sequences"
  ],
  "prerequisites": [
    "Common Lisp-15: Hash Tables"
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

# COMMON-LISP-16-SEQUENCES: Sequence Functions

## Introduction

find, position, count, subseq. By the end of this lesson you will be able to: Find elements; Get positions; Count occurrences; Slice sequences.

## Key Concepts

### 1. Find elements

Target: Find elements. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lisp
(find 3 '(1 2 3 4))
```
### 2. Get positions

Target: Get positions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lisp
(position #\o "hello")
```
### 3. Count occurrences

Target: Count occurrences. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lisp
(count #\l "hello")
```
### 4. Slice sequences

Target: Slice sequences. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lisp
(subseq "hello world" 0 5)
```

## Practice Questions

1. What is the key idea behind "Sequence Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Sequence Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Sequence Functions"
1. "Provide advanced patterns and performance considerations for Sequence Functions"

## Key Takeaways

- Master the core ideas of Sequence Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
