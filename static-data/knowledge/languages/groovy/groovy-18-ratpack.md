---
{
  "title": "Ratpack and Microservices",
  "description": "Lightweight web services.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Set up Ratpack",
    "Define routes",
    "Handle JSON",
    "Build APIs"
  ],
  "knowledge_refs": [
    "groovy/groovy-18-ratpack"
  ],
  "prerequisites": [
    "Groovy-17: Web Development with Grails"
  ],
  "references": [
    {
      "title": "Groovy Documentation",
      "url": "https://groovy-lang.org/documentation.html",
      "description": "Official docs"
    },
    {
      "title": "Groovy Tutorial (Groovy-lang)",
      "url": "https://groovy-lang.org/single-page-documentation.html",
      "description": "Official reference"
    },
    {
      "title": "Groovy in Action",
      "url": "https://www.manning.com/books/groovy-in-action-second-edition",
      "description": "Book"
    }
  ]
}
---

# GROOVY-18-RATPACK: Ratpack and Microservices

## Introduction

Lightweight web services. By the end of this lesson you will be able to: Set up Ratpack; Define routes; Handle JSON; Build APIs.

## Key Concepts

### 1. Set up Ratpack

Target: Set up Ratpack. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```groovy
import ratpack.groovy.Groovy

def app = Groovy.ratpack {
  handlers {
    get { render "Hello, World!" }
  }
}
```
### 2. Define routes

Target: Define routes. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```groovy
handlers {
  get("hello/:name") {
    render "Hello, ${pathTokens.name}!"
  }
}
```
### 3. Handle JSON

Target: Handle JSON. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```groovy
get("api/data") {
  render json([name: "Ada"])
}
```
### 4. Build APIs

Target: Build APIs. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```groovy
post("api/user") {
  def body = request.body.text
  render body
}
```

## Practice Questions

1. What is the key idea behind "Ratpack and Microservices"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Ratpack and Microservices with analogies and real-world examples"
1. "Show me common mistakes beginners make with Ratpack and Microservices"
1. "Provide advanced patterns and performance considerations for Ratpack and Microservices"

## Key Takeaways

- Master the core ideas of Ratpack and Microservices through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
