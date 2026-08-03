---
{
  "title": "Lists",
  "description": "Immutable linked lists.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Build lists",
    "Cons with ::",
    "Use List functions",
    "Fold lists"
  ],
  "knowledge_refs": [
    "ocaml/ocaml-04-lists"
  ],
  "prerequisites": [
    "Ocaml-03: Functions"
  ],
  "references": [
    {
      "title": "OCaml Manual",
      "url": "https://ocaml.org/manual/",
      "description": "Official language manual"
    },
    {
      "title": "OCaml Tutorials",
      "url": "https://ocaml.org/docs",
      "description": "Official documentation"
    },
    {
      "title": "Real World OCaml",
      "url": "https://dev.realworldocaml.org/",
      "description": "Comprehensive book"
    }
  ]
}
---

# OCAML-04-LISTS: Lists

## Introduction

Immutable linked lists. By the end of this lesson you will be able to: Build lists; Cons with ::; Use List functions; Fold lists.

## Key Concepts

### 1. Build lists

Target: Build lists. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ocaml
let nums = [1; 2; 3]
let more = 0 :: nums
```
### 2. Cons with ::

Target: Cons with ::. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ocaml
List.map (fun n -> n * 2) [1; 2; 3]
```
### 3. Use List functions

Target: Use List functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ocaml
List.filter (fun n -> n > 2) [1; 2; 3; 4]
```
### 4. Fold lists

Target: Fold lists. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ocaml
List.fold_left (+) 0 [1; 2; 3]
```

## Practice Questions

1. What is the key idea behind "Lists"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Lists with analogies and real-world examples"
1. "Show me common mistakes beginners make with Lists"
1. "Provide advanced patterns and performance considerations for Lists"

## Key Takeaways

- Master the core ideas of Lists through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
