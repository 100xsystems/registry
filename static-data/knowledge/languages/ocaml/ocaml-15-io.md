---
{
  "title": "Input/Output",
  "description": "File and console IO.",
  "type": "lesson",
  "order": 15,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Read from stdin",
    "Read files",
    "Write files",
    "Format output"
  ],
  "knowledge_refs": [
    "ocaml/ocaml-15-io"
  ],
  "prerequisites": [
    "Ocaml-14: Advanced Types"
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

# OCAML-15-IO: Input/Output

## Introduction

File and console IO. By the end of this lesson you will be able to: Read from stdin; Read files; Write files; Format output.

## Key Concepts

### 1. Read from stdin

Target: Read from stdin. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ocaml
let () = print_endline "hello"
```
### 2. Read files

Target: Read files. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ocaml
let () =
  let ic = open_in "data.txt" in
  let content = really_input_string ic (in_channel_length ic) in
  close_in ic
```
### 3. Write files

Target: Write files. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ocaml
let () =
  let oc = open_out "out.txt" in
  output_string oc "hello";
  close_out oc
```
### 4. Format output

Target: Format output. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ocaml
Printf.printf "value: %d
" 42
```

## Practice Questions

1. What is the key idea behind "Input/Output"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Input/Output with analogies and real-world examples"
1. "Show me common mistakes beginners make with Input/Output"
1. "Provide advanced patterns and performance considerations for Input/Output"

## Key Takeaways

- Master the core ideas of Input/Output through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
