---
{
  "title": "Web Development with vibe.d",
  "description": "Async HTTP servers.",
  "type": "lesson",
  "order": 20,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create a vibe.d server",
    "Define REST routes",
    "Serve JSON",
    "Handle requests"
  ],
  "knowledge_refs": [
    "d/d-20-web"
  ],
  "prerequisites": [
    "D-19: DUB and Packaging"
  ],
  "references": [
    {
      "title": "D Language Reference",
      "url": "https://dlang.org/spec/spec.html",
      "description": "Official language spec"
    },
    {
      "title": "D Programming Tour",
      "url": "https://tour.dlang.org/",
      "description": "Interactive language tour"
    },
    {
      "title": "D Wiki",
      "url": "https://wiki.dlang.org/",
      "description": "Community wiki"
    },
    {
      "title": "DUB Package Manager",
      "url": "https://code.dlang.org/",
      "description": "Package registry"
    }
  ]
}
---

# D-20-WEB: Web Development with vibe.d

## Introduction

Async HTTP servers. By the end of this lesson you will be able to: Create a vibe.d server; Define REST routes; Serve JSON; Handle requests.

## Key Concepts

### 1. Create a vibe.d server

Target: Create a vibe.d server. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```d
import vibe.d;

void main() {
    auto settings = new HTTPServerSettings;
    settings.port = 8080;
    listenHTTP(settings, &requestHandler);
    runEventLoop();
}

void requestHandler(HTTPServerRequest req, HTTPServerResponse res) {
    res.writeBody("Hello, World!");
}
```
### 2. Define REST routes

Target: Define REST routes. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```d
router.get("/hello/:name", (req, res) {
    res.writeBody("Hello, " ~ req.params["name"]);
});
```
### 3. Serve JSON

Target: Serve JSON. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```d
import std.json;
res.writeBody(JSONValue(["name": "Ada", "age": 36]).toJSON());
```
### 4. Handle requests

Target: Handle requests. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```d
router.post("/api/user", (req, res) {
    auto body = req.bodyReader.readAll().toUTF8;
    res.writeBody(body);
});
```

## Practice Questions

1. What is the key idea behind "Web Development with vibe.d"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Web Development with vibe.d with analogies and real-world examples"
1. "Show me common mistakes beginners make with Web Development with vibe.d"
1. "Provide advanced patterns and performance considerations for Web Development with vibe.d"

## Key Takeaways

- Master the core ideas of Web Development with vibe.d through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
