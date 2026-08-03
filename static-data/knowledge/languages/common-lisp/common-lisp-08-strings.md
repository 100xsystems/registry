---
{
  "title": "Strings",
  "description": "String operations.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Concatenate strings",
    "Get length",
    "Search strings",
    "Format output"
  ],
  "knowledge_refs": [
    "common-lisp/common-lisp-08-strings"
  ],
  "prerequisites": [
    "Common Lisp-07: Loops"
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

# COMMON-LISP-08-STRINGS: Strings

## Introduction

String operations. By the end of this lesson you will be able to: Concatenate strings; Get length; Search strings; Format output.

## Key Concepts

### 1. Concatenate strings

Target: Concatenate strings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lisp
(concatenate 'string "Hello" " " "World")
```
### 2. Get length

Target: Get length. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lisp
(length "hello")
```
### 3. Search strings

Target: Search strings. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lisp
(search "world" "hello world")
```
### 4. Format output

Target: Format output. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lisp
(format nil "value: ~d" 42)
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
