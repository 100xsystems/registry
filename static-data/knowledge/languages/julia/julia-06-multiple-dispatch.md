---
{
  "title": "Multiple Dispatch",
  "description": "Method definitions, abstract types, and dispatch specificity.",
  "type": "lesson",
  "order": 6,
  "duration": 35,
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define multiple methods for the same function name",
    "Use abstract types to write generic code",
    "Explain how Julia picks the most specific method"
  ],
  "knowledge_refs": [
    "julia/julia-06-multiple-dispatch"
  ],
  "prerequisites": [
    "julia-05-functions"
  ],
  "references": [
    {
      "title": "Julia Manual — Methods",
      "url": "https://docs.julialang.org/en/v1/manual/methods/"
    },
    {
      "title": "Julia Manual — Types",
      "url": "https://docs.julialang.org/en/v1/manual/types/"
    },
    {
      "title": "Julia Manual — Constructors",
      "url": "https://docs.julialang.org/en/v1/manual/constructors/"
    }
  ]
}
---

# JULIA-06-MULTIPLE-DISPATCH: Multiple Dispatch

## Introduction

Method definitions, abstract types, and dispatch specificity. By the end of this lesson you will be able to: Define multiple methods for the same function name; Use abstract types to write generic code; Explain how Julia picks the most specific method.

## Key Concepts

### 1. Define multiple methods for the same function name

Target: Define multiple methods for the same function name. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```julia
# Multiple dispatch: the heart of Julia
describe(x::Int) = "an integer: $x"
describe(x::Float64) = "a float: $x"
describe(x::String) = "a string: $x"

println(describe(42))      # an integer: 42
println(describe(4.2))     # a float: 4.2
println(describe("x"))     # a string: x

```
### 2. Use abstract types to write generic code

Target: Use abstract types to write generic code. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```julia
# Dispatch on multiple arguments
combine(a::Number, b::Number) = a + b
combine(a::String, b::String) = a * b
combine(a::String, b::Number) = a * string(b)

println(combine(2, 3))     # 5
println(combine("a", "b")) # "ab"
println(combine("x", 2))   # "x2"

```
### 3. Explain how Julia picks the most specific method

Target: Explain how Julia picks the most specific method. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```julia
# Abstract types enable generic code
abstract type Animal end

struct Dog <: Animal
    name::String
end

speak(a::Dog) = "Woof! I am $(a.name)"
println(speak(Dog("Rex"))) # Woof! I am Rex

```
### 4. Define multiple methods for the same function name

Target: Define multiple methods for the same function name. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```julia
# Method specificity: Julia picks the most specific match
f(x) = "generic: $x"
f(x::Number) = "number: $x"
f(x::Int) = "int: $x"

println(f("a"))            # generic: a
println(f(2.5))            # number: 2.5
println(f(2))              # int: 2

```

## Practice Questions

1. What is the key idea behind "Multiple Dispatch"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Multiple Dispatch with analogies and real-world examples"
1. "Show me common mistakes beginners make with Multiple Dispatch"
1. "Provide advanced patterns and performance considerations for Multiple Dispatch"

## Key Takeaways

- Master the core ideas of Multiple Dispatch through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
