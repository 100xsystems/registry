---
{
  "title": "CLI Applications",
  "description": "Build command-line tools.",
  "type": "lesson",
  "order": 18,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Parse arguments",
    "Use flag package",
    "Read stdin",
    "Build a CLI tool"
  ],
  "knowledge_refs": [
    "v/v-18-cli"
  ],
  "prerequisites": [
    "V-17: Testing"
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

# V-18-CLI: CLI Applications

## Introduction

Build command-line tools. By the end of this lesson you will be able to: Parse arguments; Use flag package; Read stdin; Build a CLI tool.

## Key Concepts

### 1. Parse arguments

Target: Parse arguments. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```v
import os

fn main() {
	args := os.args
	println(args)
}
```
### 2. Use flag package

Target: Use flag package. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```v
import flag

mut fp := flag.new_flag_parser(os.args)
name := fp.string("name", `n`, "", "your name")
fp.finalize() or { panic(err) }
println("Hello, $name")
```
### 3. Read stdin

Target: Read stdin. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```v
import os

for line in os.stdin.read_lines() {
	println(line)
}
```
### 4. Build a CLI tool

Target: Build a CLI tool. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```v
println("Usage: app [options]")
```

## Practice Questions

1. What is the key idea behind "CLI Applications"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain CLI Applications with analogies and real-world examples"
1. "Show me common mistakes beginners make with CLI Applications"
1. "Provide advanced patterns and performance considerations for CLI Applications"

## Key Takeaways

- Master the core ideas of CLI Applications through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
