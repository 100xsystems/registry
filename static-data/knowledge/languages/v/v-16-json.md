---
{
  "title": "JSON",
  "description": "Encode and decode JSON.",
  "type": "lesson",
  "order": 16,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Encode structs to JSON",
    "Decode JSON to structs",
    "Handle optional fields",
    "Work with raw JSON"
  ],
  "knowledge_refs": [
    "v/v-16-json"
  ],
  "prerequisites": [
    "V-15: Web Development with vweb"
  ],
  "references": [
    {
      "title": "V Documentation",
      "url": "https://docs.vlang.io/",
      "description": "Official docs"
    },
    {
      "title": "V Manual",
      "url": "https://docs.vlang.io/introduction.html",
      "description": "Language manual"
    },
    {
      "title": "V Language GitHub",
      "url": "https://github.com/vlang/v",
      "description": "Source code"
    }
  ]
}
---

# V-16-JSON: JSON

## Introduction

Encode and decode JSON. By the end of this lesson you will be able to: Encode structs to JSON; Decode JSON to structs; Handle optional fields; Work with raw JSON.

## Key Concepts

### 1. Encode structs to JSON

Target: Encode structs to JSON. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```v
import json

struct User {
	name string
	age int
}

u := User{"Ada", 36}
println(json.encode(u))
```
### 2. Decode JSON to structs

Target: Decode JSON to structs. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```v
data := json.decode(User, '{"name": "Ada", "age": 36}') or { panic(err) }
println(data.name)
```
### 3. Handle optional fields

Target: Handle optional fields. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```v
struct Config {
	verbose bool
	port int
}
```
### 4. Work with raw JSON

Target: Work with raw JSON. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```v
raw := json.raw_decode('{"a": 1}') or { panic(err) }
println(raw)
```

## Practice Questions

1. What is the key idea behind "JSON"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain JSON with analogies and real-world examples"
1. "Show me common mistakes beginners make with JSON"
1. "Provide advanced patterns and performance considerations for JSON"

## Key Takeaways

- Master the core ideas of JSON through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
