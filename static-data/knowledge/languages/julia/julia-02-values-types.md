---
{
  "title": "Values and Types",
  "description": "Core types: integers, floats, booleans, chars, strings.",
  "type": "lesson",
  "order": 2,
  "duration": 25,
  "difficulty": "beginner",
  "learning_objectives": [
    "Identify the core scalar types in Julia",
    "Use typeof() to inspect types at runtime",
    "Explain the differences between nothing, missing, and NaN"
  ],
  "knowledge_refs": [
    "julia/julia-02-values-types"
  ],
  "prerequisites": [
    "julia-01-getting-started"
  ],
  "references": [
    {
      "title": "Julia Manual — Integers and Floating-Point",
      "url": "https://docs.julialang.org/en/v1/manual/integers-and-floating-point-numbers/"
    },
    {
      "title": "Julia Manual — Strings",
      "url": "https://docs.julialang.org/en/v1/manual/strings/"
    },
    {
      "title": "Julia Manual — Missing Values",
      "url": "https://docs.julialang.org/en/v1/manual/missing/"
    }
  ]
}
---

# JULIA-02-VALUES-TYPES: Values and Types

## Introduction

Core types: integers, floats, booleans, chars, strings. By the end of this lesson you will be able to: Identify the core scalar types in Julia; Use typeof() to inspect types at runtime; Explain the differences between nothing, missing, and NaN.

## Key Concepts

### 1. Identify the core scalar types in Julia

Target: Identify the core scalar types in Julia. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```julia
# Core types: Int, Float64, Bool, Char, String
println(typeof(42))        # Int64
println(typeof(3.14))      # Float64
println(typeof(true))      # Bool
println(typeof('a'))       # Char (single quotes!)
println(typeof("hi"))      # String (double quotes)

```
### 2. Use typeof() to inspect types at runtime

Target: Use typeof() to inspect types at runtime. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```julia
# Integer types — pick the size you need
println(typemax(Int8))     # 127
println(typemax(UInt64))   # 18446744073709551615
x = 10
println(x isa Integer)     # true

```
### 3. Explain the differences between nothing, missing, and NaN

Target: Explain the differences between nothing, missing, and NaN. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```julia
# Float behavior: NaN, Inf, and precision
println(1.0 / 0.0)         # Inf
println(0.0 / 0.0)         # NaN
println(0.1 + 0.2)         # 0.30000000000000004 — same IEEE as everywhere

```
### 4. Identify the core scalar types in Julia

Target: Identify the core scalar types in Julia. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```julia
# Nothing, missing, and nothingness
println(nothing)           # nothing — Julia's null
println(missing)           # missing — propagates through calculations
println(1 + missing)       # missing

```

## Practice Questions

1. What is the key idea behind "Values and Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Values and Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Values and Types"
1. "Provide advanced patterns and performance considerations for Values and Types"

## Key Takeaways

- Master the core ideas of Values and Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
