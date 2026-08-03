---
{
  "title": "Strings and Text",
  "description": "UTF-8 handling, interpolation, and string functions.",
  "type": "lesson",
  "order": 8,
  "duration": "25 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Explain UTF-8 semantics of Julia strings",
    "Use string interpolation idiomatically",
    "Apply split, join, replace, and case functions"
  ],
  "knowledge_refs": [
    "julia/julia-08-strings-text"
  ],
  "prerequisites": [
    "julia-02-values-types"
  ],
  "references": [
    {
      "title": "Julia Manual — Strings",
      "url": "https://docs.julialang.org/en/v1/manual/strings/"
    },
    {
      "title": "Julia Manual — Unicode Input",
      "url": "https://docs.julialang.org/en/v1/manual/unicode-input/"
    }
  ]
}
---

# JULIA-08-STRINGS-TEXT: Strings and Text

## Introduction

UTF-8 handling, interpolation, and string functions. By the end of this lesson you will be able to: Explain UTF-8 semantics of Julia strings; Use string interpolation idiomatically; Apply split, join, replace, and case functions.

## Key Concepts

### 1. Explain UTF-8 semantics of Julia strings

Target: Explain UTF-8 semantics of Julia strings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```julia
# Strings are immutable byte sequences with UTF-8 support
s = "héllo"
println(length(s))         # 5 — character count
println(ncodeunits(s))     # 6 — bytes
println(uppercase(s))      # HÉLLO

```
### 2. Use string interpolation idiomatically

Target: Use string interpolation idiomatically. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```julia
# String interpolation — the idiomatic way to build strings
name = "Julia"
version = 1.9
println("Welcome to $name v$version")
println("2 + 2 = $(2 + 2)")   # 2 + 2 = 4

```
### 3. Apply split, join, replace, and case functions

Target: Apply split, join, replace, and case functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```julia
# String functions: split, join, replace, startswith
println(split("a,b,c", ","))       # ["a", "b", "c"]
println(join(["x", "y"], "-"))     # "x-y"
println(replace("banana", "a" => "o"))  # "bonono"
println(startswith("hello", "he")) # true

```
### 4. Explain UTF-8 semantics of Julia strings

Target: Explain UTF-8 semantics of Julia strings. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```julia
# Unicode identifiers and raw strings
α = 2.0
β = 3.0
println(α * β)             # 6.0

raw_path = raw"C:\Users\ada"
println(raw_path)          # C:\Users\ada — no escaping

```

## Practice Questions

1. What is the key idea behind "Strings and Text"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Strings and Text with analogies and real-world examples"
1. "Show me common mistakes beginners make with Strings and Text"
1. "Provide advanced patterns and performance considerations for Strings and Text"

## Key Takeaways

- Master the core ideas of Strings and Text through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
