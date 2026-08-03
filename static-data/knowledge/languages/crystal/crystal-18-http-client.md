---
{
  "title": "HTTP Clients and JSON",
  "description": "Consume APIs from Crystal.",
  "type": "lesson",
  "order": 18,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Make HTTP requests",
    "Parse JSON",
    "Use typed JSON",
    "Handle errors"
  ],
  "knowledge_refs": [
    "crystal/crystal-18-http-client"
  ],
  "prerequisites": [
    "Crystal-17: Web Servers with Kemal"
  ],
  "references": [
    {
      "title": "Crystal Language Reference",
      "url": "https://crystal-lang.org/reference/",
      "description": "Official docs"
    },
    {
      "title": "Crystal for Rubyists",
      "url": "https://crystal-lang.org/reference/guides/faq.html",
      "description": "Migration guide"
    },
    {
      "title": "Crystal Book",
      "url": "https://crystal-lang.org/reference/",
      "description": "Official reference book"
    },
    {
      "title": "Crystal Forum",
      "url": "https://forum.crystal-lang.org/",
      "description": "Community"
    }
  ]
}
---

# CRYSTAL-18-HTTP-CLIENT: HTTP Clients and JSON

## Introduction

Consume APIs from Crystal. By the end of this lesson you will be able to: Make HTTP requests; Parse JSON; Use typed JSON; Handle errors.

## Key Concepts

### 1. Make HTTP requests

Target: Make HTTP requests. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```crystal
require "http/client"

response = HTTP::Client.get("https://example.com")
puts response.body
```
### 2. Parse JSON

Target: Parse JSON. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```crystal
require "json"

data = JSON.parse(response.body)
puts data["title"]
```
### 3. Use typed JSON

Target: Use typed JSON. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```crystal
struct User
  include JSON::Serializable
  property name : String
  property age : Int32
end

user = User.from_json(response.body)
puts user.name
```
### 4. Handle errors

Target: Handle errors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```crystal
HTTP::Client.get("https://api.example.com") do |res|
  puts res.status_code
end
```

## Practice Questions

1. What is the key idea behind "HTTP Clients and JSON"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain HTTP Clients and JSON with analogies and real-world examples"
1. "Show me common mistakes beginners make with HTTP Clients and JSON"
1. "Provide advanced patterns and performance considerations for HTTP Clients and JSON"

## Key Takeaways

- Master the core ideas of HTTP Clients and JSON through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
