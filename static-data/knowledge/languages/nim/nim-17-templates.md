---
{
  "title": "Templates",
  "description": "Inline code substitution.",
  "type": "lesson",
  "order": 17,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write templates",
    "Use template parameters",
    "Avoid common pitfalls",
    "Compare with macros"
  ],
  "knowledge_refs": [
    "nim/nim-17-templates"
  ],
  "prerequisites": [
    "Nim-16: Macros and Metaprogramming"
  ],
  "references": [
    {
      "title": "Nim Manual",
      "url": "https://nim-lang.org/docs/manual.html",
      "description": "Official language manual"
    },
    {
      "title": "Nim by Example",
      "url": "https://nim-by-example.github.io/",
      "description": "Practical Nim examples"
    },
    {
      "title": "Nim Tutorial",
      "url": "https://nim-lang.org/docs/tut1.html",
      "description": "Official tutorial"
    },
    {
      "title": "Nim Forum",
      "url": "https://forum.nim-lang.org/",
      "description": "Community discussions"
    }
  ]
}
---

# NIM-17-TEMPLATES: Templates

## Introduction

Inline code substitution. By the end of this lesson you will be able to: Write templates; Use template parameters; Avoid common pitfalls; Compare with macros.

## Key Concepts

### 1. Write templates

Target: Write templates. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nim
template twice(statement: untyped) =
  statement
  statement

twice:
  echo "hello"
```
### 2. Use template parameters

Target: Use template parameters. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nim
template withRetry(body: untyped) =
  var attempts = 0
  while true:
    try:
      body
      break
    except:
      inc attempts
      if attempts > 3: raise
```
### 3. Avoid common pitfalls

Target: Avoid common pitfalls. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nim
template assertMsg(cond: bool, msg: string) =
  if not cond:
    echo "assert failed: ", msg
```
### 4. Compare with macros

Target: Compare with macros. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nim
echo "templates run at compile time"
```

## Practice Questions

1. What is the key idea behind "Templates"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Templates with analogies and real-world examples"
1. "Show me common mistakes beginners make with Templates"
1. "Provide advanced patterns and performance considerations for Templates"

## Key Takeaways

- Master the core ideas of Templates through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
