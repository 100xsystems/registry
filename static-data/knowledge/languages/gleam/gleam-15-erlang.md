---
{
  "title": "The Erlang Runtime",
  "description": "BEAM VM and OTP.",
  "type": "lesson",
  "order": 15,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand the BEAM",
    "Use processes",
    "Send messages",
    "Leverage OTP"
  ],
  "knowledge_refs": [
    "gleam/gleam-15-erlang"
  ],
  "prerequisites": [
    "Gleam-14: Generics"
  ],
  "references": [
    {
      "title": "Gleam Documentation",
      "url": "https://gleam.run/documentation/",
      "description": "Official docs"
    },
    {
      "title": "Gleam Language Tour",
      "url": "https://tour.gleam.run/",
      "description": "Interactive tour"
    },
    {
      "title": "Gleam Book",
      "url": "https://gleam.run/book/",
      "description": "The official book"
    }
  ]
}
---

# GLEAM-15-ERLANG: The Erlang Runtime

## Introduction

BEAM VM and OTP. By the end of this lesson you will be able to: Understand the BEAM; Use processes; Send messages; Leverage OTP.

## Key Concepts

### 1. Understand the BEAM

Target: Understand the BEAM. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gleam
import gleam/erlang/process

pub fn main() {
  let pid = process.new(fn() { io.println("hi") })
  process.send(pid, 42)
}
```
### 2. Use processes

Target: Use processes. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gleam
let subject = process.new_subject()
process.send(subject, "hello")
```
### 3. Send messages

Target: Send messages. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gleam
let mailbox = process.new_mailbox()
process.send(mailbox, 42)
```
### 4. Leverage OTP

Target: Leverage OTP. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gleam
// run on BEAM: gleam run --target erlang
```

## Practice Questions

1. What is the key idea behind "The Erlang Runtime"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain The Erlang Runtime with analogies and real-world examples"
1. "Show me common mistakes beginners make with The Erlang Runtime"
1. "Provide advanced patterns and performance considerations for The Erlang Runtime"

## Key Takeaways

- Master the core ideas of The Erlang Runtime through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
