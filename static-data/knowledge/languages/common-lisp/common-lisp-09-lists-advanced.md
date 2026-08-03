---
{
  "title": "List Manipulation",
  "description": "mapcar, remove, and sorting.",
  "type": "lesson",
  "order": 9,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use mapcar",
    "Filter with remove-if",
    "Sort lists",
    "Use reduce"
  ],
  "knowledge_refs": [
    "common-lisp/common-lisp-09-lists-advanced"
  ],
  "prerequisites": [
    "Common Lisp-08: Strings"
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

# COMMON-LISP-09-LISTS-ADVANCED: List Manipulation

## Introduction

mapcar, remove, and sorting. By the end of this lesson you will be able to: Use mapcar; Filter with remove-if; Sort lists; Use reduce.

## Key Concepts

### 1. Use mapcar

Target: Use mapcar. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lisp
(mapcar #'1+ '(1 2 3))
```
### 2. Filter with remove-if

Target: Filter with remove-if. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lisp
(remove-if #'oddp '(1 2 3 4 5))
```
### 3. Sort lists

Target: Sort lists. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lisp
(sort '(3 1 2) #'<)
```
### 4. Use reduce

Target: Use reduce. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lisp
(reduce #'+ '(1 2 3 4))
```

## Practice Questions

1. What is the key idea behind "List Manipulation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain List Manipulation with analogies and real-world examples"
1. "Show me common mistakes beginners make with List Manipulation"
1. "Provide advanced patterns and performance considerations for List Manipulation"

## Key Takeaways

- Master the core ideas of List Manipulation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
