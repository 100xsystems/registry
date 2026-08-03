---
{
  "title": "Foreign Function Interface",
  "description": "Call C libraries from Nim.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Import C functions",
    "Pass pointers and structs",
    "Use pragma importc",
    "Call libc functions"
  ],
  "knowledge_refs": [
    "nim/nim-18-ffi"
  ],
  "prerequisites": [
    "Nim-17: Templates"
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

# NIM-18-FFI: Foreign Function Interface

## Introduction

Call C libraries from Nim. By the end of this lesson you will be able to: Import C functions; Pass pointers and structs; Use pragma importc; Call libc functions.

## Key Concepts

### 1. Import C functions

Target: Import C functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nim
proc printf(fmt: cstring): cint {.importc, header: "<stdio.h>", varargs.}

printf("hello %s\n", "world")
```
### 2. Pass pointers and structs

Target: Pass pointers and structs. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nim
proc strlen(s: cstring): csize_t {.importc, header: "<string.h>".}

echo strlen("hello")
```
### 3. Use pragma importc

Target: Use pragma importc. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nim
proc malloc(size: csize_t): pointer {.importc, header: "<stdlib.h>".}
```
### 4. Call libc functions

Target: Call libc functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nim
type
  CFile {.importc: "FILE", header: "<stdio.h>".} = object
```

## Practice Questions

1. What is the key idea behind "Foreign Function Interface"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Foreign Function Interface with analogies and real-world examples"
1. "Show me common mistakes beginners make with Foreign Function Interface"
1. "Provide advanced patterns and performance considerations for Foreign Function Interface"

## Key Takeaways

- Master the core ideas of Foreign Function Interface through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
