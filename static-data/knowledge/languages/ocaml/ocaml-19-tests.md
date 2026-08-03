---
{
  "title": "Testing with Alcotest",
  "description": "Unit and property tests.",
  "type": "lesson",
  "order": 19,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write Alcotest tests",
    "Use check functions",
    "Group tests",
    "Run test binaries"
  ],
  "knowledge_refs": [
    "ocaml/ocaml-19-tests"
  ],
  "prerequisites": [
    "Ocaml-18: PPX and Metaprogramming"
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

# OCAML-19-TESTS: Testing with Alcotest

## Introduction

Unit and property tests. By the end of this lesson you will be able to: Write Alcotest tests; Use check functions; Group tests; Run test binaries.

## Key Concepts

### 1. Write Alcotest tests

Target: Write Alcotest tests. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ocaml
let test_add () = Alcotest.(check int) "same" 4 (2 + 2)
```
### 2. Use check functions

Target: Use check functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ocaml
let suite = [ ("math", [ Alcotest.test_case "add" `Quick test_add ]) ]
```
### 3. Group tests

Target: Group tests. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ocaml
let () = Alcotest.run "my tests" [ suite ]
```
### 4. Run test binaries

Target: Run test binaries. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ocaml
Alcotest.(check string) "msg" "hi" (String.lowercase_ascii "HI")
```

## Practice Questions

1. What is the key idea behind "Testing with Alcotest"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Testing with Alcotest with analogies and real-world examples"
1. "Show me common mistakes beginners make with Testing with Alcotest"
1. "Provide advanced patterns and performance considerations for Testing with Alcotest"

## Key Takeaways

- Master the core ideas of Testing with Alcotest through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
