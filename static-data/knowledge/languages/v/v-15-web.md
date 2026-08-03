---
{
  "title": "Web Development with vweb",
  "description": "Build HTTP apps.",
  "type": "lesson",
  "order": 15,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create a vweb app",
    "Define routes",
    "Serve HTML",
    "Handle POST"
  ],
  "knowledge_refs": [
    "v/v-15-web"
  ],
  "prerequisites": [
    "V-14: Concurrency"
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

# V-15-WEB: Web Development with vweb

## Introduction

Build HTTP apps. By the end of this lesson you will be able to: Create a vweb app; Define routes; Serve HTML; Handle POST.

## Key Concepts

### 1. Create a vweb app

Target: Create a vweb app. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```v
import vweb

struct App {
	vweb.Context
}

fn main() {
	vweb.run(App{}, 8080)
}

fn (app &App) index() vweb.Result {
	return app.text("Hello, World!")
}
```
### 2. Define routes

Target: Define routes. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```v
fn (app &App) hello(name string) vweb.Result {
	return app.text("Hello, " + name)
}
```
### 3. Serve HTML

Target: Serve HTML. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```v
v run .
curl http://localhost:8080
```
### 4. Handle POST

Target: Handle POST. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```v
fn (mut app App) submit() vweb.Result {
	name := app.form["name"]
	return app.text("hi " + name)
}
```

## Practice Questions

1. What is the key idea behind "Web Development with vweb"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Web Development with vweb with analogies and real-world examples"
1. "Show me common mistakes beginners make with Web Development with vweb"
1. "Provide advanced patterns and performance considerations for Web Development with vweb"

## Key Takeaways

- Master the core ideas of Web Development with vweb through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
