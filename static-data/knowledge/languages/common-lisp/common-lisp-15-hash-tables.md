---
{
  "title": "Hash Tables",
  "description": "Key-value storage.",
  "type": "lesson",
  "order": 15,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create hash tables",
    "Set and get values",
    "Iterate entries",
    "Remove entries"
  ],
  "knowledge_refs": [
    "common-lisp/common-lisp-15-hash-tables"
  ],
  "prerequisites": [
    "Common Lisp-14: Packages"
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

# COMMON-LISP-15-HASH-TABLES: Hash Tables

## Introduction

Key-value storage. By the end of this lesson you will be able to: Create hash tables; Set and get values; Iterate entries; Remove entries.

## Key Concepts

### 1. Create hash tables

Target: Create hash tables. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lisp
(setf *ht* (make-hash-table :test #'equal))
```
### 2. Set and get values

Target: Set and get values. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lisp
(setf (gethash "key" *ht*) 42)
(gethash "key" *ht*)
```
### 3. Iterate entries

Target: Iterate entries. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lisp
(maphash (lambda (k v) (format t "~a: ~a~%" k v)) *ht*)
```
### 4. Remove entries

Target: Remove entries. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lisp
(remhash "key" *ht*)
```

## Practice Questions

1. What is the key idea behind "Hash Tables"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Hash Tables with analogies and real-world examples"
1. "Show me common mistakes beginners make with Hash Tables"
1. "Provide advanced patterns and performance considerations for Hash Tables"

## Key Takeaways

- Master the core ideas of Hash Tables through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
