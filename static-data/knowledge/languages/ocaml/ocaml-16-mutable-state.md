---
{
  "title": "Objects and Classes",
  "description": "OCaml object system.",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define classes",
    "Use inheritance",
    "Use object types",
    "Mix OOP with FP"
  ],
  "knowledge_refs": [
    "ocaml/ocaml-16-mutable-state"
  ],
  "prerequisites": [
    "Ocaml-15: Input/Output"
  ],
  "references": [
    {
      "title": "OCaml Manual",
      "url": "https://ocaml.org/manual/",
      "description": "Official language manual"
    },
    {
      "title": "OCaml Tutorials",
      "url": "https://ocaml.org/docs",
      "description": "Official documentation"
    },
    {
      "title": "Real World OCaml",
      "url": "https://dev.realworldocaml.org/",
      "description": "Comprehensive book"
    }
  ]
}
---

# OCAML-16-MUTABLE-STATE: Objects and Classes

## Introduction

OCaml object system. By the end of this lesson you will be able to: Define classes; Use inheritance; Use object types; Mix OOP with FP.

## Key Concepts

### 1. Define classes

Target: Define classes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ocaml
class counter =
  object
    val mutable count = 0
    method increment = count <- count + 1
    method get = count
  end

let c = new counter
```
### 2. Use inheritance

Target: Use inheritance. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ocaml
class animal =
  object
    method speak = "..."
  end

class dog =
  object
    inherit animal
    method! speak = "Woof"
  end
```
### 3. Use object types

Target: Use object types. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ocaml
let o = object method x = 1 end
(o#x)
```
### 4. Mix OOP with FP

Target: Mix OOP with FP. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ocaml
let s = new counter
let () = s#increment
```

## Practice Questions

1. What is the key idea behind "Objects and Classes"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Objects and Classes with analogies and real-world examples"
1. "Show me common mistakes beginners make with Objects and Classes"
1. "Provide advanced patterns and performance considerations for Objects and Classes"

## Key Takeaways

- Master the core ideas of Objects and Classes through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
