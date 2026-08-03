---
{
  "title": "Web Servers with Kemal",
  "description": "Build HTTP services.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Set up Kemal",
    "Define routes",
    "Handle JSON",
    "Serve requests"
  ],
  "knowledge_refs": [
    "crystal/crystal-17-web"
  ],
  "prerequisites": [
    "Crystal-16: Macros"
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

# CRYSTAL-17-WEB: Web Servers with Kemal

## Introduction

Build HTTP services. By the end of this lesson you will be able to: Set up Kemal; Define routes; Handle JSON; Serve requests.

## Key Concepts

### 1. Set up Kemal

Target: Set up Kemal. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```crystal
require "kemal"

get "/" do
  "Hello, World!"
end

Kemal.run
```
### 2. Define routes

Target: Define routes. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```crystal
get "/hello/:name" do |env|
  name = env.params.url["name"]
  "Hello, #{name}!"
end
```
### 3. Handle JSON

Target: Handle JSON. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```crystal
require "json"

get "/api/user" do |env|
  user = {name: "Ada", age: 36}.to_json
  user
end
```
### 4. Serve requests

Target: Serve requests. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```crystal
post "/echo" do |env|
  env.request.body.try(&.gets_to_end)
end
```

## Practice Questions

1. What is the key idea behind "Web Servers with Kemal"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Web Servers with Kemal with analogies and real-world examples"
1. "Show me common mistakes beginners make with Web Servers with Kemal"
1. "Provide advanced patterns and performance considerations for Web Servers with Kemal"

## Key Takeaways

- Master the core ideas of Web Servers with Kemal through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
