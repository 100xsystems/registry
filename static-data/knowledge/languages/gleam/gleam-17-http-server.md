---
{
  "title": "HTTP Servers",
  "description": "Build web services.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create an HTTP server",
    "Define routes",
    "Return JSON",
    "Handle requests"
  ],
  "knowledge_refs": [
    "gleam/gleam-17-http-server"
  ],
  "prerequisites": [
    "Gleam-16: Build a CLI Tool"
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

# GLEAM-17-HTTP-SERVER: HTTP Servers

## Introduction

Build web services. By the end of this lesson you will be able to: Create an HTTP server; Define routes; Return JSON; Handle requests.

## Key Concepts

### 1. Create an HTTP server

Target: Create an HTTP server. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gleam
import gleam/erlang/process
import mist

pub fn main() {
  let handler = fn(_req) {
    mist.new_response(200)
    |> mist.set_body("Hello, World!")
  }
  let _ = mist.new(handler)
  |> mist.port(8080)
  |> start
}
```
### 2. Define routes

Target: Define routes. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gleam
// routes via pattern matching on path
```
### 3. Return JSON

Target: Return JSON. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gleam
import gleam/json

let body = json.object([#("name", json.string("Ada"))])
|> json.to_string
```
### 4. Handle requests

Target: Handle requests. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gleam
mist.set_header("Content-Type", "application/json")
```

## Practice Questions

1. What is the key idea behind "HTTP Servers"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain HTTP Servers with analogies and real-world examples"
1. "Show me common mistakes beginners make with HTTP Servers"
1. "Provide advanced patterns and performance considerations for HTTP Servers"

## Key Takeaways

- Master the core ideas of HTTP Servers through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
