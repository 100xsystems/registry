---
{
  "title": "Input/Output",
  "description": "Read and write to the user.",
  "type": "lesson",
  "order": 11,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write with write/1",
    "Read with read/1",
    "Read lines",
    "Build interactive programs"
  ],
  "knowledge_refs": [
    "prolog/prolog-11-io"
  ],
  "prerequisites": [
    "Prolog-10: Findall and Setof"
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

# PROLOG-11-IO: Input/Output

## Introduction

Read and write to the user. By the end of this lesson you will be able to: Write with write/1; Read with read/1; Read lines; Build interactive programs.

## Key Concepts

### 1. Write with write/1

Target: Write with write/1. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```prolog
write("hello"), nl.
```
### 2. Read with read/1

Target: Read with read/1. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```prolog
read(X),
write(X).
```
### 3. Read lines

Target: Read lines. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```prolog
read_line_to_string(user_input, Line).
```
### 4. Build interactive programs

Target: Build interactive programs. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```prolog
loop :- write("> "),
         read_line_to_string(user_input, Line),
         write(Line), nl,
         loop.
```

## Practice Questions

1. What is the key idea behind "Input/Output"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Input/Output with analogies and real-world examples"
1. "Show me common mistakes beginners make with Input/Output"
1. "Provide advanced patterns and performance considerations for Input/Output"

## Key Takeaways

- Master the core ideas of Input/Output through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
