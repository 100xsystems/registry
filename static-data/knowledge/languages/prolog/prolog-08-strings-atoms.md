---
{
  "title": "Atoms, Strings, and Text",
  "description": "Text data in Prolog.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Distinguish atoms and strings",
    "Convert between them",
    "Concatenate text",
    "Compare text"
  ],
  "knowledge_refs": [
    "prolog/prolog-08-strings-atoms"
  ],
  "prerequisites": [
    "Prolog-07: Arithmetic"
  ],
  "references": [
    {
      "title": "SWI-Prolog Documentation",
      "url": "https://www.swi-prolog.org/pldoc/",
      "description": "Official SWI-Prolog docs"
    },
    {
      "title": "Learn Prolog Now!",
      "url": "https://www.learnprolognow.org/",
      "description": "The classic free textbook"
    },
    {
      "title": "Prolog Wiki",
      "url": "https://en.wikipedia.org/wiki/Prolog",
      "description": "Overview article"
    }
  ]
}
---

# PROLOG-08-STRINGS-ATOMS: Atoms, Strings, and Text

## Introduction

Text data in Prolog. By the end of this lesson you will be able to: Distinguish atoms and strings; Convert between them; Concatenate text; Compare text.

## Key Concepts

### 1. Distinguish atoms and strings

Target: Distinguish atoms and strings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```prolog
atom(hello).
string("hello").
```
### 2. Convert between them

Target: Convert between them. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```prolog
atom_string(hello, S).
```
### 3. Concatenate text

Target: Concatenate text. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```prolog
string_concat("Hello", " World", Full).
```
### 4. Compare text

Target: Compare text. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```prolog
atom_length(hello, L).
```

## Practice Questions

1. What is the key idea behind "Atoms, Strings, and Text"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Atoms, Strings, and Text with analogies and real-world examples"
1. "Show me common mistakes beginners make with Atoms, Strings, and Text"
1. "Provide advanced patterns and performance considerations for Atoms, Strings, and Text"

## Key Takeaways

- Master the core ideas of Atoms, Strings, and Text through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
