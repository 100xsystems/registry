---
{
  "title": "Haxe on Node.js",
  "description": "Build Node applications.",
  "type": "lesson",
  "order": 19,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Compile to JS for Node",
    "Use Node modules",
    "Build a CLI",
    "Use NPM packages"
  ],
  "knowledge_refs": [
    "haxe/haxe-19-node"
  ],
  "prerequisites": [
    "Haxe-18: HashLink VM"
  ],
  "references": [
    {
      "title": "Haxe Documentation",
      "url": "https://haxe.org/documentation/",
      "description": "Official docs"
    },
    {
      "title": "Haxe Manual",
      "url": "https://haxe.org/manual/introduction.html",
      "description": "The language manual"
    },
    {
      "title": "Haxe Cookbook",
      "url": "https://code.haxe.org/",
      "description": "Community recipes"
    }
  ]
}
---

# HAXE-19-NODE: Haxe on Node.js

## Introduction

Build Node applications. By the end of this lesson you will be able to: Compile to JS for Node; Use Node modules; Build a CLI; Use NPM packages.

## Key Concepts

### 1. Compile to JS for Node

Target: Compile to JS for Node. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haxe
haxe -main Main -js app.js -D nodejs
```
### 2. Use Node modules

Target: Use Node modules. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haxe
import js.node.Fs;
Fs.readFile("data.txt", (err, data) -> {
  trace(data);
});
```
### 3. Build a CLI

Target: Build a CLI. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haxe
import js.node.Http;

var server = Http.createServer((req, res) -> {
  res.writeHead(200);
  res.end("Hello");
});
server.listen(8080);
```
### 4. Use NPM packages

Target: Use NPM packages. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haxe
import js.node.Path;
trace(Path.join("a", "b"));
```

## Practice Questions

1. What is the key idea behind "Haxe on Node.js"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Haxe on Node.js with analogies and real-world examples"
1. "Show me common mistakes beginners make with Haxe on Node.js"
1. "Provide advanced patterns and performance considerations for Haxe on Node.js"

## Key Takeaways

- Master the core ideas of Haxe on Node.js through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
